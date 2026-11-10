import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {dirname,join,resolve} from 'node:path';
import {fileURLToPath} from 'node:url';
import {kitScript} from '../../scripts/inline-kit.mjs';
const here=dirname(fileURLToPath(import.meta.url));
const at=process.argv.indexOf('--out');
if(at>=0&&!process.argv[at+1]) throw new Error('--out requires an output directory');
const out=at>=0?resolve(process.argv[at+1]):here;
mkdirSync(out,{recursive:true});
const scenes=JSON.parse(readFileSync(join(here,'scenes.json'),'utf8'));
const contract=JSON.parse(readFileSync(join(here,'state-contract.json'),'utf8'));
const model=readFileSync(join(here,'model.mjs'),'utf8').replace(/^export /gm,'');

function mount(scenes,contract){
  const mathState={t:0},viewState={azimuth:35},lessonState={step:0};
  const $=id=>document.getElementById(id);
  const fmt=x=>x!==0&&Math.abs(x)<0.0001?x.toExponential(4):Number(x.toFixed(4)).toString();
  const line=(a,b,cls,P)=>`<path class="${cls}" d="${pathOf([iso(a,P),iso(b,P)])}"/>`;
  const centroid=ps=>[0,1,2].map(i=>ps.reduce((sum,p)=>sum+p[i],0)/ps.length);
  const types={square:'正方形',rectangle:'长方形',segment:'退化线段',empty:'空集',invalid:'输入无效'};
  const steps=['移动截面，比较三维投影与右侧正视图。',
    '在非退化截面内，相邻边向量的数量积为 0；两条边分别平行于一组对棱。',
    '非退化时，把两条边长相乘，得到面积公式；中截面面积最大。'];
  function render(){
    const r=sectionAt(mathState.t);
    const P=fitProjection(VERTICES,620,440,{pad:55,azimuth:viewState.azimuth,elevation:26});
    const faces=[[0,1,2],[0,3,1],[0,2,3],[1,3,2]].map(ids=>ids.map(i=>VERTICES[i]));
    faces.sort((a,b)=>depthOf(centroid(a),P)-depthOf(centroid(b),P));
    let drawing=faces.map(ps=>`<path class="face" d="${pathOf(ps.map(p=>iso(p,P)),true)}"/>`).join('');
    drawing+=EDGES.map(([i,j])=>line(VERTICES[i],VERTICES[j],'edge',P)).join('');
    if(r.points.length>=3) drawing+=`<path class="section" d="${pathOf(r.points.map(p=>iso(p,P)),true)}"/>`;
    if(r.kind==='segment') drawing+=line(...r.points,'section-line',P);
    if(lessonState.step===2&&r.points.length===4) {
      drawing+=line(r.points[0],r.points[2],'aux',P)+line(r.points[1],r.points[3],'aux',P);
    }
    VERTICES.forEach((p,i)=>{
      const [x,y]=iso(p,P);
      drawing+=`<circle class="vertex" cx="${x}" cy="${y}" r="3"/><text x="${x+9}" y="${y-8}">${'ABCD'[i]}</text>`;
    });
    $('space-art').innerHTML=drawing;
    const q=p=>[170+p[0]*2.4,170-p[1]*2.4]; // same x/y scale, fixed across all states
    let flat='<path class="axis" d="M35 170H305 M170 35V305"/>';
    if(r.points.length===4) flat+=`<path class="section" d="${pathOf(r.points.map(q),true)}"/>`;
    if(r.kind==='segment') flat+=`<path class="section-line" d="${pathOf(r.points.map(q))}"/>`;
    r.points.forEach(p=>{const [x,y]=q(p);flat+=`<circle class="vertex" cx="${x}" cy="${y}" r="3"/>`;});
    $('flat-art').innerHTML=flat;
    $('kind').textContent=types[r.kind];
    $('area').textContent=r.area===null?'—':fmt(r.area);
    $('height').textContent=Number.isFinite(mathState.t)?String(mathState.t):'—';
    $('side-a').textContent=r.sides.length?fmt(r.sides[0]):'—';
    $('side-b').textContent=r.sides.length?fmt(r.sides[1]):'—';
    $('message').textContent=r.message;
    $('step-text').textContent=steps[lessonState.step];
    $('derivation').hidden=lessonState.step!==2;
    $('side-formulas').hidden=lessonState.step===0;
    $('angle-output').textContent=viewState.azimuth+'°';
    $('status').dataset.kind=r.kind;
    const snapshot=JSON.stringify({math:{...mathState},view:{...viewState},lesson:{...lessonState},result:r});
    $('demo').dataset.state=snapshot; // inspectable read-only snapshot; not a second state store
  }
  function setT(t,{syncInput=true}={}){
    mathState.t=t;
    $('t-range').value=Number.isFinite(t)?String(Math.max(-50,Math.min(50,t))):'0';
    if(syncInput) $('t-input').value=Number.isFinite(t)?String(t):'';
    render();
  }
  $('t-range').addEventListener('input',e=>setT(Number(e.target.value)));
  $('t-input').addEventListener('input',e=>setT(e.target.value.trim()===''?NaN:Number(e.target.value),{syncInput:false}));
  document.querySelectorAll('[data-t]').forEach(b=>b.addEventListener('click',()=>setT(Number(b.dataset.t))));
  $('angle').addEventListener('input',e=>{viewState.azimuth=Number(e.target.value);render();});
  $('reset-view').addEventListener('click',()=>{viewState.azimuth=35;$('angle').value='35';render();});
  $('step').addEventListener('change',e=>{lessonState.step=Number(e.target.value);render();});
  $('reset').addEventListener('click',()=>{
    viewState.azimuth=35;lessonState.step=0;$('angle').value='35';$('step').value='0';setT(0);
  });
  $('theme').addEventListener('click',()=>{
    const dark=document.documentElement.dataset.theme!=='dark';
    document.documentElement.dataset.theme=dark?'dark':'light';
    $('theme').textContent=dark?'切换浅色':'切换深色';
  });
  function applyScene(){
    const params=new URLSearchParams(location.hash.slice(1));
    const id=params.get('scene'),scene=scenes.find(s=>s.id===id);
    let merged=structuredClone(contract.default_state);
    try {
      if(id&&!scene)throw new Error('未找到场景：'+id);
      const override=params.has('state')?JSON.parse(params.get('state')):{};
      for(const source of [scene?.state??{},override]){
        if(!source||typeof source!=='object'||Array.isArray(source))throw new Error('初始状态格式无效');
        for(const [group,values] of Object.entries(source)){
          const rules=contract.state_contract[group];
          if(!rules||!values||typeof values!=='object'||Array.isArray(values))throw new Error('状态分组无效');
          for(const [key,value] of Object.entries(values)){
            const rule=Object.hasOwn(rules,key)?rules[key]:null;
            if(!rule)throw new Error('未知参数：'+key);
            const valid=rule.type==='integer'?Number.isInteger(value):rule.type==='number'?typeof value==='number'&&Number.isFinite(value):typeof value===rule.type;
            if(!valid||('minimum' in rule&&value<rule.minimum)||('maximum' in rule&&value>rule.maximum)||(rule.enum&&!rule.enum.includes(value)))throw new Error('参数无效：'+key);
            merged[group][key]=value;
          }
        }
      }
      $('scene-message').textContent='';
    }catch(error){
      merged=structuredClone(contract.default_state);
      $('scene-message').textContent=error.message+'。已显示默认状态。';
    }
    Object.assign(viewState,merged.view);Object.assign(lessonState,merged.lesson);
    $('angle').value=String(viewState.azimuth);$('step').value=String(lessonState.step);
    setT(merged.math.t);
  }
  window.addEventListener('hashchange',applyScene);
  applyScene();
}

// HTML parses script end tags before JavaScript strings; the kit includes pageHtml().
const runtime=`${kitScript()}\n${model}\n(${mount.toString()})(${JSON.stringify(scenes)},${JSON.stringify(contract)});`.replace(/<\/script/gi,'<\\/script');
const html=`<!doctype html><html lang="zh-CN" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>正四面体的平行截面 · Anatomy 数学交互</title><link rel="icon" href="data:,"><style>
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.7 system-ui,-apple-system,"PingFang SC",sans-serif}html{--bg:#f1f4ef;--card:#fff;--ink:#20383e;--muted:#607176;--accent:#087f78;--line:#c4d3ce;--fill:#19b3a0}html[data-theme=dark]{--bg:#10252b;--card:#19333a;--ink:#e7f3ee;--muted:#bad1cc;--accent:#58d7c4;--line:#45646a;--fill:#3ed8bf}main{max-width:1120px;margin:36px auto;padding:0 22px}h1{font-size:30px;line-height:1.35;margin:10px 0}p{margin:10px 0}.subtitle{color:var(--muted)}.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;margin:22px 0}.topline{display:flex;justify-content:space-between;gap:12px;align-items:center}.topline small{letter-spacing:.08em;color:var(--muted)}.figures{display:grid;grid-template-columns:1.65fr 1fr;align-items:center;gap:18px}figure{margin:0;min-width:0}svg{display:block;width:100%;height:auto;overflow:hidden}figcaption{color:var(--muted);font-size:14px;text-align:center}svg text{font:17px system-ui;fill:var(--ink)}.face{fill:var(--ink);fill-opacity:.035;stroke:none}.edge{stroke:var(--ink);stroke-width:1.6;fill:none}.section{stroke:var(--accent);stroke-width:2.5;fill:var(--fill);fill-opacity:.28}.section-line{stroke:var(--accent);stroke-width:4;fill:none}.vertex{fill:var(--ink)}.axis{stroke:var(--line);stroke-width:1;fill:none}.aux{stroke:var(--accent);stroke-width:1.4;stroke-dasharray:5 5;fill:none}.controls{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:22px}label{display:block;font-weight:600;margin-bottom:8px}input[type=range]{width:100%;accent-color:var(--accent)}input[type=number],select,button{font:inherit;background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:6px;padding:8px 12px}input[type=number]{width:110px}button{cursor:pointer}button:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid var(--accent);outline-offset:3px}.row{display:flex;gap:9px;align-items:center;flex-wrap:wrap;margin:10px 0}.preset{padding:7px 10px;font-size:14px}.readout{display:flex;gap:18px;flex-wrap:wrap;background:var(--bg);padding:14px 16px;border-radius:8px;margin-top:18px}.readout strong{color:var(--accent)}.hint{font-size:14px;color:var(--muted)}math{font-size:1.1em}math[display=block]{margin:16px 0}#status{border-left:4px solid var(--accent);padding-left:14px}#message{font-weight:600}@media(max-width:650px){main{margin:20px auto;padding:0 14px}h1{font-size:24px}.card{padding:15px}.figures,.controls{grid-template-columns:1fr}.figures{gap:24px}figure:nth-child(2){max-width:280px;margin:auto;width:100%}.topline{align-items:flex-start}button{min-height:42px}.readout{gap:10px 16px}}
</style></head><body><main id="demo"><div class="topline"><small>ANATOMY · 数学交互小样</small><button id="theme">切换深色</button></div><h1>移动一个平面，四面体截面怎样变化？</h1><p class="subtitle">比较位置、形状和面积；转动视角只改变你看到的投影。</p>
<p id="scene-message" role="alert"></p><section class="card"><div class="figures"><figure><svg id="space-art" viewBox="0 0 620 440" role="img" aria-label="正四面体与水平截面的正交投影"></svg><figcaption>半透明立体，所有棱均显示；屏幕投影角度不是真实空间夹角。</figcaption></figure><figure><svg id="flat-art" viewBox="0 0 340 340" role="img" aria-label="截面在自身平面内的等比例正视图"></svg><figcaption>截面正视图 · 横纵比例相同</figcaption></figure></div>
<div class="controls"><div><label for="t-range">截平面高度 t（任意统一长度单位）</label><input id="t-range" type="range" min="-50" max="50" step="0.1" value="0"><div class="row"><label for="t-input">精确输入</label><input id="t-input" type="number" step="any" value="0"></div><p class="hint">滑块演示 −50 到 50；数值输入接受任意有限实数。</p><div class="row"><button class="preset" data-t="0">正方形 t=0</button><button class="preset" data-t="20">长方形 t=20</button><button class="preset" data-t="40">退化 t=40</button><button class="preset" data-t="45">空集 t=45</button></div></div><div><label for="angle">视角方位角 <output id="angle-output"></output></label><input id="angle" type="range" min="5" max="175" step="1" value="35"><div class="row"><button id="reset-view">重置视角</button><button id="reset">全部重置</button></div><label for="step">讲解步骤</label><select id="step"><option value="0">1 · 观察截面</option><option value="1">2 · 判断边长</option><option value="2">3 · 推导面积</option></select></div></div>
<div class="readout" id="status" role="status" aria-live="polite"><span>高度 <strong id="height"></strong></span><span>截面 <strong id="kind"></strong></span><span>面积 <strong id="area"></strong> 平方单位</span><span>相邻边长 <strong id="side-a"></strong>、<strong id="side-b"></strong></span></div><p id="message"></p><p class="hint">边长与面积通常显示到小数点后四位；极小非零值用科学记数法，模型使用未舍入值。</p></section>
<section class="card"><h2>观察之后，怎样证明？</h2><p id="step-text"></p><p>四顶点坐标为 A(40,40,40)、B(40,−40,−40)、C(−40,40,−40)、D(−40,−40,40)，六条棱等长。</p><p>在截平面 <math aria-label="z等于t"><mi>z</mi><mo>=</mo><mi>t</mi></math> 内，四个交点为 (40,t,t)、(t,40,t)、(−40,−t,t)、(−t,−40,t)。此四点表达式仅用于 <math aria-label="负40小于t小于40"><mo>−</mo><mn>40</mn><mo>&lt;</mo><mi>t</mi><mo>&lt;</mo><mn>40</mn></math>。</p>
<div id="side-formulas" hidden><p>仅对上述非退化区间，相邻边向量数量积为 0，因此截面为长方形。两条边长为：</p><math display="block" aria-label="根号2乘以40减t，与根号2乘以40加t"><mrow><msqrt><mn>2</mn></msqrt><mo>(</mo><mn>40</mn><mo>−</mo><mi>t</mi><mo>)</mo><mo>,</mo><mspace width="1em"/><msqrt><mn>2</mn></msqrt><mo>(</mo><mn>40</mn><mo>+</mo><mi>t</mi><mo>)</mo></mrow></math></div>
<div id="derivation" hidden><math display="block" aria-label="面积等于2乘1600减t平方"><mi>S</mi><mo>=</mo><mn>2</mn><mo>(</mo><mn>1600</mn><mo>−</mo><msup><mi>t</mi><mn>2</mn></msup><mo>)</mo></math><p>t=0 时两边相等；t=±40 时退化为棱；平面在此范围之外时交集为空。上面的面积式只用于非退化截面及其边界，不能代入范围外得到负面积。</p></div><p class="hint">交互用于观察；坐标求交、数量积与边长推导给出上述结论的数学依据。</p></section></main>
<script>(()=>{${runtime}})();</script></body></html>`;
const target=join(out,'tetrahedron-section.html');
writeFileSync(target,html);
console.log(target);
