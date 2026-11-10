#!/usr/bin/env python3
"""Anatomy resource packages and a rebuildable local SQLite catalog. Python stdlib only."""
import argparse
import contextlib
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from urllib.parse import quote
import uuid
import zipfile
from types import SimpleNamespace
sys.path.insert(0, str(Path(__file__).resolve().parent))
import question_bindings as QB

SCHEMA = Path(__file__).resolve().parents[1] / 'schemas/manifest-v1.schema.json'
REF = re.compile(r'^anatomy:([0-9a-f-]{36})@((?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*))(?:#scene=([a-z][a-z0-9-]*))?$')
MAX_BYTES = 256 * 1024 * 1024

class ResourceError(ValueError):
    pass

def need(ok, message):
    if not ok:
        raise ResourceError(message)

def now():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n'

def pairs(items):
    result = {}
    for key, value in items:
        need(key not in result, 'Duplicate JSON key: ' + key)
        result[key] = value
    return result

def loads(raw):
    return json.loads(raw, object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ResourceError('Nonfinite JSON: ' + x)))

def timestamp(value):
    need(isinstance(value, str) and re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]+)?Z', value),
         'Timestamp must be YYYY-MM-DDTHH:MM:SS[.fraction]Z')
    return datetime.fromisoformat(value[:-1] + '+00:00')

def schema_check(value, spec, at='$'):
    """Validate the subset used by the bundled schema, not an arbitrary JSON Schema engine."""
    typ = spec.get('type')
    valid = {'string': lambda: isinstance(value, str),
             'object': lambda: isinstance(value, dict),
             'array': lambda: isinstance(value, list),
             'number': lambda: type(value) in (int, float) and math.isfinite(value),
             'integer': lambda: type(value) is int,
             'boolean': lambda: type(value) is bool}
    if typ:
        need(valid[typ](), at + ': expected ' + typ)
    if 'const' in spec:
        need(value == spec['const'], at + ': unsupported value')
    if 'enum' in spec:
        need(value in spec['enum'], at + ': invalid enum')
    if isinstance(value, str):
        need(len(value) >= spec.get('minLength', 0), at + ': empty string')
        need(len(value) <= spec.get('maxLength', 100000), at + ': string too long')
        if 'pattern' in spec:
            need(re.search(spec['pattern'], value), at + ': invalid pattern')
        if spec.get('format') == 'uuid':
            need(str(uuid.UUID(value)) == value, at + ': canonical UUID required')
        if spec.get('format') == 'date-time':
            timestamp(value)
    if type(value) in (int, float):
        need(math.isfinite(value), at + ': nonfinite number')
        need(value >= spec.get('minimum', -math.inf), at + ': below minimum')
        need(value <= spec.get('maximum', math.inf), at + ': above maximum')
    if isinstance(value, dict):
        props = spec.get('properties', {})
        need(all(k in value for k in spec.get('required', [])), at + ': missing required fields')
        extra = spec.get('additionalProperties', True)
        for key, child in value.items():
            need(key in props or extra is not False, at + ': unknown field ' + key)
            schema_check(child, props.get(key, extra if isinstance(extra, dict) else {}), at + '.' + key)
    if isinstance(value, list):
        need(len(value) >= spec.get('minItems', 0), at + ': too few items')
        need(len(value) <= spec.get('maxItems', 100000), at + ': too many items')
        if spec.get('uniqueItems'):
            need(len({dump(v) for v in value}) == len(value), at + ': duplicate items')
        for i, child in enumerate(value):
            schema_check(child, spec.get('items', {}), f'{at}[{i}]')

def relative(value):
    need(isinstance(value, str) and value and '\\' not in value, 'Use relative POSIX paths')
    p = PurePosixPath(value)
    need(not p.is_absolute() and value == p.as_posix(), 'Noncanonical path: ' + value)
    need(all(x not in ('.', '..') for x in p.parts), 'Path traversal: ' + value)
    need(not re.search(r'[:\x00-\x1f\x7f]', value), 'Invalid portable path: ' + value)
    return p

def file_at(root, name):
    parts = relative(name).parts
    target = root
    for part in parts:
        target = target / part
        need(not target.is_symlink(), 'Symlink not allowed: ' + name)
    need(target.is_file(), 'Missing file: ' + name)
    need(target.resolve().is_relative_to(root.resolve()), 'File outside package: ' + name)
    return target

def parse_ref(value):
    match = REF.fullmatch(value)
    need(match, 'Use anatomy:<UUID>@<major.minor.patch>[#scene=<id>]')
    aid, version, scene = match.groups()
    need(str(uuid.UUID(aid)) == aid, 'Invalid UUID')
    return aid, version, scene

def reference(m, scene=None):
    result = f"anatomy:{m['asset_id']}@{m['version']}"
    return result + ('#scene=' + scene if scene else '')

def validate(root, raw=None):
    root = Path(root).absolute()
    need(root.is_dir() and not root.is_symlink(), 'Package must be a real directory')
    if raw is None:
        raw = file_at(root, 'manifest.json').read_bytes()
    m = loads(raw)
    schema = SCHEMA if m.get('schema_version') == '1.0' else SCHEMA.parent / 'manifest-v1.1.schema.json'
    schema_check(m, loads(schema.read_bytes()))
    if m['schema_version'] == '1.1': QB.validate_manifest(SimpleNamespace(**globals()), m)
    need(timestamp(m['updated_at']) >= timestamp(m['created_at']), 'updated_at precedes created_at')
    listed = {}
    folded = set()
    for f in m['files']:
        name = f['path']
        need(name != 'manifest.json', 'manifest.json is not its own payload')
        need(name.casefold() not in folded, 'Duplicate/case-conflicting payload: ' + name)
        folded.add(name.casefold())
        payload = file_at(root, name)
        need(payload.stat().st_size == f['bytes'] and sha(payload.read_bytes()) == f['sha256'], 'Payload hash/size mismatch: ' + name)
        listed[name] = f
    actual = set()
    for p in root.rglob('*'):
        need(not p.is_symlink(), 'Symlink in package: ' + str(p))
        if p.is_file() and p.name != 'manifest.json':
            actual.add(p.relative_to(root).as_posix())
        elif p.is_file() and p != root / 'manifest.json':
            actual.add(p.relative_to(root).as_posix())
    need(actual == set(listed), 'Unlisted or missing payload: ' + str(sorted(actual ^ set(listed))))
    for name in m['entrypoints'].values():
        need(name in listed and listed[name]['role'] == 'runtime', 'Entrypoint must be a listed runtime file')
    scenes = [s['id'] for s in m['scenes']]
    need(len(scenes) == len(set(scenes)), 'Duplicate scene IDs')
    for key, p in m['math']['parameters'].items():
        default, typ = p['default'], p['type']
        need({'number': type(default) in (int, float), 'integer': type(default) is int,
              'boolean': type(default) is bool, 'enum': isinstance(default, (str, int, float, bool))}[typ], 'Invalid parameter default: ' + key)
        if 'display_range' in p:
            low, high = p['display_range']
            need(typ in ('number', 'integer') and low < high and low <= default <= high, 'Invalid display range: ' + key)
    kinds = [v['kind'] for v in m['validation']]
    need(set(kinds) == {'mathematics', 'interaction', 'visual', 'offline'}, 'Four distinct validation categories required')
    for v in m['validation']:
        for name in v['evidence']:
            need(name in listed, 'Unlisted evidence: ' + name)
        if v['status'] in ('pass', 'fail'):
            need(v.get('checked_at') and v['evidence'] and v.get('tested_files'), 'Completed validation needs time, evidence and tested hashes')
        for f in v.get('tested_files', []):
            need(f['path'] in listed and listed[f['path']]['sha256'] == f['sha256'], 'Stale validation: ' + f['path'])
    for relation in m['provenance']['relations']:
        aid, ver, scene = parse_ref(relation['target'])
        if (aid, ver) == (m['asset_id'], m['version']) and scene:
            need(scene in scenes, 'Unknown local scene relation')
    return {'root': root.resolve(), 'manifest': m, 'raw': raw, 'digest': sha(raw)}

DDL = '''
CREATE TABLE catalog_meta(key TEXT PRIMARY KEY, value TEXT NOT NULL);
INSERT INTO catalog_meta VALUES('format', 'anatomy-resource-index-v1');
CREATE TABLE releases(asset_id TEXT, version TEXT, manifest_sha256 TEXT NOT NULL, title TEXT NOT NULL, slug TEXT NOT NULL, manifest_json TEXT NOT NULL, PRIMARY KEY(asset_id,version));
CREATE TABLE locations(asset_id TEXT, version TEXT, path TEXT UNIQUE, verified_at TEXT NOT NULL, PRIMARY KEY(asset_id,version,path), FOREIGN KEY(asset_id,version) REFERENCES releases(asset_id,version));
CREATE TABLE files(asset_id TEXT, version TEXT, path TEXT, role TEXT, sha256 TEXT, bytes INTEGER, PRIMARY KEY(asset_id,version,path), FOREIGN KEY(asset_id,version) REFERENCES releases(asset_id,version));
CREATE TABLE scenes(asset_id TEXT, version TEXT, scene_id TEXT, title TEXT, state_json TEXT, PRIMARY KEY(asset_id,version,scene_id), FOREIGN KEY(asset_id,version) REFERENCES releases(asset_id,version));
CREATE TABLE relations(asset_id TEXT, version TEXT, relation TEXT, target TEXT, PRIMARY KEY(asset_id,version,relation,target), FOREIGN KEY(asset_id,version) REFERENCES releases(asset_id,version));
'''

@contextlib.contextmanager
def catalog(path, write=True):
    path = Path(path).absolute()
    if write: path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path if write else path.as_uri() + '?mode=ro', timeout=20, uri=not write)
    db.row_factory = sqlite3.Row
    try:
        db.execute('PRAGMA foreign_keys=ON')
        tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        if not tables:
            db.executescript(DDL + QB.DDL)
        need(not tables or 'catalog_meta' in tables, 'Not an Anatomy index')
        need(db.execute("SELECT value FROM catalog_meta WHERE key='format'").fetchone()[0] == 'anatomy-resource-index-v1', 'Unknown index format')
        db.execute('BEGIN IMMEDIATE' if write else 'BEGIN')
        yield db
        db.commit()
    except BaseException:
        db.rollback()
        raise
    finally:
        db.close()

def outside_db(db_path, packages):
    p = Path(db_path).resolve()
    for package in packages:
        need(not p.is_relative_to(Path(package).resolve()), 'Keep database outside immutable packages')

def register(db, package):
    m, digest, root = package['manifest'], package['digest'], str(package['root'])
    key = (m['asset_id'], m['version'])
    old = db.execute('SELECT manifest_sha256 FROM releases WHERE asset_id=? AND version=?', key).fetchone()
    need(old is None or old[0] == digest, 'Immutable version conflict: ' + reference(m))
    loc = db.execute('SELECT asset_id,version FROM locations WHERE path=?', (root,)).fetchone()
    need(loc is None or tuple(loc) == key, 'Location already belongs to another release')
    if old is None:
        db.execute('INSERT INTO releases VALUES(?,?,?,?,?,?)', (*key, digest, m['title'], m['slug'], package['raw'].decode('utf8')))
        db.executemany('INSERT INTO files VALUES(?,?,?,?,?,?)', [(*key, f['path'], f['role'], f['sha256'], f['bytes']) for f in m['files']])
        db.executemany('INSERT INTO scenes VALUES(?,?,?,?,?)', [(*key, s['id'], s['title'], dump(s['state'])) for s in m['scenes']])
        db.executemany('INSERT OR IGNORE INTO relations VALUES(?,?,?,?)', [(*key, r['relation'], r['target']) for r in m['provenance']['relations']])
    db.execute('INSERT OR REPLACE INTO locations VALUES(?,?,?,?)', (*key, root, now()))

def resolve(db, ref):
    aid, version, scene = parse_ref(ref)
    release = db.execute('SELECT * FROM releases WHERE asset_id=? AND version=?', (aid, version)).fetchone()
    need(release is not None, 'Reference is not indexed: ' + ref)
    rejected = []
    for loc in db.execute('SELECT path FROM locations WHERE asset_id=? AND version=? ORDER BY path', (aid, version)):
        try:
            p = validate(loc[0])
            need(p['digest'] == release['manifest_sha256'], 'Manifest differs from indexed version')
        except (ValueError, OSError) as error:
            rejected.append({'path': loc[0], 'error': str(error)})
            continue
        m = p['manifest']
        selected = next((s for s in m['scenes'] if s['id'] == scene), None)
        need(not scene or selected, 'Unknown scene: ' + str(scene))
        entry = p['root'] / m['entrypoints']['html']
        return {'reference': ref, 'title': m['title'], 'package': str(p['root']), 'entrypoint': str(entry),
                'url': entry.as_uri() + ('#scene=' + quote(scene) if scene else ''),
                'scene': selected, 'manifest_sha256': p['digest'], 'rejected_locations': rejected}
    raise ResourceError('No verified location; re-index moved packages. ' + dump(rejected))

def seal(root, metadata):
    root = Path(root).absolute()
    need(not (root / 'manifest.json').exists(), 'Release already sealed; make a new version directory')
    m = loads(Path(metadata).read_bytes())
    for f in m['files']:
        data = file_at(root, f['path']).read_bytes()
        f.update(sha256=sha(data), bytes=len(data))
    # Receipts are intentionally not manufactured here. Authors must supply real tested hashes.
    raw = dump(m).encode('utf8')
    package = validate(root, raw)
    with (root / 'manifest.json').open('xb') as stream:
        stream.write(raw)
    return package

def move(source, target, db_path):
    source, target = Path(source).absolute(), Path(target).absolute()
    package = validate(source)
    outside_db(db_path, [source, target])
    need(not target.exists() and not target.is_symlink(), 'Destination already exists')
    need(not target.resolve().is_relative_to(source.resolve()), 'Cannot move inside itself')
    target.parent.mkdir(parents=True, exist_ok=True)
    renamed = False
    try:
        with catalog(db_path) as db:
            register(db, package)
            # Same-filesystem rename is atomic. Cross-device transfer uses export/import instead.
            source.rename(target)
            renamed = True
            moved = validate(target)
            need(moved['digest'] == package['digest'], 'Move changed package')
            db.execute('DELETE FROM locations WHERE path=?', (str(package['root']),))
            register(db, moved)
    except BaseException:
        if renamed:
            target.rename(source)
        raise
    return {'reference': reference(package['manifest']), 'from': str(source), 'to': str(target)}

def export_zip(package, destination):
    target = Path(destination).absolute()
    need(not target.exists(), 'Export destination exists')
    need(not target.resolve().is_relative_to(package['root']), 'Export must be outside package')
    target.parent.mkdir(parents=True, exist_ok=True)
    handle, temp = tempfile.mkstemp(prefix='.anatomy-export-', dir=target.parent)
    os.close(handle)
    try:
        names = ['manifest.json'] + [f['path'] for f in package['manifest']['files']]
        with zipfile.ZipFile(temp, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for name in names:
                z.write(package['root'] / name, name)
        with zipfile.ZipFile(temp) as z:
            need(z.testzip() is None, 'ZIP CRC failed')
            expected = {'manifest.json': package['digest'], **{f['path']: f['sha256'] for f in package['manifest']['files']}}
            for name in names:
                need(sha(z.read(name)) == expected[name], 'ZIP readback differs from sealed manifest: ' + name)
        os.rename(temp, target)
    finally:
        Path(temp).unlink(missing_ok=True)
    return {'zip': str(target), 'sha256': sha(target.read_bytes()), 'files': len(names), 'crc': 'pass'}

def import_zip(archive, destination, db_path):
    with zipfile.ZipFile(archive) as check:
        if 'transfer.json' in check.namelist():
            return QB.import_transfer(SimpleNamespace(**globals()), archive, destination, db_path)
    dest = Path(destination).absolute()
    outside_db(db_path, [dest])
    need(not dest.exists() and not dest.is_symlink(), 'Import destination exists')
    dest.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.anatomy-import-', dir=dest.parent))
    renamed = False
    try:
        with zipfile.ZipFile(archive) as z:
            infos = z.infolist()
            need(len(infos) <= 5001 and sum(i.file_size for i in infos) <= MAX_BYTES, 'Archive limit exceeded')
            names = set()
            for info in infos:
                name = info.filename
                relative(name)
                need(name not in names and not info.is_dir(), 'Duplicate/non-file ZIP entry')
                names.add(name)
                mode = (info.external_attr >> 16) & 0o170000
                need(mode in (0, 0o100000), 'ZIP special entry not allowed')
                target = stage / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(z.read(info))
        package = validate(stage)
        with catalog(db_path) as db:
            # Check immutable identity before publishing the extracted directory.
            m = package['manifest']
            old = db.execute('SELECT manifest_sha256 FROM releases WHERE asset_id=? AND version=?', (m['asset_id'], m['version'])).fetchone()
            need(old is None or old[0] == package['digest'], 'Immutable version conflict on import')
            stage.rename(dest)
            renamed = True
            register(db, validate(dest))
        return {'reference': reference(m), 'package': str(dest), 'manifest_sha256': package['digest']}
    except BaseException:
        if renamed:
            dest.rename(stage)
        raise
    finally:
        shutil.rmtree(stage, ignore_errors=True)

def summary(p):
    return {'status': 'PASS', 'reference': reference(p['manifest']), 'package': str(p['root']), 'manifest_sha256': p['digest'], 'files': len(p['manifest']['files'])}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for cmd in ('validate', 'seal'):
        p = sub.add_parser(cmd); p.add_argument('package')
        if cmd == 'seal': p.add_argument('--metadata', required=True)
    for cmd in ('index', 'rebuild'):
        p = sub.add_parser(cmd); p.add_argument('packages', nargs='+'); p.add_argument('--db', required=True)
        if cmd == 'rebuild': p.add_argument('--bindings')
    p = sub.add_parser('list'); p.add_argument('--db', required=True); p.add_argument('--query', default=''); p.add_argument('--topic', default='')
    for cmd in ('resolve', 'refs', 'export'):
        p = sub.add_parser(cmd); p.add_argument('reference'); p.add_argument('--db', required=True)
        if cmd == 'export':
            p.add_argument('--out', required=True); p.add_argument('--with-bindings', action='store_true')
    p = sub.add_parser('move'); p.add_argument('source'); p.add_argument('destination'); p.add_argument('--db', required=True)
    p = sub.add_parser('import'); p.add_argument('archive'); p.add_argument('destination'); p.add_argument('--db', required=True)
    QB.add_cli(sub)
    a = parser.parse_args()
    api = SimpleNamespace(**globals())
    if a.command in ('migrate','bind','bindings','resolve-binding','bindings-export','bindings-import'):
        result = QB.dispatch(api, a)
    elif a.command in ('validate', 'seal'):
        result = summary(seal(a.package, a.metadata) if a.command == 'seal' else validate(a.package))
    elif a.command in ('index', 'rebuild'):
        if a.command == 'rebuild':
            need(not Path(a.db).exists(), 'Rebuild requires a new database path; preserve old index')
            roots = [Path(p) for p in a.packages]
            need(all(p.is_dir() and not p.is_symlink() for p in roots), 'Invalid rebuild root')
            paths = sorted({m.parent.resolve() for root in roots for m in root.rglob('manifest.json')})
            need(paths, 'No manifests under rebuild roots')
        else:
            paths = [Path(p) for p in a.packages]
        outside_db(a.db, paths)
        packages = [validate(p) for p in paths]
        with QB.fact_writes() as created:
            with catalog(a.db) as db:
                for package in packages: register(db, package)
                if a.command == 'rebuild' and a.bindings:
                    QB.put(api, db, a.db, QB.read_records(api, a.bindings), created)
        result = {'status': 'PASS', 'indexed': [summary(p) for p in packages], 'database': str(Path(a.db).resolve())}
    elif a.command == 'move': result = move(a.source, a.destination, a.db)
    elif a.command == 'import': result = import_zip(a.archive, a.destination, a.db)
    else:
        need(Path(a.db).is_file(), 'Index does not exist; use index/rebuild')
        with catalog(a.db, write=False) as db:
            if a.command == 'list':
                rows = db.execute('SELECT * FROM releases WHERE instr(title,?)>0 OR instr(slug,?)>0 OR instr(manifest_json,?)>0', (a.query, a.query, a.query))
                result = []
                for row in rows:
                    m = loads(row['manifest_json'])
                    if not a.topic or a.topic in m['math']['topics']:
                        result.append({'reference': reference(m), 'title': m['title'], 'topics': m['math']['topics'], 'version': m['version']})
            elif a.command == 'refs':
                aid, ver, scene = parse_ref(a.reference)
                need(db.execute('SELECT 1 FROM releases WHERE asset_id=? AND version=?', (aid, ver)).fetchone(), 'Reference is not indexed')
                if scene:
                    need(db.execute('SELECT 1 FROM scenes WHERE asset_id=? AND version=? AND scene_id=?', (aid, ver, scene)).fetchone(), 'Unknown scene')
                outgoing = [dict(r) for r in db.execute('SELECT relation,target FROM relations WHERE asset_id=? AND version=?', (aid, ver))]
                for edge in outgoing:
                    ta, tv, ts = parse_ref(edge['target'])
                    exists = db.execute('SELECT 1 FROM releases WHERE asset_id=? AND version=?', (ta, tv)).fetchone()
                    if ts: exists = db.execute('SELECT 1 FROM scenes WHERE asset_id=? AND version=? AND scene_id=?', (ta, tv, ts)).fetchone()
                    edge['target_indexed'] = bool(exists)
                incoming = [dict(r) for r in db.execute('SELECT asset_id,version,relation,target FROM relations WHERE target=? OR (?=0 AND instr(target,?)=1)', (a.reference, int(bool(scene)), a.reference+'#scene='))]
                result = {'reference': a.reference, 'outgoing': outgoing, 'incoming': incoming}
            else:
                resolved = resolve(db, a.reference)
                if a.command == 'export':
                    outside_db(a.out, [row[0] for row in db.execute('SELECT path FROM locations')])
                    package = validate(resolved['package'])
                    result = QB.export_transfer(api, db, package, a.out) if a.with_bindings else export_zip(package, a.out)
                else: result = resolved
    print(dump(result), end='')

if __name__ == '__main__':
    try:
        main()
    except (ResourceError, OSError, sqlite3.Error, zipfile.BadZipFile, KeyError, TypeError, ValueError) as e:
        print(dump({'status': 'ERROR', 'error': str(e)}), file=sys.stderr, end='')
        sys.exit(1)
