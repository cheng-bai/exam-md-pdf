"""Behavioral regression for question associations and transfer portability."""
import test_resources as fixtures
R=fixtures.R
import copy
import json
from pathlib import Path
import sqlite3
import unittest
import uuid
import zipfile
from types import SimpleNamespace

class BindingTests(unittest.TestCase):
    setUp=fixtures.ResourceTests.setUp
    tearDown=fixtures.ResourceTests.tearDown
    make=fixtures.ResourceTests.make
    rewrite=fixtures.ResourceTests.rewrite
    register=fixtures.ResourceTests.register
    cli=fixtures.ResourceTests.cli

    def package(self):
        p=self.make()
        contract={'math':{'t':{'type':'number'}},'view':{'azimuth':{'type':'number','minimum':5,'maximum':175}},'lesson':{'step':{'type':'integer','enum':[0,1,2]}}}
        return self.rewrite(p,lambda m:m.update(schema_version='1.1',state_link='hash-json-v1',default_state={'math':{'t':0},'view':{'azimuth':35},'lesson':{'step':0}},state_contract=contract))

    def draft(self,p,**kwargs):
        b=dict(question_namespace='school.math',question_id='000123',subquestion_id='2',asset_id=p['manifest']['asset_id'],asset_version=p['manifest']['version'],scene_id='degenerate',initial_state={'math':{'t':10},'view':{'azimuth':130},'lesson':{'step':2}},created_by='Test author')
        b.update(kwargs);path=self.root/(str(uuid.uuid4())+'.draft.json');path.write_text(R.dump(b));return path

    def bind(self,p,**kw):
        self.register(p);return self.cli('bind','--file',self.draft(p,**kw),'--db',self.db)

    def records(self):return self.cli('bindings','--db',self.db)

    def test_bidirectional_namespace_subquestion(self):
        p=self.package();b=self.bind(p)
        self.bind(p,question_namespace='other.math');self.bind(p,subquestion_id='3')
        self.assertEqual(len(self.cli('bindings','--question-namespace','school.math','--question-id','000123','--db',self.db)),2)
        self.assertEqual(len(self.cli('bindings','--question-namespace','school.math','--question-id','000123','--subquestion-id','2','--db',self.db)),1)
        self.assertEqual(len(self.cli('bindings','--reference',R.reference(p['manifest']),'--db',self.db)),3)
        self.assertEqual(b['question_id'],'000123')
        self.cli('bindings','--question-id','000123','--db',self.db,ok=False)

    def test_many_to_many_pinned_versions(self):
        p=self.package();self.bind(p);q=self.make(p['manifest']['asset_id'],version='2.0.0');self.bind(q,initial_state={});self.bind(p,question_id='000124')
        self.assertEqual(len(self.records()),3)
        self.assertEqual(len(self.cli('bindings','--reference',R.reference(p['manifest']),'--db',self.db)),2)

    def test_merge_and_move(self):
        p=self.package();b=self.bind(p,initial_state={'math':{'t':10}})
        result=self.cli('resolve-binding',b['binding_id'],'--db',self.db)
        self.assertEqual(result['effective_state'],{'math':{'t':10},'view':{'azimuth':35},'lesson':{'step':0}})
        self.assertIn('state=',result['url']);target=self.root/'moved';self.cli('move',p['root'],target,'--db',self.db)
        self.assertEqual(self.cli('resolve-binding',b['binding_id'],'--db',self.db)['package'],str(target))

    def test_old_scene_compatible(self):
        p=self.make();b=self.bind(p,initial_state={})
        result=self.cli('resolve-binding',b['binding_id'],'--db',self.db)
        self.assertTrue(result['url'].endswith('#scene=degenerate'));self.assertEqual(result['effective_state']['math']['t'],40)

    def test_old_override_rejected(self):
        p=self.make();self.register(p);self.cli('bind','--file',self.draft(p),'--db',self.db,ok=False)
        self.assertEqual(self.records(),[])

    def test_invalid_bindings_atomic(self):
        p=self.package();self.register(p)
        bad=[{'scene_id':'missing'},{'initial_state':{'math':{'unknown':1}}},{'initial_state':{'math':{'t':True}}},
             {'initial_state':{'view':{'azimuth':176}}},{'initial_state':{'lesson':{'step':3}}},
             {'initial_state':{'lesson':{'step':1.2}}},{'initial_state':{'nope':{}}},
             {'asset_manifest_sha256':'0'*64},{'question_id':123},{'question_namespace':'bad space'},
             {'asset_version':'latest'},{'created_by':''},{'subquestion_id':''}]
        for kwargs in bad:
            with self.subTest(kwargs=kwargs):self.cli('bind','--file',self.draft(p,**kwargs),'--db',self.db,ok=False)
        self.assertEqual(self.records(),[])
        self.assertFalse(list(Path(str(self.db)+'.bindings').glob('*.json')))

    def test_binding_id_immutable_idempotent(self):
        p=self.package();b=self.bind(p);source=self.root/'collection.json';source.write_text(R.dump({'schema_version':'1.0','bindings':[b]}))
        self.cli('bindings-import',source,'--db',self.db);self.assertEqual(len(self.records()),1)
        reordered=dict(reversed(list(b.items())));source.write_text(R.dump({'schema_version':'1.0','bindings':[reordered]}));self.cli('bindings-import',source,'--db',self.db)
        b['question_id']='other';source.write_text(R.dump({'schema_version':'1.0','bindings':[b]}));self.cli('bindings-import',source,'--db',self.db,ok=False)
        self.assertEqual(self.records()[0]['question_id'],'000123')

    def test_records_export_import_and_rebuild(self):
        p=self.package();b=self.bind(p);out=self.root/'bindings.json';self.cli('bindings-export','--out',out,'--db',self.db)
        target=self.root/'other.sqlite';self.cli('index',p['root'],'--db',target);self.cli('bindings-import',out,'--db',target)
        self.assertEqual(self.cli('bindings','--db',target),[b])
        new=self.root/'rebuilt.sqlite';self.cli('rebuild',p['root'],'--bindings',str(self.db)+'.bindings','--db',new)
        self.assertEqual(self.cli('resolve-binding',b['binding_id'],'--db',new)['effective_state']['math']['t'],10)

    def test_transfer_roundtrip(self):
        p=self.package();b=self.bind(p);archive=self.root/'transfer.zip'
        self.cli('export',R.reference(p['manifest']),'--with-bindings','--out',archive,'--db',self.db)
        target=self.root/'other.sqlite';dest=self.root/'imported';self.cli('import',archive,dest,'--db',target)
        self.assertEqual(R.validate(dest)['digest'],p['digest'])
        self.assertEqual(self.cli('bindings','--db',target),[b])
        self.assertEqual(self.cli('resolve-binding',b['binding_id'],'--db',target)['effective_state']['math']['t'],10)
        self.cli('import',archive,self.root/'copy','--db',target);self.assertEqual(len(self.cli('bindings','--db',target)),1)

    def test_corrupt_transfer_rolls_back(self):
        p=self.package();self.bind(p);archive=self.root/'good.zip';self.cli('export',R.reference(p['manifest']),'--with-bindings','--out',archive,'--db',self.db)
        bad=self.root/'bad.zip'
        with zipfile.ZipFile(archive) as src,zipfile.ZipFile(bad,'w') as dst:
            for name in src.namelist():dst.writestr(name,b'{}' if name=='question-bindings.json' else src.read(name))
        dest=self.root/'bad-dest';other=self.root/'other.sqlite';self.cli('import',bad,dest,'--db',other,ok=False)
        self.assertFalse(dest.exists());self.assertFalse(Path(str(other)+'.bindings').exists())

    def test_transfer_binding_conflict_rolls_back(self):
        p=self.package();b=self.bind(p);archive=self.root/'transfer.zip';self.cli('export',R.reference(p['manifest']),'--with-bindings','--out',archive,'--db',self.db)
        other=self.root/'other.sqlite';self.cli('index',p['root'],'--db',other)
        altered=copy.deepcopy(b);altered['note']='conflict';source=self.root/'conflict.json';source.write_text(R.dump({'schema_version':'1.0','bindings':[altered]}));self.cli('bindings-import',source,'--db',other)
        dest=self.root/'reject';self.cli('import',archive,dest,'--db',other,ok=False);self.assertFalse(dest.exists())
        self.assertEqual(self.cli('bindings','--db',other)[0]['note'],'conflict')

    def test_batch_bindings_roll_back(self):
        p=self.package();b=self.bind(p);fresh=copy.deepcopy(b);fresh['binding_id']=str(uuid.uuid4());bad=copy.deepcopy(b);bad['binding_id']=str(uuid.uuid4());bad['scene_id']='missing'
        source=self.root/'bad-batch.json';source.write_text(R.dump({'schema_version':'1.0','bindings':[fresh,bad]}));self.cli('bindings-import',source,'--db',self.db,ok=False)
        self.assertEqual(len(self.records()),1);self.assertFalse((Path(str(self.db)+'.bindings')/(fresh['binding_id']+'.json')).exists())

    def test_migration_preserves_and_backs_up(self):
        p=self.make();self.register(p)
        with sqlite3.connect(self.db) as db:
            db.executescript("DROP TABLE question_bindings; DELETE FROM catalog_meta WHERE key='question_bindings';")
        db.close()
        self.cli('bind','--file',self.draft(p,initial_state={}), '--db',self.db,ok=False)
        result=self.cli('migrate','--db',self.db);self.assertTrue(Path(result['backup']).exists())
        self.assertEqual(len(self.cli('list','--db',self.db)),1)
        self.assertTrue(self.cli('migrate','--db',self.db)['already_current'])
        self.bind(p,initial_state={})

    def test_manifest_contract_rejects_bad_scene(self):
        p=self.package()
        with self.assertRaises(R.ResourceError):self.rewrite(p,lambda m:m['scenes'][0]['state']['view'].update(azimuth=200))

    def test_resolve_rechecks_payload(self):
        p=self.package();b=self.bind(p);(p['root']/'index.html').write_text('tampered')
        self.cli('resolve-binding',b['binding_id'],'--db',self.db,ok=False)
        self.cli('bindings-export','--out',self.root/'bad.json','--db',self.db,ok=False)

    def test_exports_cannot_modify_any_sealed_package(self):
        p=self.package();self.bind(p);other=self.package();self.register(other)
        for package in (p,other):
            self.cli('bindings-export','--out',package['root']/'oops.json','--db',self.db,ok=False)
            for option in ([],['--with-bindings']):
                self.cli('export',R.reference(p['manifest']),*option,'--out',package['root']/'oops.zip','--db',self.db,ok=False)
            self.assertEqual(R.validate(package['root'])['digest'],package['digest'])

    def test_late_fact_conflict_cleans_new_files(self):
        p=self.package();b=self.bind(p)
        fresh=copy.deepcopy(b);fresh['binding_id']=str(uuid.uuid4())
        conflict=copy.deepcopy(b);conflict['binding_id']=str(uuid.uuid4())
        folder=Path(str(self.db)+'.bindings');badpath=folder/(conflict['binding_id']+'.json');badpath.write_text('{}')
        source=self.root/'late-conflict.json';source.write_text(R.dump({'schema_version':'1.0','bindings':[fresh,conflict]}))
        self.cli('bindings-import',source,'--db',self.db,ok=False)
        self.assertEqual(len(self.records()),1);self.assertFalse((folder/(fresh['binding_id']+'.json')).exists());self.assertEqual(badpath.read_text(),'{}')

    def test_read_only_does_not_create_missing_index(self):
        missing=self.root/'missing.sqlite';self.cli('bindings','--db',missing,ok=False);self.assertFalse(missing.exists())

if __name__=='__main__':unittest.main()
