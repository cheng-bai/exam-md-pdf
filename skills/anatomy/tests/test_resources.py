"""Behavioral tests for immutable identity, portability, receipts and transactional indexing."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import uuid
import zipfile

sys.dont_write_bytecode = True
SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/resources.py'
spec = importlib.util.spec_from_file_location('resources', SCRIPT)
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

class ResourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.db = self.root / 'index.sqlite'
        self.counter = 0

    def tearDown(self):
        self.temp.cleanup()

    def make(self, aid=None, version='1.0.0', title='数学截面', relation=None):
        self.counter += 1
        root = self.root / ('package-' + str(self.counter))
        root.mkdir()
        (root / 'index.html').write_text('<!doctype html><title>math</title><p>portable</p>')
        stamp = '2026-10-16T01:00:00Z'
        m = dict(schema_version='1.0', asset_id=aid or str(uuid.uuid4()), version=version,
                 slug='math-section', title=title, language='zh-CN', created_at=stamp, updated_at=stamp,
                 contributors=[dict(name='Test author',role='author')],
                 rights=dict(license='LicenseRef-Test',attribution='Test fixture'),
                 math=dict(topics=['立体几何'],audience=['高中'],objects=['截面'],conditions=[],learning_goals=['观察截面'],
                           parameters={'t':dict(type='number',domain='finite real',display_range=[-50,50],default=0)},approximation='none'),
                 entrypoints={'html':'index.html'},files=[dict(path='index.html',role='runtime')],
                 scenes=[dict(id='degenerate',title='退化',state=dict(math={'t':40},view={'azimuth':35},lesson={'step':0}))],
                 provenance=dict(sources=[],relations=[] if relation is None else [dict(relation='cites',target=relation)]),
                 validation=[dict(kind=k,status='pending',scope='Not tested.',evidence=[]) for k in ['mathematics','interaction','visual','offline']],extensions={})
        metadata = self.root / ('metadata-' + str(self.counter) + '.json')
        metadata.write_text(R.dump(m))
        return R.seal(root, metadata)

    def rewrite(self, package, edit):
        path=package['root']/'manifest.json'
        m=json.loads(path.read_text());edit(m);path.write_text(R.dump(m))
        return R.validate(package['root'])

    def register(self,*packages):
        with R.catalog(self.db) as db:
            for p in packages:R.register(db,p)

    def resolve(self,ref):
        with R.catalog(self.db) as db:return R.resolve(db,ref)

    def cli(self,*args,ok=True):
        p=subprocess.run([sys.executable,str(SCRIPT),*map(str,args)],capture_output=True,text=True)
        self.assertEqual(p.returncode==0,ok,p.stderr+p.stdout)
        return json.loads(p.stdout if ok else p.stderr)

    def test_seal_and_hash(self):
        p=self.make();self.assertEqual(R.validate(p['root'])['digest'],p['digest'])
        self.assertNotIn('manifest.json',[x['path'] for x in p['manifest']['files']])

    def test_double_seal_refused(self):
        p=self.make()
        with self.assertRaises(R.ResourceError):R.seal(p['root'],self.root/'metadata-1.json')

    def test_tamper(self):
        p=self.make();(p['root']/'index.html').write_text('changed')
        with self.assertRaises(R.ResourceError):R.validate(p['root'])

    def test_extra_file(self):
        p=self.make();(p['root']/'extra.txt').write_text('not in manifest')
        with self.assertRaises(R.ResourceError):R.validate(p['root'])

    def test_missing_file(self):
        p=self.make();(p['root']/'index.html').unlink()
        with self.assertRaises(R.ResourceError):R.validate(p['root'])

    def test_symlink_payload(self):
        p=self.make();f=p['root']/'index.html';outside=self.root/'outside';shutil.move(f,outside);f.symlink_to(outside)
        with self.assertRaises(R.ResourceError):R.validate(p['root'])

    def test_parent_path(self):
        p=self.make()
        with self.assertRaises(R.ResourceError):self.rewrite(p,lambda m:m['files'][0].update(path='../outside'))

    def test_unknown_field(self):
        p=self.make()
        with self.assertRaises(R.ResourceError):self.rewrite(p,lambda m:m.update(extra='unversioned extension'))

    def test_duplicate_json_keys(self):
        with self.assertRaises(R.ResourceError):R.loads('{"x":1,"x":2}')

    def test_nonfinite(self):
        for raw in ['NaN','Infinity','{"n":1e999}']:
            with self.assertRaises((R.ResourceError,ValueError)):
                value=R.loads(raw);R.schema_check(value,{})

    def test_duplicate_scene(self):
        p=self.make()
        with self.assertRaises(R.ResourceError):self.rewrite(p,lambda m:m['scenes'].append(m['scenes'][0]))

    def test_duplicate_file(self):
        p=self.make()
        with self.assertRaises(R.ResourceError):self.rewrite(p,lambda m:m['files'].append(m['files'][0]))

    def test_false_pass(self):
        p=self.make()
        with self.assertRaises(R.ResourceError):self.rewrite(p,lambda m:m['validation'][0].update(status='pass'))

    def test_stale_receipt(self):
        p=self.make()
        def edit(m):m['validation'][0].update(status='pass',checked_at=R.now(),evidence=['index.html'],tested_files=[{'path':'index.html','sha256':'0'*64}])
        with self.assertRaises(R.ResourceError):self.rewrite(p,edit)

    def test_valid_receipt(self):
        p=self.make()
        def edit(m):m['validation'][0].update(status='pass',checked_at=R.now(),evidence=['index.html'],tested_files=[{'path':'index.html','sha256':m['files'][0]['sha256']}])
        self.rewrite(p,edit)

    def test_boolean_not_numeric_default(self):
        p=self.make()
        with self.assertRaises(R.ResourceError):self.rewrite(p,lambda m:m['math']['parameters']['t'].update(default=True))

    def test_timestamp_order(self):
        p=self.make()
        with self.assertRaises(R.ResourceError):self.rewrite(p,lambda m:m.update(updated_at='2020-01-01T00:00:00Z'))

    def test_incomplete_timestamp(self):
        for value in ['2026-10-16Z','2026-10-16 01:00:00Z','2026-13-16T01:00:00Z','2026-10-16T01:00Z']:
            with self.assertRaises((R.ResourceError,ValueError)):R.timestamp(value)

    def test_identical_copies(self):
        p=self.make();self.register(p);target=self.root/'copy';shutil.copytree(p['root'],target);self.register(R.validate(target))
        with R.catalog(self.db) as db:self.assertEqual(db.execute('SELECT COUNT(*) FROM locations').fetchone()[0],2)

    def test_version_conflict(self):
        p=self.make();self.register(p);q=self.make(p['manifest']['asset_id'],title='different metadata')
        with self.assertRaises(R.ResourceError):self.register(q)
        self.assertEqual(self.resolve(R.reference(p['manifest']))['title'],'数学截面')

    def test_new_version(self):
        p=self.make();q=self.make(p['manifest']['asset_id'],'1.0.1');self.register(p,q)
        self.assertEqual(self.resolve(R.reference(q['manifest']))['package'],str(q['root']))
        self.assertEqual(self.resolve(R.reference(p['manifest']))['package'],str(p['root']))

    def test_batch_rollback(self):
        p=self.make();self.register(p);q=self.make();conflict=self.make(p['manifest']['asset_id'],title='conflict')
        self.cli('index',q['root'],conflict['root'],'--db',self.db,ok=False)
        with R.catalog(self.db) as db:self.assertEqual(db.execute('SELECT COUNT(*) FROM releases').fetchone()[0],1)

    def test_scene_resolve(self):
        p=self.make();self.register(p);r=self.resolve(R.reference(p['manifest'],'degenerate'))
        self.assertTrue(r['url'].endswith('#scene=degenerate'));self.assertEqual(r['scene']['state']['math']['t'],40)
        with self.assertRaises(R.ResourceError):self.resolve(R.reference(p['manifest'],'missing'))

    def test_unpinned_ref_rejected(self):
        with self.assertRaises(R.ResourceError):R.parse_ref('anatomy:'+str(uuid.uuid4()))

    def test_resolve_rechecks_files(self):
        p=self.make();self.register(p);(p['root']/'index.html').write_text('tampered')
        with self.assertRaises(R.ResourceError):self.resolve(R.reference(p['manifest']))

    def test_move(self):
        p=self.make();self.register(p);ref=R.reference(p['manifest'],'degenerate');target=self.root/'archive'/'moved'
        R.move(p['root'],target,self.db);r=self.resolve(ref)
        self.assertEqual(r['package'],str(target));self.assertEqual(r['manifest_sha256'],p['digest']);self.assertFalse(p['root'].exists())

    def test_move_rollback(self):
        p=self.make();self.register(p);target=self.root/'new'
        with patch.object(R,'register',side_effect=[None,R.ResourceError('injected database failure')]):
            with self.assertRaises(R.ResourceError):R.move(p['root'],target,self.db)
        self.assertTrue(p['root'].exists());self.assertFalse(target.exists())
        self.assertEqual(self.resolve(R.reference(p['manifest']))['package'],str(p['root']))

    def test_move_destination_exists(self):
        p=self.make();self.register(p);target=self.root/'exists';target.mkdir()
        with self.assertRaises(R.ResourceError):R.move(p['root'],target,self.db)
        self.assertTrue(p['root'].exists())

    def test_db_outside(self):
        p=self.make()
        with self.assertRaises(R.ResourceError):R.outside_db(p['root']/'db.sqlite',[p['root']])

    def test_finder_move_reindex(self):
        p=self.make();self.register(p);target=self.root/'finder';p['root'].rename(target)
        with self.assertRaises(R.ResourceError):self.resolve(R.reference(p['manifest']))
        self.register(R.validate(target));self.assertEqual(self.resolve(R.reference(p['manifest']))['package'],str(target))

    def test_export_import_roundtrip(self):
        p=self.make();self.register(p);z=self.root/'pack.zip';R.export_zip(p,z);dest=self.root/'imported';other=self.root/'other.sqlite'
        R.import_zip(z,dest,other);q=R.validate(dest);self.assertEqual(q['digest'],p['digest'])
        with R.catalog(other) as db:self.assertEqual(R.resolve(db,R.reference(p['manifest']))['package'],str(dest))

    def test_export_concurrent_change(self):
        p=self.make();dest=self.root/'changed.zip';original=zipfile.ZipFile.write
        def write(z,filename,arcname,*args,**kwargs):
            if arcname=='index.html':Path(filename).write_text('modified during export')
            return original(z,filename,arcname,*args,**kwargs)
        with patch.object(zipfile.ZipFile,'write',write):
            with self.assertRaises(R.ResourceError):R.export_zip(p,dest)
        self.assertFalse(dest.exists())

    def test_zip_traversal(self):
        z=self.root/'evil.zip'
        with zipfile.ZipFile(z,'w') as f:f.writestr('../escaped','bad')
        with self.assertRaises(R.ResourceError):R.import_zip(z,self.root/'dest',self.db)
        self.assertFalse((self.root/'escaped').exists());self.assertFalse((self.root/'dest').exists())

    def test_zip_duplicates(self):
        z=self.root/'duplicate.zip'
        with zipfile.ZipFile(z,'w') as f:
            f.writestr('one','a');f.writestr('one','b')
        with self.assertRaises(R.ResourceError):R.import_zip(z,self.root/'dest',self.db)

    def test_zip_symlink(self):
        z=self.root/'link.zip';info=zipfile.ZipInfo('link');info.create_system=3;info.external_attr=(0o120777<<16)
        with zipfile.ZipFile(z,'w') as f:f.writestr(info,'outside')
        with self.assertRaises(R.ResourceError):R.import_zip(z,self.root/'dest',self.db)

    def test_import_conflict_rolls_back(self):
        p=self.make();self.register(p);q=self.make(p['manifest']['asset_id'],title='conflict');z=self.root/'bad-version.zip';R.export_zip(q,z)
        with self.assertRaises(R.ResourceError):R.import_zip(z,self.root/'dest',self.db)
        self.assertFalse((self.root/'dest').exists())

    def test_rebuild(self):
        p=self.make();q=self.make();newdb=self.root/'rebuilt.sqlite'
        self.cli('rebuild',self.root,'--db',newdb)
        with R.catalog(newdb) as db:self.assertEqual(db.execute('SELECT COUNT(*) FROM releases').fetchone()[0],2)
        self.cli('rebuild',self.root,'--db',newdb,ok=False)

    def test_search_and_relation(self):
        p=self.make();target=R.reference(p['manifest'],'degenerate');q=self.make(relation=target);self.register(q)
        outgoing=self.cli('refs',R.reference(q['manifest']),'--db',self.db)['outgoing']
        self.assertFalse(outgoing[0]['target_indexed']);self.register(p)
        incoming=self.cli('refs',R.reference(p['manifest']),'--db',self.db)['incoming'];self.assertEqual(len(incoming),1)
        self.assertEqual(len(self.cli('list','--db',self.db,'--query','截面','--topic','立体几何')),2)

if __name__=='__main__':unittest.main()
