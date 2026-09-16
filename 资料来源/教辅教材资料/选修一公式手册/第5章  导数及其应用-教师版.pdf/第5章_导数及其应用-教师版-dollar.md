## 第5章 导数及其应用

### 5.1 导数的概念及意义

#### 5.1.1 导数的概念

1. 一般地，对于函数 $y = f\left( x\right)$ ，将 $\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ 称为函数 $y = f\left( x\right)$ 在以 ${x}_{0}$ 和 ${x}_{0} + h$ 为端点的区间上的平均变化率

2. 如果平均变化率有极限,把这个极限值记作 $\mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ ,并称之为函数 $y = f\left( x\right)$ 在 $x = {x}_{0}$ 处的 导数 ，记作 ${f}^{\prime }\left( {x}_{0}\right)$ .

3. ${f}^{\prime }\left( {x}_{0}\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{x}_{0} + h}\right)  - f\left( {x}_{0}\right) }{h}$ 就是函数 $y = f\left( x\right)$ 在 $x = {x}_{0}$ 处的 瞬时 变化率.

#### 5.1.2 导数的几何意义

1. 我们把连接曲线上任意两点的直线称为该曲线的一条 割线 . 给定曲线上的一点 $P$ ,考虑以 $P$ 为端点的一条小曲线段 $\overset{\text{ ⏜ }}{AB}$ 和割线 ${PQ}$ . 当曲线段 $\overset{\text{ ⏜ }}{AB}$ 取得越来越短,即点 $Q$ 越来越靠近点 $P$ 时,如果割线 ${PQ}$ 趋近于一条确定的直线，那么我们就将这条直线称为曲线在点 $P$ 处的 切线.

2. 函数 $y = f\left( x\right)$ 在 $x = {x}_{0}$ 处的导数 ${f}^{\prime }\left( {x}_{0}\right)$ 就是曲线 $y = f\left( x\right)$ 在点 $P\left( {{x}_{0}, f\left( {x}_{0}\right) }\right)$ 处切线的斜率. 从而,函数 $y = f\left( x\right)$ 在点 $P\left( {{x}_{0}, f\left( {x}_{0}\right) }\right)$ 处的切线方程为 $y - f\left( {x}_{0}\right)  = {f}^{\prime }\left( {x}_{0}\right) \left( {x - {x}_{0}}\right)$ .

3. 通常将导数为零的点称为函数的 驻点 ，曲线在其驻点处的切线是一条 水平 直线.

### 5.2 导数的运算

如果用 $x$ 表示自变量，那么 ${y}^{\prime } = {f}^{\prime }\left( x\right)$ 也是一个关于 $x$ 的函数，称为函数 $y = f\left( x\right)$ 的 导函数 (也简称为导数 ),其中 ${f}^{\prime }\left( x\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {x + h}\right)  - f\left( x\right) }{h}$ .

5.2.1 基本初等函数的导数

1. ${\left( C\right) }^{\prime } = 0\;, C$ 为常数;

2. ${\left( {x}^{a}\right) }^{\prime } = a{x}^{a - 1}\;, a$ 为常数;

3. ${\left( {e}^{x}\right) }^{\prime } = {e}^{x}$ ;

4. ${}^{ * }{\left( {a}^{x}\right) }^{\prime } = {a}^{x}\ln a\;\left( {a > 0, a \neq  1}\right)$ ;

5. ${\left( \ln x\right) }^{\prime } = \frac{1}{x}$ ;

6. $* {\left( {\log }_{a}x\right) }^{\prime } = \frac{1}{x\ln a}\;\left( {a > 0, a \neq  1}\right)$ ;

7. ${\left( \sin x\right) }^{\prime } = \cos x$

8. ${\left( \cos x\right) }^{\prime } =  - \sin x$ .

#### 5.2.2 导数的四则运算

对于函数 $y = f\left( x\right)$ 与 $y = g\left( x\right)$ ,以下等式成立:

1. ${\left( f\left( x\right)  \pm  g\left( x\right) \right) }^{\prime } = {f}^{\prime }\left( x\right)  \pm  {g}^{\prime }\left( x\right)$ ;

2. ${\left( f\left( x\right) g\left( x\right) \right) }^{\prime } = {f}^{\prime }\left( x\right) g\left( x\right)  + f\left( x\right) {g}^{\prime }\left( x\right)$ ;

3. ${\left( \frac{f\left( x\right) }{g\left( x\right) }\right) }^{\prime } = \frac{{f}^{\prime }\left( x\right) g\left( x\right)  - f\left( x\right) {g}^{\prime }\left( x\right) }{{\left( g\left( x\right) \right) }^{2}}$ ,其中 $g\left( x\right)  \neq  0$ .

#### 5.2.3 简单符合函数的单数

1. $f\left( {{ax} + b}\right)$ 型复合函数的求导法则: ${\left( f\left( ax + b\right) \right) }^{\prime } = a{f}^{\prime }\left( u\right)$ ,其中 $u = {ax} + b$ .

2. $f\left( {g\left( x\right) }\right)$ 型复合函数的求导法则: ${\left( f\left( g\left( x\right) \right) \right) }^{\prime } = {g}^{\prime }\left( x\right) {f}^{\prime }\left( u\right)$ ,其中 $u = g\left( x\right)$ .

### 5.3 导数的应用

#### 5.3.1 利用导数研究函数的单调性

1. 定理: 在区间 $I$ 上,若 ${f}^{\prime }\left( x\right)  > 0$ ,则函数 $y = f\left( x\right)$ 在该区间 严格增 ;

若 ${f}^{\prime }\left( x\right)  < 0$ ，则函数 $y = f\left( x\right)$ 在该区间 严格减 .

2. 注: ${f}^{\prime }\left( x\right)  > 0$ 恒成立是函数 $y = f\left( x\right)$ 在区间严格增的 充分非必要 条件;

${f}^{\prime }\left( x\right)  \geq  0$ 恒成立是函数 $y = f\left( x\right)$ 在区间严格增的 必要非充分 条件.

#### 5.3.2 利用导数研究函数的极值

1. 定义: 在 $x = {x}_{1}$ 附近存在一个小区间,该区间内其他自变量所对应的函数值都 不大于 $f\left( {x}_{1}\right)$ ,此时,就说函数 $y = f\left( x\right)$ 在 $x = {x}_{1}$ 处取得极大值 $f\left( {x}_{1}\right)$ ,而点 ${x}_{1}$ 称为函数 $y = f\left( x\right)$ 的 极大值点 . 类似地,在 $x = {x}_{2}$ 附近存在一个小区间,该区间内其他自变量所对应的函数值都 不小于 $f\left( {x}_{2}\right)$ ,此时, 就说函数 $y = f\left( x\right)$ 在 $x = {x}_{2}$ 处取得极小值 $f\left( {x}_{2}\right)$ ，而点 ${x}_{2}$ 称为函数 $y = f\left( x\right)$ 的 极小值点 .

2. 极大值和极小值统称为 极值 ，而极大值点和极小值点则统称为 极值点

3. 定理: 设点 $x = {x}_{0}$ 是函数 $y = f\left( x\right)$ 的驻点.

(1)若在点 ${x}_{0}$ 的左侧附近有 ${f}^{\prime }\left( x\right)  > 0$ ，而在 ${x}_{0}$ 的右侧附近有 ${f}^{\prime }\left( x\right)  < 0$ ，则函数 $y = f\left( x\right)$ 在 ${x}_{0}$ 处取得 极大值；

(2)若在点 ${x}_{0}$ 的左侧附近有 ${f}^{\prime }\left( x\right)  < 0$ ，而在 ${x}_{0}$ 的右侧附近有 ${f}^{\prime }\left( x\right)  > 0$ ，则函数 $y = f\left( x\right)$ 在 ${x}_{0}$ 处取得 极小值.

#### 5.3.3 利用导数研究函数的最值

考虑一个在闭区间上的 连续 函数，函数的最大值与最小值一定存在. 利用导数研究函数的驻点、单调性与极值后, 对 驻点 处与 区间端点 处的函数值进行比较, 其中最大的就是最大值, 最小的就是最小值.

## *5.4 导数章节拓展知识

5.4.1 常见函数的单调性、极值、最值与同构关系

<table><tr><td>函数</td><td>图像</td><td>单调性、极值、最值</td></tr></table>

<table id="cross-table-1"><tr><td>$f\left( x\right)  = x{e}^{x}$</td><td>[失效外部图片：bo_d7nktbc91nqc7384ijv0_3.jpg]</td><td>单调减区间: $\left( {-\infty , - 1}\right)$ ； <br>  单调增区间: $\left( {-1, + \infty }\right)$ ； <br>  极小值与最小值: $\;f\left( {-1}\right)  =  - \frac{1}{e}$ .</td></tr><tr><td>$f\left( x\right)  = \frac{x}{{e}^{x}}$</td><td>[失效外部图片：bo_d7nktbc91nqc7384ijv0_3.jpg]</td><td>单调增区间: $\;\left( {-\infty ,1}\right)$ ; <br>  单调减区间: $\;\left( {1, + \infty }\right)$ ; <br>  极大值与最大值: $\;f\left( 1\right)  = \frac{1}{e}$ .</td></tr><tr><td>$f\left( x\right)  = \frac{{e}^{x}}{x}$</td><td>[失效外部图片：bo_d7nktbc91nqc7384ijv0_3.jpg]</td><td>单调减区间: $\;\left( {-\infty ,0}\right)$ ; <br>  单调增区间: $\left( {0, + \infty }\right)$ ； <br>  极小值: $\;f\left( 1\right)  = e$ .</td></tr><tr><td>$f\left( x\right)  = x\ln x$</td><td>[失效外部图片：bo_d7nktbc91nqc7384ijv0_3.jpg]</td><td>单调减区间: $\;\left( {0,\frac{1}{e}}\right)$ ; <br>  单调增区间: $\;\left( {\frac{1}{e}, + \infty }\right)$ ; <br>  极小值与最小值: $\;f\left( \frac{1}{e}\right)  =  - \frac{1}{e}$ .</td></tr><tr><td>$f\left( x\right)  = \frac{x}{\ln x}$</td><td>[失效外部图片：bo_d7nktbc91nqc7384ijv0_3.jpg]</td><td>单调减区间: $\;\left( {0,1}\right)$ 和 $\left( {1, e}\right)$ ; <br>  单调增区间: $\left( {e, + \infty }\right)$ ； <br>  极小值: $\;f\left( e\right)  = e$ .</td></tr><tr><td>$f\left( x\right)  = \frac{\ln x}{x}$</td><td>[失效外部图片：bo_d7nktbc91nqc7384ijv0_4.jpg]</td><td>单调增区间: $\;\left( {0, e}\right) \;;$ <br>  单调减区间: $\;\left( {e, + \infty }\right)$ ; <br>  极大值与最大值: $\;f\left( e\right)  = \frac{1}{e}$ .</td></tr></table>

#### 5.4.2 导数中常用的不等式

1. ${e}^{x} \geq  x + 1$ ,当且仅当 $x = 0$ 时等号成立;

2. $x - 1 \geq  \ln x$ ,当且仅当 $x = 1$ 时等号成立;

3. 对数均值不等式:已知 $a > 0, b > 0$ ，设 $F\left( {a, b}\right)  = \left\{  \begin{array}{ll} \frac{a - b}{\ln a - \ln b}, & a \neq  b, \\  a, & a = b. \end{array}\right.$ 则 $\sqrt{ab} \leq  F\left( {a, b}\right)  \leq  \frac{a + b}{2}$ ， 当且仅当 $a = b$ 时等号成立.

## *5.4.3 罗尔定理与拉格朗日中值定理

1. 罗尔定理: 设函数 $g\left( x\right)$ 在 $\left\lbrack  {a, b}\right\rbrack$ 上连续,在 $\left( {a, b}\right)$ 内可导,且 $g\left( a\right)  = g\left( b\right)$ ,则存在 $c \in  \left( {a, b}\right)$ ,使得 ${g}^{\prime }\left( c\right)  = 0$

2. 拉格朗日中值定理: 设函数 $f\left( x\right)$ 在 $\left\lbrack  {a, b}\right\rbrack$ 上连续,在 $\left( {a, b}\right)$ 内可导,则存在 $c \in  \left( {a, b}\right)$ ,使得 ${f}^{\prime }\left( c\right)  = \frac{f\left( b\right)  - f\left( a\right) }{b - a}.$

## *5.4.4 洛必达法则

设(1)当 $x$ 趋近于 $a$ 时，函数 $f\left( x\right)$ 及 $g\left( x\right)$ 都趋于零；

(2)点 $a$ 的某去心邻域内， ${f}^{\prime }\left( x\right)$ 及 ${g}^{\prime }\left( x\right)$ 都存在且 ${g}^{\prime }\left( x\right)  \neq  0$ ；

(3) $\mathop{\lim }\limits_{{x \rightarrow  a}}\frac{{f}^{\prime }\left( x\right) }{{g}^{\prime }\left( x\right) }$ 存在(或为无穷大)，那么 $\mathop{\lim }\limits_{{x \rightarrow  a}}\frac{f\left( x\right) }{g\left( x\right) } = \mathop{\lim }\limits_{{x \rightarrow  a}}\frac{{f}^{\prime }\left( x\right) }{{g}^{\prime }\left( x\right) }$ .
