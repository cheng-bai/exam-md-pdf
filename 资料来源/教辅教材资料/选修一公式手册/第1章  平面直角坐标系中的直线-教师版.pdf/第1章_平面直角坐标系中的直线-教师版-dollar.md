## 第1章 平面直角坐标系中的直线

### 1.1 直线的倾斜角与斜率

#### 1.1.1 直线的倾斜角

1. 不妨设直线 $l$ 与 $x$ 轴相交于点 $A$ ，将 $x$ 轴绕点 $A$ 沿 逆时针 方向旋转到与 $l$ 重合时所转过的 最小正 ${\text{ 角 }\mathbf{\theta }}$ : 叫做直线 $l$ 的倾斜角，规定直线 $l$ 与 $x$ 轴平行或重合时，倾斜角为 0 . 故倾斜角的取值范围是 $\lbrack 0,\pi )$ ,特别地,当倾斜角 $\theta  = \frac{\pi }{2}$ 时,直线 $l$ 与 $x$ 轴垂直.

#### 1.1.2 直线的斜率

1. 当直线的倾斜角 $\theta  \neq  \frac{\pi }{2}$ 时，定义 $\tan \theta$ 为直线 $l$ 的斜率，常用字母 $k$ 表示，即 $k = \tan \theta$ . 当 $\theta  = \frac{\pi }{2}$ 即直线 $l$ 与 $x$ 轴垂直时,我们说直线 $l$ 的斜率 $r$ 不存在.

2. 在平面直角坐标系中，经过不同的两点 $A\left( {{x}_{1},{y}_{1}}\right) , B\left( {{x}_{2},{y}_{2}}\right) \left( {{x}_{1} \neq  {x}_{2}}\right)$ 的直线 $l$ 的斜率为 $k = \frac{{y}_{2} - {y}_{1}}{{x}_{2} - {x}_{1}}$ .

3. 若 $\overrightarrow{a} = \left( {m, n}\right) \left( {m \neq  0}\right)$ 为直线的方向向量，则直线的斜率 $k = \frac{n}{m}$ .

#### 1.1.3 求倾斜角与斜率的方法

1. 当直线斜率 $k$ 存在时, $\alpha  = \left\{  \begin{array}{ll} \arctan k, & k \geq  0 \\  \pi  - \arctan \left( {-k}\right) , & k < 0 \end{array}\right.$

### 1.2 直线方程

#### 1.2.1 直线的方程类型

<table id="cross-table-1"><tr><td>名称</td><td>方程</td><td>说明</td><td>适用范围</td></tr><tr><td>两点式</td><td>$\frac{x - {x}_{1}}{{x}_{2} - {x}_{1}} = \frac{y - {y}_{1}}{{y}_{2} - {y}_{1}}$</td><td>$\left( {{x}_{1},{y}_{1}}\right) \left( {{x}_{2},{y}_{2}}\right)$ 为直线上已知点</td><td>分母不为零</td></tr><tr></tr><tr><td>横截式</td><td>$y = {kx} + b$</td><td>$k$ 、 $b$ 分别表示直线的斜率和在纵轴上的截距</td><td>直线斜率存在</td></tr><tr><td>纵截式</td><td>$x = {ty} + m$</td><td>$t = \frac{1}{k}, m$ 为直线在横轴上的截距</td><td>$k \neq  0$</td></tr><tr><td>截距式</td><td>$\frac{x}{a} + \frac{y}{b} = 1$</td><td>$\left( {a,0}\right) ,\left( {0, b}\right)$ 为直线与 $x, y$ 轴交点</td><td>不能平行于 $x, y$ 轴, 也不能过原点</td></tr><tr><td>点方向式</td><td>$\frac{x - {x}_{0}}{u} = \frac{y - {y}_{0}}{v}$</td><td>$\left( {{x}_{0},{y}_{0}}\right)$ 为直线上已知点, $\overrightarrow{d} = \left( {u, v}\right)$ 为直线的法向量</td><td>不能平行于 $x, y$ 轴</td></tr><tr><td>点法向式</td><td>$a\left( {x - {x}_{0}}\right)  + b\left( {y - {y}_{0}}\right)  = 0$ <br>   [失效外部图片：bo_d7nksg2lb0pc73f2r3b0_1.jpg]</td><td>$\left( {{x}_{0},{y}_{0}}\right)$ 为直线上已知点, $\overrightarrow{n} = \left( {a, b}\right)$ 为直线的法向量</td><td>平面直角坐标系内的直线都适用</td></tr><tr><td>一般式</td><td>${ax} + {by} + c = 0 \; \left( {{a}^{2} + {b}^{2} \neq  0}\right)$</td><td>$\overrightarrow{d} = \left( {a, b}\right)$ 为直线 法 向量</td><td>平面直角坐标系内的直线都适用</td></tr></table>

### 1.3 两条直线的位置关系

1.3.1 两条直线的相交、平行与重合

<table id="cross-table-2"><tr><td>位置关系</td><td>一般式</td><td>斜截式</td></tr><tr><td>直线方程</td><td>${l}_{1} : {a}_{1}x + {b}_{1}y + {c}_{1} = 0$ <br>  ${l}_{2} : {a}_{2}x + {b}_{2}y + {c}_{2} = 0$</td><td>${l}_{1} : y = {k}_{1}x + {b}_{1}$ <br>  ${l}_{2} : y = {k}_{1}x + {b}_{1}$</td></tr><tr><td>相交</td><td>$\frac{{a}_{1}}{{a}_{2}} \neq  \frac{{b}_{1}}{{b}_{2}}\left( {{a}_{2},{b}_{2} \neq  0}\right)$</td><td>${k}_{1} \neq  {k}_{2}$</td></tr><tr><td>平行</td><td>$\frac{{a}_{1}}{{a}_{2}} = \frac{{b}_{1}}{{b}_{2}} \neq  \frac{{c}_{1}}{{c}_{2}}\left( {{a}_{2},{b}_{2},{c}_{2} \neq  0}\right)$</td><td>${k}_{1} = {k}_{2},{b}_{1} \neq  {b}_{2}$</td></tr><tr><td>重合</td><td>$\frac{{a}_{1}}{{a}_{2}} = \frac{{b}_{1}}{{b}_{2}} = \frac{{c}_{1}}{{c}_{2}}\left( {{a}_{2},{b}_{2},{c}_{2} \neq  0}\right)$</td><td>${k}_{1} = {k}_{2},{b}_{1} = {b}_{2}$</td></tr></table>

#### 1.3.2 两条直线垂直的判定与夹角的求法

1. 当直线 ${l}_{1} : {a}_{1}x + {b}_{1}y + {c}_{1} = 0$ 与 ${l}_{2} : {a}_{2}x + {b}_{2}y + {c}_{2} = 0$ 垂直时,它们的夹角为 $\frac{\pi }{2}$ 方向向量 (法向量) 垂直,即 ${a}_{1}{a}_{2} + {b}_{1}{b}_{2} = 0$ .

2. 当直线 ${l}_{1} : y = {k}_{1}x + {b}_{1}$ 与直线 ${l}_{2} : y = {k}_{2}x + {b}_{2}$ 垂直时, ${k}_{1}{k}_{2} =  - 1$ .

3. 给定两条直线 ${l}_{1} : {a}_{1}x + {b}_{1}y + {c}_{1} = 0,{l}_{2} : {a}_{2}x + {b}_{2}y + {c}_{2} = 0$ ,它们的夹角 $\alpha$ 的余弦公式为 $\cos \alpha  = \; \frac{\left| {a}_{1}{a}_{2} + {b}_{1}{b}_{2}\right| }{\sqrt{{a}_{1}^{2} + {b}_{1}^{2}}\sqrt{{a}_{2}^{2} + {b}_{2}^{2}}}.$

4. 给定两条直线 ${l}_{1} : y = {k}_{1}x + {b}_{1},{l}_{2} : y = {k}_{2}x + {b}_{2}$ ,它们的夹角 $\alpha$ 的正切公式为 $\tan \alpha  = \; \left| \frac{{k}_{2} - {k}_{1}}{1 + {k}_{1}{k}_{2}}\right| \;\left( {{k}_{1}{k}_{2} \neq   - 1}\right) .$

### 1.4 点到直线的距离

1.4.1 点到直线的距离公式

1. 点 $P\left( {{x}_{0},{y}_{0}}\right)$ 到直线 $l : {ax} + {by} + c = 0$ 的距离 $d = \frac{\left| a{x}_{0} + b{y}_{0} + c\right| }{\sqrt{{a}^{2} + {b}^{2}}}$ .

#### 1.4.2 平行直线间的距离公式

1. 两条平行直线 ${l}_{1} : {ax} + {by} + {c}_{1} = 0,{l}_{2} : {ax} + {by} + {c}_{2} = 0$ 的距离 $d = \frac{\left| {c}_{1} - {c}_{2}\right| }{\sqrt{{a}^{2} + {b}^{2}}}$ .

## *1.4.3 两点在直线的同侧或异侧的判断

1. 给定直线 $l : {ax} + {by} + c = 0, P\left( {{x}_{1},{y}_{1}}\right) , Q\left( {{x}_{2},{y}_{2}}\right)$ ,令 $\delta  = \frac{a{x}_{0} + b{y}_{0} + c}{\sqrt{{a}^{2} + {b}^{2}}}$ ,

当两点在直线 $l$ 的同侧，则 ${\delta }_{1}{\delta }_{2} > 0$ ；当两点在直线 $l$ 的异侧，则 ${\delta }_{1}{\delta }_{2} < 0$ .

*1.4.4 直线中的对称问题

1. ①若 $A\left( {{x}_{1},{y}_{1}}\right) , B\left( {{x}_{2},{y}_{2}}\right)$ ，则 ${AB}$ 的中点坐标是 $\left( {\frac{{x}_{1} + {x}_{2}}{2},\frac{{y}_{1} + {y}_{2}}{2}}\right)$ .

② $P\left( {x, y}\right)$ 关于 $M\left( {a, b}\right)$ 的对称点坐标是 $\;\left( {{2a} - x,{2b} - y}\right) \;$ .

2. 直线关于点的对称直线:

已知直线 $l : {ax} + {by} + c = 0$ ，点 $P\left( {m, n}\right)$ ，求直线 $l$ 关于点 $P$ 的对称直线 ${l}^{\prime }$ . 在直线 ${l}^{\prime }$ 上任取一点 $A\left( {x, y}\right)$ ， 则点 $A$ 关于点 $P\left( {m, n}\right)$ 对称的点 ${A}^{\prime }\left( {{2m} - x,{2n} - y}\right)$ 在直线 $l$ 上，即有 $a\left( {{2m} - x}\right)  + b\left( {{2n} - y}\right)  + c = 0$ .

3. 点关于线的对称问题:

① $P\left( {x, y}\right)$ 关于 $x = a$ 的对称点为 $\left( {{2a} - x, y}\right)$ ；

② $P\left( {x, y}\right)$ 关于 $y = b$ 的对称点为 $\left( {x,{2b} - y}\right)$ ；

③ $P\left( {x, y}\right)$ 关于 $y = x$ 的对称点为 $\left( {y, x}\right)$ ；

④ $P\left( {x, y}\right)$ 关于 $y =  - x$ 的对称点为 $\left( {-y, - x}\right)$ ；

⑤ $P\left( {x, y}\right)$ 关于 $y = x + b$ 的对称点为 $\left( {y - b, x + b}\right)$ ；(巧记:代入 $x$ 求 $y$ ，代入 $y$ 求 $x$ )

⑥ $P\left( {x, y}\right)$ 关于 $y =  - x + b$ 的对称点为 $\left( {b - y, - x + b}\right)$ ；(巧记:代入 $x$ 求 $y$ ，代入 $y$ 求 $x$ )

⑤求解 $P\left( {x, y}\right)$ 关于 $l : {ax} + {by} + c = 0$ 的对称点的一般步骤:

(1)设对称点 ${P}^{\prime }\left( {m, n}\right)$ ；(2)列方程组 $\left\{  \begin{array}{l} a\frac{x + m}{2} + b\frac{y + n}{2} + c = 0 \\  \frac{a - x}{b - y} = \frac{b}{a} \end{array}\right.$ ；(3)求解 $\left( {m, n}\right)$ .

4. 直线关于直线的对称直线:转化为点 关于线的对称问题.
