// Make a portable draft package. Seal only after recording the remaining real checks.
import {readFileSync,writeFileSync,mkdirSync,copyFileSync,existsSync,readdirSync} from 'node:fs';
import {dirname,join,resolve,basename} from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
const here=dirname(fileURLToPath(import.meta.url));
const root=resolve(here,'../..');
const at=process.argv.indexOf('--out');
if(at<0||!process.argv[at+1])throw new Error('Usage: node package.mjs --out <empty-directory>');
const out=resolve(process.argv[at+1]);
const metadata=join(dirname(out),basename(out)+'.metadata.json');
if(existsSync(metadata)||(existsSync(out)&&readdirSync(out).length))throw new Error('Output/metadata already exists');
mkdirSync(out,{recursive:true});
execFileSync(process.execPath,[join(here,'build.mjs'),'--out',out]);
copyFileSync(join(out,'tetrahedron-section.html'),join(out,'index.html'));
// Remove only the duplicate this build just created.
const {unlinkSync}=await import('node:fs');unlinkSync(join(out,'tetrahedron-section.html'));
const sources=['examples/math-tetrahedron/package.mjs','references/resource-package.md','references/question-bindings.md','schemas/manifest-v1.1.schema.json','schemas/question-bindings-v1.schema.json','scripts/question_bindings.py','examples/math-tetrahedron/state-contract.json','schemas/manifest-v1.schema.json','scripts/resources.py','examples/math-tetrahedron/build.mjs','examples/math-tetrahedron/model.mjs','examples/math-tetrahedron/check.mjs','examples/math-tetrahedron/scenes.json','examples/math-tetrahedron/CONCEPT.md','scripts/inline-kit.mjs','kit/iso-kit.mjs','LICENSE'];
for(const name of sources){const dest=join(out,'source',name);mkdirSync(dirname(dest),{recursive:true});copyFileSync(join(root,name),dest)}
mkdirSync(join(out,'evidence'),{recursive:true});
writeFileSync(join(out,'evidence/model.json'),execFileSync(process.execPath,[join(here,'check.mjs')]));
const hash=path=>createHash('sha256').update(readFileSync(join(out,path))).digest('hex');
const names=['index.html',...sources.map(s=>'source/'+s),'evidence/model.json'];
const stamp=new Date().toISOString();
const option=(flag,fallback)=>{const i=process.argv.indexOf(flag);if(i>=0&&!process.argv[i+1])throw new Error(flag+' requires value');return i>=0?process.argv[i+1]:fallback};
const assetId=option('--asset-id','ee8d0713-4f88-44d6-88da-57e9d25aef21');
const version=option('--version','1.1.0');
const checks=['mathematics','interaction','visual','offline'].map(kind=>({kind,status:kind==='mathematics'?'pass':'pending',scope:kind==='mathematics'?'151 checks: equal edges, edge/plane incidence, orthogonality, independent cross-product area and invalid input.':'Not yet checked for this package.',evidence:kind==='mathematics'?['evidence/model.json']:[],...(kind==='mathematics'?{checked_at:stamp,tested_files:['source/examples/math-tetrahedron/model.mjs','source/examples/math-tetrahedron/check.mjs'].map(path=>({path,sha256:hash(path)}))}:{})}));
const m={schema_version:'1.1',state_link:'hash-json-v1',...JSON.parse(readFileSync(join(here,'state-contract.json'),'utf8')),asset_id:assetId,version,slug:'tetrahedron-parallel-sections',title:'正四面体平行截面：形状、边长与面积',language:'zh-CN',created_at:stamp,updated_at:stamp,contributors:[{name:'Codex',role:'author'}],rights:{license:'LicenseRef-User-Controlled',attribution:'作品使用与外发遵循所有者授权；source/LICENSE 保留 Anatomy kit 的 MIT 许可。'},math:{topics:['立体几何','截面','参数分类讨论'],audience:['高中'],objects:['正四面体','水平截平面','长方形截面'],conditions:['顶点 A(40,40,40), B(40,-40,-40), C(-40,40,-40), D(-40,-40,40)。','截平面 z=t；非退化截面条件为 -40<t<40。'],learning_goals:['区分空间投影与截面真实形状','用临界值分类截面','用空间向量与边长推导面积'],parameters:{t:{type:'number',domain:'所有有限实数；|t|>40 时交集为空，|t|=40 时退化。',display_range:[-50,50],default:0,unit:'任意统一长度单位'}},approximation:'模型使用未舍入浮点数；一般读数显示四位小数，极小非零值使用科学记数法。'},entrypoints:{html:'index.html'},files:names.map(path=>({path,role:path==='index.html'?'runtime':path.startsWith('evidence/')?'evidence':path.endsWith('LICENSE')?'license':'source',sha256:hash(path),bytes:readFileSync(join(out,path)).length})),scenes:JSON.parse(readFileSync(join(here,'scenes.json'),'utf8')),provenance:{sources:[{title:'Anatomy 数学分支：正四面体坐标模型',note:'本地示例的坐标推导与检验；原始机械绘图 kit 许可见 source/LICENSE。'}],relations:[]},validation:checks,extensions:{}};
writeFileSync(metadata,JSON.stringify(m,null,2)+'\n');
console.log(JSON.stringify({package:out,metadata,next:'Record actual checks, then seal with scripts/resources.py.'}));
