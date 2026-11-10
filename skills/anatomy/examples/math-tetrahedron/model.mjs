// Mathematical coordinates, independent of camera, DOM, animation and lesson state.
export const HALF = 40;
export const VERTICES = [[40,40,40],[40,-40,-40],[-40,40,-40],[-40,-40,40]];
export const EDGES = [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];

export function sectionAt(t) {
  if (typeof t !== 'number' || !Number.isFinite(t)) {
    return {kind:'invalid',points:[],area:null,sides:[],message:'请输入有限实数。'};
  }
  if (Math.abs(t) > HALF) {
    return {kind:'empty',points:[],area:0,sides:[],message:'平面位于四面体之外，交集为空。'};
  }
  if (Math.abs(t) === HALF) {
    const indices = t > 0 ? [0,3] : [1,2];
    return {kind:'segment',points:indices.map(i=>[...VERTICES[i]]),area:0,
      sides:[],message:'截面退化为一条棱，面积为 0。'};
  }
  const points = [[40,t,t],[t,40,t],[-40,-t,t],[-t,-40,t]];
  const sides = [Math.SQRT2*(40-t),Math.SQRT2*(40+t)];
  return {kind:t===0?'square':'rectangle',points,sides,area:2*(40-t)*(40+t),
    message:t===0?'中截面是正方形，面积达到最大值。':'截面是长方形；相邻边分别平行于两条对棱。'};
}
