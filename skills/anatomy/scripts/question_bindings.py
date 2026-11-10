"""Immutable question-to-release associations; package-independent JSON is the source of truth."""
import contextlib
import json
from pathlib import Path
import os
import shutil
import sqlite3
import tempfile
import uuid
from urllib.parse import urlencode
import zipfile

DDL = '''
CREATE TABLE question_bindings(
 binding_id TEXT PRIMARY KEY, question_namespace TEXT NOT NULL, question_id TEXT NOT NULL,
 subquestion_id TEXT, asset_id TEXT NOT NULL, asset_version TEXT NOT NULL, scene_id TEXT,
 record_json TEXT NOT NULL, record_sha256 TEXT NOT NULL,
 FOREIGN KEY(asset_id,asset_version) REFERENCES releases(asset_id,version));
CREATE INDEX bindings_question ON question_bindings(question_namespace,question_id,subquestion_id);
CREATE INDEX bindings_asset ON question_bindings(asset_id,asset_version,scene_id);
INSERT INTO catalog_meta VALUES('question_bindings','1.0');
'''

def record_raw(b):
    return (json.dumps(b,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()

def ready(r, db):
    row = db.execute("SELECT value FROM catalog_meta WHERE key='question_bindings'").fetchone()
    r.need(row is not None and row[0] == '1.0', 'Run migrate --db before using question bindings')

def migrate(r, path):
    path = Path(path).absolute()
    r.need(path.is_file(), 'Index does not exist')
    with r.catalog(path, write=False) as db:
        if db.execute("SELECT value FROM catalog_meta WHERE key='question_bindings'").fetchone():
            ready(r, db)
            return {'status':'PASS','already_current':True}
        backup = path.with_name(path.name + '.before-bindings-' + uuid.uuid4().hex + '.bak')
        with contextlib.closing(sqlite3.connect(backup)) as target:
            db.backup(target)
    with r.catalog(path) as db:
        for statement in DDL.split(';'):
            if statement.strip(): db.execute(statement)
    return {'status':'PASS','backup':str(backup),'bindings_schema':'1.0'}

def state(r, m, override=None, scene_id=None):
    override = {} if override is None else override
    r.need(isinstance(override, dict) and set(override) <= {'math','view','lesson'}, 'Invalid state groups')
    r.need(all(isinstance(v,dict) for v in override.values()), 'State groups must be objects')
    scene = next((s for s in m['scenes'] if s['id']==scene_id), None)
    r.need(not scene_id or scene is not None, 'Unknown scene: ' + str(scene_id))
    if m['schema_version']=='1.0':
        r.need(not any(override.values()), 'Manifest 1.0 cannot restore parameter overrides; use a 1.1 release')
        return scene['state'] if scene else None
    contract=m['state_contract']
    def check(value, complete):
        r.need(isinstance(value,dict) and set(value) <= set(contract), 'Unknown state group')
        if complete:r.need(set(value)==set(contract), 'Incomplete state groups')
        for group, values in value.items():
            r.need(isinstance(values,dict) and set(values)<=set(contract[group]), 'Unknown state parameter in ' + group)
            if complete:r.need(set(values)==set(contract[group]), 'Incomplete state: ' + group)
            for key, v in values.items():
                r.schema_check(v,contract[group][key], '$.state.'+group+'.'+key)
    check(m['default_state'],True)
    for s in m['scenes']:check(s['state'],True)
    check(override,False)
    result={group:dict(values) for group,values in m['default_state'].items()}
    for source in ((scene['state'] if scene else {}),override):
        for group,values in source.items():result[group].update(values)
    return result

def validate_manifest(r,m):
    for group,rules in m['state_contract'].items():
        for key,rule in rules.items():
            if 'minimum' in rule or 'maximum' in rule:
                r.need(rule['type'] in ('number','integer'), 'Range requires numeric state parameter')
                r.need(rule.get('minimum',float('-inf'))<=rule.get('maximum',float('inf')), 'Reversed state range')
            for value in rule.get('enum',[]):r.schema_check(value,{k:v for k,v in rule.items() if k!='enum'})
    state(r,m)
    r.need(set(m['math']['parameters']) <= set(m['state_contract']['math']), 'Math parameters missing from state contract')
    for key,rule in m['math']['parameters'].items():
        r.need(m['default_state']['math'][key]==rule['default'], 'Math default disagrees with default_state')

def check_records(r,db,records):
    ready(r,db)
    spec=r.loads((r.SCHEMA.parent/'question-bindings-v1.schema.json').read_bytes())
    r.schema_check({'schema_version':'1.0','bindings':records},spec)
    ids=set()
    for b in records:
        r.need(b['binding_id'] not in ids,'Duplicate binding ID in input');ids.add(b['binding_id'])
        ref=f"anatomy:{b['asset_id']}@{b['asset_version']}"+('#scene='+b['scene_id'] if b.get('scene_id') else '')
        resolved=r.resolve(db,ref)
        r.need(resolved['manifest_sha256']==b['asset_manifest_sha256'],'Binding manifest fingerprint mismatch')
        state(r,r.validate(resolved['package'])['manifest'],b['initial_state'],b.get('scene_id'))
        old=db.execute('SELECT record_sha256 FROM question_bindings WHERE binding_id=?',(b['binding_id'],)).fetchone()
        r.need(old is None or old[0]==r.sha(record_raw(b)),'Immutable binding ID conflict')

def facts_path(db_path):
    return Path(str(Path(db_path).absolute())+'.bindings')

@contextlib.contextmanager
def fact_writes():
    created=[]
    try:yield created
    except BaseException:
        for path in reversed(created):path.unlink(missing_ok=True)
        raise

def put(r,db,db_path,records,created):
    check_records(r,db,records)
    folder=facts_path(db_path)
    r.need(not folder.is_symlink(),'Binding fact directory cannot be a symlink')
    # Keep facts outside every immutable package indexed by this database.
    r.outside_db(folder,[row[0] for row in db.execute('SELECT path FROM locations')])
    folder.mkdir(parents=True,exist_ok=True)
    for b in records:
        raw=record_raw(b);target=folder/(b['binding_id']+'.json')
        r.need(not target.is_symlink(),'Binding fact cannot be a symlink')
        if target.exists():r.need(target.read_bytes()==raw,'Immutable binding fact conflict')
        else:
            fd,name=tempfile.mkstemp(prefix='.binding-',dir=folder)
            try:
                with os.fdopen(fd,'wb') as stream:stream.write(raw);stream.flush();os.fsync(stream.fileno())
                try:os.link(name,target);created.append(target)
                except FileExistsError:r.need(target.read_bytes()==raw,'Concurrent binding fact conflict')
            finally:Path(name).unlink(missing_ok=True)
        db.execute('INSERT OR IGNORE INTO question_bindings VALUES(?,?,?,?,?,?,?,?,?)',
                   (b['binding_id'],b['question_namespace'],b['question_id'],b.get('subquestion_id'),b['asset_id'],b['asset_version'],b.get('scene_id'),raw.decode(),r.sha(raw)))

def read_records(r,source):
    source=Path(source)
    if source.is_dir():
        r.need(not source.is_symlink(),'Binding directory cannot be a symlink')
        result=[]
        for f in sorted(source.glob('*.json')):
            r.need(not f.is_symlink(),'Binding fact cannot be a symlink')
            result.append(r.loads(f.read_bytes()))
        return result
    value=r.loads(source.read_bytes())
    r.schema_check(value,r.loads((r.SCHEMA.parent/'question-bindings-v1.schema.json').read_bytes()))
    return value['bindings']

def query(r,db,namespace=None,qid=None,subquestion=None,ref=None):
    ready(r,db);conditions=[];args=[]
    for key,value in [('question_namespace',namespace),('question_id',qid),('subquestion_id',subquestion)]:
        if value is not None:conditions.append(key+'=?');args.append(value)
    if ref:
        aid,version,scene=r.parse_ref(ref)
        conditions.extend(['asset_id=?','asset_version=?']);args.extend([aid,version])
        if scene:conditions.append('scene_id=?');args.append(scene)
    sql='SELECT record_json FROM question_bindings'+(' WHERE '+' AND '.join(conditions) if conditions else '')+' ORDER BY question_namespace,question_id,binding_id'
    return [r.loads(row[0]) for row in db.execute(sql,args)]

def resolve_binding(r,db,bid):
    ready(r,db)
    row=db.execute('SELECT record_json FROM question_bindings WHERE binding_id=?',(bid,)).fetchone()
    r.need(row is not None,'Unknown binding ID')
    b=r.loads(row[0]);check_records(r,db,[b])
    ref=f"anatomy:{b['asset_id']}@{b['asset_version']}"+('#scene='+b['scene_id'] if b.get('scene_id') else '')
    result=r.resolve(db,ref)
    m=r.validate(result['package'])['manifest'];effective=state(r,m,b['initial_state'],b.get('scene_id'))
    if m['schema_version']=='1.1':
        params={}
        if b.get('scene_id'):params['scene']=b['scene_id']
        params['state']=r.dump(effective).strip()
        result['url']=Path(result['entrypoint']).as_uri()+'#'+urlencode(params)
    return {**result,'binding':b,'effective_state':effective}

def bind(r,db_path,draft):
    b=r.loads(Path(draft).read_bytes())
    r.need(isinstance(b,dict),'Binding draft must be an object')
    b.setdefault('binding_id',str(uuid.uuid4()));b.setdefault('created_at',r.now());b.setdefault('initial_state',{})
    with fact_writes() as created:
        with r.catalog(db_path) as db:
            ready(r,db)
            row=db.execute('SELECT manifest_sha256 FROM releases WHERE asset_id=? AND version=?',(b.get('asset_id'),b.get('asset_version'))).fetchone()
            r.need(row is not None,'Binding target is not indexed')
            b.setdefault('asset_manifest_sha256',row[0]);put(r,db,db_path,[b],created)
    return b

def import_records(r,db_path,source):
    records=read_records(r,source)
    with fact_writes() as created:
        with r.catalog(db_path) as db:put(r,db,db_path,records,created)
    return {'status':'PASS','bindings':len(records),'facts':str(facts_path(db_path))}

def export_records(r,db,out,ref=None):
    records=query(r,db,ref=ref);check_records(r,db,records)
    target=Path(out)
    r.outside_db(target,[row[0] for row in db.execute('SELECT path FROM locations')])
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('x') as stream:stream.write(r.dump({'schema_version':'1.0','bindings':records}))
    return {'status':'PASS','bindings':len(records),'file':str(target.absolute())}

def export_transfer(r,db,package,out):
    records=query(r,db,ref=r.reference(package['manifest']));check_records(r,db,records)
    out=Path(out).absolute();r.need(not out.exists(),'Export destination exists')
    r.need(not out.is_relative_to(package['root']),'Export must be outside package')
    r.outside_db(out,[row[0] for row in db.execute('SELECT path FROM locations')])
    out.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.anatomy-transfer-',dir=out.parent) as temp:
        temp=Path(temp);raw=r.dump({'schema_version':'1.0','bindings':records}).encode()
        receipt=r.dump({'format':'anatomy-transfer-v1','manifest_sha256':package['digest'],'bindings_sha256':r.sha(raw)}).encode()
        source=temp/'package.zip';r.export_zip(package,source)
        transfer=temp/'transfer.zip'
        with zipfile.ZipFile(transfer,'w',compression=zipfile.ZIP_DEFLATED) as z,zipfile.ZipFile(source) as original:
            z.writestr('transfer.json',receipt);z.writestr('question-bindings.json',raw)
            for name in original.namelist():z.writestr('package/'+name,original.read(name))
        with zipfile.ZipFile(transfer) as z:r.need(z.testzip() is None,'Transfer CRC failed')
        os.link(transfer,out)
    return {'zip':str(out),'sha256':r.sha(out.read_bytes()),'bindings':len(records),'crc':'pass'}

def import_transfer(r,archive,dest,db_path):
    dest=Path(dest).absolute();r.outside_db(db_path,[dest])
    r.need(not dest.exists() and not dest.is_symlink(),'Import destination exists')
    dest.parent.mkdir(parents=True,exist_ok=True)
    stage=Path(tempfile.mkdtemp(prefix='.anatomy-transfer-',dir=dest.parent));published=False
    try:
        with zipfile.ZipFile(archive) as z:
            infos=z.infolist();r.need(len(infos)<=5003 and sum(i.file_size for i in infos)<=r.MAX_BYTES,'Archive limit exceeded')
            names=set()
            for info in infos:
                name=info.filename;r.relative(name)
                r.need(name not in names and not info.is_dir(),'Duplicate/non-file ZIP entry');names.add(name)
                r.need((info.external_attr>>16)&0o170000 in (0,0o100000),'ZIP special entry not allowed')
                r.need(name in ('transfer.json','question-bindings.json') or name.startswith('package/'),'Unexpected transfer file')
                target=stage/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(z.read(info))
        receipt=r.loads((stage/'transfer.json').read_bytes())
        r.need(set(receipt)=={'format','manifest_sha256','bindings_sha256'} and receipt['format']=='anatomy-transfer-v1','Invalid transfer receipt')
        package=r.validate(stage/'package');raw=(stage/'question-bindings.json').read_bytes()
        r.need(package['digest']==receipt['manifest_sha256'] and r.sha(raw)==receipt['bindings_sha256'],'Transfer hash mismatch')
        records=read_records(r,stage/'question-bindings.json');m=package['manifest']
        r.need(all((b['asset_id'],b['asset_version'])==(m['asset_id'],m['version']) for b in records),'Transfer binding targets another release')
        with fact_writes() as created:
            with r.catalog(db_path) as db:
                register_package=package
                r.register(db,register_package)
                check_records(r,db,records)
                (stage/'package').rename(dest);published=True
                db.execute('DELETE FROM locations WHERE path=?',(str(package['root']),))
                r.register(db,r.validate(dest));put(r,db,db_path,records,created)
        return {'reference':r.reference(m),'package':str(dest),'manifest_sha256':package['digest'],'bindings':len(records)}
    except BaseException:
        if published:dest.rename(stage/'package')
        raise
    finally:shutil.rmtree(stage,ignore_errors=True)


def add_cli(sub):
    p=sub.add_parser('migrate');p.add_argument('--db',required=True)
    p=sub.add_parser('bind');p.add_argument('--file',required=True);p.add_argument('--db',required=True)
    p=sub.add_parser('bindings');p.add_argument('--db',required=True)
    p.add_argument('--question-namespace');p.add_argument('--question-id');p.add_argument('--subquestion-id');p.add_argument('--reference')
    p=sub.add_parser('resolve-binding');p.add_argument('binding_id');p.add_argument('--db',required=True)
    p=sub.add_parser('bindings-export');p.add_argument('--out',required=True);p.add_argument('--db',required=True);p.add_argument('--reference')
    p=sub.add_parser('bindings-import');p.add_argument('source');p.add_argument('--db',required=True)

def dispatch(r,a):
    if a.command=='migrate':return migrate(r,a.db)
    if a.command=='bind':return bind(r,a.db,a.file)
    if a.command=='bindings-import':return import_records(r,a.db,a.source)
    with r.catalog(a.db,write=False) as db:
        if a.command=='bindings':
            r.need(not a.question_id or a.question_namespace,'Use namespace with question ID')
            return query(r,db,a.question_namespace,a.question_id,a.subquestion_id,a.reference)
        if a.command=='resolve-binding':return resolve_binding(r,db,a.binding_id)
        return export_records(r,db,a.out,a.reference)
