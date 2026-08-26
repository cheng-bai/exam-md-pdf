# 导数及其应用

![bo_d4slovref24c73be0r3g_0_0_4_1654_1172_0.jpg](images/bo_d4slovref24c73be0r3g_0_0_4_1654_1172_0.jpg)

初等数学可以帮助我们对匀速运动进行描述和分析, 也能够顺利解决一些具有规则形状的物体的度量问题. 然而, 人类在实际生活中所面临的问题往往更为复杂. 例如, 运动中速度可以不断变化, 图形的边界不再具有规则的形状，等等. 要处理这一类问题，本质上要有处理变化和变化中的瞬时状态的数学工具, 这就需要用到高等数学, 特别是微积分的知识.

由于系统深入地介绍高等数学的内容不是高中课程所能承担的任务，因此本章将用比较直观和粗略的方式引入微积分中的一个最基本的概念——导数，为研究函数性质提供一个有力的工具，并展示其在解决变速运动等现实问题中的一些应用.

由于知识基础不足且为了避免产生理解上的困难及误导，本章中的某些结论没有给出证明, 而仅作形式化的表述. 希望同学们对导数的基本内涵及其应用有所认识和体会，并对未来在大学课程中继续深入学习微积分抱有渴望.

## 5.1 导数的概念及意义

在本节中, 我们将学习如何刻画运动物体的瞬时速度, 以及如何确定一条曲线上一点处的切线, 通过这些例子初步认识导数这一表示函数瞬时变化率的数学概念.

### 1 导数的概念

当物体作匀速运动时,运动的速度 $v$ 等于距离 $s$ 除以运动时间 $t$ ,即 $v = \frac{s}{t}$ . 但是,如果一个作变速运动的物体在时间段 $t$ 内的运动距离是 $s$ ,上面的公式所给出的只能是这段运动过程中运动物体的平均速度 $\bar{v} = \frac{s}{t}$ .

![bo_d4slovref24c73be0r3g_1_197_867_325_188_0.jpg](images/bo_d4slovref24c73be0r3g_1_197_867_325_188_0.jpg)

图 5-1-1

当我们乘坐高铁时, 常常会在车厢内看到如图 5-1-1 所示的列车信息显示屏. 如何理解图中“速度 ${303}\mathrm{\;{km}}/\mathrm{h}$ ”呢?

仅用一个时间段内的平均速度难以准确地描述在该时间段内变速运动的过程. 为了精准地描述变速运动, 一个自然的想法是把整个运动时间分割成若干个小的时间段, 并分别求每个时间段内的平均速度. 可以想象, 随着时间段的分割越来越精细, 利用分段的平均速度就可以越来越精确地对整个运动过程进行描述.

以自由落体运动为例，已知物体下落的距离 $d$ (单位: $\mathrm{m}$ ) 与时间 $t$ (单位: $\mathrm{s}$ )满足函数关系 $d = \frac{1}{2}g{t}^{2}$ ,其中 $g$ 是重力加速度. 若近似地取 $g = {10}\mathrm{\;m}/{\mathrm{s}}^{2}$ ,则 $d = 5{t}^{2}$ .

考虑从 $t = 1$ 到 $t = 3$ (用区间符号记作 $\left\lbrack  {1,3}\right\rbrack$ )时间段内的自由落体运动. 它的平均速度是 $\frac{d\left( 3\right)  - d\left( 1\right) }{3 - 1} = {20}\left( {\mathrm{\;m}/\mathrm{s}}\right)$ . 如果把这段时间分成 $\left\lbrack  {1,2}\right\rbrack$ 与 $\left\lbrack  {2,3}\right\rbrack$ 两段，那么在这两个时间段内自由落体的平均速度分别是 $\frac{d\left( 2\right)  - d\left( 1\right) }{2 - 1} = {15}\left( {\mathrm{\;m}/\mathrm{s}}\right)$ 与 $\frac{d\left( 3\right)  - d\left( 2\right) }{3 - 2} = {25}\left( {\mathrm{\;m}/\mathrm{s}}\right)$ . 而如果以 ${0.5}\mathrm{\;s}$ 为间隔把 $\left\lbrack  {1,3}\right\rbrack$ 分为 4 个时间段,可以得出这 4 个时间段内的平均速度分别是 ${12.5}\mathrm{\;m}/\mathrm{s}\text{ 、 }{17.5}\mathrm{\;m}/\mathrm{s}\text{ 、 }{22.5}\mathrm{\;m}/\mathrm{s}$ 与 27.5 m/s. 由此可见，随着时间段的不断细分，自由落体的运动状态确实得到了越来越精确的描述. 这种做法其实蕴含着 “极限” 这个朴素而深刻的思想.

先把时间段分割，在越来越小的时间段内对运动进行分析， 再从整体上得到对运动状态越来越精确的描述, 这就是被称为 “微积分”的数学工具给我们提供的解决此类问题的基本途径. 在这里, 我们只介绍如何寻找适当的数学工具刻画运动物体在某一时刻的瞬时速度. 这里的瞬时速度指的是, 运动物体在临近指定时刻的某个时间段内的平均速度在时间段长度越来越小的变化过程中所趋近于的一个稳定值. 下面的例子展现了利用平均速度趋近瞬时速度的过程.

例 1 自由落体运动中，物体下落的距离 $d$ (单位: $\mathrm{m}$ ) 与时间 $t$ (单位: $\mathrm{s}$ )近似满足函数关系 $d = 5{t}^{2}$ . 试求物体在 $t = 2$ 时的瞬时速度.

解 对不同时间段长度值 $\left| h\right| , t = 2$ 附近时间段 $\left\lbrack  {2 + h,2}\right\rbrack \; \left( {h < 0}\right)$ 或者 $\left\lbrack  {2,2 + h}\right\rbrack  \left( {h > 0}\right)$ 内的平均速度为

$$
\bar{v} = \frac{d\left( {2 + h}\right)  - d\left( 2\right) }{h} = \frac{5 \times  {\left( 2 + h\right) }^{2} - 5 \times  {2}^{2}}{h},
$$

得到表 5-1.

表 5-1

<table><tr><td>$h\left( { < 0}\right)$</td><td>$\left\lbrack  {2 + h,2}\right\rbrack$ 上的 $\bar{v}$</td><td>$h\left( { > 0}\right)$</td><td>$\left\lbrack  {2,2 + h}\right\rbrack$ 上的 $\bar{v}$</td></tr><tr><td>-0.1</td><td>19.5</td><td>0.1</td><td>20.5</td></tr><tr><td>-0.01</td><td>19.95</td><td>0.01</td><td>20.05</td></tr><tr><td>-0.001</td><td>19.995</td><td>0.001</td><td>20.005</td></tr><tr><td>-0.000 1</td><td>19.9995</td><td>0.000 1</td><td>20.000 5</td></tr><tr><td>-0.000 01</td><td>19.999 95</td><td>0.000 01</td><td>20.000 05</td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

在表 5-1 中,我们通过不断缩小 $h$ 的绝对值,发现在 $h$ 趋近于 0 时, 平均速度趋近于一个确定的值 20. 因此, 从表中数值我们可以初步判断物体在 $t = 2$ 时的瞬时速度为 ${20}\mathrm{\;m}/\mathrm{s}$ .

下面用数学的计算与推理证实我们的判断.

当 $h \neq  0$ 时, $t = 2$ 附近时间段 $\left\lbrack  {2 + h,2}\right\rbrack  \left( {h < 0}\right)$ 或者 $\left\lbrack  {2,2 + h}\right\rbrack \; \left( {h > 0}\right)$ 的平均速度是

$$
\bar{v} = \frac{d\left( {2 + h}\right)  - d\left( 2\right) }{h} = \frac{5 \times  {\left( 2 + h\right) }^{2} - 5 \times  {2}^{2}}{h} = \frac{{20h} + 5{h}^{2}}{h} = {20} + {5h}.
$$

因为当 $h$ 趋近于 0 时, $\bar{v}$ 趋近于 20,所以物体在 $t = 2$ 时的瞬时速度为 ${20}\mathrm{\;m}/\mathrm{s}$ .

---

左边的式子在 $h > 0$ 时是显然的. 在 $h < 0$ 时，时间段 $\left\lbrack  {2 + h,2}\right\rbrack$ 上的平均速度一开始应写为 $\frac{d\left( 2\right)  - d\left( {2 + h}\right) }{\left| h\right| } = \; \frac{d\left( 2\right)  - d\left( {2 + h}\right) }{-h}$ ,它和 $h > 0$ 时一样,也可统一地写为 $\frac{d\left( {2 + h}\right)  - d\left( 2\right) }{h}$ .

---

用瞬时速度的说法, 图 5-1-1 中所示的高铁速度可解释为: 在 9 时 30 分的某一瞬间(列车信息屏的时间显示只精确到分，但瞬时速度在时间上的精确度远高于分), 列车以 303 km/h 的瞬时速度前进.

例 1 告诉我们, 研究运动物体的瞬时速度, 本质上就是在已知函数关系 $y = f\left( x\right)$ 的前提下,对于自变量某个给定值 ${x}_{0}$ ,赋予 ${x}_{0}$ 一个变化量 $h$ ,分析当 $h$ 趋近于 0 时,函数值的变化量 $f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right)$ 相对于自变量变化量 $h$ 的比值 $\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ 是否趋近于某个稳定值.

如果这个稳定值存在,就说明 $\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ 在 $h$ 趋近于 0 时有极限,并把这个极限值记作 $\mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ ,称为函数 $y = f\left( x\right)$ 在 $x = {x}_{0}$ 处的导数 (derivative),记作 ${f}^{\prime }\left( {x}_{0}\right)$ , 即有

$$
{f}^{\prime }\left( {x}_{0}\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}.
$$

因此,在满足函数关系 $d = f\left( t\right)$ 的运动中,函数 $d = f\left( t\right)$ 在 $t = {t}_{0}$ 处的导数 ${f}^{\prime }\left( {t}_{0}\right)$ 就是 ${t}_{0}$ 时刻的瞬时速度.

一般地,对于一个函数 $y = f\left( x\right)$ ,通常将 $\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ 称为函数 $y = f\left( x\right)$ 在以 ${x}_{0}$ 和 ${x}_{0} + h$ 为端点的区间上的平均变化率, 而 ${f}^{\prime }\left( {x}_{0}\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ 就是函数 $y = f\left( x\right)$ 在 $x = {x}_{0}$ 处的瞬时变化率. 平均变化率反映了一个函数在一个区间上的平均变化情况,而瞬时变化率则反映了该函数在某个自变量 ${x}_{0}$ 处的瞬时变化情况.

例 2 已知在使用某种杀菌剂 $t$ 小时后室内的细菌数量为

$$
f\left( t\right)  = {10}^{5} + {10}^{4}t - {10}^{3}{t}^{2}.
$$

(1)求 ${f}^{\prime }\left( {10}\right)$ ；

(2) ${f}^{\prime }\left( {10}\right)$ 的实际意义是什么？

解(1)当 $h \neq  0$ 时，在使用杀菌剂 10 小时附近的时间段 $\left\lbrack  {{10} + h,{10}}\right\rbrack  \left( {h < 0}\right)$ 或者 $\left\lbrack  {{10},{10} + h}\right\rbrack  \left( {h > 0}\right)$ 内,细菌数量关于时

间的平均变化率为

$$
\frac{f\left( {{10} + h}\right)  - f\left( {10}\right) }{h}
$$

$$
= \frac{{10}^{5} + {10}^{4}\left( {{10} + h}\right)  - {10}^{3}{\left( {10} + h\right) }^{2} - \left( {{10}^{5} + {10}^{4} \times  {10} - {10}^{3} \times  {10}^{2}}\right) }{h}
$$

$$
= \frac{-{10}^{4}h - {10}^{3}{h}^{2}}{h}
$$

$$
=  - {10}^{4} - {10}^{3}h\text{ , }
$$

从而,令 $h$ 趋近于 0,就得到

$$
{f}^{\prime }\left( {10}\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\left( {-{10}^{4} - {10}^{3}h}\right)  =  - {10}^{4}.
$$

(2) ${f}^{\prime }\left( {10}\right)$ 的实际意义是细菌数量在 $t = {10}$ 时的瞬时变化率. 它表明在 $t = {10}$ 附近,细菌数量大约以每小时 ${10}^{4}$ 的速率减少.

#### 练习 5.1(1)

1. 自由落体运动中，物体下落的距离 $d$ (单位: $\mathrm{m}$ ) 与时间 $t$ (单位: $\mathrm{s}$ ) 近似满足函数关系 $d = 5{t}^{2}$ .

(1)求物体在 $\left\lbrack  {2,4}\right\rbrack$ 时间段内的平均速度；

(2)求物体在 $t = 3$ 时的瞬时速度；

(3)求物体在 $t = a\left( {a > 0}\right)$ 时的瞬时速度.

2. 将石子投入水中，水面产生的圆形波纹不断扩散.

(1)当半径 $r$ 从 $a$ 增加到 $a + h\left( {h > 0}\right)$ 时,求圆周长相对于半径的平均变化率;

(2)当半径 $r = a$ 时,求圆周长相对于半径的瞬时变化率.

### 2 导数的几何意义

在上一节中谈到, 在研究物体的变速运动时, 我们可以通过把时间分成若干个小的时间段, 并计算每个时间段内物体的平均速度, 以近似地描述物体的运动状况. 当时间段的划分越来越细时, 对运动的描述就越来越精确. 特别地, 在一个时间点附近的时间段越来越小时, 如果相应的平均速度趋近于一个稳定值, 这个稳定值就是运动物体在这个时间点的瞬时速度.

在几何学中有类似的情境:为了研究一条曲线的特性，我们可以把曲线划分成小段, 并把连接每一小段两端点的线段看作曲线的这一小段的近似. 当曲线的划分越来越细时, 由这些小线段所连接起来的折线就越来越接近于原来的曲线.

我们把连接曲线上任意两点的直线称为该曲线的一条割线 (secant line). 如图 5-1-2,给定曲线上的一点 $P$ ,考虑以 $P$ 为端点的一条小曲线段 $\overset{\text{ ⏜ }}{PQ}$ 和割线 ${PQ}$ . 像平均速度趋近于瞬时速度那样,当曲线段 $\overset{\text{ ⏜ }}{PQ}$ 取得越来越短,即点 $Q$ 越来越靠近点 $P$ 时,如果割线 ${PQ}$ 趋近于一条确定的直线,那么我们就将这条直线称为曲线在点 $P$ 处的切线 (tangent line). 就像瞬时速度是物体在给定时刻的运动状态的最好描述一样,在点 $P$ 处的切线是曲线在点 $P$ 附近性质的最好描述.

![bo_d4slovref24c73be0r3g_5_580_662_874_298_0.jpg](images/bo_d4slovref24c73be0r3g_5_580_662_874_298_0.jpg)

图 5-1-2

切线这个术语我们并不陌生, 在平面几何的学习中已定义过圆的切线, 并讨论过它的性质. 那里所定义的圆的切线是否与上面这个新定义一致呢?

![bo_d4slovref24c73be0r3g_5_192_1195_285_190_0.jpg](images/bo_d4slovref24c73be0r3g_5_192_1195_285_190_0.jpg)

图 5-1-3

例 3 如图 5-1-3,曲线 $y = \sqrt{2 - {x}^{2}}\left( {-\sqrt{2} \leq  x \leq  \sqrt{2}}\right)$ 是圆 ${x}^{2} + {y}^{2} = 2$ 在 $x$ 轴及其上方的部分, $P\left( {1,1}\right)$ 和 $Q\left( {0,\sqrt{2}}\right)$ 是该曲线上的两点.

(1)求割线 ${PQ}$ 的斜率；

(2)对正整数 $n$ ，令 ${x}_{n} = 1 - \frac{1}{n},{y}_{n} = \sqrt{2 - {x}_{n}^{2}},{Q}_{n}\left( {{x}_{n},{y}_{n}}\right)$ 均在该圆周上,且随着 $n$ 的增大越来越接近点 $P$ . 借助信息技术工具,适当地计算一些割线 $P{Q}_{n}$ 的斜率,观察并总结当 $n$ 逐渐增大时,割线 $P{Q}_{n}$ 的斜率的变化趋势.

解 (1) 割线 ${PQ}$ 的斜率是

$$
{k}_{PQ} = \frac{{y}_{Q} - {y}_{P}}{{x}_{Q} - {x}_{P}} = \frac{\sqrt{2} - 1}{0 - 1} = 1 - \sqrt{2}.
$$

(2)割线 $P{Q}_{n}$ 的斜率是

$$
{k}_{P{Q}_{n}} = \frac{{y}_{{Q}_{n}} - {y}_{P}}{{x}_{{Q}_{n}} - {x}_{P}} = \frac{{y}_{n} - {y}_{P}}{{x}_{n} - {x}_{P}} = \frac{\sqrt{2 - {\left( 1 - \frac{1}{n}\right) }^{2}} - 1}{1 - \frac{1}{n} - 1} = n\left( {1 - \sqrt{2 - {\left( 1 - \frac{1}{n}\right) }^{2}}}\right) .
$$

借助计算器或计算机可以得到表 5-2 中关于 ${k}_{P{Q}_{n}}$ 的近似值 (结果精确到 0.000 000 001):

表 5-2

<table><tr><td>$n$</td><td>${Q}_{n}$</td><td>${k}_{P{Q}_{n}}$</td></tr><tr><td>1</td><td>(0.000000000, 1.414213562)</td><td>-0.414213562</td></tr><tr><td>5</td><td>(0.800000000, 1.166 190 379)</td><td>-0.830951895</td></tr><tr><td>10</td><td>(0.900000000, 1.090871211)</td><td>-0.908712115</td></tr><tr><td>100</td><td>(0.990000000, 1.009 900 985)</td><td>-0.990098525</td></tr><tr><td>1000</td><td>(0.999 000 000, 1.000 999 001)</td><td>-0.999 000 999</td></tr><tr><td>10000</td><td>(0.999 900 000, 1.000 099 990)</td><td>-0.999 900 010</td></tr><tr><td>100000</td><td>(0.999990000, 1.000010000)</td><td>-0.999 990 000</td></tr><tr><td>1000000</td><td>(0.999999000, 1.000001000)</td><td>-0.999 999 000</td></tr><tr><td>10 000 000</td><td>(0.999999900, 1.000000100)</td><td>-0.999 999 898</td></tr><tr><td>...</td><td>...</td><td>...</td></tr></table>

观察表 5-2 可知,当 $n$ 逐渐增大时,割线 $P{Q}_{n}$ 的斜率逐渐减小, 并趋近于 -1 .

由例 3 可以看出,根据现在的定义,曲线在点 $P\left( {1,1}\right)$ 处的切线的斜率是 -1,容易求得它的点斜式方程是 $y - 1 =  - \left( {x - 1}\right)$ , 即 $x + y - 2 = 0$ . 另一方面,因为平面几何所定义的圆的切线垂直于过切点的半径,即向量 $\overrightarrow{OP} = \left( {1,1}\right)$ 是切线的法向量,用直线的点法式方程可求出切线的方程也是 $x + y - 2 = 0$ . 这就说明,对于圆来说,两个切线的定义一致.

对于任意曲线 $y = f\left( x\right)$ ,如何从定义出发求它在点 $P \; \left( {{x}_{0}, f\left( {x}_{0}\right) }\right)$ 处的切线?

例 3 给我们的启示是先求切线的斜率, 且进一步揭示了斜率的求法: 如果记 $f\left( x\right)  = \sqrt{2 - {x}^{2}}$ ,那么

$$
{k}_{P{Q}_{n}} = \frac{{y}_{n} - {y}_{P}}{{x}_{n} - {x}_{P}} = \frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h},
$$

![bo_d4slovref24c73be0r3g_6_1110_1835_357_208_0.jpg](images/bo_d4slovref24c73be0r3g_6_1110_1835_357_208_0.jpg)

图 5-1-4

其中 ${x}_{0} = 1, h =  - \frac{1}{n}$ . 当 $n$ 增大时, $h$ 趋近于 $0,{k}_{P{Q}_{n}}$ 的稳定值就是

$$
\mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}.
$$

这个方法适用于一般情况. 如图 5-1-4,在曲线上点 $P$ 的附近取一点 $Q\left( {{x}_{0} + h, f\left( {{x}_{0} + h}\right) }\right)$ ,割线 ${PQ}$ 的斜率 $\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ 就是函数 $y = f\left( x\right)$ 在以 ${x}_{0}$ 和 ${x}_{0} + h$ 为端点的区间上的平均变化率. 当点 $Q$ 沿曲线趋近于点 $P$ 时,割线 ${PQ}$ 的斜率趋近于某一稳定值, 这个稳定值

$$
\mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}
$$

就是函数 $y = f\left( x\right)$ 在 $x = {x}_{0}$ 处的瞬时变化率 ${f}^{\prime }\left( {x}_{0}\right)$ . 因此,函数 $y = f\left( x\right)$ 在 $x = {x}_{0}$ 处的导数 ${f}^{\prime }\left( {x}_{0}\right)$ 就是曲线 $y = f\left( x\right)$ 在点 $P\left( {{x}_{0}, f\left( {x}_{0}\right) }\right)$ 处切线的斜率. 从而,函数 $y = f\left( x\right)$ 在点 $P\left( {{x}_{0}, f\left( {x}_{0}\right) }\right)$ 处的切线方程为

$$
y - f\left( {x}_{0}\right)  = {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right) .
$$

例 4 已知 $f\left( x\right)  = {x}^{2}$ ,求曲线 $y = f\left( x\right)$ 在点 $P\left( {1,1}\right)$ 处的切线方程.

解 先求曲线 $y = f\left( x\right)$ 在点 $P\left( {1,1}\right)$ 处切线的斜率 ${f}^{\prime }\left( 1\right)$ :

当 $h \neq  0$ 时,

$$
\frac{f\left( {1 + h}\right)  - f\left( 1\right) }{h} = \frac{{\left( 1 + h\right) }^{2} - {1}^{2}}{h} = 2 + h,
$$

从而当 $h$ 趋近于 0 时,

$$
{f}^{\prime }\left( 1\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\left( {2 + h}\right)  = 2.
$$

因此,曲线 $y = {x}^{2}$ 在点 $P\left( {1,1}\right)$ 处切线的斜率为 2 . 于是,所求切线方程为

$$
y - 1 = 2\left( {x - 1}\right) ,
$$

即

$$
y = {2x} - 1.
$$

例 5 已知 $f\left( x\right)  = {x}^{3}$ ,求曲线 $y = f\left( x\right)$ 在点 $P\left( {0,0}\right)$ 处的切线方程.

解 先求曲线 $y = f\left( x\right)$ 在点 $P\left( {0,0}\right)$ 处切线的斜率 ${f}^{\prime }\left( 0\right)$ :

当 $h \neq  0$ 时,

$$
\frac{f\left( h\right)  - f\left( 0\right) }{h} = \frac{{h}^{3} - {0}^{3}}{h} = {h}^{2},
$$

从而当 $h$ 趋近于 0 时,

$$
{f}^{\prime }\left( 0\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}{h}^{2} = 0.
$$

因此,曲线 $y = {x}^{3}$ 在点 $P\left( {0,0}\right)$ 处切线的斜率为 0 . 于是,所求切线方程为

$$
y = 0\text{ . }
$$

在例 5 中,函数 $y = {x}^{3}$ 在 $x = 0$ 处的导数为零,即曲线 $y = {x}^{3}$ 在点 $P\left( {0,0}\right)$ 处的切线斜率为零,此时曲线的切线是一条水平直线.

通常, 我们将导数为零的点称为函数的驻点 (stationary point),曲线在其驻点处的切线是一条水平直线. 例如, $x = 0$ 是函数 $y = {x}^{3}$ 的驻点.

---

尝试寻找例 3 和例 4 中函数的驻点.

---

#### 练习 5.1(2)

1. 已知 $f\left( x\right)  = 3{x}^{2}$ ,分别求曲线 $y = f\left( x\right)$ 在点 $P\left( {-1,3}\right)$ 和点 $Q\left( {1,3}\right)$ 处的切线方程.

2. 借助函数图像, 判断下列导数的正负 (可利用信息技术工具):

(1) ${f}^{\prime }\left( \frac{\pi }{4}\right)$ ，其中 $f\left( x\right)  = \sin x$ ； (2) ${f}^{\prime }\left( 0\right)$ ,其中 $f\left( x\right)  = {\left( \frac{1}{2}\right) }^{x}$ .

#### 习题 5.1

##### A 组

1. 自由落体运动的位移 $d$ (单位: $\mathrm{m}$ ) 与时间 $t$ (单位: $\mathrm{s}$ ) 满足函数关系 $d = \frac{1}{2}g{t}^{2}$ ( $g$ 为重力加速度).

(1)分别求[4,4.1]、[4,4.01]、[4,4.001]这些时间段内自由落体的平均速度；

(2)求 $t = 4$ 时的瞬时速度；

(3)求 $t = a\left( {a > 0}\right)$ 时的瞬时速度；

(4)借助(3)的结果，求 $t = \frac{5}{2}$ 时的瞬时速度.

2. 竖直向上发射的火箭熄火时上升速度达到 ${100}\mathrm{\;m}/\mathrm{s}$ ，此后其位移 $H$ (单位: $\mathrm{m}$ )与时间 $t$ (单位: $\mathrm{s}$ )近似满足函数关系 $H = {100t} - 5{t}^{2}$ .

(1)分别求火箭在 $\left\lbrack  {0,2}\right\rbrack$ 、 $\left\lbrack  {2,4}\right\rbrack$ 这些时间段内的平均速度；

(2)求火箭在 $t = 2$ 时的瞬时速度；

(3)熄火后多长时间火箭上升速度为 0

3. 某水管的流水量 $y$ (单位: ${\mathrm{m}}^{3}$ ) 与时间 $t$ (单位: $\mathrm{s}$ ) 满足函数关系 $y = f\left( t\right)$ ,其中 $f\left( t\right)  = {3t}.$

(1)求 $f\left( t\right)$ 在 $t = a$ 处的导数 ${f}^{\prime }\left( a\right)$ ；

(2) ${f}^{\prime }\left( a\right)$ 的实际意义是什么？

(3)随着 $a$ 的取值变化， ${f}^{\prime }\left( a\right)$ 是否发生变化？为什么？

4. 将石子投入水中，水面产生的圆形波纹不断扩散. 计算:

(1)当半径 $r$ 从 $a$ 增加到 $a + h\left( {h > 0}\right)$ 时,圆面积相对于半径的平均变化率;

(2)当半径 $r = a$ 时,圆面积相对于半径的瞬时变化率.

5. 函数 $y = f\left( x\right)$ 的图像如图所示.

![bo_d4slovref24c73be0r3g_9_1125_311_357_242_0.jpg](images/bo_d4slovref24c73be0r3g_9_1125_311_357_242_0.jpg)

(第 5 题)

(1)求割线 ${PQ}$ 的斜率；

(2)当点 $Q$ 沿曲线向点 $P$ 运动时,割线 ${PQ}$ 的斜率会变大还是变小?

6. 已知 $f\left( x\right)  =  - {x}^{2}$ ,求曲线 $y = f\left( x\right)$ 在下列各点处的切线斜率, 并说明这些斜率的值是如何随着自变量的变化而变化的:

(1) $x =  - 2$ ； (2) $x =  - 1$ ； (3) $x = 0$ ；

(4) $x = 1$ ； (5) $x = 2$ .

7. 借助函数图像,判断下列导数的正负:

(1) ${f}^{\prime }\left( {-\frac{\pi }{4}}\right)$ ，其中 $f\left( x\right)  = \cos x$ ； (2) ${f}^{\prime }\left( 3\right)$ ，其中 $f\left( x\right)  = \ln x$ .

##### B 组

1. 已知车辆启动后的一段时间内，车轮旋转的角度和时间 (单位:秒) 的平方成正比， 且车辆启动后车轮转动第一圈需要 1 秒.

(1)求车轮转动前 2 秒的平均角速度；

(2)求车轮在转动开始后第 3 秒的瞬时角速度.

2. 根据导数的几何意义,求函数 $y = \sqrt{4 - {x}^{2}}$ 在下列各点处的导数:

(1) $x =  - 1$ ； (2) $x = 0$ ； (3) $x = 1$ .

3. 已知函数 $y = f\left( x\right)$ 在 $x = 1$ 处的切线方程为 $y = {4x} - 3$ ,求 $f\left( 1\right)$ 和 ${f}^{\prime }\left( 1\right)$ .

4. 如图,已知直线 $l$ 是曲线 $y = f\left( x\right)$ 在 $x = 3$ 处的切线,求 ${f}^{\prime }\left( 3\right)$ .

![bo_d4slovref24c73be0r3g_9_626_1380_422_239_0.jpg](images/bo_d4slovref24c73be0r3g_9_626_1380_422_239_0.jpg)

(第 4 题)

## 5.2 导数的运算

在本章 5.1 节的学习中, 我们已经了解到一个函数在某点处导数的概念. 从导数的定义中不难发现: 给定函数 $y = f\left( x\right)$ ,在导数存在的前提下,对于不同的 ${x}_{0}$ ,总有一个确定的导数值 ${f}^{\prime }\left( {x}_{0}\right)$ 与之对应. 换句话说,如果用 $x$ 表示自变量,那么 ${y}^{\prime } = \; {f}^{\prime }\left( x\right)$ 也是一个关于 $x$ 的函数. 称为函数 $y = f\left( x\right)$ 的导函数 (derived function, 也简称为导数), 其中

$$
{f}^{\prime }\left( x\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {x + h}\right)  - f\left( x\right) }{h}.
$$

求一个函数的导 (函) 数的过程常简称为求导.

如果能够求出函数 $y = f\left( x\right)$ 的导数 ${y}^{\prime } = {f}^{\prime }\left( x\right)$ ,那么求该函数在某点处导数的问题就可以通过简单的代入求值来解决.

### 1 基本初等函数的导数

根据导数的定义, 可以求出一些基本初等函数的导数.

例 1 求常数函数 $y = C$ 的导数.

解 记 $f\left( x\right)  = C$ . 当 $h \neq  0$ 时,

$$
\frac{f\left( {x + h}\right)  - f\left( x\right) }{h} = \frac{C - C}{h} = \frac{0}{h} = 0.
$$

因此,当 $h$ 趋近于 0 时, ${f}^{\prime }\left( x\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}0 = 0$ .

对于例 1 中的函数 $y = f\left( x\right)$ ,坐标平面中的相应曲线 $y = \; f\left( x\right)$ 是平行于 $x$ 轴的直线 $y = C$ ,连接该直线上任何两点的割线都是这条直线本身, 从而该直线上任何一点处的切线也是这条直线本身. 由此可见, 该直线上任何一点处的切线的斜率都是 0 , 即对任何给定的 ${x}_{0}$ ,都有 ${f}^{\prime }\left( {x}_{0}\right)  = 0$ . 由此推出 ${f}^{\prime }\left( x\right)  = 0$ . 这就从导数的几何意义诠释了例 1 的结论.

类似的分析适用于函数 $y = {kx} + b$ . 记 $f\left( x\right)  = {kx} + b$ . 直线 $y \; = {kx} + b$ 上任何一点处的切线都是这条直线本身,从而都具有斜率 $k$ ,即对任何给定的 ${x}_{0}$ ,都有 ${f}^{\prime }\left( {x}_{0}\right)  = k$ . 由此推出 ${f}^{\prime }\left( x\right)  = k$ . 这个从几何上推出的结论也可用导数的定义来验证.

---

常数函数、幂函数、指数函数、对数函数、三角函数、反三角函数被称为基本初等函数.

---

例 2 求函数 $y = {kx} + b$ 的导数.

解 记 $f\left( x\right)  = {kx} + b$ . 当 $h \neq  0$ 时,

$$
\frac{f\left( {x + h}\right)  - f\left( x\right) }{h} = \frac{k\left( {x + h}\right)  + b - \left( {{kx} + b}\right) }{h} = \frac{kh}{h} = k.
$$

因此,当 $h$ 趋近于 0 时, ${f}^{\prime }\left( x\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}k = k$ .

例 3 求下列幂函数 $y = f\left( x\right)$ 的导数,其中:

(1) $f\left( x\right)  = {x}^{2}$ ； (2) $f\left( x\right)  = {x}^{-1}$ ； (3) $f\left( x\right)  = {x}^{\frac{1}{2}}$ .

解(1)当 $h \neq  0$ 时，

$$
\frac{f\left( {x + h}\right)  - f\left( x\right) }{h} = \frac{{\left( x + h\right) }^{2} - {x}^{2}}{h} = \frac{{2xh} + {h}^{2}}{h} = {2x} + h.
$$

因此,当 $h$ 趋近于 0 时, ${f}^{\prime }\left( x\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\left( {{2x} + h}\right)  = {2x}$ .

(2)当 $h \neq  0$ 时，

$$
\frac{f\left( {x + h}\right)  - f\left( x\right) }{h} = \frac{{\left( x + h\right) }^{-1} - {x}^{-1}}{h} = \frac{x - \left( {x + h}\right) }{x\left( {x + h}\right) h} = \frac{-1}{x\left( {x + h}\right) }.
$$

因此,当 $h$ 趋近于 0 时, ${f}^{\prime }\left( x\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{-1}{x\left( {x + h}\right) } =  - \frac{1}{{x}^{2}} =  - {x}^{-2}$ .

(3)当 $h \neq  0$ 时,

$$
\frac{f\left( {x + h}\right)  - f\left( x\right) }{h} = \frac{\sqrt{x + h} - \sqrt{x}}{h}
$$

$$
= \frac{\left( {\sqrt{x + h} - \sqrt{x}}\right) \left( {\sqrt{x + h} + \sqrt{x}}\right) }{h\left( {\sqrt{x + h} + \sqrt{x}}\right) }
$$

$$
= \frac{1}{\sqrt{x + h} + \sqrt{x}}.
$$

因此,当 $h$ 趋近于 0 时, ${f}^{\prime }\left( x\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{1}{\sqrt{x + h} + \sqrt{x}} = \frac{1}{2\sqrt{x}} = \frac{1}{2}{x}^{-\frac{1}{2}}$ .

为了更便捷地处理求导问题, 我们通常将以下基本初等函数的导数作为公式使用:

(1) ${\left( C\right) }^{\prime } = 0$ ， $C$ 为常数；

(2) ${\left( {x}^{\alpha }\right) }^{\prime } = \alpha {x}^{\alpha  - 1},\alpha$ 为常数；

(3) ${\left( {\mathrm{e}}^{x}\right) }^{\prime } = {\mathrm{e}}^{x}$ ；

(4) ${\left( \ln x\right) }^{\prime } = \frac{1}{x}$ ；

(5) ${\left( \sin x\right) }^{\prime } = \cos x$

(6) ${\left( \cos x\right) }^{\prime } =  - \sin x$ .

---

我们已经推导了公式(1)以及公式(2) 的一些特殊情况. 如果对这些公式的完整推导过程感兴趣, 可参阅高等数学的有关教科书.

---

例 4 已知函数 $y = f\left( x\right)$ ,其中 $f\left( x\right)  = \frac{1}{{x}^{2}}$ . 求 ${f}^{\prime }\left( 2\right)$ .

解 因为

$$
{f}^{\prime }\left( x\right)  = {\left( \frac{1}{{x}^{2}}\right) }^{\prime } = {\left( {x}^{-2}\right) }^{\prime } =  - 2{x}^{-2 - 1} =  - 2{x}^{-3},
$$

所以

$$
{f}^{\prime }\left( 2\right)  =  - 2 \times  {2}^{-3} =  - \frac{1}{4}.
$$

例 5 求正弦函数 $y = \sin x$ 的驻点.

解 因为 ${y}^{\prime } = \cos x$ ,而 $\cos x = 0$ 的解是 $x = {k\pi } + \frac{\pi }{2}\left( {k \in  \mathbf{Z}}\right)$ , 所以当且仅当 $x = {k\pi } + \frac{\pi }{2}\left( {k \in  \mathbf{Z}}\right)$ 时,正弦函数 $y = \sin x$ 的导数为零,即正弦函数 $y = \sin x$ 的驻点为 $x = {k\pi } + \frac{\pi }{2}\left( {k \in  \mathbf{Z}}\right)$ .

---

从函数图像上看， 这些驻点有什么特殊性质?

---

#### 练习 5.2(1)

1. 用导数的定义求函数 $y = {x}^{2} + {3x} - 5$ 的导数.

2. 用公式求下列函数 $y = f\left( x\right)$ 的导数,其中:

(1) $f\left( x\right)  = \sqrt[3]{{x}^{2}}$ ； (2) $f\left( x\right)  = {x}^{\pi }$ .

3. 求余弦函数 $y = \cos x$ 在 $x = \frac{\pi }{2}$ 处的导数.

4. 证明函数 $y = \ln x$ 与 $y = {\mathrm{e}}^{x}$ 没有驻点.

#### 探究与实践

在我们熟悉的基本初等函数中, 有哪些函数的图像存在水平切线? 有哪些函数的图像在所有点处切线的斜率均大于 0 ? 尝试从导数公式和函数图像两个角度进行探究.

### 2 导数的四则运算

基本初等函数可以通过四则运算产生新的初等函数. 这些初等函数的求导可以通过以下的“导数四则运算法则”归结为基本初等函数的求导.

对函数 $y = f\left( x\right)$ 与 $y = g\left( x\right)$ ,以下等式成立:

(7) ${\left( f\left( x\right)  \pm  g\left( x\right) \right) }^{\prime } = {f}^{\prime }\left( x\right)  \pm  {g}^{\prime }\left( x\right)$ ;

(8) ${\left( f\left( x\right) g\left( x\right) \right) }^{\prime } = {f}^{\prime }\left( x\right) g\left( x\right)  + f\left( x\right) {g}^{\prime }\left( x\right)$ ;

(9) ${\left( \frac{f\left( x\right) }{g\left( x\right) }\right) }^{\prime } = \frac{{f}^{\prime }\left( x\right) g\left( x\right)  - f\left( x\right) {g}^{\prime }\left( x\right) }{{\left( g\left( x\right) \right) }^{2}}$ ,其中 $g\left( x\right)  \neq  0$ .

用导数的定义可以推导出这些公式. 这里只推导关于积的求导公式(8)，其余的留给有兴趣的同学自行完成.

由导数的定义,

$$
f\left( {x + h}\right) g\left( {x + h}\right)  - f\left( x\right) g\left( x\right)
$$

$$
= f\left( {x + h}\right) g\left( {x + h}\right)  - f\left( x\right) g\left( {x + h}\right)  + f\left( x\right) g\left( {x + h}\right)  - f\left( x\right) g\left( x\right)
$$

$$
= \left\lbrack  {f\left( {x + h}\right)  - f\left( x\right) }\right\rbrack  g\left( {x + h}\right)  + f\left( x\right) \left\lbrack  {g\left( {x + h}\right)  - g\left( x\right) }\right\rbrack  ,
$$

于是可得

$$
\frac{f\left( {x + h}\right) g\left( {x + h}\right)  - f\left( x\right) g\left( x\right) }{h}
$$

$$
= \frac{f\left( {x + h}\right)  - f\left( x\right) }{h}g\left( {x + h}\right)  + f\left( x\right) \frac{g\left( {x + h}\right)  - g\left( x\right) }{h}.
$$

所以,当 $h$ 趋近于 0 时,就有

$$
{\left( f\left( x\right) g\left( x\right) \right) }^{\prime } = {f}^{\prime }\left( x\right) g\left( x\right)  + f\left( x\right) {g}^{\prime }\left( x\right) .
$$

例 6 证明: 对函数 $y = f\left( x\right)$ 与任何常数 $C$ ,都有

$$
\text{ (10) }{\left( Cf\left( x\right) \right) }^{\prime } = C{f}^{\prime }\left( x\right) \text{ . }
$$

证明 用积的求导公式和常数函数的求导公式, 得到

$$
{\left( Cf\left( x\right) \right) }^{\prime } = {\left( C\right) }^{\prime }f\left( x\right)  + C{f}^{\prime }\left( x\right)  = C{f}^{\prime }\left( x\right) .
$$

例 7 求下列函数 $y = f\left( x\right)$ 的导数，其中:

(1) $f\left( x\right)  = {x}^{2}\sin x$ ；___

(2) $f\left( x\right)  = \frac{{x}^{2}}{x + 2}$ ；

(3) $f\left( x\right)  = {\left( x - 2\right) }^{2}$ .

解 (1) 用积的求导公式以及幂函数与正弦函数的求导公式, 得到

${f}^{\prime }\left( x\right)  = {\left( {x}^{2}\sin x\right) }^{\prime } = {\left( {x}^{2}\right) }^{\prime }\sin x + {x}^{2}{\left( \sin x\right) }^{\prime } = {2x}\sin x + {x}^{2}\cos x.$

(2)用商的求导公式、和的求导公式以及幂函数与常数函数的求导公式, 得到

$$
{f}^{\prime }\left( x\right)  = {\left( \frac{{x}^{2}}{x + 2}\right) }^{\prime } = \frac{{\left( {x}^{2}\right) }^{\prime }\left( {x + 2}\right)  - {x}^{2}{\left( x + 2\right) }^{\prime }}{{\left( x + 2\right) }^{2}} = \frac{{2x}\left( {x + 2}\right)  - {x}^{2}}{{\left( x + 2\right) }^{2}} = \frac{{x}^{2} + {4x}}{{\left( x + 2\right) }^{2}}.
$$

(3)先把函数表达式展开，得 $f\left( x\right)  = {x}^{2} - {4x} + 4$ ，再用和、

差的求导公式、公式 (10) 以及幂函数与常数函数的求导公式, 得到

$$
{f}^{\prime }\left( x\right)  = {\left( {x}^{2}\right) }^{\prime } - {\left( 4x\right) }^{\prime } + {\left( 4\right) }^{\prime } = {2x} - 4.
$$

例 8 设实数 $a > 0$ 且 $a \neq  1$ ,求证: ${\left( {\log }_{a}x\right) }^{\prime } = \frac{1}{x\ln a}$ .

证明 先用换底公式,有 ${\log }_{a}x = \frac{\ln x}{\ln a}$ ,再由公式 (10) 以及对数函数的求导公式, 得到

$$
{\left( {\log }_{a}x\right) }^{\prime } = {\left( \frac{\ln x}{\ln a}\right) }^{\prime } = \frac{1}{\ln a}{\left( \ln x\right) }^{\prime } = \frac{1}{x\ln a}.
$$

#### 练习 5.2(2)

求下列函数 $y = f\left( x\right)$ 的导数,其中:

(1) $f\left( x\right)  = 3{\mathrm{e}}^{x} - {x}^{\mathrm{e}} + \mathrm{e}$ ； (2) $f\left( x\right)  = \cos x - \frac{2}{x}$ ；

(3) $f\left( x\right)  = {\left( 2x + 1\right) }^{3}$ ； (4) $f\left( x\right)  = \sqrt{x}\sin x$ ；

(5) $f\left( x\right)  = x\ln x - \frac{1}{{x}^{2}}$ ; (6) $f\left( x\right)  = \frac{{x}^{2} - 1}{x}$ ；

(7) $f\left( x\right)  = \frac{{x}^{2} - 1}{{x}^{2} + 1}$ ; (8) $f\left( x\right)  = \tan x$ .

### 3 简单复合函数的导数

在本节例 7 第( 3 )小题中，为了求 $f\left( x\right)  = {\left( x - 2\right) }^{2}$ 的导数，我们先借助于完全平方公式将 ${\left( x - 2\right) }^{2}$ 化为 ${x}^{2} - {4x} + 4$ ,再利用导数四则运算法则求导. 从另一个角度看,函数 $y = {\left( x - 2\right) }^{2}$ 也可以看作由两个函数 $y = {u}^{2}\text{ 、 }u = x - {2}^{u}$ 套”在一起所构成的新函数. 像这样,如果一个函数 $y = f\left( u\right)$ 的自变量 $u$ 又是另一个变量 $x$ 的函数 $u = g\left( x\right)$ , 那么就可将 $y$ 直接看作变量 $x$ 的函数而得到一个新函数 $y = \; f\left( {g\left( x\right) }\right)$ ，这个新函数被称为两个函数的复合函数(composite function).

在对复合函数求导数时, 往往不是把两个预先给定的函数先复合成较复杂的函数, 然后直接求导, 而是反过来, 先引进一个中间变量, 把原来的函数看作两个相对简单的函数的复合, 再利用复合函数的求导法则求其导数, 从而使求导过程得到简化. 例如,函数 $f\left( x\right)  = {\left( x - 2\right) }^{2}$ 可看作由函数 $y = {u}^{2}$ 与 $u = x - 2$ 复合而成,而函数 $y = \sin {2x}$ 可看作由函数 $y = \sin u$ 与 $u = {2x}$ 复合而成.

我们不讨论一般复合函数的求导问题,仅考虑由 $y = f\left( u\right)$ 与 $u = {ax} + b\left( {a \neq  0}\right)$ 复合而成的 $f\left( {{ax} + b}\right)$ 型复合函数的求导法则.

因为当 $h \neq  0$ 时,有

$$
\frac{f\left( {a\left( {x + h}\right)  + b}\right)  - f\left( {{ax} + b}\right) }{h} = a \cdot  \frac{f\left( {u + {ah}}\right)  - f\left( u\right) }{ah},
$$

且注意到 $h$ 趋近于 0 当且仅当 ${ah}$ 趋近于 0 ，所以

$$
\mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {a\left( {x + h}\right)  + b}\right)  - f\left( {{ax} + b}\right) }{h} = a\mathop{\lim }\limits_{{{ah} \rightarrow  0}}\frac{f\left( {u + {ah}}\right)  - f\left( u\right) }{ah}.
$$

这就给出了 $f\left( {{ax} + b}\right)$ 型复合函数的如下求导法则:

(11) ${\left( f\left( ax + b\right) \right) }^{\prime } = a{f}^{\prime }\left( u\right)$ ,其中 $u = {ax} + b$ .

例 9 求 $f\left( x\right)  = \ln \left( {2 - {5x}}\right)$ 的导数.

解 将 $f\left( x\right)  = \ln \left( {2 - {5x}}\right)$ 看作由 $f\left( u\right)  = \ln u$ 与 $u = 2 - {5x}$ 复合而成, 则

$$
{f}^{\prime }\left( x\right)  =  - 5{\left( \ln u\right) }^{\prime } =  - \frac{5}{u} = \frac{5}{{5x} - 2}.
$$

例 10 设实数 $a > 0$ 且 $a \neq  1$ ,求证: ${\left( {a}^{x}\right) }^{\prime } = {a}^{x}\ln a$ .

证明 因为 ${a}^{x} = {\mathrm{e}}^{\ln {a}^{x}} = {\mathrm{e}}^{x\ln a}$ ,可以把 $f\left( x\right)  = {\mathrm{e}}^{x\ln a}$ 看作由 $f\left( u\right)  = {\mathrm{e}}^{u}$ 与 $u = x\ln a$ 复合而成,所以

$$
{f}^{\prime }\left( x\right)  = {\left( {\mathrm{e}}^{u}\right) }^{\prime }\ln a = {\mathrm{e}}^{u}\ln a = {\mathrm{e}}^{x\ln a}\ln a = {a}^{x}\ln a,
$$

即 ${\left( {a}^{x}\right) }^{\prime } = {a}^{x}\ln a$ .

#### 练习 5.2(3)

1. 利用 $f\left( {{ax} + b}\right)$ 型复合函数的求导法则求下列函数的导数:

(1) $y = {\left( 3 - 2x\right) }^{2}$ ; (2) $y = \sin {2x}$ .

2. 尝试用两种不同的方法求 $f\left( x\right)  = \frac{1}{{2x} - 1}$ 的导数.

3. 求曲线 $y = {2}^{1 - {3x}}$ 在点 $\left( {0,2}\right)$ 处的切线方程.

4. 求下列函数的导数:

(1) $y = {3x}\sqrt{2 - x}$ ； (2) $y = \frac{\ln \left( {{2x} + 1}\right) }{x}$ .

#### 探究与实践

按以下步骤探究复合函数求导的一般规律:

1. 分别求 $y = {\left( {x}^{3} - 2\right) }^{2}\text{ 、 }y = {u}^{2}$ 与 $u = {x}^{3} - 2$ 的导数,并探索三个导数之间的联系;

2. 分别求 $y = {\sin }^{2}x + \sin x - 1\text{ 、 }y = {u}^{2} + u - 1$ 与 $u = \sin x$ 的导数,并探索三个导数之间的联系;

3. 根据上述两个特例, 猜想复合函数求导的一般规律, 并用一些实例验证你的猜想.

#### 习题 5.2

##### A 组

1. 求下列函数 $y = f\left( x\right)$ 的导数:

(1) $f\left( x\right)  = \pi$ ； (2) $f\left( x\right)  = \sqrt[3]{{x}^{5}}$ ；

(3) $f\left( x\right)  = \frac{1}{{x}^{3}}$ .

2. 求曲线 $y = \cos x$ 在 $x = \frac{\pi }{2}$ 处的切线方程.

3. 已知曲线 $y = {x}^{3}$ 在原点以外某点 $P$ 处切线的斜率为 $a$ .

(1)求点 $P$ 的坐标； (2)判断 $a$ 的正负.

4. 求曲线 $y = {x}^{3} - {3x} + 5$ 平行于 $x$ 轴的切线及其切点坐标.

5. 求曲线 $y = \frac{1}{x}$ 平行于直线 $y =  - x$ 的切线及其切点坐标.

6. 求下列函数 $y = f\left( x\right)$ 的导数:

(1) $f\left( x\right)  = 2{x}^{\mathrm{e}} - {\mathrm{e}}^{2}$ ； (2) $f\left( x\right)  = {\mathrm{e}}^{x}\cos x$ ；

(3) $f\left( x\right)  = \frac{x - 1}{x - 2}$ ； (4) $f\left( x\right)  = \frac{\ln x}{\sin x}$ .

7. 用两种方法求函数 $y = \left( {x - 2}\right) \left( {3 - {4x}}\right)$ 的导数.

8. 已知函数 $y = f\left( x\right)$ 与 $y = g\left( x\right)$ 满足条件 $f\left( 1\right)  = 2,{f}^{\prime }\left( 1\right)  = 3, g\left( 1\right)  = 4$ 与 ${g}^{\prime }\left( 1\right)  = 5$ . 对于下列函数 $y = h\left( x\right)$ ,求 $h\left( 1\right)$ 和 ${h}^{\prime }\left( 1\right)$ :

(1) $h\left( x\right)  = {2g}\left( x\right)  - \frac{1}{3}f\left( x\right)$ ； (2) $h\left( x\right)  = {2g}\left( x\right) f\left( x\right)  - \frac{1}{3};$

(3) $h\left( x\right)  = \frac{{2g}\left( x\right)  - 1}{{3f}\left( x\right) }$ .

9. 利用 $f\left( {{ax} + b}\right)$ 型复合函数的求导法则,求下列函数的导数:

(1) $y = \sqrt{{2x} - 5}$ ； (2) $y = \cos \frac{x}{2}$ ；

(3) $y = \frac{1}{{\mathrm{e}}^{x + 1}}$ .

10. 用两种方法求函数 $y = \frac{2}{x - 1}$ 的导数.

11. 某种动物的体温 $T$ (单位:℃)与太阳落山后经过的时间 $t$ (单位:min) 满足函数关系 $T = \frac{120}{t + 5} + {15}$ .

(1)当 $t = 5$ 时，求该动物体温的瞬时变化率；

(2)在哪一时刻该动物体温的瞬时变化率是 $- 2{}^{ \circ  }\mathrm{C}/\mathrm{{min}}$ ？(结果精确到 ${0.1}\mathrm{\;{min}}$ )

12. 已知某港口一天内潮水的深度 $y$ (单位: $\mathrm{m}$ ) 与时间 $t$ (单位: $\mathrm{h}$ ) 近似满足函数关系 $y = 3\sin \left( {\frac{\pi }{12}t + \frac{5\pi }{6}}\right) ,0 \leq  t \leq  {24}$ . 分别求上午 6 时与下午 6 时潮水涨(落) 的速度.

##### B 组

1. 已知一列火车从静止开始加速的一段时间内,其行驶速度 $v$ (单位: $\mathrm{m}/\mathrm{s}$ )与行驶时间 $t$ (单位: $\mathrm{s}$ )满足函数关系 $v = {0.4t} + {0.6}{t}^{2}$ .

(1)求这段时间内火车行驶的加速度；

(2)火车行驶到哪一时刻，其加速度为 $4\mathrm{\;m}/{\mathrm{s}}^{2}$ ？

2. 直线 $y =  - x + b$ 是下列函数的切线吗? 如果是,请求出 $b$ 的值; 如果不是,请说明理由.

(1) $y = \ln x$ ； (2) $y = \frac{1}{x}$ .

3. 吹一个球形的气球时,气球半径 $r$ 将随空气容量 $V$ 的增加而增大.

(1)写出气球半径 $r$ 关于气球内空气容量 $V$ 的函数表达式；

(2)求 $V = 1$ 时，气球的瞬时膨胀率(即气球半径关于气球内空气容量的瞬时变化率).

4. 判断下列求导结果是否正确. 如果不正确, 请指出错在哪里, 并予以改正.

(1) ${\left( \frac{\sin x}{x}\right) }^{\prime } =  - \frac{1}{{x}^{2}}\sin x - \frac{\cos x}{x}$ ; (2) ${\left( \ln \left( 2 - x\right) \right) }^{\prime } = \frac{1}{2 - x}$ .

5. 求过点 $\left( {0, - 1}\right)$ 且与曲线 $y = 2{x}^{2}$ 相切的直线的方程.

6. 已知一罐汽水放入冰箱后的温度 $x$ (单位: $\text{ ℃ }$ ) 与时间 $t$ (单位: $\mathrm{h}$ ) 满足函数关系 $x = 4 + {16}{\mathrm{e}}^{-{2t}}.$

(1)求 ${x}^{\prime }\left( 1\right)$ ，并解释其实际意义；

(2)已知摄氏度 $x$ 与华氏度 $y$ (单位: $F$ 】满足函数关系 $x = \frac{5}{9}\left( {y - {32}}\right)$ ，求 $y$ 关于 $t$ 的导数, 并解释其实际意义.

7. 求下列函数 $y = f\left( x\right)$ 的导数,其中:

(1) $f\left( x\right)  = {x}^{2}\sin {3x} - \frac{2}{\sqrt{x}}$ ; (2) $f\left( x\right)  = \frac{{\mathrm{e}}^{x} - {\mathrm{e}}^{-x}}{{\mathrm{e}}^{x} + {\mathrm{e}}^{-x}}$ .

## 5.3 导数的应用

在对函数的研究中, 单调性与极大 (小) 值、最大 (小) 值是重要的主题之一. 但限于初等数学所能提供的工具, 在很多常见函数面前, 我们往往束手无策, 而导数则为我们研究函数的这些性质提供了通用和便捷的手段.

本章引入的定理大多需要高等数学的知识才能严格证明, 但同学们可以借助一些熟悉的函数 (如二次函数) 来验证这些结论的合理性.

### 1 利用导数研究函数的单调性

函数的单调性研究的是在一个区间内函数是否严格增或严格减, 即函数值是否随着自变量的增大而增大, 或随着自变量的增大而减小. 导数是函数的瞬时变化率, 反映了在自变量发生变化的瞬间, 函数值随之发生的增减变化, 因此, 导数是研究函数单调性的最佳工具. 特别地, 从导数的正负就可以直接判断函数的单调性:

定理 在区间 $I$ 上,若 ${f}^{\prime }\left( x\right)  > 0$ ,则函数 $y = f\left( x\right)$ 在该区间严格增; 若 ${f}^{\prime }\left( x\right)  < 0$ ,则函数 $y = f\left( x\right)$ 在该区间严格减.

在导数值都存在的情况下, 导数值由正变负或由负变正的过程中会出现导数等于零的点, 即函数的驻点. 因此, 要把函数的单调增区间和单调减区间划分出来, 就要先找到函数的驻点. 找到驻点后, 再看驻点两侧导数值的正负是否发生变化, 如果发生变化了, 此驻点就成为单调增区间与单调减区间的分界点.

例 1 已知 $f\left( x\right)  = {x}^{2} - {4x} + 2$ ,求函数 $y = f\left( x\right)$ 的单调区间.

解 先求函数的驻点: ${f}^{\prime }\left( x\right)  = {2x} - 4$ . 令 ${f}^{\prime }\left( x\right)  = 0$ ,解得 $x = 2$ . 此函数只有一个驻点.

当 $x > 2$ 时, ${f}^{\prime }\left( x\right)  > 0$ ,函数 $y = f\left( x\right)$ 严格增;

当 $x < 2$ 时, ${f}^{\prime }\left( x\right)  < 0$ ,函数 $y = f\left( x\right)$ 严格减.

---

对一些你熟悉的函数, 借助信息技术工具，从数值和图像两个角度进行尝试， 获得的结论一致吗?

---

因此,函数 $y = f\left( x\right)$ 的单调增区间为 $\left( {2, + \infty }\right)$ ,单调减区间为 $\left( {-\infty ,2}\right)$ .

例 2 已知 $f\left( x\right)  = {x}^{3} + {x}^{2} - x - 1$ ,求函数 $y = f\left( x\right)$ 的单调区间.

解 对函数求导,得 ${f}^{\prime }\left( x\right)  = 3{x}^{2} + {2x} - 1$ . 令 ${f}^{\prime }\left( x\right)  = 0$ , 解得 ${x}_{1} =  - 1,{x}_{2} = \frac{1}{3}$ . 此函数有两个驻点.

当 $x <  - 1$ 或 $x > \frac{1}{3}$ 时, ${f}^{\prime }\left( x\right)  > 0$ ,函数 $y = f\left( x\right)$ 严格增;

当 $- 1 < x < \frac{1}{3}$ 时, ${f}^{\prime }\left( x\right)  < 0$ ,函数 $y = f\left( x\right)$ 所格减.

因此，函数 $y = f\left( x\right)$ 的单调增区间为 $\left( {-\infty , - 1}\right)$ 及 $\left( {\frac{1}{3}, + \infty }\right)$ , 单调减区间为 $\left( {-1,\frac{1}{3}}\right)$ .

注意, 有时驻点并不是单调增区间与单调减区间的分界点.

例 3 已知 $f\left( x\right)  = {x}^{3}$ ,求函数 $y = f\left( x\right)$ 的单调区间.

解 对函数求导,得 ${f}^{\prime }\left( x\right)  = 3{x}^{2}$ . 令 ${f}^{\prime }\left( x\right)  = 0$ ,解得 $x = 0$ ,所以此函数在 $x = 0$ 时有唯一的驻点. 但是,由于永远成立 ${f}^{\prime }\left( x\right)  \geq  0$ ,驻点两侧导数值的正负没有发生变化,因此该驻点不是单调区间的分界点. 此函数的单调增区间为 $\left( {-\infty , + \infty }\right)$ .

在讨论中, 我们也要注意函数没有定义的点. 这样的点也可能成为单调增区间与单调减区间的分界点.

例 4 已知 $f\left( x\right)  = {x}^{-2}$ ,求函数 $y = f\left( x\right)$ 的单调区间.

解 该函数在 $x = 0$ 处没有定义. 当 $x \neq  0$ 时, ${f}^{\prime }\left( x\right)  = \; - 2{x}^{-3}$ ,因为方程 ${f}^{\prime }\left( x\right)  = 0$ 无解,所以函数 $y = f\left( x\right)$ 没有驻点. 但当 $x > 0$ 时, ${f}^{\prime }\left( x\right)  < 0, f\left( x\right)$ 严格减; 当 $x < 0$ 时, ${f}^{\prime }\left( x\right)  > 0$ , $f\left( x\right)$ 严格增. 可见,函数 $y = f\left( x\right)$ 的单调增区间为 $\left( {-\infty ,0}\right)$ ,单调减区间为 $\left( {0, + \infty }\right)$ ,而其分界点恰是该函数没有定义的点.

上面我们用导数值的正负来判断函数在某区间上的单调性. 除此之外，导数值还可用以判断函数变化速度的快慢:导数 ${f}^{\prime }\left( {x}_{0}\right)$ 是函数 $y = f\left( x\right)$ 在点 ${x}_{0}$ 处的切线的斜率,它描述了曲线 $y = f\left( x\right)$ 在点 ${x}_{0}$ 附近相对于 $x$ 轴的倾斜程度: 当 ${f}^{\prime }\left( {x}_{0}\right)  > 0$ 时, ${f}^{\prime }\left( {x}_{0}\right)$ 越大,曲线 $y = f\left( x\right)$ 在点 ${x}_{0}$ 附近相对于 $x$ 轴倾斜程度越大,函数值 $y = f\left( x\right)$ 递增得越快; 而当 ${f}^{\prime }\left( {x}_{0}\right)  < 0$ 时, ${f}^{\prime }\left( {x}_{0}\right)$ 越小,曲线 $y = f\left( x\right)$ 在点 ${x}_{0}$ 附近相对于 $x$ 轴倾斜程度越大,函数值 $y = f\left( x\right)$ 递减得越快. 总之,导数的绝对值越大,函数图像就越“陡峭”，也就是函数值的变化速度越快.

---

用已经学过的二次函数知识验证这个结果.

利用信息技术工具绘制这个函数的图像以验证结果.

此例表明, ${f}^{\prime }\left( x\right)$ >0 并不是函数在一个区间上严格增的必要条件.

---

例 5 已知在区间 $\left( {0,1}\right)$ 上 ${f}^{\prime }\left( x\right)  > 1$ . 在图 5-3-1 所示的图像中,哪些有可能表示函数 $y = f\left( x\right)$ ? 为什么?

![bo_d4slovref24c73be0r3g_20_172_430_925_249_0.jpg](images/bo_d4slovref24c73be0r3g_20_172_430_925_249_0.jpg)

图 5-3-1

解 在区间 $\left( {0,1}\right)$ 上,因为 ${f}^{\prime }\left( x\right)  > 1$ ,所以函数图像中每一点处切线的斜率都应大于 1 . 在图 5-3-1 中，由观察可知:

图(1)中的曲线越来越“陡峭”，在区间 $\left( {0,1}\right)$ 上各点处的切线斜率始终大于 1 ;

图(2)中的曲线由“陡峭”变得“平缓”，在区间 $\left( {0,1}\right)$ 的右半段的切线斜率小于 1 ;

图(3)中的曲线由 “平缓” 变得 “陡峭”，在区间 $\left( {0,1}\right)$ 的左半段的切线斜率小于 1 ;

图(4)中的曲线越来越“平缓”，在区间 $\left( {0,1}\right)$ 上各点处的切线斜率始终小于 1 .

因此,只有图 5-3-1(1) 中的图像有可能表示函数 $y = f\left( x\right)$ .

#### 练习 5.3(1)

1. 利用导数研究下列函数的单调性, 并说明所得结果与你之前的认识是否一致:

(1) $y = {\mathrm{e}}^{x}$ ； (2) $y = \ln x$ ；

(3) $y = a{x}^{2} + {bx} + c$ ，其中 $a \neq  0$ .

2. 确定下列函数的单调区间:

(1) $y = x{\mathrm{e}}^{x}$ ; (2) $y = 4{x}^{3} - 9{x}^{2} + {6x} + 7$ .

### 2 利用导数研究函数的极值

观察图 5-3-2 中函数 $y = f\left( x\right)$ 的图像,其中有一些特殊的点, 在这些特殊点的左右两侧附近, 函数的单调性发生了改变. 例如,函数在点 $\left( {{x}_{1}, f\left( {x}_{1}\right) }\right)$ 的左侧附近严格增,右侧附近严格减，此处出现了一个“山峰”；又如，函数在点 $\left( {{x}_{2}, f\left( {x}_{2}\right) }\right)$ 的左侧附近严格减，右侧附近严格增，此处出现了一个“山谷”.

![bo_d4slovref24c73be0r3g_21_629_257_776_309_0.jpg](images/bo_d4slovref24c73be0r3g_21_629_257_776_309_0.jpg)

图 5-3-2

换句话说,在 $x = {x}_{1}$ 附近存在一个小区间,该区间内其他自变量所对应的函数值都不大于 $f\left( {x}_{1}\right)$ ,此时,就说函数 $y = f\left( x\right)$ 在 $x = {x}_{1}$ 处取得极大值 $f\left( {x}_{1}\right)$ ,而点 ${x}_{1}$ 称为函数 $y = f\left( x\right)$ 的极大值点. 类似地,在 $x = {x}_{2}$ 附近存在一个小区间,该区间内其他自变量所对应的函数值都不小于 $f\left( {x}_{2}\right)$ ,此时,就说函数 $y = f\left( x\right)$ 在 $x = {x}_{2}$ 处取得极小值 $f\left( {x}_{2}\right)$ ,而点 ${x}_{2}$ 称为函数 $y = f\left( x\right)$ 的极小值点.

因此,图 5-3-2 所示的函数有三个极大值点 ${x}_{1}\text{ 、 }{x}_{3}\text{ 、 }{x}_{5}$ , 还有三个极小值点 ${x}_{2}\text{ 、 }{x}_{4}\text{ 、 }{x}_{6}$ .

极大值和极小值统称为极值, 而极大值点和极小值点则统称为极值点.

在导数都存在的前提下, 极值点一定是相应函数单调增区间及单调减区间的分界点, 从而是函数的驻点, 函数曲线在该点的切线是水平的. 但反过来, 我们却不能说一个函数的驻点一定是其极值点. 例如,在函数 $y = {x}^{3}$ 中,点 $x = 0$ 虽是其驻点,但不是极值点,因为这个函数在整个区间 $\left( {-\infty , + \infty }\right)$ 上是严格增的. 因此,要找到函数 $y = f\left( x\right)$ 的极值点,通过 ${f}^{\prime }\left( {x}_{0}\right)  = 0$ 找到驻点 $x = {x}_{0}$ 只是第一步,还要根据驻点附近 ${f}^{\prime }\left( x\right)$ 的符号才能断定 ${x}_{0}$ 是否为 $f\left( x\right)$ 的极值点.

具体地说,我们有如下定理:

定理 设点 $x = {x}_{0}$ 是函数 $y = f\left( x\right)$ 的驻点.

(1)若在点 ${x}_{0}$ 的左侧附近有 ${f}^{\prime }\left( x\right)  > 0$ ，而在 ${x}_{0}$ 的右侧附近有 ${f}^{\prime }\left( x\right)  < 0$ ,则函数 $y = f\left( x\right)$ 在 ${x}_{0}$ 处取得极大值;

(2)若在点 ${x}_{0}$ 的左侧附近有 ${f}^{\prime }\left( x\right)  < 0$ ，而在 ${x}_{0}$ 的右侧附近有 ${f}^{\prime }\left( x\right)  > 0$ ,则函数 $y = f\left( x\right)$ 在 ${x}_{0}$ 处取得极小值.

例 6 已知 $f\left( x\right)  =  - {x}^{2} + {6x} - 1$ ,求函数 $y = f\left( x\right)$ 的单调区间和极值.

解 对函数求导,得 ${f}^{\prime }\left( x\right)  =  - {2x} + 6$ . 令 ${f}^{\prime }\left( x\right)  = 0$ ,解得 $x = 3$ ,从而 $x = 3$ 为函数 $y = f\left( x\right)$ 的唯一驻点. 把该驻点与其两侧的区间列表如下:

表 5-3

<table><tr><td>$x$</td><td>$\left( {-\infty ,3}\right)$</td><td>3</td><td>(3,十 $\infty$ )</td></tr><tr><td>${f}^{\prime }\left( x\right)$</td><td>+</td><td>0</td><td>-</td></tr><tr><td>$f\left( x\right)$</td><td>↗</td><td>极大值 8</td><td>↘</td></tr></table>

因此, $y = f\left( x\right)$ 在区间 $\left( {-\infty ,3}\right)$ 内严格增,在区间 $\left( {3, + \infty }\right)$ 内严格减，在 $x = 3$ 处取得极大值 $f\left( 3\right)  = 8$ .

例 7 求正弦函数 $y = \sin x$ 的单调区间和极值.

解 这是一个周期为 ${2\pi }$ 的周期函数. 记 $f\left( x\right)  = \sin x$ ,求导可得 ${f}^{\prime }\left( x\right)  = \cos x$ . 令 ${f}^{\prime }\left( x\right)  = 0$ ,解得 $x = {2k\pi } \pm  \frac{\pi }{2}, k \in  \mathbf{Z}$ . 将不同驻点及其所划分出的区间在一个周期上的情况列表如下:

表 5-4

<table><tr><td>$x$</td><td>${2k\pi } - \frac{\pi }{2}$</td><td>$\left( {{2k\pi } - \frac{\pi }{2},}\right.$ <br> ${2k\pi } + \frac{\pi }{2})$</td><td>${2k\pi } + \frac{\pi }{2}$</td><td>$\left( {{2k\pi } + \frac{\pi }{2},}\right.$ <br> $\left. {2\left( {k + 1}\right) \pi  - \frac{\pi }{2}}\right)$</td><td>$2\left( {k + 1}\right) \pi  - \frac{\pi }{2}$</td></tr><tr><td>${f}^{\prime }\left( x\right)$</td><td>0</td><td>+</td><td>0</td><td>-</td><td>0</td></tr><tr><td>$f\left( x\right)$</td><td>极小值 -1</td><td>↗</td><td>极大值 1</td><td>↘</td><td>极小值 -1</td></tr></table>

因此,对任意给定的 $k \in  \mathbf{Z}$ ,正弦函数 $y = \sin x$ 在区间 $\left( {{2k\pi } - \frac{\pi }{2},{2k\pi } + \frac{\pi }{2}}\right)$ 内严格增，在区间 $\left( {{2k\pi } + \frac{\pi }{2},2\left( {k + 1}\right) \pi  - \frac{\pi }{2}}\right)$ 内严格减，在 $x = {2k\pi } - \frac{\pi }{2}$ 时取得极小值 -1 ，在 $x = {2k\pi } + \frac{\pi }{2}$ 时取得极大值 1 .

例 8 已知 $f\left( x\right)  = \frac{1}{3}{x}^{3} - x + 2$ ,求函数 $y = f\left( x\right)$ 的单调区间和极值.

解 对函数求导,得 ${f}^{\prime }\left( x\right)  = {x}^{2} - 1$ . 令 ${f}^{\prime }\left( x\right)  = 0$ ,解得两个驻点 ${x}_{1} =  - 1,{x}_{2} = 1$ . 列表如下:

表 5-5

<table><tr><td>$x$</td><td>$\left( {-\infty , - 1}\right)$</td><td>-1</td><td>(-1,1)</td><td>1</td><td>(1,+∞)</td></tr><tr><td>${f}^{\prime }\left( x\right)$</td><td>+</td><td>0</td><td>-</td><td>0</td><td>+</td></tr><tr><td>$f\left( x\right)$</td><td>↗</td><td>极大值 $\frac{8}{3}$</td><td>↘</td><td>极小值 $\frac{4}{3}$</td><td>↗</td></tr></table>

---

把驻点与驻点所划分的区间列表, 可以简明清晰地呈现函数的增减情况和极值点.

---

因此,函数 $y = f\left( x\right)$ 的单调增区间为 $\left( {-\infty , - 1}\right)$ 及 $\left( {1, + \infty }\right)$ , 单调减区间为 $\left( {-1,1}\right) .y = f\left( x\right)$ 在 $x =  - 1$ 处取得极大值 $f\left( {-1}\right)  = \; \frac{8}{3}$ ,在 $x = 1$ 处取得极小值 $f\left( 1\right)  = \frac{4}{3}$ .

#### 练习 5.3(2)

1. 求余弦函数 $y = \cos x$ 的单调区间和极值.

2. 求函数 $y = {x}^{3} - {3x}$ 的单调区间和极值.

### 3 利用导数研究函数的最值

在许多理论和现实的问题中, 常常需要求函数的最大值或者最小值(统称为最值). 最值反映了函数在定义域上整体的情况， 而极值则仅考虑函数在某点附近的局部特征. 有时最值和极值是一致的,如函数 $y = \sin x$ ; 但有时却不一致,如图 5-3-2 所示的函数. 当然, 一个函数的极值与最值可能都不存在, 如函数 $y = {x}^{3}$ . 但是,如果考虑一个在闭区间上的连续函数,函数的最大值与最小值一定存在.

![bo_d4slovref24c73be0r3g_23_232_1114_256_419_0.jpg](images/bo_d4slovref24c73be0r3g_23_232_1114_256_419_0.jpg)

图 5-3-3

上面所说的一个区间 $I$ 上的连续函数,可以直观地理解为在区间 $I$ 上图像为一条连绵不断的曲线的函数. 更精确及普适的连续函数的定义, 要用到严格的极限语言, 在高等数学中才能给出.

例 9 已知 $f\left( x\right)  =  - {x}^{2} + {6x} - 1$ ,求函数 $y = f\left( x\right)$ 在区间 $\left\lbrack  {0,7}\right\rbrack$ 上的最大值与最小值.

解 由本节例 6 可知,函数 $y =  - {x}^{2} + {6x} - 1$ 的驻点为 $x = 3$ , 比较 $f\left( 3\right)  = 8, f\left( 0\right)  =  - 1, f\left( 7\right)  =  - 8$ ,可知该函数在 $\left\lbrack  {0,7}\right\rbrack$ 上的最大值是 8 , 最小值是 -8 , 如图 5-3-3 所示.

---

为什么只要比较这几个点的函数值(甚至不必分析驻点是不是极值点), 就可以求出最值?

---

在例 9 中, 我们对驻点处与区间两端点处的函数值进行比较, 其中最大的就是最大值, 最小的就是最小值. 在导数存在的前提下, 闭区间上的连续函数的最值原则上都可以按照这样的方法求出.

例 10 已知 $f\left( x\right)  = \frac{1}{3}{x}^{3} - x + 2$ ,求函数 $y = f\left( x\right)$ 在 $\left\lbrack  {0,3}\right\rbrack$ 上的最大值与最小值.

解 由本节例 8 可知,函数 $y = \frac{1}{3}{x}^{3} - x + 2$ 的两个驻点为 ${x}_{1} =  - 1,{x}_{2} = 1$ .

由于驻点 ${x}_{1} =  - 1$ 不在区间 $\left\lbrack  {0,3}\right\rbrack$ 内,因此只需比较 $f\left( 1\right)  = \frac{4}{3}, f\left( 0\right)  = 2, f\left( 3\right)  = 8$ ,可知函数 $y = \frac{1}{3}{x}^{3} - x + 2$ 在 $\left\lbrack  {0,3}\right\rbrack$ 上的最大值是 8,最小值是 $\frac{4}{3}$ .

### 4 利用导数研究二次函数

导数为研究函数的单调性、极值与最值提供了有力的工具. 利用这一工具,我们可以对熟悉的二次函数 $y = a{x}^{2} + {bx} + c \; \left( {a \neq  0}\right)$ 进行回顾和再认识. 以下仅讨论 $a > 0$ 的情况, $a < 0$ 的情况也可以用类似的方法获得相应的结果.

首先,可以利用导数的正负来判断函数 $y = a{x}^{2} + {bx} + c\left( {a > 0}\right)$ 的单调性, 同时求出它的极值.

记 $f\left( x\right)  = a{x}^{2} + {bx} + c$ . 对该函数求导,可得 ${f}^{\prime }\left( x\right)  = {2ax} + b$ , 令 ${f}^{\prime }\left( x\right)  = 0$ ,解得函数有唯一驻点 ${x}_{0} =  - \frac{b}{2a}$ . 可以列表如下:

表 5-6

<table><tr><td>$x$</td><td>$\left( {-\infty , - \frac{b}{2a}}\right)$</td><td>$- \frac{b}{2a}$</td><td>$\left( {-\frac{b}{2a}, + \infty }\right)$</td></tr><tr><td>${f}^{\prime }\left( x\right)$</td><td>-</td><td>0</td><td>+</td></tr><tr><td>$f\left( x\right)$</td><td>↘</td><td>极小值 $\frac{{4ac} - {b}^{2}}{4a}$</td><td>↗</td></tr></table>

因此,函数 $y = f\left( x\right)$ 的单调减区间为 $\left( {-\infty , - \frac{b}{2a}}\right)$ ,单调增区间为 $\left( {-\frac{b}{2a}, + \infty }\right) .y = f\left( x\right)$ 在 ${x}_{0} =  - \frac{b}{2a}$ 处取得极小值 $f\left( {-\frac{b}{2a}}\right)  = \frac{{4ac} - {b}^{2}}{4a}$ . 这个极小值也是该函数在区间 $\left( {-\infty , + \infty }\right)$ 上的最小值.

知道了该函数的单调区间之后, 结合函数的零点, 就可以解决相应的不等式问题.

我们已经知道,求二次函数 $y = a{x}^{2} + {bx} + c\left( {a > 0}\right)$ 的零点, 就是求一元二次方程 $a{x}^{2} + {bx} + c = 0\left( {a > 0}\right)$ 的实根.

---

此处所得结果与你之前的认识是否一致? 方法是不是更简便?

---

令 $\Delta  = {b}^{2} - {4ac}$ ,我们已知: 当 $\Delta  > 0$ 时,方程有两个不相等的实根 ${x}_{1} = \frac{-b - \sqrt{{b}^{2} - {4ac}}}{2a},{x}_{2} = \frac{-b + \sqrt{{b}^{2} - {4ac}}}{2a}$ ; 当 $\Delta  = 0$ 时,方程有两个相等的实根 ${x}_{1} = {x}_{2} =  - \frac{b}{2a}$ ; 当 $\Delta  < 0$ 时,方程无实根.

上述方程 $a{x}^{2} + {bx} + c = 0$ 的实根就是函数 $y = a{x}^{2} + {bx} + c$ 的零点; 再结合函数 $y = f\left( x\right)$ 的单调性,我们就可以求得使 $f\left( x\right)  \geq  0$ (或 $f\left( x\right)  \leq  0$ ) 的 $x$ 的取值范围,也就是不等式 $a{x}^{2} + {bx} + c \geq  0$ (或 $a{x}^{2} + {bx} + c \leq  0$ ) 的解集.

记 $f\left( x\right)  = a{x}^{2} + {bx} + c$ . 为了解不等式 $a{x}^{2} + {bx} + c \geq  0\left( {a > 0}\right)$ , 可以分以下三种情况讨论:

(1)当 $\Delta  > 0$ 时,比较函数零点与驻点的大小关系,有

$$
{x}_{1} = \frac{-b - \sqrt{{b}^{2} - {4ac}}}{2a} < {x}_{0} < {x}_{2} = \frac{-b + \sqrt{{b}^{2} - {4ac}}}{2a}.
$$

因为 $y = f\left( x\right)$ 在区间 $\left( {-\infty ,{x}_{0}}\right)$ 上严格减,所以

当 $x \in  \left( {-\infty ,{x}_{1}}\right)$ 时, $f\left( x\right)  > f\left( {x}_{1}\right)  = 0$ ; 当 $x \in  \left( {{x}_{1},{x}_{0}}\right)$ 时, $f\left( x\right)  < f\left( {x}_{1}\right)  = 0$ .

同样地,因为 $y = f\left( x\right)$ 在区间 $\left( {{x}_{0}, + \infty }\right)$ 上严格增,所以

当 $x \in  \left( {{x}_{0},{x}_{2}}\right)$ 时, $f\left( x\right)  < f\left( {x}_{2}\right)  = 0$ ; 当 $x \in  \left( {{x}_{2}, + \infty }\right)$ 时, $f\left( x\right)  > f\left( {x}_{2}\right)  = 0$ .

此外, $f\left( {x}_{1}\right)  = f\left( {x}_{2}\right)  = 0, f\left( {x}_{0}\right)  = \frac{{4ac} - {b}^{2}}{4a} < 0$ .

因此,该不等式的解集为 $\left( {-\infty ,{x}_{1}}\right\rbrack   \cup  \left\lbrack  {{x}_{2}, + \infty }\right)$ , 即 $\left( {-\infty ,\frac{-b - \sqrt{{b}^{2} - {4ac}}}{2a}}\right\rbrack   \cup  \left\lbrack  {\frac{-b + \sqrt{{b}^{2} - {4ac}}}{2a}, + \infty }\right)$ .

(2)当 $\Delta  = 0$ 时,有 ${x}_{1} = {x}_{2} = {x}_{0} =  - \frac{b}{2a}$ ,由函数单调性可知,当 $x \in  \left( {-\infty , + \infty }\right)$ 时,均有 $f\left( x\right)  \geq  f\left( {x}_{0}\right)  = f\left( {x}_{1}\right)  = \; f\left( {x}_{2}\right)  = 0$ . 因此,该不等式的解集为 $\mathbf{R}$ .

(3)当 $\Delta  < 0$ 时，由函数单调性可知，当 $x \in  \left( {-\infty , + \infty }\right)$ 时,均有 $f\left( x\right)  \geq  f\left( {x}_{0}\right)  = f\left( {-\frac{b}{2a}}\right)  = \frac{{4ac} - {b}^{2}}{4a} > 0$ . 因此,该不等式的解集为 $\mathbf{R}$ .

综合以上分析可得: 当 $\Delta  > 0$ 时,不等式 $a{x}^{2} + {bx} + c \geq  0 \; \left( {a > 0}\right)$ 的解集为 $\left( {-\infty ,\frac{-b - \sqrt{{b}^{2} - {4ac}}}{2a}}\right\rbrack   \cup  \left\lbrack  {\frac{-b + \sqrt{{b}^{2} - {4ac}}}{2a}, + \infty }\right)$ ; 当 $\Delta  \leq  0$ 时,该不等式的解集为 $\mathbf{R}$ . 这就很方便地得到必修课程第 2 章中的相应结论.

---

知道了函数的单调性和零点, 相应的不等式问题就迎刃而解了.

---

#### 练习 5.3(3)

1. 判断下列说法是否正确，并说明理由:

(1)函数在某区间上的极大值不会小于它的极小值；

(2)函数在某区间上的最大值不会小于它的最小值；

(3)函数在某区间上的极大值就是它在该区间上的最大值；

(4)函数在某区间上的最大值就是它在该区间上的极大值.

2. 求函数 $y = {x}^{2} - {6x} + 5, x \in  \left\lbrack  {1,4}\right\rbrack$ 的值域.

3. 求函数 $y = {x}^{3} - {3x}$ 在区间 $\left\lbrack  {-\frac{3}{2},0}\right\rbrack$ 上的最大值与最小值.

### 5 利用导数解决实际问题

前面已经看到, 导数可用来研究函数在某区间上的最大 (小)值, 从而对解决何时利润最大、何时用料最省等优化问题发挥着重要作用.

例 11 图 5-3-4 是一张边长为 3 的正方形硬纸板, 现把它的四个角上裁去边长为 $x$ 的四个小正方形,再折叠成无盖纸盒. 当裁去的小正方形边长 $x$ 发生变化时,纸盒的容积 $V$ 会随之发生变化. 当 $x$ 在什么范围内变化时,容积 $V$ 随着 $x$ 的增大而增大? $x$ 在什么范围内变化时,容积 $V$ 随着 $x$ 的增大而减小? 当 $x$ 取何值时,容积 $V$ 最大? 最大值是多少? (纸板厚度忽略不计)

![bo_d4slovref24c73be0r3g_26_303_1540_657_276_0.jpg](images/bo_d4slovref24c73be0r3g_26_303_1540_657_276_0.jpg)

图 5-3-4

解 由题意, 得

$$
V\left( x\right)  = x{\left( 3 - 2x\right) }^{2}, x \in  \left( {0,\frac{3}{2}}\right) .
$$

求导可得

$$
{V}^{\prime }\left( x\right)  = {12}{x}^{2} - {24x} + 9.
$$

为求驻点,令 ${12}{x}^{2} - {24x} + 9 = 0$ ,得 ${x}_{1} = \frac{1}{2}$ 与 ${x}_{2} = \frac{3}{2}$ ,后者不在定义域内，舍去.

容易算出，当 $x \in  \left( {0,\frac{1}{2}}\right)$ 时， ${V}^{\prime }\left( x\right)  > 0$ ；当 $x \in  \left( {\frac{1}{2},\frac{3}{2}}\right)$ 时， ${V}^{\prime }\left( x\right)  < 0$ . 因此,当 $x$ 在 0 到 $\frac{1}{2}$ 之间变化时,容积 $V$ 随着 $x$ 的增大而增大; 当 $x$ 在 $\frac{1}{2}$ 到 $\frac{3}{2}$ 之间变化时,容积 $V$ 随着 $x$ 的增大而减小; 而当 $x = \frac{1}{2}$ 时,容积 $V\left( \frac{1}{2}\right)  = 2$ 是极大值,也是最大值.

例 12 已知某商品的成本 $C$ 与产量 $q$ 满足函数关系 $C = \; C\left( q\right)$ ,其中 $C\left( q\right)  = {100} + \frac{1}{4}{q}^{2}$ ,并定义平均成本为 $\bar{C} = \bar{C}\left( q\right)$ , 其中 $\bar{C}\left( q\right)  = \frac{C\left( q\right) }{q}$ .

---

经济学中通常将 ${C}^{\prime }\left( q\right)$ 称为边际成本, 它代表产量为 $q$ 时, 增加单位产量需付出的成本增加量.

---

(1)比较 ${C}^{\prime }\left( {10}\right)$ 和 ${C}^{\prime }\left( {20}\right)$ ,解释两者的大小代表了怎样的实际意义；

(2)当产量为多少时，平均成本最少？

解(1)因为 ${C}^{\prime }\left( q\right)  = \frac{1}{2}q$ ,所以 ${C}^{\prime }\left( {10}\right)  = 5,{C}^{\prime }\left( {20}\right)  = {10}$ , 有 ${C}^{\prime }\left( {10}\right)  < {C}^{\prime }\left( {20}\right)$ .

${C}^{\prime }\left( {10}\right)  = 5$ 代表当产量为 $q = {10}$ 时,增加单位产量需付出的成本增加量为 5 ; 而 ${C}^{\prime }\left( {20}\right)  = {10}$ 代表当产量为 $q = {20}$ 时,增加单位产量需付出的成本增加量为 10 .

(2)平均成本 $\bar{C}\left( q\right)  = \frac{C\left( q\right) }{q} = \frac{100}{q} + \frac{q}{4},{\bar{C}}^{\prime }\left( q\right)  =  - \frac{100}{{q}^{2}} + \frac{1}{4}$ .

令 ${\bar{C}}^{\prime }\left( q\right)  = 0$ ,得 ${q}^{2} = {400}$ ,根据实际意义,可知 $q > 0$ ,因此, $q = {20}$ 是其驻点.

当 $0 < q < {20}$ 时, ${\bar{C}}^{\prime }\left( q\right)  < 0$ ,函数 $\bar{C} = \bar{C}\left( q\right)$ 严格减; 而当 $q >$ 20 时, ${\bar{C}}^{\prime }\left( q\right)  > 0$ ,函数 $\bar{C} = \bar{C}\left( q\right)$ 严格增. 因此,当产量 $q = {20}$ 时, 平均成本最少.

解 根据题意,可知 ${h}^{2} = {d}^{2} - {b}^{2}$ ,所以 $W\left( b\right)  = \frac{1}{6}b\left( {{d}^{2} - {b}^{2}}\right)$ , $0 < b < d$ .

![bo_d4slovref24c73be0r3g_27_235_1821_252_253_0.jpg](images/bo_d4slovref24c73be0r3g_27_235_1821_252_253_0.jpg)

图 5-3-5

例 13 如图 5-3-5,将一根直径为 $d$ 的圆木锯成截面为矩形的梁. 问: 矩形的高 $h$ 和宽 $b$ 应如何选择,才能使梁的抗弯强度 $W = \frac{1}{6}b{h}^{2}$ 最大?

求导,得 ${W}^{\prime }\left( b\right)  = \frac{1}{6}{d}^{2} - \frac{1}{2}{b}^{2}$ . 令 ${W}^{\prime }\left( b\right)  = 0$ ,得到驻点 $b = \frac{\sqrt{3}}{3}d$ .

由问题的实际意义,当 $b = \frac{\sqrt{3}}{3}d$ 时,梁的抗弯强度最大,此时, ${h}^{2} = {d}^{2} - {b}^{2} = \frac{2}{3}{d}^{2}$ ,即 $h = \frac{\sqrt{6}}{3}d$ .

在很多情形下(如例 11 与例 13)，由实际问题本身的意义， 可知函数在区间内部必定存在最大值(或最小值)，而区间内部只有一个驻点, 由此即可断定: 该函数在区间内部的唯一驻点处取得最大值(或最小值).

例 14 一艘船航行所需的燃料费与船速的平方成正比. 如果船速是 ${10}\mathrm{\;{km}}/\mathrm{h}$ ,那么每小时的燃料费是 80 元. 已知该船航行的其他费用为每小时 480 元,在 ${100}\mathrm{\;{km}}$ 的航程中,保持怎样的船速可使航行总费用最少? (结果精确到 $1\mathrm{\;{km}}/\mathrm{h}$ )

解 设当船速为 $x\left( {\mathrm{\;{km}}/\mathrm{h}}\right)$ 时,每小时所需燃料费为 $k{x}^{2}$ 元.

根据题意,当 $x = {10}$ 时, $k{x}^{2} = {100k} = {80}$ ,从而解得 $k = \frac{4}{5}$ . 因此,船在 ${100}\mathrm{\;{km}}$ 航程中的总费用为

$$
y = f\left( x\right)  = \frac{100}{x}\left( {\frac{4}{5}{x}^{2} + {480}}\right)  = {80x} + \frac{48000}{x}, x > 0.
$$

求导,得 ${f}^{\prime }\left( x\right)  = {80} - \frac{48000}{{x}^{2}}$ ,令 ${f}^{\prime }\left( x\right)  = 0$ ,得 $x = {10}\sqrt{6}$ 是唯一驻点. 当 $0 < x < {10}\sqrt{6}$ 时, ${f}^{\prime }\left( x\right)  < 0$ ,函数 $y = f\left( x\right)$ 严格减; 而当 $x > {10}\sqrt{6}$ 时, ${f}^{\prime }\left( x\right)  > 0$ ,函数 $y = f\left( x\right)$ 严格增. 因此,函数 $y = f\left( x\right)$ 在 $x = {10}\sqrt{6} \approx  {24}\left( {\mathrm{\;{km}}/\mathrm{h}}\right)$ 处取得最小值.

所以,在 ${100}\mathrm{\;{km}}$ 的航程中,保持约 ${24}\mathrm{\;{km}}/\mathrm{h}$ 的船速可使航行总费用最少.

#### 练习 5.3(4)

1. 某商品的成本 $C$ 和产量 $q$ 满足函数关系 $C = {50000} + {200q}$ ,该商品的销售单价 $p$ 和产量 $q$ 满足函数关系 $p = {24200} - \frac{1}{5}{q}^{2}$ . 问: 要使利润最大, 应如何确定产量?

![bo_d4slovref24c73be0r3g_28_1236_1793_220_248_0.jpg](images/bo_d4slovref24c73be0r3g_28_1236_1793_220_248_0.jpg)

(第 2 题)

2. 采矿、采石或取土时，常用炸药包进行爆破，部分爆破呈圆锥漏斗形状 (如图), 已知圆锥的母线长是炸药包的爆破半径 $R$ , 它的值是固定的. 问:炸药包埋多深可使爆破体积最大？

#### 习题 5.3

##### A 组

1. 利用导数研究下列函数的单调性, 并说明结果与你之前的认识是否一致:

(1) $y = {\left( \frac{1}{\mathrm{e}}\right) }^{x}$ ; (2) $y = {\log }_{\frac{1}{\mathrm{e}}}x$ .

2. 利用导数判断函数 $y = \frac{1}{\cos x}, x \in  \left( {-\frac{\pi }{2},\frac{\pi }{2}}\right)$ 的单调性,并求出极值.

3. 某函数图像如图所示,它在 $\left\lbrack  {a, b}\right\rbrack$ 上哪一点取得最大值? 它是极大值点吗? 在哪一点取得最小值? 它是极小值点吗?

![bo_d4slovref24c73be0r3g_29_556_893_564_228_0.jpg](images/bo_d4slovref24c73be0r3g_29_556_893_564_228_0.jpg)

(第 3 题)

4. 求下列函数的单调区间、极值点和极值:

(1) $y = {x}^{2} + {2x} + {3;}$ (2) $y = x + \frac{1}{x}$ ；

(3) $y = {3x} - {x}^{3}$ ； (4) $y = {x}^{2}{\mathrm{e}}^{x}$ .

5. 证明: 函数 $y = {x}^{3} + {4x}$ 在 $\left( {-\infty , + \infty }\right)$ 上严格增.

6. 求函数 $y =  - {x}^{3} + {12x} - 1$ 的单调减区间.

7. 证明: 函数 $y = x - \frac{1}{x}$ 没有极值点.

8. 求函数 $y =  - {x}^{3} + {12x} - 1, x \in  \left\lbrack  {0,3}\right\rbrack$ 的值域.

##### B 组

1. 判断下列函数在 $\left( {-\infty , + \infty }\right)$ 上是否存在驻点,是否存在极值点,并说明理由:

(1) $y = {x}^{n}$ ， $n$ 为正奇数； (2) $y = {x}^{n}$ ， $n$ 为正偶数.

2. 已知函数 $y = {x}^{3} + {2m}{x}^{2} - {nx} + m$ 在 $x = 1$ 处有极值 0,求 $m + n$ 的值.

3. 用长为 ${18}\mathrm{\;m}$ 的钢条制作一个如图所示的长方体框架. 已知长方体的长宽比为 $2 : 1$ ，间:该长方体的长、宽、高各为多少时，其体积最大? 最大体积是多少?

![bo_d4slovref24c73be0r3g_29_1238_1869_246_157_0.jpg](images/bo_d4slovref24c73be0r3g_29_1238_1869_246_157_0.jpg)

(第 3 题)

4. 某分公司经销一品牌产品, 每件产品的成本为 4 元, 且每件产品需向总公司交 3 元的管理费,预计当每件产品的售价为 $x$ 元 $\left( {8 \leq  x \leq  {11}}\right)$ 时,一年的销售量为 ${\left( {12} - x\right) }^{2}$ 万件. 问: 当每件产品的售价为多少元时,该分公司一年的利润 $L$ 最大?(结果精确到 1 元)

#### 课后阅读

##### 微积分简史

17 世纪，两位科学巨匠伽利略(G. Galilei)和开普勒(J. Kepler)的一系列发现导致了数学从古典数学向现代数学的转折. 自然科学, 特别是天文学和力学等学科的发展都需要一种新的数学工具来研究运动和变化的过程, 这促成了微积分的发明和发展.

朴素的积分学思想其实可以追溯到古希腊时代，在中国古代的数学中也有其踪迹，但直到 17 世纪，微积分才出现重大突破. 微积分主要来源于对四类问题的研究: 面积、体积、弧长问题; 位移、速度、加速度关系问题; 切线问题; 最值问题. 许多数学家对此作出了贡献, 这其中有卡瓦列利(F. Cavalieri)、费马(P. de Fermat)、沃利斯(J. Wallis)、笛卡儿(R. Descartes)和巴罗(I. Barrow)等. 在经过了半个世纪的酝酿后，牛顿(I. Newton) 和莱布尼茨(G. Leibniz)分别独立地完成了微积分创立过程中最后也是最关键的一步. 牛顿和莱布尼茨的杰出贡献，不在于发现求切线和求面积的方法，而是给出了一般的无穷小算法, 同时又找出了微分学和积分学的互逆关系, 现称为微积分基本定理, 这一深刻的思想已成为人类文明中的瑰宝.

牛顿对微积分问题的研究始于 1664 年秋, 当时他正在剑桥大学读书. 他因对笛卡儿圆法产生兴趣而开始寻找更好的求切线方法. 1665 年 11 月，牛顿发明了“正流数术”(微分法)，次年 5 月又建立了“反流数术”(积分法). 1666 年 10 月，牛顿将前两年的研究成果整理成一篇总结性论文, 现以《流数简论》著称. 这是历史上第一篇系统的微积分文献. 在这篇论文中，牛顿通过揭示微分和积分的互逆关系而将两者统一为一个整体. 尽管如此，这一论文在许多方面还是不成熟的. 在其后的大约四分之一世纪的时间里, 牛顿不断地完善自己的微积分学说, 先后著成了三篇微积分论文: 《分析学》(1669)、《流数法》(1671) 和 《求积术》(1691). 它们真实地再现了牛顿创建微积分的思想历程.

与牛顿发明微积分的运动学背景不同, 莱布尼茨创立微积分首先是出于对几何学问题的思考. 1673 年, 他因在帕斯卡 (B. Pascal) 的有关论文中获得启迪, 而提出自己的“微分三角形”理论. 在对微分三角形的研究中, 莱布尼茨逐渐认识到什么是求曲线的切线和求曲线下的面积的实质, 并发现了这两类问题的互逆关系. 由此他建立起一种更一般的算法, 并将以往解决这两类问题的各种结果和技巧加以统一.

刚刚诞生的微积分以其神奇的效果赢得了普遍的关注, 但在理论上却是粗糙和不完美的, 后世的许多数学家为其理论的建立和完善作出了不懈的努力, 特别是欧拉(L. Euler)、 达朗贝尔(J. d'Alembert)、波尔查诺(B. Bolzano)、柯西(A. L. Cauchy)和维尔斯特拉斯 (K. Weierstrass)等人作出了重要的贡献. 直到 19 世纪后半叶, 现代意义的严密的微积分与数学分析理论才真正成形. 特别值得一提的是, 1859 年, 我国历史上首部微积分中文教科书《代微积拾级》在上海出版，标志着高等数学的传入. 此书的原作者为美国数学家罗密士(E. Loomis)，译者为中国数学家李善兰和英国人伟烈亚力(A. Wylie).

微积分的创立具有划时代的意义，它开辟了数学的新时代，使数学获得了极大的发展, 取得了空前的繁荣, 诸如微分方程、复变函数、微分几何等数学分支都应运而生. 微积分给出了一整套的科学方法, 开创了科学的新纪元, 并因此加强和加深了数学的巨大作用与应用. 有了微积分，人类才有能力把握运动和变化，进而推动了工业革命，促进了大工业生产, 最终有了现代化的社会. 微积分不仅极大地促进了天文学、力学、物理学等基础学科的发展，还在现代化学、生物学、工程学、地理学、经济学等自然科学、社会科学及应用科学各个分支获得了极其广泛的应用. 几乎所有现代技术领域, 如机械、仪器仪表、建筑、航海、航空航天、信息与通讯等，其技术的发展和产品的设计也都以微积分为基本数学工具.

纵观微积分的历史之旅，有着说不完的数学故事. 请同学们课后查阅有关书籍和资料, 认真地进行回顾和小结.

## 内容提要

### 1. 导数的概念及意义

(1)导数的概念:函数 $y = f\left( x\right)$ 在 $x = {x}_{0}$ 处的导数 ${f}^{\prime }\left( {x}_{0}\right)$ ，是函数在 $x = {x}_{0}$ 附近的平均变化率 $\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ 当 $h$ 趋近于 0 时所趋近的稳定值，记作

$$
{f}^{\prime }\left( {x}_{0}\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}.
$$

把自变量值 ${x}_{0}$ 对应到 ${f}^{\prime }\left( {x}_{0}\right)$ 所给出的函数记作 $y = {f}^{\prime }\left( x\right)$ ,称为 $y = f\left( x\right)$ 的导函数,简称导数.

(2)导数的物理意义:在满足函数关系 $d = f\left( t\right)$ 的运动中，该函数在 $t = {t}_{0}$ 处的导数 ${f}^{\prime }\left( {t}_{0}\right)$ 就是 ${t}_{0}$ 时刻的瞬时速度.

(3)导数的几何意义:对于曲线 $y = f\left( x\right)$ ，函数 $y = f\left( x\right)$ 在 $x = {x}_{0}$ 处的导数 ${f}^{\prime }\left( {x}_{0}\right)$ 就是曲线在点 $\left( {{x}_{0}, f\left( {x}_{0}\right) }\right)$ 处的切线斜率.

### 2. 常用的求导公式与法则

(1) ${\left( C\right) }^{\prime } = 0$ ， $C$ 为常数；

(2) ${\left( {x}^{\alpha }\right) }^{\prime } = \alpha {x}^{\alpha  - 1}$ ， $\alpha$ 为常数；

(3) ${\left( {\mathrm{e}}^{x}\right) }^{\prime } = {\mathrm{e}}^{x}$ ；

(4) ${\left( \ln x\right) }^{\prime } = \frac{1}{x}$ ；

(5) ${\left( \sin x\right) }^{\prime } = \cos x$ ；

(6) ${\left( \cos x\right) }^{\prime } =  - \sin x$ ；

(7) ${\left( f\left( x\right)  \pm  g\left( x\right) \right) }^{\prime } = {f}^{\prime }\left( x\right)  \pm  {g}^{\prime }\left( x\right)$ ；

(8) ${\left( f\left( x\right) g\left( x\right) \right) }^{\prime } = {f}^{\prime }\left( x\right) g\left( x\right)  + f\left( x\right) {g}^{\prime }\left( x\right)$ ;

(9) ${\left( \frac{f\left( x\right) }{g\left( x\right) }\right) }^{\prime } = \frac{{f}^{\prime }\left( x\right) g\left( x\right)  - f\left( x\right) {g}^{\prime }\left( x\right) }{{\left( g\left( x\right) \right) }^{2}}$ ,其中 $g\left( x\right)  \neq  0$ ;

(10) ${\left( Cf\left( x\right) \right) }^{\prime } = C{f}^{\prime }\left( x\right)$ ， $C$ 为常数；

(11) ${\left( f\left( ax + b\right) \right) }^{\prime } = a{f}^{\prime }\left( u\right)$ ，其中 $u = {ax} + b$ .

### 3. 用导数研究函数

(1)函数的单调性:在区间 $I$ 上，若 ${f}^{\prime }\left( x\right)  > 0$ ，则函数 $y = f\left( x\right)$ 严格增；若 ${f}^{\prime }\left( x\right)  < 0$ ， 则函数 $y = f\left( x\right)$ 严格减.

(2)函数的极值:若 ${x}_{0}$ 是函数 $y = f\left( x\right)$ 的极值点，则 ${f}^{\prime }\left( {x}_{0}\right)  = 0$ ，即 ${x}_{0}$ 是函数 $y = f\left( x\right)$ 的驻点. 反之,在 ${x}_{0}$ 是函数 $y = f\left( x\right)$ 的驻点的前提下,若在 ${x}_{0}$ 的左侧附近有 ${f}^{\prime }\left( x\right)  > 0$ ,在 ${x}_{0}$ 的右侧附近有 ${f}^{\prime }\left( x\right)  < 0$ ,则 $y = f\left( x\right)$ 在 ${x}_{0}$ 处取得极大值; 若在 ${x}_{0}$ 的左侧附近有 ${f}^{\prime }\left( x\right)  < 0$ ,在 ${x}_{0}$ 的右侧附近有 ${f}^{\prime }\left( x\right)  > 0$ ,则 $y = f\left( x\right)$ 在 ${x}_{0}$ 处取得极小值.

(3)连续函数在闭区间上必存在最值(最大值与最小值).

## 复习题

### A 组

1. 请根据图中的函数图像，将下列数值按从小到大的顺序排列:___.

![bo_d4slovref24c73be0r3g_33_1151_617_330_206_0.jpg](images/bo_d4slovref24c73be0r3g_33_1151_617_330_206_0.jpg)

(第 1 题)

① 曲线在点 $A$ 处切线的斜率；

② 曲线在点 $B$ 处切线的斜率；

③ 曲线在点 $C$ 处切线的斜率;

④ 割线 ${AB}$ 的斜率;

⑤ 数值 0 ;

⑥ 数值 1 .

2. 已知 $f\left( x\right)  = \sqrt{x}, g\left( x\right)  = k{x}^{2}$ .

(1)求曲线 $y = f\left( x\right)$ 在点 $\left( {4,2}\right)$ 处的切线方程；

(2)若曲线 $y = g\left( x\right)$ 经过点 $\left( {4,2}\right)$ ，求它与(1)中切线的另一个交点.

3. 从桥上将一小球掷向空中，小球相对于地面的高度 $h$ (单位: $\mathrm{m}$ )和时间 $t$ (单位: $\mathrm{s}$ ) 近似满足函数关系 $h =  - 5{t}^{2} + {15t} + {12}$ . 问:

(1)小球的初始高度是多少？

(2)小球在 $t = 0$ 到 $t = 1$ 这段时间内的平均速度是多少？

(3)小球在 $t = 1$ 时的瞬时速度是多少？

(4)小球所能达到的最大高度是多少？何时达到？

4. 已知 $f\left( x\right)  = {\mathrm{e}}^{x}, g\left( x\right)  = \ln x$ ,计算下列函数 $y = h\left( x\right)$ 在点 $x = 1$ 处的导数值:

(1) $h\left( x\right)  = {3f}\left( x\right)  - {5g}\left( x\right)$ ; (2) $h\left( x\right)  = f\left( x\right) g\left( x\right)$ ；

(3) $h\left( x\right)  = \frac{f\left( x\right) }{g\left( x\right) }$ ； (4) $h\left( x\right)  = f\left( {{2x} + 1}\right)  + g\left( {{3x} - 1}\right)$ .

5. 计算下列函数 $y = f\left( x\right)$ 的导数,其中:

(1) $f\left( x\right)  = \frac{\pi }{2} + \sin \left( {-x}\right)$ ； (2) $f\left( x\right)  = \sqrt[3]{x} - \frac{1}{{x}^{3}}$ ；___

(3) $f\left( x\right)  = \left( {\frac{1}{2}x - 5}\right) \left( {3 - {4x}}\right)$ ； (4) $f\left( x\right)  = \frac{\cos x}{{x}^{2}}$ .

6. 求下列函数 $y = f\left( x\right)$ 的单调区间和极值点,其中:

(1) $f\left( x\right)  = \frac{2}{3}x - 1$ (2) $f\left( x\right)  = 2 + x - {x}^{2}$ ；

(3) $f\left( x\right)  = {x}^{3} + {x}^{2} - {8x} + 7$ .

7. 借助第 6 题的结果,求下列函数 $y = f\left( x\right)$ 在给定区间上的最大值和最小值,其中:

(1) $f\left( x\right)  = \frac{2}{3}x - 1, x \in  \left\lbrack  {0,3}\right\rbrack$ ；

(2) $f\left( x\right)  = 2 + x - {x}^{2}, x \in  \left\lbrack  {-1,1}\right\rbrack$ ；

(3) $f\left( x\right)  = {x}^{3} + {x}^{2} - {8x} + 7, x \in  \left\lbrack  {-3,3}\right\rbrack$ .

### B 组

![bo_d4slovref24c73be0r3g_34_1135_460_318_188_0.jpg](images/bo_d4slovref24c73be0r3g_34_1135_460_318_188_0.jpg)

(第 1 题)

1. 已知 $y = {f}^{\prime }\left( x\right)$ 的图像如图所示,求函数 $y = f\left( x\right)$ 在 $\left( {-2,2}\right)$ 上的单调区间和极值点.

2. 若直线 $y = x$ 是曲线 $y = {x}^{3} - 3{x}^{2} + {ax}$ 的切线,求 $a$ 的值.

3. 设函数 $y = {x}^{3} + a{x}^{2} + {bx} + c$ 的图像与 $y = 0$ 在原点相切, 若函数的极小值为 -4 ，求函数的表达式与单调减区间.

4. 某种型号的汽车在匀速行驶中每小时的耗油量 $y$ (单位: $\mathrm{L}$ ) 关于行驶速度 $x$ (单位: $\mathrm{{km}}/\mathrm{h}$ ) 满足函数关系 $y = \frac{1}{128000}{x}^{3} - \frac{3}{80}x + 8\left( {0 < x \leq  {120}}\right)$ . 已知甲、乙两地相距 100 km. 问:当汽车保持怎样的速度匀速行驶时，从甲地到乙地的耗油量最小?

5. 要建造一个给定容积 $V$ 的圆柱体蓄水池,已知池底单位造价为池侧面单位造价的 2 倍. 问: 应如何选择蓄水池的底面半径 $r$ 和高 $h$ ,才能使总造价最低?

6. 已知某厂生产一种产品的总成本 $C$ (单位:万元) 与产品件数 $x$ 满足函数关系 $C = {1200} + \frac{2}{75}{x}^{3}$ ,产品单价 $P$ (单位: 万元)和产品件数 $x$ 满足函数关系 ${P}^{2} = \frac{250000}{x}$ . 问: 产量为多少件时, 总利润最大?

## 拓展与思考

1. 讨论函数 $y = {x}^{3} + {ax} + b$ 的单调性. (可借助信息技术工具)

2. 判断方程 ${x}^{3} + {ax} + b = 0$ 有几个实根. (可借助信息技术工具)
