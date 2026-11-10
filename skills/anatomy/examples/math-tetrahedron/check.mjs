import assert from 'node:assert/strict';
import {sectionAt,VERTICES,EDGES} from './model.mjs';

let count=0;
const near=(a,b,eps=1e-8)=>{assert.ok(Math.abs(a-b)<=eps,`${a} != ${b}`);count++;};
const dist=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
for(const [i,j] of EDGES) near(dist(VERTICES[i],VERTICES[j]),80*Math.SQRT2);
for(const [t,kind,area] of [[0,'square',3200],[20,'rectangle',2400],[-20,'rectangle',2400],
  [40,'segment',0],[-40,'segment',0],[41,'empty',0],[-41,'empty',0]]) {
  const r=sectionAt(t);assert.equal(r.kind,kind);count++;near(r.area,area);
}
for(const x of [NaN,Infinity,-Infinity,'20',null]) {assert.equal(sectionAt(x).kind,'invalid');count++;}
// Independent geometric relations, not a repetition of the area formula.
for(const t of [-40+1e-7,-39,-20,-.01,0,.01,20,39,40-1e-7]) {
  const r=sectionAt(t), p=r.points;
  assert.equal(p.length,4);count++;
  for(const point of p) {
    near(point[2],t);
    assert.ok(EDGES.some(([i,j])=>Math.abs(dist(VERTICES[i],point)+dist(point,VERTICES[j])-
      dist(VERTICES[i],VERTICES[j]))<1e-8));count++;
  }
  const u=p[1].map((x,i)=>x-p[0][i]),v=p[3].map((x,i)=>x-p[0][i]);
  near(u.reduce((s,x,i)=>s+x*v[i],0),0);
  const cross=[u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]];
  near(Math.hypot(...cross),r.area);
  near(dist(p[0],p[1]),r.sides[0]);near(dist(p[0],p[3]),r.sides[1]);
  near(sectionAt(-t).area,r.area);
}
console.log(JSON.stringify({status:'PASS',checks:count,scope:'math model; not browser interaction'},null,2));
