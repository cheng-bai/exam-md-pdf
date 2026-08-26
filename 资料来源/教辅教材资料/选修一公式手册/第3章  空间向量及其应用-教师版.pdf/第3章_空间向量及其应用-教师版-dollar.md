## 第3章 空间向量及其应用

### 3.1 空间向量及其运算

1. 共面向量的概念: 如果一组向量可以平移到同一个平面上, 那么称这组向量是 共面 的. 显然, 任意 两个向量都是共面的.

2. 空间向量平行 (共线) 的充要条件 (亦可称 “向量共线定理”): 空间中的向量 $\overrightarrow{b}$ 与非零向量 $\overrightarrow{a}$ 平行的充要条件是存在实数 $\lambda$ ,使得 $\overrightarrow{b} = \lambda \overrightarrow{a}$ .

### 3.2 空间向量基本定理

#### 3.2.1 向量共面的充要条件

1. 向量共面的充要条件: 如果 ${\overrightarrow{e}}_{1}$ 与 ${\overrightarrow{e}}_{2}$ 是两个不平行的向量,那么空间中的向量 $\overrightarrow{a}$ 与 ${\overrightarrow{e}}_{1}\text{ 、 }{\overrightarrow{e}}_{2}$ 共面的充要条件是,存在唯一的一对实数 $\lambda$ 与 $\mu$ ,使得 $\overrightarrow{a} = \lambda {\overrightarrow{e}}_{1} + \mu {\overrightarrow{e}}_{2}$ .

2. 拓展:空间一点 $P$ 在平面 ${ABC}$ 上的充要条件是对平面 ${ABC}$ 外任意一点 $O$ ，有 $\overrightarrow{OP} = x\overrightarrow{OA} + y\overrightarrow{OB} + z\overrightarrow{OC}$ 其中 $x + y + z = 1$ .

#### 3.2.2 空间向量基本定理

1. 空间向量基本定理: 如果 ${\overrightarrow{e}}_{1}\text{ 、 }{\overrightarrow{e}}_{2}$ 与 ${\overrightarrow{e}}_{3}$ 是不共面的向量,那么对空间中任意一个向量 $\overrightarrow{a}$ ,存在唯一的一组实数 $\lambda \text{ 、 }\mu$ 与 $\nu$ ,使得 $\overrightarrow{a} = \lambda {\overrightarrow{e}}_{1} + \mu {\overrightarrow{e}}_{2} + \nu {\overrightarrow{e}}_{3}$ .

### 3.3 空间向量的坐标表示

#### 3.3.1 空间直角坐标系

1. 点 $O$ 叫做坐标原点，三条坐标轴分别是横轴 (即 $x$ 轴)、纵轴 (即 $y$ 轴) 与竖轴 (即 $z$ 轴). 约定坐标系采用 右手制，即右手翘起拇指、其他四指握拳做“点赞”状，当四指所指的方向是 $x$ 轴正方向到 $y$ 轴正方向的旋转方向时，拇指所指为 $z$ 轴正方向.

2. 通过每两个坐标轴的平面叫坐标平面，分别称为 ${xOy}$ 平面， ${yOz}$ 平面与 ${zOx}$ 平面. 三个坐标平面把空间划分成八个部分，每个部分称为一个 卦限 .

3. 给定空间一点 $P$ ，过点 $P$ 分别作与坐标平面 ${yOz}$ 、 ${zOx}$ 与 ${xOy}$ 平行的平面，与坐标平面一起围出一个长方体，所作的三个平面与 $x$ 轴、 $y$ 轴、 $z$ 轴的交点在轴上的坐标，给出了点 $P$ 的坐标 $\left( {x, y, z}\right)$ ，其中 $x, y, z$ 分别称为点 $P$ 的 横 坐标、 纵 坐标与 竖 坐标.

#### 3.3.2 空间向量的坐标表示

1. 给定任意一个向量 $\overrightarrow{p}$ ，我们先通过平移把 $\overrightarrow{p}$ 的起点放到坐标原点 $O$ ，这时得到的向量 $\overrightarrow{OP}$ 称为 $\overrightarrow{p}$ 的 位置向量 . 设 $\overrightarrow{OP}$ 的终点坐标是 $P\left( {x, y, z}\right)$ ，则直接记 $\overrightarrow{p} = \left( {x, y, z}\right)$ ，并称向量的这种表示法为它的坐标表示. $\left| \overrightarrow{OP}\right|  = \left| \left( {x, y, z}\right) \right|  = \sqrt{{x}^{2} + {y}^{2} + {z}^{2}}$ .

2. 设有空间任意两点 $P\left( {{x}_{1},{y}_{1},{z}_{1}}\right)$ 与 $Q\left( {{x}_{2},{y}_{2},{z}_{2}}\right)$ ,则

$\overrightarrow{PQ} = \overrightarrow{OQ} - \overrightarrow{OP} = \left( {{x}_{2} - {x}_{1},{y}_{2} - {y}_{1},{z}_{2} - {z}_{1}}\right) \;;\left| \overrightarrow{PQ}\right|  = \sqrt{{\left( {x}_{2} - {x}_{1}\right) }^{2} + {\left( {y}_{2} - {y}_{1}\right) }^{2} + {\left( {z}_{2} - {z}_{1}\right) }^{2}}$

$\overrightarrow{OP} \cdot  \overrightarrow{OQ} = {x}_{1}{x}_{2} + {y}_{1}{y}_{2} + {z}_{1}{z}_{2}\;;\cos \left\langle  {\overrightarrow{OP},\overrightarrow{OQ}}\right\rangle   = \frac{{x}_{1}{x}_{2} + {y}_{1}{y}_{2} + {z}_{1}{z}_{2}}{\sqrt{{x}_{1}^{2} + {y}_{1}^{2} + {z}_{1}^{2}}\sqrt{{x}_{2}^{2} + {y}_{2}^{2} + {z}_{2}^{2}}};$

$\overrightarrow{OP} \bot  \overrightarrow{OQ} \Leftrightarrow  {x}_{1}{x}_{2} + {y}_{1}{y}_{2} + {z}_{1}{z}_{2} = 0\;;$

$\overrightarrow{OP}\parallel \overrightarrow{OQ} \Leftrightarrow$ 存在 $\lambda  \in  \mathbf{R}$ ,使得 $\left( {{x}_{1},{y}_{1},{z}_{1}}\right)  = \lambda \left( {{x}_{2},{y}_{2},{z}_{2}}\right)$ ;

3. 空间向量的定比分点公式:

设 $A\left( {{x}_{1},{y}_{1},{z}_{1}}\right) , B\left( {{x}_{2},{y}_{2},{z}_{2}}\right) , P$ 是直线 ${AB}$ 上的点，且 $\overrightarrow{AP} = \lambda \overrightarrow{PB}$ ，其中 $\lambda  \in  \mathbf{R}$ 且 $\lambda  \neq   - 1$ ，则 $\overrightarrow{OP} =$

$$
\left( {\frac{{x}_{1} + \lambda {x}_{2}}{1 + \lambda },\frac{{y}_{1} + \lambda {y}_{2}}{1 + \lambda },\frac{{z}_{1} + \lambda {z}_{2}}{1 + \lambda }}\right) .
$$

### 3.4 空间向量在立体几何中的应用

1. 直线的方向向量:与直线 $r$ 平行 的任何非零向量.

2. 平面的法向量: 垂直于平面的任何非零向量.

#### 3.4.1 判断空间直线、平面的位置关系

1. 两条直线平行的充要条件是它们的方向向量 平行； 两条直线垂直的充要条件是它们的方向向量 垂直.

2. 直线和平面垂直的充要条件是直线的方向向量为平面的 法向量；

不在平面上的一条直线和平面平行的充要条件是直线的方向向量 垂直于平面的法向量.

3. 两个平面垂直的充要条件是它们的法向量 垂直；

两个平面平行的充要条件是它们的法向量 平行.

#### 3.4.2 求距离

1. 求点到平面的距离:如果 $A$ 、 $B$ 是空间中的两个点，其中点 $B$ 在平面 $\alpha$ 上， $\overrightarrow{n}$ 是平面 $\alpha$ 的一个法向量，那么点 $A$ 到平面 $\alpha$ 的距离 $d = \frac{\left| \overrightarrow{AB} \cdot  \overrightarrow{n}\right| }{\left| \overrightarrow{n}\right| }$ .

2. 求平面的平行线与平面的距离，只要求平行线上任意一点到平面的距离；求两个平行平面的距离, 也只要求其中一个平面上的任意一点 到另一个平面的距离.

3. 求异面直线间的距离:空间中两条异面直线 $a$ 、 $b$ 的距离 $d$ 可以通过公垂线段计算，或利用向量公式.

#### 3.4.3 求角的大小

1. 若异面直线 ${l}_{1},{l}_{2}$ 的方向向量为 $\overrightarrow{a},\overrightarrow{b},{l}_{1}$ 与 ${l}_{2}$ 所成的角为 $\theta$ ，则 $\cos \theta  = \frac{\left| \overrightarrow{a} \cdot  \overrightarrow{b}\right| }{\left| \overrightarrow{a}\right| \left| \overrightarrow{b}\right| }$ .

2. 求直线与平面所成的角:已知直线 $l$ 的方向向量为 $\overrightarrow{d}$ ，平面 $\alpha$ 的法向量 $\overrightarrow{n}$ ， $l$ 与平面 $\alpha$ 所成的角为 $\theta$ ，则

$$
\sin \theta  = \cos \left\langle  {\overrightarrow{d},\overrightarrow{n}}\right\rangle   = \frac{\left| \overrightarrow{d} \cdot  \overrightarrow{n}\right| }{\left| \overrightarrow{d}\right| \left| \overrightarrow{n}\right| }.
$$

3. 求二面角的平面角:已知二面角 $\alpha  - l - \beta$ 的两个半平面 $\alpha$ 和 $\beta$ 的法向量分别为 ${\overrightarrow{n}}_{1},{\overrightarrow{n}}_{2}$ ，二面角的平面角大小为 $\theta$ ,则 $\left| {\cos \theta }\right|  = \frac{\left| {\overrightarrow{n}}_{1} \cdot  {\overrightarrow{n}}_{2}\right| }{\left| {\overrightarrow{n}}_{1}\right| \left| {\overrightarrow{n}}_{2}\right| }$ , $\theta$ 为锐角还是钝角由实际情况决定.
