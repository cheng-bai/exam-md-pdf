---
title: 暑假讲义-Q老师
subtitle: 公式识别版 · 课堂留白排版
date: 2026-05-29
lang: zh-CN
---

> 说明：本版基于公式识别 Markdown 重新整理层级、分页和打印样式；增加课堂讲解留白，并将选择题选项纵向排列。

# 第一讲函数恒成立

### 补充概念对于数集 $S$ ,定义:

(1)有界与无界:若存在 $m \in R$ ，对 $\forall x \in S$ ， $\left| x\right| \leq m$ ，称 $S$ 有界；否则称 $S$ 无界

(2)上界:若存在 $m \in R$ ，对 $\forall x \in S$ ， $x \leq m$ ，称 $m$ 为 $S$ 的一个上界

① 上确界:若 $S$ 的所有上界中存在最小值 ${x}_{0}$ ，则称 ${x}_{0}$ 为 $S$ 的上确界，记作 $\operatorname{Sup}\{ S\}$

② 最大值: 若 $S$ 存在上确界 ${x}_{0}$ ,且 ${x}_{0} \in S$ ,称 ${x}_{0}$ 为 $S$ 的最大值,记作 $\operatorname{Max}\{ S\}$

(3)下界:若存在 $m \in R$ ，对 $\forall x \in S$ ， $x \geq m$ ，称 $m$ 为 $S$ 的一个下界

① 下确界:若 $S$ 的所有下界中存在最大值 ${x}_{0}$ ，则称 ${x}_{0}$ 为 $S$ 的下确界，记作 $\inf \{ S\}$

② 最小值:若 $S$ 存在下确界 ${x}_{0}$ ，且 ${x}_{0} \in S$ ，称 ${x}_{0}$ 为 $S$ 的最小值，记作 $\min \{ S\}$

## 一、恒成立问题的等价条件及分析方法

### 变量分离型: 转化为等价条件后求解

(1) $\forall x \in \left\lbrack {a, b}\right\rbrack , k > f\left( x\right) \Leftrightarrow k > \operatorname{Max}\{ f\}$ ；若 $\operatorname{Max}\{ f\}$ 不存在，则 $k \geq \operatorname{Sup}\{ f\}$

(2) $\exists x \in \left\lbrack {a, b}\right\rbrack , k > f\left( x\right) \Leftrightarrow k > \inf \{ f\}$

(3) $\forall {x}_{1} \in \left\lbrack {a, b}\right\rbrack ,\forall {x}_{2} \in \left\lbrack {c, d}\right\rbrack , f\left( {x}_{1}\right) > g\left( {x}_{2}\right) \Leftrightarrow \min \{ f\} > \operatorname{Max}\{ g\}$

(3) $\exists {x}_{1} \in \left\lbrack {a, b}\right\rbrack ,\exists {x}_{2} \in \left\lbrack {c, d}\right\rbrack , f\left( {x}_{1}\right) > g\left( {x}_{2}\right) \Leftrightarrow \operatorname{Max}\{ f\} > \min \{ g\}$

(4) $\forall {x}_{1} \in \left\lbrack {a, b}\right\rbrack ,\exists {x}_{2} \in \left\lbrack {c, d}\right\rbrack , f\left( {x}_{1}\right) > g\left( {x}_{2}\right) \Leftrightarrow \min \{ f\} > \min \{ g\}$

(5) $\exists {x}_{1} \in \left\lbrack {a, b}\right\rbrack ,\forall {x}_{2} \in \left\lbrack {c, d}\right\rbrack , f\left( {x}_{1}\right) > g\left( {x}_{2}\right) \Leftrightarrow \operatorname{Max}\{ f\} > \operatorname{Max}\{ g\}$

(6) $\exists {x}_{1} \in \left\lbrack {a, b}\right\rbrack ,\exists {x}_{2} \in \left\lbrack {c, d}\right\rbrack , f\left( {x}_{1}\right) = g\left( {x}_{2}\right) \Leftrightarrow {A}_{f} \cap {A}_{g} \neq \varnothing$

(7) $\forall {x}_{1} \in \left\lbrack {a, b}\right\rbrack ,\exists {x}_{2} \in \left\lbrack {c, d}\right\rbrack , f\left( {x}_{1}\right) = g\left( {x}_{2}\right) \Leftrightarrow {A}_{f} \subseteq {A}_{g}$

### 变量缠绕型:

**策略 1：** 转化为其他等价条件, 用其他变量来解决问题

**策略 2：** 定住第 1 个变量, 以第 2 个变量为主元求解恒成立问题; 待第 2 个变量从式子中消失后, 再解第 1 个变量的恒成立问题

## 二、多元恒成立的求解

1. 设函数 $f\left( x\right) = {x}^{2} - \left( {{k}^{2} - {5ak} + 3}\right) x + 7\left( {a, k \in \mathbf{R}}\right)$ ,已知对于任意的 $k \in \left\lbrack {0,2}\right\rbrack$ ,若当 ${x}_{1} \in \left\lbrack {k, k + a}\right\rbrack$ , ${x}_{2} \in \left\lbrack {k + {2a}, k + {4a}}\right\rbrack$ ，必有 $f\left( {x}_{1}\right) \geq f\left( {x}_{2}\right)$ ，则正实数 $a$ 的最大值为\_\_\_

2. 已知函数 $f\left( x\right) = {\left( x - 1\right) }^{2}$ ,若存在实数 $x \in \left\lbrack {\frac{4}{3},4}\right\rbrack$ ,使得对任意的 $t \in R$ ,有不等式 $f\left( x\right) \geq - {t}^{2} + \left( {s - t}\right) x + 4$ 都成立,求实数 $s$ 的最大值.

3. 给定自然数 $t \geq 2$ ,要求存在正整数 $n$ ,使不等式 ${1}^{-t} + {2}^{-t} + \cdots + {n}^{-t} \geq 2$ 成立,这样的 $t$ 共有\_\_\_个

4. 记 $\max \{ a, b\} = \left\{ \begin{array}{ll} a & a \geq b \\ b & a < b \end{array}\right.$ ,设 $M = \max \left\{ {\left| {x - {y}^{2} + 4}\right| ,\left| {2{y}^{2} - x + 8}\right| }\right\}$ ,若对一切实数 $x\text{ 、 }y, M \geq {m}^{2} - {2m}$ 都成立,则实数 $m$ 的取值范围是\_\_\_

5. 对开区间 $I = \left( {a, b}\right)$ ,定义 $\left| I\right| = b - a$ ,当实数集合 $M$ 为 $n$ 段( $n$ 为正整数)互不相交的开区间 ${I}_{1}\text{ 、 }{I}_{2}\text{ 、 }\cdots \text{ 、 }{I}_{n}$ 的并集时,定义 $\left| M\right| = \mathop{\sum }\limits_{{k = 1}}^{n}\left| {I}_{k}\right|$ ,若对任意上述形式的 $\left( {0,{2\pi }}\right)$ 的子集 $\mathrm{A}$ ,总存在 $k \in \mathrm{Z}$ ,使得 $\left| {A}_{k}\right| \geq \lambda \left| A\right|$ ，其中 ${A}_{k} = \left\{ {x\left| {x \in A,}\right| \tan \left( {x + \frac{k\pi }{4}}\right) \mid < \sqrt{2} - 1}\right\}$ ，则 $\lambda$ 的最大值为\_\_\_.

6. 已知 $\theta > 0$ ，若存在实数 $\varphi$ ，使得对任意 $n \in {\mathbf{N}}^{ * }$ 都有 $\cos \left( {{n\theta } + \varphi }\right) < \frac{\sqrt{3}}{2}$ ，则 $\theta$ 的最小值是\_\_\_.

7. 在平面直角坐标系 ${xOy}$ 中,起点为坐标原点的向量 $\overrightarrow{a}\text{ 、 }\overrightarrow{b}$ 满足 $\left| \overrightarrow{a}\right| = \left| \overrightarrow{b}\right| = 1$ ,且 $\overrightarrow{a} \cdot \overrightarrow{b} = - \frac{1}{2}$ , $\overrightarrow{c} = \left( {m,1 - m}\right) ,\overrightarrow{d} = \left( {n,1 - n}\right) \left( {m, n \in \mathbf{R}}\right)$ ,若存在向量 $\overrightarrow{a}\text{ 、 }\overrightarrow{b}$ ,对于任意实数 $m\text{ 、 }n$ ,不等式 $\left| {\overrightarrow{a} - \overrightarrow{c}}\right| + \left| {\overrightarrow{b} - \overrightarrow{d}}\right| \geq T$ 成立，则实数 $T$ 的最大值为\_\_\_

8. 已知 $\overrightarrow{e}$ 为单位向量， $\left| {\overrightarrow{m} - 2\overrightarrow{e}}\right| = 1$ ， $\left| {\overrightarrow{n} - 2\overrightarrow{e}}\right| = 2$ ，则 $\overrightarrow{m} \cdot \overrightarrow{n}$ 的取值范围为\_\_\_

9. 已知函数. $f\left( x\right) = {x}^{2} - {ax} - a$ ,设 $g\left( x\right) = \left| {f\left( x\right) }\right|$ ,若对任意实数 $a$ ,存在 $x \in \left\lbrack {0,1}\right\rbrack$ 使不等式 $g\left( {x}_{0}\right) \geq k$ 恒成立，则实数 $k$ 的取值范围为\_\_\_

# 第二讲函数的对称性与周期性 I

## 一、函数轴对称、中心对称的等价条件, 图像特征, 变换特点
### 轴对称性
若对定义域上任意 $x, g\left( x\right) = f\left( {{2a} - x}\right)$ 均成立,则 $f\left( x\right)$ 和 $g\left( x\right)$ 关于 $x = a$ 轴对称。

若 $f\left( x\right) = f\left( {{2a} - x}\right)$ 对定义域上任意 $x$ 成立,则 $f\left( x\right)$ 为轴对称函数,其对称轴为 $x = a$

**易混淆点：**

若对定义域上任意 $x, g\left( x\right) = f\left( {a + x}\right) , h\left( x\right) = f\left( {b - x}\right)$ ,则 $g\left( x\right)$ 和 $h\left( x\right)$ 关于 $x = \frac{b - a}{2}$ 轴对称。

若 $f\left( {a + x}\right) = f\left( {b - x}\right)$ 对定义域上任意 $x$ 成立,则 $f\left( x\right)$ 为轴对称函数,其对称轴为 $x = \frac{b + a}{2}$

### 中心对称性
若对定义域上任意 $x, g\left( x\right) = {2c} - f\left( {{2b} - x}\right)$ 均成立，则 $f\left( x\right)$ 和 $g\left( x\right)$ 关于 $\left( {b, c}\right)$ 中心对称。

若 $f\left( x\right) + f\left( {{2b} - x}\right) = {2c}$ 对定义域上任意 $x$ 成立,则 $f\left( x\right)$ 为中心对称函数,对称中心为点 $\left( {b, c}\right)$ **易混淆点：**

若对定义域上任意 $x, g\left( x\right) = f\left( {a + x}\right) , h\left( x\right) = {2c} - f\left( {b - x}\right)$ ,则 $g\left( x\right)$ 和 $h\left( x\right)$ 关于 $\left( {\frac{b - a}{2}, c}\right)$ 中心对称。

若 $f\left( {a + x}\right) + f\left( {b - x}\right) = {2c}$ 对定义域上任意 $x$ 成立,则 $f\left( x\right)$ 为中心对称函数,对称中心为 $\left( {\frac{b + a}{2}, c}\right)$

1. 若函数 $f\left( x\right)$ 关于 $x = 1$ 轴对称,且 $f\left( x\right) = {x}^{2} + \sin x$ 在 $x \in ( - \infty ,1\rbrack$ 时成立,求 $f\left( x\right)$ 在 $x \in \left( {1, + \infty }\right)$ 上的解析式。

2. 若函数 $f\left( x\right)$ 关于 $\left( {2,0}\right)$ 中心对称,且 $f\left( x\right) = {x}^{2} + \sin x$ 在 $x \in \left( {-\infty ,2}\right)$ 时成立,求 $f\left( x\right)$ 在 $x \in \left( {2, + \infty }\right)$ 上的解析式。

## 二、对称性的线性继承
定理 1: 已知 $f\left( x\right)$ 关于 $\left( {a, m}\right)$ 中心对称, $g\left( x\right)$ 关于 $\left( {a, n}\right)$ 中心对称,则 $f\left( x\right) + g\left( x\right)$ 关于 $\left( {a, m + n}\right)$ 中心对称，$f\left( x\right) - g\left( x\right)$ 关于 $\left( {a, m - n}\right)$ 中心对称。

证明: 因为 $f\left( x\right)$ 关于 $\left( {a, m}\right)$ 中心对称,所以 $f\left( x\right) + f\left( {{2a} - x}\right) = {2m}$ ,同理 $g\left( x\right) + g\left( {{2a} - x}\right) = {2n}$

则 $F\left( x\right) + F\left( {{2a} - x}\right) = \left\lbrack {f\left( x\right) \pm g\left( x\right) }\right\rbrack + \left\lbrack {f\left( {{2a} - x}\right) \pm g\left( {{2a} - x}\right) }\right\rbrack$

$= \left\lbrack {f\left( x\right) + f\left( {{2a} - x}\right) }\right\rbrack \pm \left\lbrack {g\left( x\right) + g\left( {{2a} - x}\right) }\right\rbrack = {2m} \pm {2n} = 2\left( {m \pm n}\right)$

所以, $F\left( x\right)$ 关于 $\left( {a, m + n}\right)$ 中心对称定理 2: 已知 $f\left( x\right)$ 关于 $\left( {a, m}\right)$ 中心对称, $g\left( x\right)$ 关于 $\left( {b, n}\right)$ 中心对称,当 $g\left( x\right)$ 和 $f\left( x\right)$ 的图像可以通过平移完全重合时, $F\left( x\right) = f\left( x\right) + g\left( x\right)$ 关于 $\left( {\frac{a + b}{2}, m + n}\right)$ 中心对称。

证明: 由条件可知,将 $f\left( x\right)$ 右移 ${\Delta x} = b - a$ ,上移 ${\Delta y} = n - m$ 可以得到 $g\left( x\right)$ ,

即 $g\left( x\right) = f\left( {x - {\Delta x}}\right) + {\Delta y} = f\left( {x - b + a}\right) + n - m$

因此 $F\left( x\right) + F\left( {a + b - x}\right) = \left\lbrack {f\left( x\right) + g\left( x\right) }\right\rbrack + \left\lbrack {f\left( {a + b - x}\right) + g\left( {a + b - x}\right) }\right\rbrack$

$= \left\lbrack {f\left( x\right) + f\left( {x - b + a}\right) + n - m}\right\rbrack + \left\{ {f\left( {a + b - x}\right) + f\left\lbrack {\left( {a + b - x}\right) - b + a}\right\rbrack + n - m}\right\}$

$= f\left( x\right) + f\left( {x - b + a}\right) + f\left( {a + b - x}\right) + f\left( {{2a} - x}\right) + {2n} - {2m}$

$= \left\lbrack {f\left( x\right) + f\left( {{2a} - x}\right) }\right\rbrack + \{ f\left\lbrack {a + \left( {x - b}\right) }\right\rbrack + f\left\lbrack {a - \left( {x - b}\right) }\right\rbrack \} + {2n} - {2m}$

$= {2m} + {2m} + {2n} - {2m}$

$= 2\left( {m + n}\right)$

所以, $F\left( x\right)$ 关于 $\left( {\frac{a + b}{2}, m + n}\right)$ 中心对称定理 3: 已知 $f\left( x\right)$ 关于 $x = a$ 轴对称, $g\left( x\right)$ 关于 $x = a$ 轴对称,则 $F\left( x\right) = f\left( x\right) \pm g\left( x\right)$ 也关于 $x = a$ 轴对称。(证明同定理 1，请自行尝试)

定理 4:已知 $f\left( x\right)$ 关于 $x = a$ 轴对称， $g\left( x\right)$ 关于 $x = b$ 轴对称，当 $g\left( x\right)$ 和 $f\left( x\right)$ 的图像可以通过平移完全重合时, $F\left( x\right) = f\left( x\right) + g\left( x\right)$ 关于 $x = \frac{a + b}{2}$ 轴对称。(证明同定理 2,请自行尝试)

3. 已知 $f\left( x\right) = \frac{x}{x - 1} + \sin {\pi x}$ ,记 $\left\lbrack x\right\rbrack$ 表示不超过 $x$ 的最大整数,如 $\left\lbrack \pi \right\rbrack = 3,\left\lbrack {-e}\right\rbrack = - 3$ ,则 $y = \left\lbrack {f\left( x\right) }\right\rbrack + \left\lbrack {f\left( {2 - x}\right) }\right\rbrack$ 的值域为\_\_\_

4. 已知函数 $f\left( x\right) = \left| {x + \frac{1}{x}}\right|$ ,给出下列命题:① 存在实数 $a$ ，使得函数 $y = f\left( x\right) + f\left( {x - a}\right)$ 为奇函数；② 对任意实数 $a$ ,均存在实数 $m$ ,使得函数 $g\left( x\right) = f\left( x\right) + f\left( {x - a}\right)$ 关于 $x = m$ 对称; ③ 若对任意非零实数 $a$ , $f\left( x\right) + f\left( {x - a}\right) \geq k$ 都成立,则实数 $k$ 的取值范围为 $( - \infty ,4\rbrack$ ; ④ 存在实数 $k$ ,使得函数 $y = f\left( x\right) + f\left( {x - a}\right) - k$ 对任意非零实数 $a$ 均存在 6 个零点.其中的真命题是\_\_\_. (写出所有真命题的序号)

## 三、对称性质的应用

5. 设函数 $f\left( x\right)$ 的定义域为 $D$ ,已知真命题: “点 $A\left( {m, n}\right)$ 是 $f\left( x\right)$ 图像的对称中心的充要条件是 $f\left( {m + x}\right) + f\left( {m - x}\right) = {2n}, x \in D$ "。

(1)分别求函数 $f\left( x\right) = \frac{x + 2}{x}$ 和 $g\left( x\right) = \lg \frac{x + 2}{x}$ 的图像的对称中心;

(2)设 $d \in \left( {0,1}\right)$ ，是否存在 $h\left( x\right)$ ，使 $y = \lg h\left( x\right)$ 与 $h\left( x\right)$ 的图像有相同的对称中心 $\left( {c, d}\right)$ ?

(3)已知函数 $f\left( x\right)$ 在 $\left( {-\infty ,0}\right) \cup \left( {0, + \infty }\right)$ 上的图像关于点 $\left( {0,1}\right)$ 中心对称,且当 $x \in \left( {0, + \infty }\right)$ 时, $f\left( x\right) = {x}^{2} + x + 1$ , 求 $f\left( x\right)$ 在 $\left( {-\infty ,0}\right)$ 上的解析式;

(4)求函数 $f\left( x\right) = \frac{1}{x} + \frac{1}{x + 1} + \frac{1}{x + 2} + \frac{1}{x + 3} + \cdots + \frac{1}{x + {2023}}$ 的图像的对称中心。

6. 已知 $f\left( x\right)$ 是定义在 $\left\lbrack {-4,4}\right\rbrack$ 上的奇函数， $g\left( x\right) = f\left( {x - 2}\right) + \frac{1}{3}$ ，当 $x \in \left\lbrack {-2,0)\cup (0,2}\right\rbrack$ 时， $g\left( x\right) = \frac{1}{{2}^{\left| x\right| } - 1}, g\left( 0\right) = 0$ ,则方程 $g\left( x\right) = {\log }_{\frac{1}{2}}\left( {x + 1}\right)$ 的解的个数为( )

::: choices
- A.1 个
- B. 2 个
- C. 3 个
- D. 4 个
:::


7. 已知函数 $f\left( x\right) = {x}^{2} + {e}^{x} - \frac{1}{2}\left( {x < 0}\right)$ 与 $g\left( x\right) = {x}^{2} + \ln \left( {x + a}\right)$ 的图像上存在关于 $y$ 轴对称的点,则实数 $a$ 的取值范围是\_\_\_.

8. 如果函数 $y = f\left( x\right)$ 的定义域为 $R$ ,且存在实常数 $a$ ,使得对于定义域内任意 $x$ ,都有 $f\left( {x + a}\right) = f\left( {2 - x}\right)$ 成立,则称此函数 $f\left( x\right)$ 具有 “ $P\left( a\right)$ 性质”。已知函数 $y = g\left( x\right)$ 既具有 “ $P\left( 0\right)$ 性质”,又具有 “ $P\left( 4\right)$ 性质”,且当 $- 1 \leq x \leq 1$ 时, $g\left( x\right) = {\left( x + 1\right) }^{2}$ ,若函数 $y = g\left( x\right)$ 的图像与直线 $y = {px}$ 有 2018 个公共点,求实数 $p$ 的值.

9. 已知函数 $f\left( x\right) = {2024}^{x - 1} + {\left( x - 1\right) }^{3} - {2024}^{1 - x} + {2x}$ ,则不等式 $f\left( {{x}^{2} - 4}\right) + f\left( {2 - {3x}}\right) \leq 4$ 的解集为\_\_\_

## 四、函数的周期性
若函数对定义域上任意 $x, f\left( x\right) = f\left( {x + T}\right) ,\left( {T > 0}\right)$ 均成立,则称 $f\left( x\right)$ 为周期函数, $T$ 为 $f\left( x\right)$ 的一个周期。特别的,若 ${T}_{0}$ 是能使上述式子成立的最小实数,则称 ${T}_{0}$ 为 $f\left( x\right)$ 的最小正周期。

周期函数定义域 $D$ 必定呈周期性,且无界:

若周期函数 $f\left( x\right)$ 存在最小正周期 ${T}_{0}$ ,则有:

(1)若 $f\left( x\right) = f\left( {x + T}\right)$ 在定义域上恒成立，则必有 $T = k{T}_{0}$ ，其中 $k \in Z$

(2)若 $f\left( x\right) = f\left( {x + {T}_{1}}\right) , f\left( x\right) = f\left( {x + {T}_{2}}\right)$ ，则必定存在有理数 $\alpha$ 使 ${T}_{1} = \alpha {T}_{2}$ ，且 ${T}_{0}$ 是 ${T}_{1},{T}_{2}$ 的一个最大公约数具有以下性质的函数也是周期函数:

① 若 $f\left( {x + a}\right) = - f\left( x\right)$ ，则 $y = f\left( x\right)$ 的周期为 $2\left| a\right|$ ；特别的，我们称这个性质为“奇周期性”

② 若 $f\left( {x + a}\right) = \pm \frac{1}{f\left( x\right) }$ ，则 $y = f\left( x\right)$ 的周期为 $2\left| a\right|$ ；

③ 若 $f\left( {x + a}\right) = \frac{f\left( x\right) + 1}{f\left( x\right) - 1}$ 或 $f\left( {x + a}\right) = \frac{1 - f\left( x\right) }{1 + f\left( x\right) }$ ，则 $y = f\left( x\right)$ 的周期为 $2\left| a\right|$ ；

④ 若 $f\left( {x + a}\right) = \frac{1 + f\left( x\right) }{1 - f\left( x\right) }$ 或 $f\left( {x + a}\right) = \frac{f\left( x\right) - 1}{f\left( x\right) + 1}$ ，则 $y = f\left( x\right)$ 的周期为 $4\left| a\right|$ ；

10. 设 $f\left( x\right)$ 是定义在 $R$ 上以 2 为周期的函数,记 ${I}_{k} = ({2k} - 1,{2k} + 1\rbrack \left( {k \in Z}\right)$ ,已知 $x \in {I}_{0}$ 时, $f\left( x\right) = {x}^{2}$ ,求 $f\left( x\right)$ 在 ${I}_{k}$ 上的解析式

11. 设 $g\left( x\right)$ 是定义在 $R$ 上,以 1 为周期的函数,若函数 $f\left( x\right) = x + g\left( x\right)$ 在区间 $\left\lbrack {3,4}\right\rbrack$ 上的值域为 $\left\lbrack {-2,5}\right\rbrack$ ,则 $f\left( x\right)$ 在区间 $\left\lbrack {-{10},{10}}\right\rbrack$ 上的值域为\_\_\_。

12. 已知函数 $f\left( x\right)$ ,对任意的 $x \in \lbrack 0, + \infty )$ ,恒有 $f\left( {x + 2}\right) = f\left( x\right)$ 成立,且当 $x \in \lbrack 0,2)$ 时, $f\left( x\right) = 2 - x$ . 则方程 $f\left( x\right) = \frac{1}{n}x$ 在区间 $\lbrack 0,{2n})$ (其中 $n \in {\mathbf{N}}^{ * }$ )上所有根的和为\_\_\_.

# 课后练习 1

1. 已知函数 $f\left( x\right) = \left\{ \begin{array}{ll} x - \frac{8}{x} & x < 0 \\ \left| {x - a}\right| & x \geq 0 \end{array}\right.$ ,若对任意的 ${x}_{1} \in \lbrack 2, + \infty )$ ,都存在 ${x}_{2} \in \left\lbrack {-2, - 1}\right\rbrack$ ,使得 $f\left( {x}_{1}\right) \cdot f\left( {x}_{2}\right) \geq a$ ，则实数 $a$ 的取值范围为\_\_\_.

2. 已知函数 $f\left( x\right) = \left\{ \begin{array}{ll} \frac{{x}^{2} + 4}{x} & x \geq 2 \\ {2}^{\left| x - a\right| } & x < 2 \end{array}\right.$ ,若对任意的 ${x}_{1} \in \lbrack 2, + \infty )$ ,都存在唯一的 ${x}_{2} \in \left( {-\infty ,2}\right)$ ,满足 $f\left( {x}_{2}\right) = f\left( {x}_{1}\right)$ ,则实数 $a$ 的取值范围是\_\_\_.

3. 若存在实常数 $k$ 和 $b$ ,使得 $F\left( x\right)$ 和 $G\left( x\right)$ 对其公共定义域上的任意实数 $x$ 都满足: $F\left( x\right) \geq {kx} + b$ 和 $G\left( x\right) \leq {kx} + b$ 恒成立,则称此直线 $y = {kx} + b$ 为 $F\left( x\right)$ 和 $G\left( x\right)$ 的 “分隔直线”. 已知函数 $f\left( x\right) = - {x}^{2}\left( {x \in R}\right)$ , $g\left( x\right) = \frac{1}{x}\left( {x > 0}\right)$ ，若 $f\left( x\right)$ 和 $g\left( x\right)$ 之间存在“分隔直线”，则 $b$ 的取值范围为\_\_\_.

4. 函数 $f\left( x\right) = x - \frac{2}{x}, x \in \left\lbrack {1,2}\right\rbrack , g\left( x\right) = a\cos \frac{\pi x}{2} + 5 - {2a},\left( {a > 0}\right)$ ,对任意的 ${x}_{1} \in \left\lbrack {1,2}\right\rbrack$ ,总存在 ${x}_{2} \in \left\lbrack {0,1}\right\rbrack$ ,使得 $g\left( {x}_{2}\right) = f\left( {x}_{1}\right)$ 成立,则 $a$ 的取值范围为\_\_\_.

5. 已知对任意的 $x \in \left( {-\infty ,0}\right) \cup \left( {0, + \infty }\right) , y \in \left\lbrack {-1,1}\right\rbrack$ ，不等式 ${x}^{2} + \frac{16}{{x}^{2}} - {2xy} - \frac{8}{x}\sqrt{1 - {y}^{2}} - a \geq 0$ 恒成立，则实数 $a$ 的取值范围为\_\_\_.

6. 已知函数 $f\left( x\right) = \left\{ \begin{array}{l} {\log }_{2}x, x > 0 \\ \left| {{2x} + 1}\right| , x \leq 0 \end{array}\right.$ ,若对任意 $a \leq - 1$ ,当 $- 1 < b \leq m$ 时,总有 $a\left( {f\left( b\right) - 1}\right) \geq b$ 成立,则实数 $m$ 的最大值为\_\_\_.

7. 已知定义在 $\mathbf{R}$ 上的偶函数 $f\left( x\right)$ ,满足 ${\left\lbrack f\left( x\right) \right\rbrack }^{3} - {\left\lbrack f\left( x\right) \right\rbrack }^{2} - {x}^{2}f\left( x\right) + {x}^{2} = 0$ 对任意的实数 $x$ 都成立,且值域为 $\left\lbrack {0,1}\right\rbrack$ . 设函数 $g\left( x\right) = \left| {x - m}\right| - \left| {x - 1}\right| \left( {m < 1}\right)$ ,若对任意的 ${x}_{1} \in \left( {-2,\frac{1}{2}}\right)$ ,存在 ${x}_{2} > {x}_{1}$ ,使得 $g\left( {x}_{2}\right) = f\left( {x}_{1}\right)$ 成立,则实数 $m$ 的取值范围为\_\_\_.

# 课后练习 2

1. 若函数 $f\left( x\right) = {x}^{2} + {bx} + c$ 对一切实数都有 $f\left( {2 + x}\right) = f\left( {2 - x}\right)$ ，则()

::: choices
- A. $f\left( 2\right) < f\left( 1\right) < f\left( 4\right)$
- B. $f\left( 1\right) < f\left( 2\right) < f\left( 4\right)$
- C. $f\left( 2\right) < f\left( 4\right) < f\left( 1\right)$
- D. $f\left( 4\right) < f\left( 2\right) < f\left( 1\right)$
:::


2. 设函数 $y = f\left( x\right)$ 定义在实数集 $R$ 上，则函数 $y = f\left( {x - 1}\right)$ 与 $y = f\left( {1 - x}\right)$ 的图象关于( )对称。

::: choices
- A. 直线 $y = 0$
- B. 直线 $x = 0$
- C. 直线 $y = 1$
- D. 直线 $x = 1$
:::


3. 已知函数 $y = f\left( x\right)$ 的定义域为 $R$ ,给出以下两个结论:

① 若函数 $y = f\left( x\right)$ 的图像是轴对称图形,则函数 $y = f\left( {f\left( x\right) }\right)$ 的图像也是轴对称图形;

② 若函数 $y = f\left( x\right)$ 的图像是中心对称图形,则函数 $y = f\left( {f\left( x\right) }\right)$ 的图像也是中心对称图形. 它们的成立情况为( )

::: choices
- (A) ① 成立，② 不成立
- (B) ① 不成立，② 成立
- (C) ①② 均不成立
- (D) ①② 均成立
:::


4. 函数 $y = f\left( x\right)$ 是定义在实数集 $R$ 上的函数，那么 $y = - f\left( {x + 4}\right)$ 与 $y = f\left( {6 - x}\right)$ 的图象之间 ( )

::: choices
- A. 关于直线 $x = 5$ 称
- B. 关于直线 $x = 1$ 对称
- C. 关于点 $\left( {5,0}\right)$ 对称
- D. 关于点 $\left( {1,0}\right)$ 对称
:::


5. 函数 $f\left( x\right)$ 对于任意实数 $x$ 满足条件 $f\left( {x + 2}\right) = \frac{1}{f\left( x\right) }$ ,若 $f\left( 1\right) = - 5$ ,则 $f\left( {f\left( 5\right) }\right) =$ ( )等于

::: choices
- A. 5
- B. -5
- C. $\frac{1}{5}$
- D. $- \frac{1}{5}$
:::


6. 定义域均为 $D$ 的三个函数 $f\left( x\right) , g\left( x\right) , h\left( x\right)$ 满足条件: 对任意 $x \in D$ ,点 $\left( {x, g\left( x\right) }\right)$ 与点 $\left( {x, h\left( x\right) }\right)$ 都关于点 $\left( {x, f\left( x\right) }\right)$ 对称,则称 $h\left( x\right)$ 是 $g\left( x\right)$ 关于 $f\left( x\right)$ 的“对称函数”. 已知函数 $g\left( x\right) = \sqrt{1 - x}, h\left( x\right) = \sqrt{3x}, h\left( x\right)$ 是 $g\left( x\right)$ 关于 $f\left( x\right)$ 的 “对称函数”,若 $f\left( x\right)$ 的定义域为 $D$ ,若对任意 $s \in D$ ,都存在 $t \in D$ ,使得 ${2f}\left( s\right) = {t}^{2} + {2t} + {a}^{2} + a - 1$ 成立，则实数 $a$ 的取值范围为( )

::: choices
- (A) $\left\lbrack {-1,0}\right\rbrack \cup \left\lbrack {1,2}\right\rbrack$
- (B) $\{ - 1\} \cup \left\lbrack {0,2}\right\rbrack$
- (C) $\left\lbrack {-2, - 1}\right\rbrack \cup \left\lbrack {0,1}\right\rbrack$
- (D) $\{ 1\} \cup \left\lbrack {-2,0}\right\rbrack$
:::


7. 若 $M, N$ 两点分别在函数 $y = f\left( x\right)$ 与 $y = g\left( x\right)$ 的图像上,且关于直线 $x = 1$ 对称,称 $M, N$ 是 $y = f\left( x\right)$ 与 $y = g\left( x\right)$ 的一对“伴点” ( $M, N$ 与 $N, M$ 视为相同的一对).

已知 $f\left( x\right) = \left\{ \begin{matrix} - \sqrt{2 - x} & x < 2 \\ \sqrt{4 - {\left( x - 4\right) }^{2}} & x \geq 2 \end{matrix}\right.$ , $g\left( x\right) = \left| {x + a}\right| + 1$ ,若 $y = f\left( x\right)$ 与 $y = g\left( x\right)$ 存在两对“伴点”,则实数 $a$ 的取值范围为\_\_\_

8. 若函数 $f\left( x\right) = \left\{ \begin{matrix} {2}^{-x} & x \leq 0 \\ f\left( {x - 1}\right) - f\left( {x - 2}\right) & x > 0 \end{matrix}\right.$ ，则 $f\left( {2025}\right) =$ \_\_\_

9. 设函数 $f\left( x\right) = \left\{ \begin{array}{l} \left| {{\log }_{2}x}\right| ,0 < x < 2 \\ f\left( {4 - x}\right) ,2 < x < 4 \end{array}\right.$ ,方程 $f\left( x\right) = m$ 有四个不相等的实根 ${x}_{i}\left( {i = 1,2,3,4}\right)$ ,则 ${x}_{1}^{2} + {x}_{2}^{2} + {x}_{3}^{2} + {x}_{4}^{2}$ 的取值范围是\_\_\_.

# 第三讲函数的对称性与周期性 II

## 一、函数图像的周期变换

1. 设函数 $f\left( x\right) = \left\{ \begin{array}{l} a + {2}^{-x}, x \leq 0 \\ f\left( {x - 1}\right) , x > 0 \end{array}\right.$ ，记 $g\left( x\right) = f\left( x\right) - x$ ，若函数 $g\left( x\right)$ 有且仅有两个零点，则实数 $a$ 的取值范围是\_\_\_。

2. 已知定义域为 $\mathrm{R}$ 的函数 $y = f\left( x\right)$ 满足 $f\left( {x + 2}\right) = f\left( x\right)$ ，且 $- 1 \leq x < 1$ 时， $f\left( x\right) = 1 - {x}^{2}$ ；函数 $g\left( x\right) = \left\{ \begin{array}{l} \lg \left| x\right| , x \neq 0, \\ 1, x = 0. \end{array}\right.$ ，若 $F\left( x\right) = f\left( x\right) - g\left( x\right)$ ，则 $x \in \left\lbrack {-5,{10}}\right\rbrack$ ，函数 $F\left( x\right)$ 零点的个数是\_\_\_.

3. 已知函数 $f\left( x\right) = \left\{ \begin{matrix} \sqrt{1 - {\left( x - 1\right) }^{2}},0 \leq x < 2 \\ f\left( {x - 2}\right) , x \geq 2 \end{matrix}\right.$ ,若对于正数 ${k}_{n}\left( {n \in {N}^{ * }}\right)$ ,直线 $y = {k}_{n}x$ 与函数 $f\left( x\right)$ 的图像恰好有 ${2n} + 1$ 个不同的交点，则 ${k}_{1}^{2} + {k}_{2}^{2} + \ldots + {k}_{n}^{2} =$ \_\_\_.

## 二、函数图像的类周期变换
假设 $f\left( x\right)$ 定义域为 $R$ ,在区间 $\left\lbrack {a, b}\right\rbrack$ 上的图像为 $\Gamma$ ,则(以下 $k \in Z$ )

(1)若 $f\left( {x + T}\right) = f\left( x\right) + a, f\left( x\right)$ 在 $\left\lbrack {a + {kT}, b + {kT}}\right\rbrack$ 上的图像为 $\Gamma$ 上移 ${ka}$ 得到；

(2)若 $f\left( {x + T}\right) = {\lambda f}\left( x\right) ,\left( {\lambda > 0,{ab} \geq 0}\right) , f\left( x\right)$ 在 $\left\lbrack {a + {kT}, b + {kT}}\right\rbrack$ 上的图像为 $\Gamma$ 在竖直方向伸缩 $\lambda$ 倍得到

(3)若 $f\left( {\lambda x}\right) = {\mu f}\left( x\right) ,\left( {\lambda > 1,\mu > 0, b = {\lambda a} > 0}\right) , f\left( x\right)$ 在 $\left\lbrack {{\lambda }^{k - 1}a,{\lambda }^{k - 1}b}\right\rbrack$ 上的图像为 $\Gamma$ 在竖直方向伸缩 ${\mu }^{k - 1}$ 倍得到

4. 已知函数 $y = f\left( x\right)$ 的定义域是 $\lbrack 0, + \infty )$ ,满足 $f\left( x\right) = \left\{ \begin{matrix} {2x} & 0 \leq x < 1 \\ {x}^{2} - {4x} + 5 & 1 \leq x < 3 \\ - {2x} + 8 & 3 \leq x < 4 \end{matrix}\right.$ ，且 $f\left( {x + 4}\right) = f\left( x\right) + a$ ，若存在实数 $k$ ,使函数 $g\left( x\right) = f\left( x\right) + k$ 在区间 $\left\lbrack {0,{2024}}\right\rbrack$ 上恰好有 2024 个零点,则实数 $a$ 的取值范围为\_\_\_

5. 定义在 $\left( {0, + \infty }\right)$ 上的函数 $f\left( x\right)$ 满足: $f\left( {2x}\right) = {2f}\left( x\right)$ ,且当 $x \in (1,2\rbrack$ 时, $f\left( x\right) = 2 - x$ ,若 ${x}_{1},{x}_{2}$ 是方程 $f\left( x\right) = a\left( {0 < a \leq 1}\right)$ 的两个实数根,则 ${x}_{1} - {x}_{2}$ 不可能是 ( )

::: choices
- A. 24
- B. 72
- C. 96
- D. 120
:::


6. 已知定义在 $R$ 上的函数 $f\left( x\right)$ 满足 $f\left( {x + 1}\right) = {2f}\left( x\right) + 1$ ，当 $x \in \lbrack 0,1)$ 时， $f\left( x\right) = {x}^{3}$ . 设 $f\left( x\right)$ 在区间 $\lbrack n, n + 1)\left( {n \in {\mathbf{N}}^{ * }}\right)$ 上的最小值为 ${a}_{n}$ . 若存在 $n \in {\mathbf{N}}^{ * }$ ,使得 $\lambda \left( {{a}_{n} + 1}\right) < {2n} - 7$ 有解,则实数 $\lambda$ 的取值范围是 \_\_\_.

7. 已知函数 $f\left( x\right)$ 是定义在 $\lbrack 1, + \infty )$ 上的函数,且 $f\left( x\right) = \left\{ \begin{array}{l} 1 - \left| {{2x} - 3}\right| ,1 \leq x < 2 \\ {0.5f}\left( {0.5x}\right) , x \geq 2 \end{array}\right.$ ,则函数 $y = {2xf}\left( x\right) - 3$ 在区间 (1,2024) 上的零点个数为\_\_\_.

## 三、周期与对称性的绑定关系
函数的周期性和对称性间存在以下绑定关系，当任意两个条件成立时，第三个条件自动成立。

第一组: $\text{ ① }f\left( x\right)$ 关于 $x = a$ 轴对称; ② $f\left( x\right)$ 关于 $x = b$ 轴对称; ③ $f\left( x\right)$ 为周期函数，且 $T = 2\left| {a - b}\right|$

第二组: $\text{ ① }f\left( x\right)$ 关于 $\left( {a,0}\right)$ 中心对称; $\text{ ② }f\left( x\right)$ 关于 $\left( {b,0}\right)$ 中心对称; $\text{ ③ }f\left( x\right)$ 为周期函数,且 $T = 2\left| {a - b}\right|$

第三组: $\text{ ① }f\left( x\right)$ 关于 $x = a$ 轴对称; $\text{ ② }f\left( x\right)$ 关于 $\left( {b,0}\right)$ 中心对称; $\text{ ③ }f\left( x\right)$ 为奇周期函数,且 $T = 4\left| {a - b}\right|$

![](images/bo_d68j3a77aajc739aivpg_28_120_514_1406_1150_0.jpg)

一旦出现任意一组绑定关系，则函数的对称轴或对称中心，都以将 $\frac{T}{2}$ 为间隔均匀分布在 $x$ 轴上。

10. 已知 $f\left( x\right)$ 为奇函数,当 $x \in (0,1\rbrack , f\left( x\right) = \ln x$ ,且 $f\left( x\right)$ 关于直线 $x = 1$ 对称。设方程 $f\left( x\right) = x + 1$ 的正数解为 ${x}_{1},{x}_{2},\cdots ,{x}_{n},\cdots$ ,且任意的 $n \in \mathrm{N}$ ，总存在实数 $M$ ，使得 $\left| {{x}_{n + 1} - {x}_{n}}\right| < M$ 成立，则实数 $M$ 的最小值为

8 已知定义在 $R$ 上的奇函数 $f\left( x\right)$ 满足 $f\left( {x - 4}\right) = - f\left( x\right)$ ，且 $x \in \left\lbrack {0,2}\right\rbrack$ 时， $f\left( x\right) = {\log }_{2}\left( {x + 1}\right)$ ，若 $m \in \left( {0,1}\right)$ ，关于 $x$ 的方程 $f\left( x\right) - m = 0$ 在 $\left\lbrack {-8,8}\right\rbrack$ 上的所有根之和为\_\_\_

9. 【2025 上海高考 21 改编】已知函数 $y = f\left( x\right)$ 是定义域为 $\mathbf{R}$ ，周期为 $T = 2$ 的周期函数，若 $y = f\left( x\right)$ 也是偶函数,且当 $x \in (0,1\rbrack$ 时, $f\left( x\right) = 1 - x$ ,求 $y = f\left( x\right) , x \in \left( {1,2}\right)$ 的解析式,并证明: 对任意实数 $c$ , 函数 $y = f\left( x\right) - c$ 在 $\left\lbrack {-3,3}\right\rbrack$ 上至多有 9 个零点.

10. 已知定义在 $R$ 上的奇函数 $f\left( x\right)$ 满足 $f\left( {x + 2}\right) = - f\left( x\right)$ ,且 $0 \leq x \leq 1$ 时, $f\left( x\right) = {\log }_{2}\left( {x + a}\right)$ 。若对于任意 $x \in \left\lbrack {0,1}\right\rbrack$ ，都有 $f\left( {-{x}^{2} + {tx} + \frac{1}{2}}\right) \geq 1 - {\log }_{2}3$ ，则实数 $t$ 的取值范围为\_\_\_。

12 设函数 $f\left( x\right) \left( {x \in \mathbf{R}}\right)$ 满足 $f\left( {-x}\right) = f\left( x\right) , f\left( x\right) = f\left( {2 - x}\right)$ ，且当 $x \in \left\lbrack {0,1}\right\rbrack$ 时 $f\left( x\right) = {x}^{3}$ ，又函数 $g\left( x\right) = \left| {x\cos \left( {\pi x}\right) }\right|$ ,则函数 $h\left( x\right) = g\left( x\right) - f\left( x\right)$ 在 $\left\lbrack {-\frac{1}{2},\frac{3}{2}}\right\rbrack$ 上的零点个数为\_\_\_.

# 第四讲平面向量基础要点

## 一、基本概念回顾

1. 下列命题中，正确的是 ( )

::: choices
- A. $\left| \overrightarrow{a}\right| = \left| \overrightarrow{b}\right| \Rightarrow \overrightarrow{a} = \overrightarrow{b}$
- B. $\left| \overrightarrow{a}\right| > \left| \overrightarrow{b}\right| \Rightarrow \overrightarrow{a} > \overrightarrow{b}$
- C. $\left| \overrightarrow{a}\right| = \left| \overrightarrow{b}\right| \Rightarrow \overrightarrow{a}$ 与 $\overrightarrow{b}$ 共线
- D. $\left| \overrightarrow{a}\right| = 0 \Rightarrow \overrightarrow{a} = 0$
:::


2. 在下列说法中，正确的是( )

::: choices
- A. 两个有公共起点且共线的向量，其终点必相同;
- B. 模为 0 的向量与任一非零向量平行;
- C. 向量就是有向线段;
- D. 若 $\left| \overrightarrow{a}\right| = \left| \overrightarrow{b}\right|$ ，则 $\overrightarrow{a} = \overrightarrow{b}$
:::


3. 下列命题中正确的是 1 \_\_\_:① 向量 $\overrightarrow{AB}$ 的长度与向量 $\overrightarrow{BA}$ 的长度相等；② 两个非零向量 $\mathbf{a}$ 与 $\mathbf{b}$ 平行，则 $\mathbf{a}$ 与 $\mathbf{b}$ 的方向相同或相反；③ 两个有公共终点的向量一定是共线向量；④ 共线向量是可以移动到同一条直线上的向量；⑤ 平行向量就是向量所在直线平行

4. 下列命题中正确的是\_\_\_:① ${\left( \overrightarrow{a} \cdot \overrightarrow{b}\right) }^{2} = {\overrightarrow{a}}^{2} \cdot {\overrightarrow{b}}^{2}$ ；② 若 $\overrightarrow{a},\overrightarrow{b},\overrightarrow{c}$ 为非零向量，且 $\overrightarrow{a} \cdot \overrightarrow{b} = \overrightarrow{a} \cdot \overrightarrow{c}$ ，则 $\overrightarrow{b} = \overrightarrow{c}$ ； ③ 若 $\overrightarrow{a}//\overrightarrow{b},\overrightarrow{b}//\overrightarrow{c}$ ，则 $\overrightarrow{a}//\overrightarrow{c}$ ；④ $\overrightarrow{0} \cdot \overrightarrow{0} = \overrightarrow{0},0 \cdot \overrightarrow{a} = 0$ ；⑤ 若 ${\overrightarrow{a}}^{2} + {\overrightarrow{b}}^{2} = 0$ ，则 $\overrightarrow{a} = \overrightarrow{b} = \overrightarrow{0}$ 。

5. 下列命题中

① $\overrightarrow{a} \cdot \left( {\overrightarrow{b} - \overrightarrow{c}}\right) = \overrightarrow{a} \cdot \overrightarrow{b} - \overrightarrow{a} \cdot \overrightarrow{c}$ ② $\overrightarrow{a} \cdot \left( {\overrightarrow{b} \cdot \overrightarrow{c}}\right) = \left( {\overrightarrow{a} \cdot \overrightarrow{b}}\right) \cdot \overrightarrow{c}$ ③ ${\left( \overrightarrow{a} - \overrightarrow{b}\right) }^{2} = {\left| \overrightarrow{a}\right| }^{2} - 2\left| \overrightarrow{a}\right| \cdot \left| \overrightarrow{b}\right| + {\left| \overrightarrow{b}\right| }^{2}$

④ 若 $\overrightarrow{a} \cdot \overrightarrow{b} = 0$ ，则 $\overrightarrow{a} = \overrightarrow{0}$ 或 $\overrightarrow{b} = \overrightarrow{0}$ ⑤ 若 $\overrightarrow{a} \cdot \overrightarrow{b} = \overrightarrow{c} \cdot \overrightarrow{b}$ ,则 $\overrightarrow{a} = \overrightarrow{c}$ ⑥ ${\left| \overrightarrow{a}\right| }^{2} = {\overrightarrow{a}}^{2}$

⑦ $\frac{\overrightarrow{a} \cdot \overrightarrow{b}}{{a}^{2}} = \frac{\overrightarrow{b}}{a}$ ⑧ ${\left( \overrightarrow{a} \cdot \overrightarrow{b}\right) }^{2} = {\overrightarrow{a}}^{2} \cdot {\overrightarrow{b}}^{2}$ ⑨ ${\left( \overrightarrow{a} - \overrightarrow{b}\right) }^{2} = {\overrightarrow{a}}^{2} - 2\overrightarrow{a} \cdot \overrightarrow{b} + {\overrightarrow{b}}^{2}$

其中正确的命题是\_\_\_

6. 给出下列命题: ① 若 $\lambda \overrightarrow{a} = \lambda \overrightarrow{b}\left( {\lambda \neq 0}\right)$ ，则 $\overrightarrow{a} = \overrightarrow{b}$ ；② $\overrightarrow{a} \cdot \overrightarrow{c} = \overrightarrow{b} \cdot \overrightarrow{c}\left( {\overrightarrow{c} \neq \overrightarrow{0}}\right)$ ，则 $\overrightarrow{a} = \overrightarrow{b}$ ；③ 若 $\overrightarrow{a} \cdot \overrightarrow{b} = - \left| \overrightarrow{a}\right| \times \left| \overrightarrow{b}\right| \neq 0$ ， 那么 $\overrightarrow{a},\overrightarrow{b}$ 方向相反; (e)如果 $\overrightarrow{a} \cdot \overrightarrow{b} < 0$ ,那么 $\overrightarrow{a},\overrightarrow{b}$ 的夹角为钝角; ⑤ $\left( {\overrightarrow{b} \cdot \overrightarrow{c}}\right) \overrightarrow{a} - \left( {\overrightarrow{c} \cdot \overrightarrow{a}}\right) \overrightarrow{b}$ 垂直于 $\overrightarrow{c}$ 。其中假命题的序号是\_\_\_。

## 二、坐标表达
位置向量与向量的坐标:在一个平面直角坐标系内，我们将向量 $\overrightarrow{a}$ 平移，使其起点与原点 $O$ 重合，设此时终点为 $A$ ,则称 $\overrightarrow{OA}$ 为 $\overrightarrow{a}$ 在该坐标系下的位置向量,将 $A$ 点的坐标 $\left( {x, y}\right)$ 称为向量 $\overrightarrow{a}$ 的坐标。

两个向量 $\overrightarrow{a}$ 、 $\overrightarrow{b}$ 在平面直角坐标系下的坐标分别为 $\left( {{x}_{1},{y}_{1}}\right)$ 和 $\left( {{x}_{2},{y}_{2}}\right)$ ，它们具有以下性质:

(1) $\overrightarrow{a} + \overrightarrow{b}$ 的坐标为 $\left( {{x}_{1} + {x}_{2},{y}_{1} + {y}_{2}}\right)$ ， $\overrightarrow{a} - \overrightarrow{b}$ 的坐标为 $\left( {{x}_{1} - {x}_{2},{y}_{1} - {y}_{2}}\right)$

(2) $\lambda \overrightarrow{a}$ 的坐标为 $\left( {\lambda {x}_{1},\lambda {y}_{1}}\right)$ ，其中 $\lambda \in R$

(3) $\left| \overrightarrow{a}\right| = \sqrt{{x}_{1}^{2} + {y}_{1}^{2}}$

(4) $\overrightarrow{a} \cdot \overrightarrow{b} = {x}_{1}{x}_{2} + {y}_{1}{y}_{2}$

这意味着, 平面向量的所有运算都可以转化为坐标表达来获得结果。

除向量间的运算外, 向量的坐标还可以用于判定向量间的位置关系:

(5) $\overrightarrow{a}\text{ 、 }\overrightarrow{b}$ 共线的充要条件为: ${x}_{1}{y}_{2} - {x}_{2}{y}_{1} = 0$ ;

(6) $\overrightarrow{a}$ 、 $\overrightarrow{b}$ 垂直的充要条件为: ${x}_{1}{x}_{2} + {y}_{1}{y}_{2} = 0$ ；

(7)若 $\overrightarrow{a}$ 、 $\overrightarrow{b}$ 为非零向量，则 $\cos \langle \overrightarrow{a},\overrightarrow{b}\rangle = \frac{{x}_{1}{x}_{2} + {y}_{1}{y}_{2}}{\sqrt{{x}_{1}^{2} + {y}_{1}^{2}}\sqrt{{x}_{2}^{2} + {y}_{2}^{2}}}$

1. 已知向量 $\overrightarrow{a} = \left( {\sin \theta ,\cos \theta - 2\sin \theta }\right) ,\overrightarrow{b} = \left( {1,2}\right)$

(1)若 $\overrightarrow{a}$ 、 $\overrightarrow{b}$ 共线，求 $\tan \theta$ 的值；(2)若 $\left| \overrightarrow{a}\right| = \left| \overrightarrow{b}\right| ,0 < \theta < \pi$ ，求 $\theta$ 的值；(3)在(2)成立的前提下，求向量 $\overrightarrow{a}$ 和 $\overrightarrow{b}$ 的夹角

2. 已知向量 $\overrightarrow{a} = \left( {1,2}\right) ,\overrightarrow{b} = \left( {\cos \alpha ,\sin \alpha }\right)$ ，设 $\overrightarrow{m} = \overrightarrow{a} + t\overrightarrow{b}\left( {t \in R}\right)$ 。

(1)若 $\alpha = \frac{\pi }{4}$ ，求当 $\left| \overrightarrow{m}\right|$ 取最小值时实数 $t$ 的值；

(2)若 $\overrightarrow{a}\bot \overrightarrow{b}$ ，是否存在实数 $t$ ，使得向量 $\overrightarrow{a} - \overrightarrow{b}$ 和向量 $m$ 的夹角为 $\frac{\pi }{4}$ ？说明理由。

3. 已知 $A\text{ 、 }B\text{ 、 }C$ 是单位圆上三个互不相同的点，若 $\left| \overrightarrow{AB}\right| = \left| \overrightarrow{AC}\right|$ ，则 $\overrightarrow{AB} \cdot \overrightarrow{AC}$ 的最小值是\_\_\_.

![](images/bo_d68j3a77aajc739aivpg_35_467_1424_197_226_0.jpg)

![](images/bo_d68j3a77aajc739aivpg_35_845_1412_280_259_0.jpg)

4. 在四边形 ${ABCD}$ 中，已知 $\bigtriangleup {ABC}$ 的面积是 $\bigtriangleup {ACD}$ 面积的 3 倍，若存在正实数 $x$ 、 $y$ 使得 $\overrightarrow{AC} = \left( {\frac{1}{x} - 3}\right) \overrightarrow{AB} + \left( {1 - \frac{1}{y}}\right) \overrightarrow{AD}$ 成立，则 $x + y$ 的最小值为\_\_\_

## 三、几何转化

$>$ 和差归一

7. 在 $\bigtriangleup {ABC}$ 中， $O$ 为中线 ${AM}$ 上一个动点，若 ${AM} = 2$ ，则 $\overrightarrow{OA} \cdot \left( {\overrightarrow{OB} + \overrightarrow{OC}}\right)$ 的最小值是\_\_\_。

8. 已知向量 $\overrightarrow{a} = \left( {\cos \alpha ,\sin \alpha }\right) ,\overrightarrow{b} = \left( {\cos \beta ,\sin \beta }\right)$ ，且 $\alpha - \beta = \frac{\pi }{3}$ ，若向量 $\overrightarrow{c}$ 满足 $\left| {\overrightarrow{c} - \overrightarrow{a} - \overrightarrow{b}}\right| = 1$ ，则 $\left| \overrightarrow{c}\right|$ 的大值为\_\_\_

9. $\bigtriangleup {ABC}$ 所在平面上一点 $\mathbf{P}$ 满足 $\overrightarrow{PA} + \overrightarrow{PC} = m\overrightarrow{AB}\;\left( {m > 0, m\text{ 为常数 }}\right)$ ,若 $\bigtriangleup {ABP}$ 的面积为 6,则 $\bigtriangleup {ABC}$ 的面积为\_\_\_。

10. 已知平面向量 $\overrightarrow{a}$ 、 $\overrightarrow{b}\left( {\overrightarrow{a} \neq \overrightarrow{0},\overrightarrow{a} \neq \overrightarrow{b}}\right)$ 满足 $\left| \overrightarrow{b}\right| = 1$ ，若 $\overrightarrow{a}$ 与 $\overrightarrow{b} - \overrightarrow{a}$ . 的夹角为 ${120}^{ \circ }$ ，则 $\left| \overrightarrow{a}\right|$ 的取值范围是\_\_\_.

![](images/bo_d68j3a77aajc739aivpg_37_313_737_228_202_0.jpg)

11. 已知 $\overrightarrow{a}$ 、 $\overrightarrow{b}$ 、 $\overrightarrow{c}$ 均为单位向量， $\overrightarrow{a} \cdot \overrightarrow{b} = 0$ ， $\left( {\overrightarrow{a} - \overrightarrow{c}}\right) \cdot \left( {\overrightarrow{b} - \overrightarrow{c}}\right) \leq 0$ ，则 $\left| {\overrightarrow{a} + \overrightarrow{b} - \overrightarrow{c}}\right|$ 的取值范围是\_\_\_.

12. 向量 $\overrightarrow{i}\text{ 、 }\overrightarrow{j}$ 是平面直角坐标系 $x$ 轴、 $y$ 轴的基本单位向量，且 $\left| {\overrightarrow{a} - \overrightarrow{i}}\right| + \left| {\overrightarrow{a} - 2\overrightarrow{j}}\right| = \sqrt{5}$ ，则 $\left| {\overrightarrow{a} + 2\overrightarrow{i}}\right|$ 的取值范围为\_\_\_

13. 已知 $\langle \overrightarrow{a},\overrightarrow{b}\rangle \geq \frac{\pi }{3},\left| {\overrightarrow{a} - \overrightarrow{b}}\right| = 5$ ，向量 $\overrightarrow{c} - \overrightarrow{a}$ 与 $\overrightarrow{c} - \overrightarrow{b}$ 的夹角为 $\frac{2\pi }{3}$ ， $\left| {\overrightarrow{c} - \overrightarrow{a}}\right| = 2\sqrt{3}$ ，则 $\overrightarrow{a} \cdot \overrightarrow{c}$ 的最大为\_\_\_.

14. 【2025 上海高考 12】已知函数 $f\left( x\right) = \left\{ \begin{array}{ll} 1, & x > 0 \\ 0, & x = 0 \\ - 1, & x < 0 \end{array}\right.$ ，向量 $\overrightarrow{a}$ 、 $\overrightarrow{b}$ 、 $\overrightarrow{c}$ 是平面内三个不同的单位向量，满足 $f\left( {\overrightarrow{a} \cdot \overrightarrow{b}}\right) + f\left( {\overrightarrow{b} \cdot \overrightarrow{c}}\right) + f\left( {\overrightarrow{c} \cdot \overrightarrow{a}}\right) = 0$ ，则 $\left| {\overrightarrow{a} + \overrightarrow{b} + \overrightarrow{c}}\right|$ 的取值范围为\_\_\_

15. 已知 $\bigtriangleup {ABC}$ 的三个顶点 $A, B, C$ 及所在平面内一点 $P$ 满足 $\overrightarrow{PA} + \overrightarrow{PB} + \overrightarrow{PC} = \overrightarrow{AB}$ ,则 $\bigtriangleup {BCP}$ 的面积 ${S}_{1}$ 与 ${\Delta ABP}$ 的面积 ${S}_{2}$ 之比为 ${S}_{1} : {S}_{2} =$ \_\_\_。

16. 已知正三角形 ${ABC}$ 的边长为 $\sqrt{3}$ ，点 $M$ 是 $\bigtriangleup {ABC}$ 所在平面内的任一动点，若 $\left| \overrightarrow{MA}\right| = 1$ ，则 $\left| {\overrightarrow{MA} + \overrightarrow{MB} + \overrightarrow{MC}}\right|$ 的取值范围为\_\_\_

向量积

17. 在平面直角坐标系中,已知向量 $\overrightarrow{a} = \left( {1,2}\right) , O$ 是坐标原点, $M$ 是曲线 $\left| x\right| + 2\left| y\right| = 2$ 上的动点,则 $\overrightarrow{a} \cdot \overrightarrow{OM}$ 的取值范围为\_\_\_。

18. 已知 $A\text{ 、 }B$ 为平面上的两个定点,且 $\left| \overrightarrow{AB}\right| = 2$ ,该平面上的动线段 $\mathrm{{PQ}}$ 的端点 $\mathrm{P}\text{ 、 }\mathrm{Q}$ 满足 $\left| \overrightarrow{AP}\right| \leq 5$ , $\overrightarrow{AP} \cdot \overrightarrow{AB} = 6$ ， $\overrightarrow{AQ} = - 2\overrightarrow{AP}$ ，则动线段 ${PQ}$ 所形成的图形面积为\_\_\_。

19. 在 $\bigtriangleup {ABC}$ 中， $M$ 是 ${BC}$ 的中点， $\angle A = {120}^{ \circ }$ ， $\overrightarrow{AB} \cdot \overrightarrow{AC} = - \frac{1}{2}$ ，则线段 ${AM}$ 长的最小值为\_\_\_

# 第五讲平面向量综合解法 I

## 一、建系法

1. 【21 宝山二模 12】已知平面向量 $\overrightarrow{a}\text{ 、 }\overrightarrow{b},\overrightarrow{e}$ 满足 $\left| \overrightarrow{e}\right| = 1,\overrightarrow{a} \cdot \overrightarrow{e} = 1,\overrightarrow{b} \cdot \overrightarrow{e} = - 1,\left| {\overrightarrow{a} - \overrightarrow{b}}\right| = 4$ ，则 $\overrightarrow{a} \cdot \overrightarrow{b}$ 的最小值是\_\_\_

2. 已知平面上三个不同的单位向量 $\overrightarrow{a}\text{ 、 }\overrightarrow{b}\text{ 、 }\overrightarrow{c}$ 满足 $\overrightarrow{a} \cdot \overrightarrow{b} = \overrightarrow{b} \cdot \overrightarrow{c} = \frac{1}{2}$ ，若 $\overrightarrow{e}$ 为平面内的任意单位向量，则 $\left| {\overrightarrow{a} \cdot \overrightarrow{e}}\right| + 2\left| {\overrightarrow{b} \cdot \overrightarrow{e}}\right| + 3\left| {\overrightarrow{c} \cdot \overrightarrow{e}}\right|$ 的最大值为\_\_\_

3. 如图，已知 $P$ 是半径为 2，圆心角为 $\frac{\pi }{3}$ 的一段圆弧 ${AB}$ 上的一点，若 $\overrightarrow{AB} = 2\overrightarrow{BC}$ ，则 $\overrightarrow{PC} \cdot \overrightarrow{PA}$ 的值域是\_\_\_

![](images/bo_d68j3a77aajc739aivpg_43_1214_293_335_250_0.jpg)

4. 如图，若同一平面上的四边形 ${PQRS}$ 满足: ${mn}\overrightarrow{RP} = n\left( {1 - {3m}}\right) \overrightarrow{QP} + m\left( {n - 1}\right) \overrightarrow{SP}\left( {m > 0, n > 0}\right)$ ， 则当 $\bigtriangleup {PRS}$ 的面积是 $\bigtriangleup {PQR}$ 的面积的 $\frac{1}{3}$ 倍时， $\frac{1}{m + n}$ 的最大值为\_\_\_

5. 在 $\bigtriangleup {ABC}$ 中, ${AC} = 2,\frac{2}{\tan A} + \frac{1}{\tan B} = 1$ ,若 $\bigtriangleup {ABC}$ 的面积为 2,则 ${AB} =$ \_\_\_

6. 已知点 $D$ 为圆 $O : {x}^{2} + {y}^{2} = 4$ 的弦 ${MN}$ 的中点，点 $A$ 的坐标为 $\left( {1,0}\right)$ ，且 $\overrightarrow{AM} \cdot \overrightarrow{AN} = 1$ ，则 $\overrightarrow{OA} \cdot \overrightarrow{OD}$ 的最大值为\_\_\_

二、几何法

7. 在 $\bigtriangleup {ABC}$ 所在的平面上有三点 $P$ 、 $Q$ 、 $R$ ,满足 $\overrightarrow{PA} + \overrightarrow{PB} + \overrightarrow{PC} = \overrightarrow{AB},\overrightarrow{QA} + \overrightarrow{QB} + \overrightarrow{QC} = \overrightarrow{BC}$ , $\overrightarrow{RA} + \overrightarrow{RB} + \overrightarrow{RC} = \overrightarrow{CA}$ ，则 $\frac{{S}_{\bigtriangleup {PQR}}}{{S}_{\bigtriangleup {ABC}}}$ 的值为\_\_\_

8. 如图，在 $\bigtriangleup {ABC}$ 中， $C = \frac{\pi }{2}$ ， ${AC} = \sqrt{3}$ ， ${BC} = 1$ ，若 $O$ 为 $\bigtriangleup {ABC}$ 内部的点且满足 $\frac{\overrightarrow{OA}}{\left| \overrightarrow{OA}\right| } + \frac{\overrightarrow{OB}}{\left| \overrightarrow{OB}\right| } + \frac{\overrightarrow{OC}}{\left| \overrightarrow{OC}\right| } = \overrightarrow{0}$ ，则 $\left| \overrightarrow{OA}\right| : \left| \overrightarrow{OB}\right| : \left| \overrightarrow{OC}\right| =$

![](images/bo_d68j3a77aajc739aivpg_45_1366_1125_168_211_0.jpg)

9. 已知 $A$ 、 $B$ 、 $C$ 是边长为 1 的正方形边上的任意三点，则 $\overrightarrow{AB} \cdot \overrightarrow{AC}$ 的取值范围为\_\_\_

10. 已知边长为 2 的正方形 ${ABCD}$ 边上有两点 $P\text{ 、 }Q$ ,满足 $\left| {PQ}\right| \geq 1$ ,设 $O$ 是正方形的中心，则 $\overrightarrow{OP} \cdot \overrightarrow{OQ}$ 的取值范围是\_\_\_

11. 设 $P$ 是边长为 $2\sqrt{2}$ 的正六边形 ${A}_{1}{A}_{2}{A}_{3}{A}_{4}{A}_{5}{A}_{6}$ 的边上的任意一点,长度为 4 的线段 ${MN}$ 是该正六边形外接圆的一条动弦， $\overrightarrow{PM} \cdot \overrightarrow{PN}$ 的取值范围为\_\_\_

12. 在 $\bigtriangleup {ABC}$ 中,已知 $\left| \overrightarrow{BC}\right| = 1, B\overrightarrow{A} \cdot \overrightarrow{BC} = 2$ ,点 $P$ 为线段 ${BC}$ 上的动点,动点 $Q$ 满足 $\overrightarrow{PQ} = \overrightarrow{PA} + \overrightarrow{PB} + \overrightarrow{PC}$ ，则 $\overrightarrow{PQ} \cdot \overrightarrow{PB}$ 的最小值为\_\_\_

13. 在平面上, $\overrightarrow{A{B}_{1}} \bot \overrightarrow{A{B}_{2}},\left| \overrightarrow{O{B}_{1}}\right| = \left| \overrightarrow{O{B}_{2}}\right| = 1,\overrightarrow{AP} = \overrightarrow{A{B}_{1}} + \overrightarrow{A{B}_{2}}$ ,若 $\left| \overrightarrow{OP}\right| < \frac{1}{2}$ ,则 $\left| \overrightarrow{OA}\right|$ 的取值范围是 ( )

::: choices
- A. $\left( {0,\frac{\sqrt{5}}{2}}\right\rbrack$
- B. $\left( {\frac{\sqrt{5}}{2},\frac{\sqrt{7}}{2}}\right\rbrack$
- C. $\left( {\frac{\sqrt{5}}{2},\sqrt{2}}\right\rbrack$
- D. $\left( {\frac{\sqrt{7}}{2},\sqrt{2}}\right\rbrack$
:::


14. 已知 $x\text{ 、 }y$ 是正实数， $\bigtriangleup {ABC}$ 的三边长为 ${CA} = 3,{CB} = 4,{AB} = 5$ ，点 $P$ 是边 ${AB}$ ( $P$ 与点 $A\text{ 、 }B$ 不重合) 上任一点，且 $\overrightarrow{CP} = x \cdot \frac{\overrightarrow{CA}}{\left| \overrightarrow{CA}\right| } + y \cdot \frac{\overrightarrow{CB}}{\left| \overrightarrow{CB}\right| }$ ，若不等式 ${2x} + {3y} \geq m \cdot x \cdot y$ 恒成立,则实数 $m$ 的取值范围是( )

::: choices
- A. $m \leq \frac{3}{2} + \sqrt{2}$
- B. $m \leq 2\sqrt{6}$
- C. $m \leq \frac{3}{2}\sqrt{2}$
- D. $m \leq 3$
:::


15. 已知平面上四个点 ${A}_{1}\left( {0,0}\right) \text{ 、 }{A}_{2}\left( {2\sqrt{3},2}\right) \text{ 、 }{A}_{3}\left( {2\sqrt{3} + 4,2}\right) \text{ 、 }{A}_{4}\left( {4,0}\right)$ ,设 $D$ 是四边形 ${A}_{1}{A}_{2}{A}_{3}{A}_{4}$ 极其内部的点构成的点的集合,点 ${P}_{0}$ 是四边形对角线的交点,若集合

$S = \left\{ {P \in D\begin{Vmatrix}{P{P}_{0}}\end{Vmatrix} \leq \left| {P{A}_{j}}\right| , i = 1,2,3,4}\right\}$ ，则集合 $S$ 所表示的平面区域的面积为( )

::: choices
- A. 2
- B. 4
- C. 8
- D. 16
:::


# 第六讲平面向量综合解法 II

## 一、直接计算法
设点 $P$ 是 $\bigtriangleup {ABC}$ 所在平面内一动点，满足 $\overrightarrow{CP} = \lambda \overrightarrow{CA} + \mu \overrightarrow{CB}$ ， ${3\lambda } + {4\mu } = 2\left( {\lambda ,\mu \in \mathbf{R}}\right)$ ， $\left| \overrightarrow{PA}\right| = \left| \overrightarrow{PB}\right| = \left| \overrightarrow{PC}\right|$ ，若 $\left| \overrightarrow{AB}\right| = 3$ ，则 $\bigtriangleup {ABC}$ 面积的最大值是\_\_\_

![](images/bo_d68j3a77aajc739aivpg_50_1116_451_300_267_0.jpg)

2. 如图，已知 ${AC} = 4$ ， $B$ 为 ${AC}$ 的中点，分别以 ${AB}\text{ 、 }{AC}$ 为直径在 ${AC}$ 的同侧作半圆， $M\text{ 、 }N$ 分别为两半圆上的动点(不含端点 $A\text{ 、 }B\text{ 、 }C$ )，且 $\overrightarrow{BM} \cdot \overrightarrow{BN} = 0$ ，则 $\overrightarrow{AM} \cdot \overrightarrow{CN}$ 的最大值为\_\_\_

![](images/bo_d68j3a77aajc739aivpg_51_1259_318_281_171_0.jpg)

3. 已知 $\left| \overrightarrow{OA}\right| = \left| \overrightarrow{OB}\right| = 1$ ,若存在 $m\text{ 、 }n \in \mathbf{R}$ ,使得 $m\overrightarrow{AB} + \overrightarrow{OA}$ 与 $n\overrightarrow{AB} + \overrightarrow{OB}$ 夹角为 ${60}^{ \circ }$ ,且 $\left| {\left( {m\overrightarrow{AB} + \overrightarrow{OA}}\right) - \left( {n\overrightarrow{AB} + \overrightarrow{OB}}\right) }\right| = \frac{1}{2}$ ，则 $\left| \overrightarrow{AB}\right|$ 的最小值为\_\_\_

## 二、斜坐标系法
平面向量基本定理: $\overset{ - }{a}$ 、 $\overline{b}$ 是平面上任意两个不共线的非零向量，对该平面上的任意向量 $\overset{ - }{c}$ ，必定存在唯一的实数对 $\left( {\lambda ,\mu }\right)$ ,使得 $\overset{ - }{c} = \lambda \overset{ - }{a} + \mu \overrightarrow{b}$ 成立,我们称这样的等式为向量 $\overrightarrow{c}$ 的线性展开,称 $\overrightarrow{a}\text{ 、 }\overrightarrow{b}$ 为该线性展开的基底。

$>$ 定比分点定理: 点 $C$ 在线段 ${AB}$ 上 (异于 $A\text{ 、 }B$ ),则向量 $\overrightarrow{OC}$ 在基底 $\overrightarrow{OA}\text{ 、 }\overrightarrow{OB}$ 下的线性展开

$\overrightarrow{OC} = \lambda \overrightarrow{OA} + \mu \overrightarrow{OB}$ 满足 $\lambda + \mu = 1$ ,且 $\lambda = \frac{BC}{AB},\mu = \frac{AC}{AB}$

推论: 若 $\overrightarrow{OC}$ 在基底 $\overrightarrow{OA}\text{ 、 }\overrightarrow{OB}$ 下的展开 $\overrightarrow{OC} = \lambda \overrightarrow{OA} + \mu \overrightarrow{OB}$ 满足 $\lambda + \mu = 1$ ,则 $A\text{ 、 }B\text{ 、 }C$ 三点共线,且

(1) $\lambda > 0,\mu > 0$ 时, $C$ 在线段 ${AB}$ 上

(2) $\lambda > 0,\mu < 0$ 时， $C$ 在射线 ${BA}$ 的延长线上

(3) $\lambda < 0,\mu > 0$ 时， $C$ 在射线 ${AB}$ 的延长线上

4. 已知 $\bigtriangleup {ABC}$ 为等边三角形, ${AB} = 2$ ,设点 $P\text{ 、 }Q$ 满足 $\overrightarrow{AP} = \lambda \overrightarrow{AB},\overrightarrow{AQ} = \left( {1 - \lambda }\right) \overrightarrow{AC},\lambda \in \mathbf{R}$ ,若 $\overrightarrow{BQ} \cdot \overrightarrow{CP} = - \frac{3}{2}$ ，则 $\lambda =$ \_\_\_.

5. 向量集合 $S = \left\{ {\overrightarrow{a} \mid \overrightarrow{a} = \left( {x, y}\right) , x, y \in \mathbf{R}}\right\}$ ，对于任意 $\overrightarrow{\alpha }$ 、 $\overrightarrow{\beta } \in S$ ，以及任意 $\lambda \in \left( {0,1}\right)$ ，都有 $\lambda \overrightarrow{\alpha } + \left( {1 - \lambda }\right) \overrightarrow{\beta } \in S$ ,则称 $S$ 为 “ $C$ 类集”. 现有四个命题:

① 若 $S$ 为 “ $C$ 类集”，则集合 $M = \{ \mu \overrightarrow{a} \mid \overrightarrow{a} \in S,\mu \in \mathbf{R}\}$ 也是 “ $C$ 类集”

② 若 $S\text{ 、 }T$ 都是 “ $C$ 类集”,则集合 $M = \{ \overrightarrow{a} + \overrightarrow{b} \mid \overrightarrow{a} \in S,\overrightarrow{b} \in T\}$ 也是 “ $C$ 类集”:

③ 若 ${A}_{1}\text{ 、 }{A}_{2}$ 都是 “ $C$ 类集”,则 ${A}_{1} \cup {A}_{2}$ 也是 “ $C$ 类集”;

④ 若 ${A}_{1}\text{ 、 }{A}_{2}$ 都是 “ $C$ 类集”,且交集非空,则 ${A}_{1} \cap {A}_{2}$ 也是 “ $C$ 类集”

其中正确的命题有\_\_\_

6. 【2025 上海高考 16】已知数列 $\left\{ {a}_{n}\right\}$ 、 $\left\{ {b}_{n}\right\}$ 、 $\left\{ {c}_{n}\right\}$ ，满足 ${a}_{n} = {10n} - 9,{b}_{n} = {2}^{n}$ ，

${c}_{n} = \lambda {a}_{n} + \left( {1 - \lambda }\right) {b}_{n}$ . 若对任意 $\lambda \in \left\lbrack {0,1}\right\rbrack$ ， ${a}_{n}$ 、 ${b}_{n}$ 、 ${c}_{n}$ 均能作为三角形的三边长，则满足条件的 $n$ 有 ( 1 )

::: choices
- A. 1
- B. 3
- C. 4
- D. 无数
:::

斜坐标系: $\overrightarrow{i}\text{ 、 }\overrightarrow{j}$ 是平面上任意两个不共线的非零向量,对该平面上的任意向量 $\overrightarrow{a}$ ,必定存在唯一的实数对 $\left( {\lambda ,\mu }\right)$ ,使得 $\overrightarrow{a} = \lambda \overrightarrow{i} + \mu \overrightarrow{j}$ 成立。我们称这样的等式为向量 $\overrightarrow{a}$ 的线性展开,称 $\overrightarrow{i}\text{ 、 }\overrightarrow{j}$ 为该线性展开的坐标基底,称实数对 $\left( {\lambda ,\mu }\right)$ 为任意向量 $\overrightarrow{a}$ 在该基底下的坐标。


(1)若 $\overrightarrow{i} \cdot \overrightarrow{j} = 0$ 且 $\left| i\right| = \left| j\right| = 1$ ，称以 $\overrightarrow{i}$ 、 $\overrightarrow{j}$ 为基底的坐标系为 “平面直角坐标系”

(2)若 $\overrightarrow{i}$ 、 $\overrightarrow{j}$ 不满足(1)的条件，则称以 $\overrightarrow{i}$ 、 $\overrightarrow{j}$ 为基底的坐标系为 “斜坐标系”

7. 两个向量 $\overrightarrow{a}$ 、 $\overrightarrow{b}$ 在以 $\overrightarrow{i}$ 、 $\overrightarrow{j}$ 为基底的坐标系下的坐标分别为 $\left( {{x}_{1},{y}_{1}}\right)$ 和 $\left( {{x}_{2},{y}_{2}}\right)$ ，请判断以下结论在斜坐标系下是否仍然成立:

(1) $\overrightarrow{a} + \overrightarrow{b}$ 的坐标为 $\left( {{x}_{1} + {x}_{2},{y}_{1} + {y}_{2}}\right) ,\overrightarrow{a} - \overrightarrow{b}$ 的坐标为 $\left( {{x}_{1} - {x}_{2},{y}_{1} - {y}_{2}}\right)$

(2) $\lambda \overrightarrow{a}$ 的坐标为 $\left( {\lambda {x}_{1},\lambda {y}_{1}}\right)$ ，其中 $\lambda \in R$

(3) $\left| \overrightarrow{a}\right| = \sqrt{{x}_{1}^{2} + {y}_{1}^{2}}$

(4) $\overrightarrow{a} \cdot \overrightarrow{b} = {x}_{1}{x}_{2} + {y}_{1}{y}_{2}$

(5) $\bar{a}$ 、 $\bar{b}$ 共线的充要条件为: $\left| \begin{array}{ll} {x}_{1} & {y}_{1} \\ {x}_{2} & {y}_{2} \end{array}\right| = 0$ ；

(6) $\overrightarrow{a}$ 、 $\overrightarrow{b}$ 垂直的充要条件为: ${x}_{1}{x}_{2} + {y}_{1}{y}_{2} = 0$

(7)若 $\overrightarrow{a}\text{ 、 }\overrightarrow{b}$ 为非零向量，则 $\cos \langle \overrightarrow{a},\overrightarrow{b}\rangle = \frac{{x}_{1}{x}_{2} + {y}_{1}{y}_{2}}{\sqrt{{x}_{1}^{2} + {y}_{1}^{2}}\sqrt{{x}_{2}^{2} + {y}_{2}^{2}}}$

截距式不变性: 向量 $\overrightarrow{OP}$ 在以 $\overrightarrow{i}\text{ 、 }\overrightarrow{j}$ 为基底的坐标系下的坐标为 $\left( {x, y}\right)$ ,若其满足等式 $\frac{x}{m} + \frac{y}{n} = 1$ ,则 $P$ 点在一条定直线 $l$ 上，且 $l$ 与坐标轴分别交于 $\left( {m,0}\right)$ 和 $\left( {0, n}\right)$ 。

8. 已知正六边形 ${ABCDEF}$ (顶点的字母依次按逆时针顺序确定)的边长为 1，点 $P$ 是 $\bigtriangleup {CDE}$ 内(含边界) 的动点，设 $\overline{AP} = x \cdot \overline{AB} + y \cdot \overline{AF}\;\left( {x, y \in R}\right)$ ，则 $x + y$ 的取值范围是\_\_\_.

9. 如图所示，将一圆的八个等分点分成相间的两组，连接每组的四个点得到两个正方形，去掉两个正方形内部的八条线段后可以形成一正八角星，设正八角星的中心为 $O$ ，并且 $\overrightarrow{OA} = \overrightarrow{{e}_{1}},\overrightarrow{OB} = \overrightarrow{{e}_{2}}$ ，若将点 $O$ 到正八角星 16 个顶点的向量都写成 $\lambda \overrightarrow{{e}_{1}} + \mu \overrightarrow{{e}_{2}},\lambda ,\mu \in \mathrm{R}$ 的形式，则 $\lambda + \mu$ 的取值范围为( )

![](images/bo_d68j3a77aajc739aivpg_58_924_359_259_251_0.jpg)

::: choices
- A. $\left\lbrack {-2\sqrt{2},2}\right\rbrack$
- B. $\left\lbrack {-2\sqrt{2},1 + \sqrt{2}}\right\rbrack$
- C. $\left\lbrack {-1 - \sqrt{2},1 + \sqrt{2}}\right\rbrack$
- D. $\left\lbrack {-1 - \sqrt{2},2}\right\rbrack$
:::


10. $B$ 是 ${AC}$ 的中点， $\overrightarrow{BE} = 2\overrightarrow{OB}$ ， $P$ 是平行四边形 BCDE 内(含边界)的一点，且 $\overrightarrow{OP} = x\overrightarrow{OA} + y\overrightarrow{OB}\left( {x, y \in \mathbf{R}}\right)$ ， 有以下结论:

① 当 $x = 0$ 时， $y \in \left\lbrack {2,3}\right\rbrack$ ；

② 当 $P$ 是线段 ${CE}$ 的中点时， $x = - \frac{1}{2}, y = \frac{5}{2}$ ；

③ 若 $x + y = \frac{5}{2}$ ，则在平面直角坐标系中，点 $P$ 轨迹是一条线段；

④ $x - y$ 的最大值为 -1 .

其中正确结论的个数是( )

::: choices
- A. 1 个
- B. 2 个
- C. 3 个
- D. 4 个
:::


11. 在平面直角坐标系中, $O$ 是坐标原点,两定点 $A, B$ 满足 $\left| \overrightarrow{OA}\right| = \left| \overrightarrow{OB}\right| = \overrightarrow{OA} \cdot \overrightarrow{OB} = 2$ ,则点集 $\left\{ {P\left| {\overline{OP} = \lambda \overline{OA} + \mu \overline{OB},}\right| \lambda \left| +\right| \mu \mid \leq 1,\lambda ,\mu \in R}\right\}$ 所表示的区域的面积是\_\_\_。

12. 若点 $\mathrm{P}$ 在 $\bigtriangleup {ABC}$ 的边界和内部运动，且 $\overline{AP} = x\overline{AB} + y\overline{AC}$ ，另有 $a \geq 0, b \geq 0$ ，且恒有 ${ax} + {by} \leq 1$ ，则以 $a, b$ 为坐标的点 $P\left( {a, b}\right)$ 所形成的平面区域的面积为\_\_\_。

13. 已知向量 $\overrightarrow{a}$ 、 $\overrightarrow{b}$ 满足 $\left| \overrightarrow{a}\right| = \frac{8}{\sqrt{15}}$ 、 $\left| \overrightarrow{b}\right| = \frac{4}{\sqrt{15}}$ ，若对任意 $\left( {x, y}\right) \in \left\{ {\left( {x, y}\right) \left| \right| x\overrightarrow{a} + y\overrightarrow{b} \mid = 1,{xy} > 0}\right\}$ ，都有 $\left| {x + y}\right| \leq 1$ 成立,则 $\bar{a} \cdot \bar{b}$ 的最小值为多少?

# 第七讲复数

## 一、复数概念与综合运算

1. 若对一切 $\theta \in R$ ，复数 $z = \left( {a + \cos \theta }\right) + \left( {{2a} - \sin \theta }\right) i$ 的模不超过 2，则实数 $a$ 的取值范围是\_\_\_。

2. 若复数 $\left( {{a}^{2} - {3a} + 2}\right) + \left( {a - 1}\right) i$ 是纯虚数，则实数 $a$ 的值为\_\_\_。

3. 设 ${z}_{1}$ 是复数， ${z}_{2} = {z}_{1} - i\overline{{z}_{1}}$ (其中 $\overline{{z}_{1}}$ 表示 ${z}_{1}$ 的共轭复数)，已知 ${z}_{2}$ 的实部是 -1，则 ${z}_{2}$ 的虚部为\_\_\_。

4. 在下列命题中，正确命题的个数为\_\_\_:① 两个复数不能比较大小；② 若 $\left( {{x}^{2} - 1}\right) + \left( {{x}^{2} + {3x} + 2}\right) \mathrm{i}$ 是纯虚数,则实数 $x = \pm 1;$ ③ $z$ 是虚数的一个充要条件是 $z + \bar{z} \in \mathbf{R}$ ; ④ 若 $a, b$ 是两个相等的实数，则 $\left( {a - b}\right) + \left( {a + b}\right) \mathrm{i}$ 是纯虚数:⑤ $z \in \mathbf{R}$ 的一个充要条件是 $z = \bar{z}$ ; ⑥ $\left| z\right| = 1$ 的充要条件是 $\bar{z} = \frac{1}{z}$ 。

5. 设复数 ${z}_{1} = 2 + i,2{z}_{2} = \frac{{z}_{1} + i}{\left( {{2i} + 1}\right) - {z}_{1}}$ 。若 $\bigtriangleup {ABC}$ 的三内角 $A, B, C$ 依次成等差数列,且 $u = \cos A + {2i}{\cos }^{2}\frac{C}{2}$ , 求 $\left| {u + {z}_{2}}\right|$ 的取值范围。

6. 已知复数 $z = \sqrt{2}\left( {\cos \theta + i\sin \theta }\right)$ 的实部大于零,且 ${z}^{2}$ 的虚部为 2 。设 $z,{z}^{2}, z - {z}^{2}$ 在复平面上的对应点分别是 $A, B, C$ ,求 $\overrightarrow{AB} \cdot \overrightarrow{AC}$ 的值。

## 二、实系数一元二次方程

7. 已知复数 ${z}_{1},{z}_{2}$ 是实系数方程 ${x}^{2} + {mx} + m = 0$ 的两根，且 $\left| {z}_{1}\right| < 2,\left| {z}_{2}\right| < 2$ 。

(1)求实数 $m$ 的取值范围；(2)求 $\left| {z}_{1}\right| + \left| {z}_{2}\right|$ 的取值范围。

8. 设 $\alpha ,\beta$ 是 ${x}^{2} - {2x} + m = 0\left( {m \in R}\right)$ 的两根，求 $f\left( m\right) = \alpha \left| \alpha \right| + \beta \left| \beta \right|$ 及其最值。

9. 设 $a, b \in R$ ，已知 $\alpha ,\beta$ 是关于 $x$ 的实系数方程 ${x}^{2} + {2ax} + b = 0$ 的两个虚根，且 $\left| {\alpha - \beta }\right| = 4$ ， $\frac{\alpha }{\beta } + \frac{\beta }{\alpha } = 1$ ，求实数 $a, b$ 的值。

## 三、复向量

10. 在复平面内,复数 $z = \sin 2 + i\cos 2$ 对应的点位于第\_\_\_象限；

11. 设 ${z}_{1}$ 是已知复数， $z$ 为任意复数且 $\left| z\right| = 1,{2\omega } = z - {z}_{1}$ ，则复数 $\omega$ 对应的点的轨迹是( )

::: choices
- A. 以 ${z}_{1}$ 的对应点为圆心，1 为半径的圆
- B. 以 $- {z}_{1}$ 的对应点为圆心，1 为半径的圆
- C. 以 $\frac{1}{2}{z}_{1}$ 的对应点为圆心, $\frac{1}{2}$ 为半径的圆
- D. 以 $- \frac{1}{2}{z}_{1}$ 的对应点为圆心, $\frac{1}{2}$ 为半径的圆
:::


12. 在复平面上,复数 ${z}_{1}$ 在连结点 $1 + {2i}$ 和 $1 - {2i}$ 的线段上移动,复数 ${z}_{2}$ 在以原点为中心,半径为 1 的圆周上移动，求 ${z}_{1} + {z}_{2}$ 的轨迹所形成的图形的面积。

13. 已知 $\left| {z}_{1}\right| = 1,\left| {z}_{2}\right| = 3$ ，则 ${z}_{1} + {z}_{2}$ 在复平面上的轨迹所形成的图形的面积为\_\_\_

14. 复平面上有曲线 ${C}_{1} : z = \frac{1}{1 + {2ai}}$ ( $a$ 为非负实数) 和直线 ${C}_{2} : \left| {z + 1}\right| = \left| {z - 1 - {2i}}\right|$ 。

(1)判断 ${C}_{1}$ 与 ${C}_{2}$ 的位置关系；(2)求曲线 ${C}_{1}$ 上的点到 ${C}_{2}$ 的距离的最大值。

# 第八讲空间元素的位置关系

## 一、平行关系

### 线线平行
定义:$l,m$ 共面且 $l \cap m = \varnothing$ ，称为 $l//m$

判定方式 1: 先证明 $l$ 与 $m$ 在同一平面，再用平面几何的知识进行判定判定方式 2:公理 4 一平行于同一直线的两条直线平行性质定理: 一切平面几何中平行带来的性质均可继续使用推论: 过直线外一点, 有且仅有一条直线与已知直线平行线面平行定义: $l \cap \alpha = \varnothing$ ，称为 $l//\alpha$

判定定理:若 $l \text{ ⊄ } \alpha ,\exists m \subset \alpha$ 使 $m//l$ ，则 $l//\alpha$

> 性质定理:若 $l//\alpha$ ，且 $l \subset \beta$ ， $\alpha \cap \beta = m$ ，则 $l//m$

推论: 过平面外一点, 有无数条直线与已知平面平行面面平行定义: $\alpha \cap \beta = \varnothing$ ，称为 $\alpha //\beta$

判定定理:已知 $m \subset \alpha , n \subset \alpha$ ，且 $m \cap n \neq \varnothing$ ；若 $m//\beta , n//\beta$ ，则 $\alpha //\beta$

性质定理: 若 $\alpha //\beta , r \cap \alpha = m, r \cap \beta = n$ ,则 $m//n$

推论 1: 垂直于同一直线的两个平面平行推论 2: 两个平面平行, 其中一个平面内的直线必平行于另一个平面推论 3: 一条直线垂直于两个平行平面中的一个平面, 那么它必垂直于另一个平面推论 4: 经过平面外一点只有一个平面与已知平面平行推论 5:过已知平面外一点且平行于该平面的直线，都在过已知点且平行于该平面的平面内。

推论 6:平行于同一平面的两个平面平行

1. 下列说法正确的是\_\_\_.

① 若直线 $l$ 与平面 $\alpha$ 内无数条直线平行，则 $l//\alpha$ .

② 空间四边形 ${ABCD}$ 中， $E$ 、 $F$ 分别为 ${AB}$ 、 ${AD}$ 的中点，则 ${EF}//$ 平面 ${BCD}$ .

③ 若直线 $l$ 不平行于平面 $\alpha$ ，且 $l$ 不在平面 $\alpha$ 内，则 $\alpha$ 内存在唯一的直线与 $l$ 平行.

2. 已知 $l$ 、 $m$ 是两条不重合的直线， $\alpha$ 、 $\beta$ 是两个不重合的平面，则下列命题中正确的是\_\_\_.

③ 若平面 $\alpha //$ 平面 $\beta$ ，直线 $l//\alpha$ ，则 $l//\beta$ . ② 若 $l//m, m \subset \alpha ,$ 则 $l//\alpha$ .

③ 若 l、m $\subseteq \alpha ,$ 1// $\beta , m//\beta$ ，则 $\alpha //\beta$ . ④ 若 l $\bot \alpha , m//\alpha$ ，则 l $\bot m$ .

⑤ 若 l、m 异面，且 l//平面 α，l//平面 β，m//平面 α，m//平面 β，则 α//β.

### 注意: 三类平行关系的核心是寻找线线平行关系

3. 已知有公共边 ${AB}$ 的两个全等矩形 ${ABCD}$ 和 ${ABEF}$ 不在同意平面内， $P$ 、 $Q$ 分别是对角线 ${AE}$ 、 ${BD}$ 上的点，且 ${AP} = {DQ}$ ，求证: ${PQ}//$ 平面 ${CBE}$

4. 如图所示，在正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中， $O$ 为底面 ${ABCD}$ 的中心， $P$ 是 $D{D}_{1}$ 的中点，设 $Q$ 是 $C{C}_{1}$ 上的点,试讨论,当点 $Q$ 在什么位置时,平面 ${D}_{1}{BQ}//$ 平面 ${PAO}$ .

![](images/bo_d68j3a77aajc739aivpg_68_1099_785_374_317_0.jpg)

5. 如图所示，已知 ${AB}$ 与 ${CD}$ 为异面直线， ${CD}$ 在平面 $\alpha$ 内， ${AB}//\alpha$ ， $M$ 、 $N$ 分别是线段 ${AC}$ 、 ${BD}$ 的中点，求证: ${MN}//\alpha$ .

![](images/bo_d68j3a77aajc739aivpg_68_1073_1260_409_263_0.jpg)

6. 在四棱锥 P-ABCD 中，底面 ABCD 为梯形，AD//BC，且 AD-2BC。已知 E 是 PD 中点，求证:CE// 面 PAB

7. 如图， ${\Delta {A}_{1}{B}_{1}{C}_{1}}$ 是由 ${\Delta ABC}$ 沿向量 $\overline{A{A}_{1}}$ 平移得到， $O$ 为 ${AC}$ 中点，在 ${BC}$ 上是否存在一点 $E$ ，使得 ${OE}//$ 平面 ${A}_{1}{AB}$ ? 说明理由。

![](images/bo_d68j3a77aajc739aivpg_69_1052_318_402_301_0.jpg)

## 二、垂直关系

### 线线垂直
定义:$l$ 与 $m$ 夹角为 ${90}^{ \circ }$ 时，称为 $l \bot m$

判定方式 1: 先将 $l$ 与 $m$ 平移至同一平面,再用平面几何的知识进行判定判定方式 2: 证明 $l$ 与 $m$ 所在的某个平面垂直推论: 过空间中任意一点,有无数条直线与已知直线垂直

### 线面垂直
定义:若对 $\forall m \subset \alpha , l \bot m$ ,则称为 $l \bot \alpha$

判定定理: 已知 $m \subset \alpha , n \subset \alpha$ ,且 $m \cap n \neq \varnothing$ ; 若 $l \bot m, l \bot n$ ,则 $l \bot \alpha$

性质定理: 若 ${l}_{1} \bot \alpha ,{l}_{2} \bot \alpha$ ,则 ${l}_{1}//{l}_{2}$

推论 1: 若 ${l}_{1} \bot \alpha ,{l}_{1}//{l}_{2}$ ; 则 ${l}_{2} \bot \alpha$

推论 2: 过一点有且仅有一条直线与已知平面垂直推论 3: 过一点有且仅有一个平面与已知直线垂直

### 面面垂直
定义:若 $\alpha$ 与 $\beta$ 所成二面角为直角，称 $\alpha \bot \beta$

判定定理: 若 $l \bot \alpha$ ,且 $l \subset \beta$ ,则 $\alpha \bot \beta$

性质定理: 已知 $\alpha \bot \beta$ ,且 $l = \alpha \cap \beta$ ,若 $m \subset \alpha$ 且 $m \bot l$ ,则 $m \bot \beta$

8. 下列说法正确的是\_\_\_.

① 若直线 $l\bot$ 平面 $\alpha$ ，直线 $m//\alpha$ ，则直线 $l$ 与 $m$ 垂直.

② 若直线 $l$ 与平面 $\alpha$ 不垂直，则 $l$ 不可能垂直于 $\alpha$ 内无数条直线.

③ 若直线 $l$ 与直线 $m$ 异面，则过 $l$ 且与 $m$ 垂直的平面有且只有一个.

9. 在空间内， $l$ 、 $m$ 、 $n$ 是三条不同的直线， $\alpha$ 、 $\beta$ 、 $\gamma$ 是三个不同的平面，则下列命题正确的是\_\_\_.

① 若 $\alpha \bot \gamma ,\beta \bot \gamma ,\alpha \cap \beta = l$ ，则 $l \bot \gamma .$ ② 若 $l//\alpha$ ， $l//\beta ,\alpha \cap \beta = m$ ，则 $l//m$ .

② $\alpha \cap \beta = l,\beta \cap \gamma = m,\gamma \cap \alpha = n$ ，若 $l//m$ ，则 $l//n$ . ④ 若 $\alpha \bot \gamma ,\beta \bot \gamma$ ，则 $\alpha \bot \beta$ 或 $\alpha //\beta$ .

### 注意: 三类垂直关系的核心是线线-线面垂直关系的互相转化

10. 如图，在长方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中，底面 ${ABCD}$ 是正方形， ${A{A}_{1}} = {2AB} = 4$ ，点 $E$ 在 $C{C}_{1}$ 上且 ${C}_{1}E = {3EC}$ 。证明: ${A}_{1}C \bot$ 平面 ${BED}$ 。

![](images/bo_d68j3a77aajc739aivpg_70_1245_688_242_333_0.jpg)

11. 在正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中， $P$ 为 $D{D}_{1}$ 中点， $O$ 为底面 ${ABCD}$ 的中心，求证: ${B}_{1}O \bot {PA}$ .

![](images/bo_d68j3a77aajc739aivpg_70_1158_1357_324_293_0.jpg)

12. 已知四面体 ${ABCD}$ 的边 ${BC} = {AC}$ ， ${AD} = {BD}$ ，作 ${BE}\bot {CD}$ 于 $E$ ， ${AH}\bot {BE}$ 于 $H$ ，求证: ${AH}\bot$ 平面 ${BCD}$ .

13. 已知矩形 ${ABCD},{AB} = 1,{BC} = \sqrt{2}$ ，将 $\bigtriangleup {ABD}$ 沿矩形的对角线 ${BD}$ 所在的直线进行翻折，在翻折过程中，正确的是 ( )

::: choices
- A. 存在某个位置，使得直线 ${AC}$ 与直线 ${BD}$ 垂直
- B. 存在某个位置，使得直线 ${AB}$ 与直线 ${CD}$ 垂直
- C. 存在某个位置,使得直线 ${AD}$ 与直线 ${BC}$ 垂直
- D. 对任意位置，三对直线 “ ${AC}$ 与 ${BD}$ ”、 “ ${AB}$ 与 ${CD}$ ”、 “ ${AD}$ 与 ${BC}$ ” 均不垂直
:::


14. 下列 5 个正方体图形中, $l$ 是正方体的一条对角线,点 $M, N, P$ 分别为其所在棱的中点,能得出 $l \bot$ 面 ${MNP}$ 的图形的序号是\_\_\_(写出所有符合要求的图形序号)

![](images/bo_d68j3a77aajc739aivpg_72_266_341_194_224_0.jpg)

①

![](images/bo_d68j3a77aajc739aivpg_72_482_355_188_205_0.jpg)

②

![](images/bo_d68j3a77aajc739aivpg_72_675_345_207_218_0.jpg)

③

![](images/bo_d68j3a77aajc739aivpg_72_895_364_222_201_0.jpg)

④

![](images/bo_d68j3a77aajc739aivpg_72_1123_366_213_203_0.jpg)

⑤

15. 在矩形 ${ABCD}$ 中，已知 ${AB} = {2AD}$ ，且为 ${AB}$ 中点，将 $\bigtriangleup {ADE}$ 沿 ${DE}$ 折起，翻折后 ${A}^{\prime }B = {A}^{\prime }C$ ， 求证: 平面 ${A}^{\prime }{DE} \bot$ 平面 ${BCDE}$ .

![](images/bo_d68j3a77aajc739aivpg_72_1132_1395_411_338_0.jpg)

16. 如图所示，在正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中，已知 $P$ 、 $Q$ 、 $R$ 、 $S$ 分别为棱 ${A}_{1}{D}_{1}$ 、 ${A}_{1}{B}_{1}$ 、 ${AB}$ 、 $B{B}_{1}$ 的中点,求证: 平面 ${PQS} \bot$ 平面 ${B}_{1}{RC}$

![](images/bo_d68j3a77aajc739aivpg_73_1038_328_383_335_0.jpg)

# 第九讲空间元素的夹角

## 一、线线夹角

17. 异面直线 $a, b$ 所成的角为锐角 $\theta , M, N \in a,{M}_{1},{N}_{1} \in b, M{M}_{1} \bot b, N{N}_{1} \bot b$ ,若 ${MN} = m$ ,则 ${M}_{1}{N}_{1} =$ \_\_\_(用 $m,\theta$ 表示)。

18. 在空间四边形 ${ABCD}$ 中,

(1) 若 ${AB} = {BC} = {CD} = {DA} = {BD} = {AC} = a, M, N$ 分别是 ${BC},{AD}$ 的中点，求异面直线 ${AM},{CN}$ 所成的角:

(2) $E$ 是 ${AC}$ 中点， ${AF}$ 是 ${BD}$ 上的高， ${BD} - {BE} = {CF} = 1,{AB} = {AD} = \frac{3}{2}$ 。求异面直线 ${BE},{CF}$ 所成的角。

![](images/bo_d68j3a77aajc739aivpg_74_1051_1734_423_399_0.jpg)

## 二、二面角与线面角

### 二面角找平面角类型总结

1. 如图，四边形 ${ABCD}$ 是正方形， ${PD} \bot$ 面 ${ABCD}$ ， ${PD} \simeq {DC}$ ， $E$ 是 ${PC}$ 的中点，作 ${EF} \bot {PB}$ 于点 $F$ 。求下列二面角的大小:

(1) $C - {PB} - A$ ；(2) $C - {PB} - D$ ；(3)面 ${BPC}$ 与面 ${APD}$ 所成的锐二面角；

(4) $E - {BD} - C$ ；(5) $P - {DE} - F$ ；

![](images/bo_d68j3a77aajc739aivpg_76_1147_476_337_349_0.jpg)

![](images/bo_d68j3a77aajc739aivpg_76_1147_872_341_353_0.jpg)

![](images/bo_d68j3a77aajc739aivpg_76_1152_1277_337_349_0.jpg)

![](images/bo_d68j3a77aajc739aivpg_76_1155_1672_334_360_0.jpg)

2. 如图的几何体中， $\Delta {A}_{1}{B}_{1}{C}_{1}$ 是正三角形，三条线段 $A{A}_{1}, B{B}_{1}, C{C}_{1}$ 都垂直于平面 ${A}_{1}{B}_{1}{C}_{1}$ ，且 $A{A}_{1} = B{B}_{1} = C{C}_{1} = {A}_{1}{B}_{1}$ 。若 $E$ 为 $B{B}_{1}$ 的中点，求面 ${A}_{1}{EC}$ 与面 ${A}_{1}{B}_{1}{C}_{1}$ 所成二面角。

![](images/bo_d68j3a77aajc739aivpg_77_1168_371_373_362_0.jpg)

3. 正方体 ${ABCD} - {A}^{\prime }{B}^{\prime }{C}^{\prime }{D}^{\prime }$ 中， $E$ 是 ${BC}$ 的中点， $F$ 在 $A{A}^{\prime }$ 上，且 $\frac{{A}_{1}F}{FA} = \frac{1}{2}$ ，求面 ${B}_{1}{EF}$ 与面 ${ABCD}$ 所成锐二面角的大小。

![](images/bo_d68j3a77aajc739aivpg_77_1106_1343_405_371_0.jpg)

4. 如图， $\bigtriangleup {ABC}$ 是以点 $C$ 为直角顶点的等腰直角三角形，线段 $A{A}_{1}$ ， $B{B}_{1}$ ， $C{C}_{1}$ 垂直于平面 ${ABC}$ ，且 ${AC} = {BC} = \sqrt{3}, A{A}_{1} = B{B}_{1} = C{C}_{1} = 1$ 。问:在 ${A}_{1}{B}_{1}$ 边上是否存在一点 $Q$ ，使得平面 ${QBC}$ 与平面 ${A}_{1}{BC}$ 所成的角为 ${30}^{ \circ }$ ? 说明理由。

![](images/bo_d68j3a77aajc739aivpg_78_1087_417_402_276_0.jpg)

5. 如图， ${PB} \bot$ 面 ${ABCD}$ ， ${CD} \bot {PD}$ 。底面 ${ABCD}$ 为直角梯形， ${AD}//{BC}$ ， ${AB} \bot {BC}$ ， ${AB} = {AD} = {PB} = 3$ 。点 $E$ 在棱 ${PA}$ 上，且 ${PE} = {2EA}$ 。求二面角 $A - {BE} - D$ 的大小。

![](images/bo_d68j3a77aajc739aivpg_78_1141_1437_360_433_0.jpg)

6. 已知点 $O$ 是边长为 4 的正方形 ${ABCD}$ 的中心，点 $E$ ， $F$ 分别是 ${AD},{BC}$ 的中点，沿对角线 ${AC}$ 把正方形 ${ABCD}$ 折成直二面角 $D - {AC} - B$ 。求二面角 $E - {OF} - A$ 的大小；

![](images/bo_d68j3a77aajc739aivpg_79_986_391_239_233_0.jpg)

![](images/bo_d68j3a77aajc739aivpg_79_1231_392_312_226_0.jpg)

7. 在正 $\bigtriangleup {ABC}$ 中， $E$ ， $F$ ， $P$ 分别是 ${AB}$ ， ${AC}$ ， ${BC}$ 边上的点，满足 $\frac{AE}{EB} = \frac{CF}{FA} = \frac{CP}{PB} = \frac{1}{2}$ (如图 1)。将 $\bigtriangleup {AEF}$ 沿 ${EF}$ 折起到 $\Delta {A}_{1}{EF}$ 的位置，使二面角 ${A}_{1} - {EF} - B$ 成直二面角，连结 ${A}_{1}B,{A}_{1}P$ (如图 2)。

(1)求证: ${A}_{1}E \bot$ 平面 ${BEP}$ ；(2)求直线 ${A}_{1}E$ 与平面 ${A}_{1}{BP}$ 所成角的大小；

(3)求二面角 $B - {A}_{1}P - F$ 的大小。

![](images/bo_d68j3a77aajc739aivpg_80_698_539_281_303_0.jpg)

图 1

![](images/bo_d68j3a77aajc739aivpg_80_1004_643_136_165_0.jpg)

![](images/bo_d68j3a77aajc739aivpg_80_1158_557_296_256_0.jpg)

图 2

8. 如图，已知四棱柱 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中， ${A}_{1}D\bot$ 底面 ${ABCD}$ ，底面 ${ABCD}$ 是边长为 1 的正方形，侧棱 $\mathcal{A}{A}_{1} = 2$ 。

(1)求证: ${C}_{1}D//$ 平面 ${AB}{B}_{1}{A}_{1}$ ； (2)求直线 $B{D}_{1}$ 与平面 ${A}_{1}{C}_{1}D$ 所成角的正弦值；

(2)求二面角 $D - {A}_{1}{C}_{1} - A$ 的余弦值。

![](images/bo_d68j3a77aajc739aivpg_81_1128_515_428_268_0.jpg)

# 第十讲空间几何体

## 一、动点轨迹

1. 如图，在棱长为 2 的正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中，点 $P$ 是平面 ${AC}{C}_{1}{A}_{1}$ 上一动点，且满足 $\overrightarrow{{D}_{1}P} \cdot \overrightarrow{CP} = 0$ ，则满足条件的所有点 $P$ 所围成的平面区域的面积是\_\_\_

![](images/bo_d68j3a77aajc739aivpg_82_1186_879_266_242_0.jpg)

2. 如图，正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 的棱长为 4， $M$ 为底面 ${ABCD}$ 两条对角线的交点， $P$ 为平面 ${BC}{C}_{1}{B}_{1}$ 内的动点,设直线 ${PM}$ 与平面 ${BC}{C}_{1}{B}_{1}$ 所成的角为 $\alpha$ ,直线 ${PD}$ 与平面 ${BC}{C}_{1}{B}_{1}$ 所成的角为 $\beta$ ,若 $\alpha = \beta$ ，则动点 $P$ 的轨迹长度为\_\_\_

![](images/bo_d68j3a77aajc739aivpg_82_1095_1658_352_332_0.jpg)

3. 如图，在长方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中， ${AB} = {BC} = 4,\;{A{A}_{1}} = 3,$ ， $M$ 为 ${AD}$ 中点， $P$ 为矩形 $C{C}_{1}{D}_{1}D$ 内的动点(包括边界)，且 $\angle {MPD} = \angle {BPC}$ ，则点 $P$ 的轨迹长度为\_\_\_.

![](images/bo_d68j3a77aajc739aivpg_83_1220_336_348_276_0.jpg)

4. 已知正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 的棱长为 2,点 $M, N$ 分别是棱 ${BC},{GD}$ 的中点，点 $P$ 在底面 ${ABCD}$ 内，点 $Q$ 在线段 ${AN}$ 上，若 ${PM} = 5$ ，则 ${PQ}$ 长度的最小值为\_\_\_

![](images/bo_d68j3a77aajc739aivpg_83_1251_1267_292_265_0.jpg)

5. 已知 $E$ 为四面体 $P - {ABC}$ 的侧面 ${PBC}$ 内的一个动点，且点 $E$ 到顶点 $P$ 的距离等于点 $E$ 到底面 ${ABC}$ 的距离，则动点 $E$ 的轨迹是某曲线的一部分，则该曲线一定为( )

::: choices
- A. 圆或椭圆
- B. 椭圆或双曲线
- C. 双曲线或抛物线
- D. 抛物线或椭圆
:::


![](images/bo_d68j3a77aajc739aivpg_84_1243_439_296_343_0.jpg)

6. 已知正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 的棱长为 3、 ${E}_{1}$ 、 ${E}_{2}$ 、 $\cdots$ 、 ${E}_{k}$ 为正方形 ${ABCD}$ 边上的 $K$ 个两两不同的点. 若对任意的点 ${E}_{i}$ ，存在点 ${E}_{j}\left( {i\text{ 、 }j \in \{ 1,2,\cdots , k\} \text{ ， }i \neq j}\right)$ . 使得直线 ${A}_{1}A$ 与平面 ${A}_{1}{E}_{i}{E}_{j}$ 以及平面 ${C}_{1}{E}_{i}{E}_{j}$ 所成角大小均为 $\frac{\pi }{6}$ ，则正整数 $k$ 的最大值为\_\_\_

7. 一个半径为 1 的小球在一个棱长为 $4\sqrt{6}$ 的正四面体容器内可向各个方向自由运动，则该小球永远不可能接触到的容器内壁的面积是\_\_\_

## 二、外接球

8. 已知三棱锥 $P - {ABC}$ 的侧棱两两相互垂直，且该三棱锥的外接球的体积为 ${36\pi }$ ，则该三棱锥的侧面积的最大值为\_\_\_

9. $\bigtriangleup {ABC}$ 是边长为 $2\sqrt{3}$ 的等边三角形， $E$ ， $F$ 分别为 ${AB}$ ， ${AC}$ 的中点，沿 ${EF}$ 把 ${OAEF}$ 折起，使点 $A$ 翻折到点 $P$ 的位置,连接 ${PB}\text{ 、 }{PC}$ ,当四棱锥 $P - {BCFE}$ 的外接球的表面积最小时,四棱锥 $P - {BCFE}$ 的体积为\_\_\_

10. 如图，直四棱柱 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中，底面 ${ABCD}$ 为平行四边形， ${AB} = 1,{AD} = 2,$ ， ${A{A}_{1}} = 2, \; \angle {BAD} = {60}^{ \circ }$ ，点 $P$ 是半圆弧 ${A}_{1}{D}_{1}$ 上的动点(不包括端点)，点 $Q$ 是半圆弧 ${BC}$ 上的动点(不包括端点),若三棱锥 $P - {BCQ}$ 的外接球表面积为 $S$ ，则 $S$ 的取值范围是\_\_\_

![](images/bo_d68j3a77aajc739aivpg_87_1156_436_325_319_0.jpg)

## 三、动线段和

11. 如图所示，长方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中， ${AB} = {AD} = 1$ ， $A{A}_{1} = \sqrt{2}$ ，面对角线 ${B}_{1}{D}_{1}$ 上存在一点 $P$ 使得 ${A}_{1}P + {PB}$ 最短，则 ${A}_{1}P + {PB}$ 的最小值为\_\_\_

![](images/bo_d68j3a77aajc739aivpg_88_1158_400_320_309_0.jpg)

12. 如图，在四棱锥 $P - {ABCD}$ 中，顶点 $P$ 在底面的投影 $O$ 恰为正方形 ${ABCD}$ 的中心且 ${AB} = 2\sqrt{2}$ ，设点 $M, N$ 分别为线段 ${PD},{PO}$ 上的动点，已知当 ${AN} + {MN}$ 取得最小值时，动点 $M$ 恰为 ${PD}$ 的中点， 则该四棱锥的外接球的表面积为\_\_\_

![](images/bo_d68j3a77aajc739aivpg_88_1083_1294_409_332_0.jpg)

13. 如图，在棱长为 2 的正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中，点 $P$ 是该正方体棱上一点，若满足 $\left| {PB}\right| + \left| {P{C}_{1}}\right| = m\left( {m > 0}\right)$ 的点 $P$ 的个数为 4，则 $m$ 的取值范围是\_\_\_

![](images/bo_d68j3a77aajc739aivpg_89_1263_327_293_240_0.jpg)

# 第十一讲直线

## 一、直线基本概念一览

$>$ 倾斜角:将 $x$ 轴正方向单位向量 $\left( {1,0}\right)$ 沿逆时针旋转到与直线 $l$ 共线，所需要转过的角度 $\alpha$ ，称为该直线的倾斜角。

(1)倾斜角的取值范围为 $\lbrack 0,\pi )$

( 2 )倾斜角与直线斜率的关系为: $k = \left\{ \begin{array}{ll} \tan \alpha & ,\alpha \in \left\lbrack {0,\frac{\pi }{2}}\right) \cup \left( {\frac{\pi }{2},\pi }\right) \\ \text{ 不存在 } & ,\alpha = \frac{\pi }{2} \end{array}\right.$

### 直线方程

<table><tr><td></td><td>已知条件</td><td>直线方程</td><td>备注</td></tr><tr><td>点方向式方程</td><td>方向向量 $\overrightarrow{t} = \left( {a, b}\right)$ 直线上一点 $\left( {{x}_{0},{y}_{0}}\right)$</td><td>$- b\left( {x - {x}_{0}}\right) + a\left( {y - {y}_{0}}\right) = 0$</td><td>适用任意直线</td></tr><tr><td>点法向式方程</td><td>法向量 $\overrightarrow{n} = \left( {a, b}\right)$ <br> 直线上一点 $\left( {{x}_{0},{y}_{0}}\right)$</td><td>$a\left( {x - {x}_{0}}\right) + b\left( {y - {y}_{0}}\right) = 0$</td><td>适用任意直线</td></tr><tr><td>截距式方程</td><td>与 $x$ 轴交点 $\left( {a,0}\right)$ <br> 与 $y$ 轴交点 $\left( {0, b}\right)$</td><td>$\frac{x}{a} + \frac{y}{b} = 1$</td><td>直线不能与坐标轴平行直线不能过原点</td></tr><tr><td>点斜式方程 I</td><td>直线斜率 $k$ 直线上一点 $\left( {{x}_{0},{y}_{0}}\right)$</td><td>$y - {y}_{0} = k\left( {x - {x}_{0}}\right)$</td><td>直线不能与 $y$ 轴平行 (即 $k$ 需要存在)</td></tr><tr><td>点斜式方程 II</td><td>直线倒斜率 $t = \frac{1}{k}$ <br> 直线上一点 $\left( {{x}_{0},{y}_{0}}\right)$</td><td>$x - {x}_{0} = t\left( {y - {y}_{0}}\right)$</td><td>直线不能与 $x$ 轴平行 (即 $t = \frac{1}{k}$ 需要存在)</td></tr><tr><td>斜截式方程 I</td><td>直线斜率 $k$ <br> 与 $y$ 轴交点 $\left( {0, m}\right)$</td><td>$y = {kx} + m$</td><td>直线不能与 $y$ 轴平行 (即 $k$ 需要存在)</td></tr><tr><td>斜截式方程 II</td><td>直线倒斜率 $t = \frac{1}{k}$ <br> 与 $x$ 轴交点 $\left( {n,0}\right)$</td><td>$x = {ty} + n$</td><td>直线不能与 $x$ 轴平行 (即 $t = \frac{1}{k}$ 需要存在)</td></tr><tr><td>两点式方程</td><td>直线上一点 $\left( {{x}_{1},{y}_{1}}\right)$ 直线上另一点 $\left( {{x}_{2},{y}_{2}}\right)$</td><td>$\left| \begin{matrix} x & y \\ {x}_{1} - {x}_{2} & {y}_{1} - {y}_{2} \end{matrix}\right| = \left| \begin{array}{ll} {x}_{2} & {y}_{2} \\ {x}_{1} & {y}_{1} \end{array}\right|$</td><td>为一般两点式化简结果尽量不求两点式</td></tr></table>

### 直线距离

(1)点 $\left( {{x}_{0},{y}_{0}}\right)$ 到直线 $l : {ax} + {by} + c = 0$ 的距离: $d = \frac{\left| a{x}_{0} + b{y}_{0} + c\right| }{\sqrt{{a}^{2} + {b}^{2}}}$

(2)直线 ${l}_{1} : {ax} + {by} + {c}_{1} = 0$ 到直线 ${l}_{2} : {ax} + {by} + {c}_{2} = 0$ 的距离: $d = \frac{\left| {c}_{1} - {c}_{2}\right| }{\sqrt{{a}^{2} + {b}^{2}}}$

(3)点 $\left( {{x}_{0},{y}_{0}}\right)$ 到直线 $l : {ax} + {by} + c = 0$ 的有向距离: $\delta = \frac{a{x}_{0} + b{y}_{0} + c}{\sqrt{{a}^{2} + {b}^{2}}}$

(4)两点 $A\left( {{x}_{1},{y}_{1}}\right)$ 和 $B\left( {{x}_{2},{y}_{2}}\right)$ 在直线 $l : {ax} + {by} + c = 0$ 同侧时， ${\delta }_{1}{\delta }_{2} > 0$ ；异侧时， ${\delta }_{1}{\delta }_{2} < 0$

直线夹角:直线 ${l}_{1} : {a}_{1}x + {b}_{1}y + {c}_{1} = 0$ 与直线 ${l}_{2} : {a}_{2}x + {b}_{2}y + {c}_{2} = 0$ 的夹角 $\theta$ 可以利用两直线的方向向量 $\overrightarrow{{n}_{1}} = \left( {{a}_{1},{b}_{1}}\right)$ 和 $\overrightarrow{{n}_{2}} = \left( {{a}_{2},{b}_{2}}\right)$ 求解 (类似空间向量):

$$
\cos \theta  = \frac{\left| \overrightarrow{{n}_{1}} \cdot  \overrightarrow{{n}_{2}}\right| }{\left| \overrightarrow{{n}_{1}}\right| \left| \overrightarrow{{n}_{2}}\right| } = \frac{\left| {a}_{1}{a}_{2} + {b}_{1}{b}_{2}\right| }{\sqrt{{a}_{1}^{2} + {b}_{1}^{2}}\sqrt{{a}_{2}^{2} + {b}_{2}^{2}}}
$$

点关于直线对称: 两点 $A\left( {{x}_{1},{y}_{1}}\right)$ 和 $B\left( {{x}_{2},{y}_{2}}\right)$ 关于直线 $l : {ax} + {by} + c = 0$ 对称的等价条件为:

$$
\left\{  {\begin{array}{l} {AB} \bot l \\ {AB}\text{ 中点 } \in l\end{array} \Rightarrow  \left\{  \begin{array}{l} a\left( {{y}_{1} - {y}_{2}}\right) - b\left( {{x}_{1} - {x}_{2}}\right) = 0 \\ a\left( {{x}_{1} + {x}_{2}}\right) + b\left( {{y}_{1} + {y}_{2}}\right) = - {2c}\end{array}\right. }\right.
$$

含参直线系: 两直线 ${l}_{1} : {a}_{1}x + {b}_{1}y + {c}_{1} = 0,{l}_{2} : {a}_{2}x + {b}_{2}y + {c}_{2} = 0$ ; 则 $l : {a}_{1}x + {b}_{1}y + {c}_{1} + \lambda \left( {{a}_{2}x + {b}_{2}y + {c}_{2}}\right) = 0$ (其中 $\lambda$ 为任意实数) 表示一簇直线系,满足:

(1)若 ${l}_{1} \cap {l}_{2} = P$ ，则 $l$ 为除 ${l}_{2}$ 外的过 $P$ 点直线；

(2)若 ${l}_{1} \cap {l}_{2} = \varnothing$ ，则 $l$ 为除 ${l}_{2}$ 外与 ${l}_{1},{l}_{2}$ 平行的直线；

直线同构: 若两直线 ${l}_{1} : {a}_{1}x + {b}_{1}y + c = 0,{l}_{2} : {a}_{2}x + {b}_{2}y + c = 0$ 交于点 $P\left( {{x}_{0},{y}_{0}}\right)$ ,则过点 $\left( {{a}_{1},{b}_{1}}\right)$ 和 $\left( {{a}_{2},{b}_{2}}\right)$ 的直线为 ${x}_{0}x + {y}_{0}y + c = 0$

## 二、直线相关问题

1. 已知直线 $l$ 的方程为 $\left( {a - 2}\right) x + \left( {a + 1}\right) y - {3a} = 0\left( {x \in \mathbf{R}}\right)$ ,则点 $P\left( {4,5}\right)$ 到直线 $l$ 的距离 $d$ 的取值范围是\_\_\_.

2. 设 $a \in R, k \in R$ ,三条直线 ${l}_{1} : {ax} - y - {2a} + 5 = 0,{l}_{2} : x + {ay} - {3a} - 4 = 0,{l}_{3} : y = {kx}$ ,则 ${l}_{1}$ 与 ${l}_{2}$ 的交点 $M$ 到 ${l}_{3}$ 的距离的最大值为\_\_\_。

3. 在平面直角坐标系 ${xOy}$ 中,若动点 $P\left( {a, b}\right)$ 到两直线 ${l}_{1} : y = x$ 和 ${l}_{2} : y = - x + 2$ 的距离之和为 $2\sqrt{2}$ ,则 ${a}^{2} + {b}^{2}$ 的最大值为\_\_\_。

4. 在平面直角坐标系 ${xOy}$ 中,定义 $A\left( {{x}_{1},{y}_{1}}\right) , B\left( {{x}_{2},{y}_{2}}\right)$ 两点的折线距离 $d\left( {A, B}\right) = \left| {{x}_{1} - {x}_{2}}\right| + \left| {{y}_{1} - {y}_{2}}\right|$ ,设点 $P\left( {{m}^{2},{n}^{2}}\right) , Q\left( {m, n}\right) , O\left( {0,0}\right) , C\left( {2,0}\right) \left( {m, n \in R}\right)$ ,若 $d\left( {P, O}\right) = 1$ ,则 $d\left( {Q, C}\right)$ 的取值范围为\_\_\_。

5. 对于平面上点 $P$ 和曲线 $C$ ,任取 $C$ 上一点 $Q$ ,若线段 ${PQ}$ 的长度存在最小值,则称该值为点 $P$ 到曲线 $C$ 的距离,记作 $d\left( {P, C}\right)$ . 若曲线 $C$ 是边长为 6 的等边三角形,则点集 $D = \left\{ {P \mid d\left( {P, C}\right) \leq 1}\right\}$ 所表示的图形的面积为\_\_\_

6. 记 $d\left( {P, l}\right)$ 为点 $P$ 到直线 $l$ 的距离。直线集 $S = \left\{ {\text{ 直线 }l\left| \right| d\left( {A, l}\right) - d\left( {B, l}\right) \mid = 2\sqrt{2}}\right\}$ ，其中 $A\left( {-2,0}\right)$ ， $B\left( {2,0}\right)$ 为定点。若点 $P$ 不在任何一条 $S$ 中的直线上,则这样的点 $P$ 所构成的区域面积为\_\_\_

![](images/bo_d68j3a77aajc739aivpg_94_234_1740_189_163_0.jpg)

7. 如图，用 35 个单位正方形拼成一个矩形，点 ${P}_{1}$ 、 ${P}_{2}$ 、 ${P}_{3}$ 、 ${P}_{4}$ 以及四个标记为 “▲” 的点在正方形的顶点处,设集合 $\Omega = \left\{ {{P}_{1},{P}_{2},{P}_{3},{P}_{4}}\right\}$ ,点 $P \in \Omega$ ,过 $P$ 作直线 ${l}_{P}$ ,使得不在 ${l}_{P}$ 上的 “ $\Delta$ ” 的点分布在 ${l}_{P}$ 的两侧. 用 ${D}_{1}\left( {l}_{P}\right)$ 和 ${D}_{2}\left( {l}_{P}\right)$ 分别表示 ${l}_{P}$ 一侧和另一侧的 “ $\Delta$ ” 的点到 ${l}_{P}$ 的距离之和. 若过 $P$ 的直线 ${l}_{P}$ 中有且只有一条满足 ${D}_{1}\left( {l}_{P}\right) = {D}_{2}\left( {l}_{P}\right)$ ,则 $\Omega$ 中所有这样的 $P$ 为\_\_\_

S. 在平面直角坐标系中,定义 $d\left( {A, B}\right) = \max \left\{ {\left| {{x}_{1} - {x}_{2}}\right| ,\left| {{y}_{1} - {y}_{2}}\right| }\right\}$ 为两点 $A\left( {{x}_{1},{y}_{1}}\right) , B\left( {{x}_{2},{y}_{2}}\right)$ 的 “契比雪夫距离”,又设点 $P$ 及直线 $l$ 上任意一点 $Q$ ,称 $d\left( {P, Q}\right)$ 的最小值为点 $P$ 到直线 $l$ 的 “契比雪夫距离”,记作 $d\left( {P, l}\right)$ ,给出下列三个命题,其中真命题的个数为\_\_\_。

① 对任意三点 $A, B, C$ 都有 $d\left( {C, A}\right) + d\left( {C, B}\right) \geq d\left( {A, B}\right)$ ；

② 已知点 $P\left( {3,1}\right)$ 和直线 $l : {2x} - y - 1 = 0$ ，则 $d\left( {P, l}\right) = \frac{4}{3}$ ；

③ 定点 ${F}_{1}\left( {-c,0}\right)$ ， ${F}_{2}\left( {c,0}\right)$ ，动点 $P\left( {x, y}\right)$ 满足 $\left| {d\left( {P,{F}_{1}}\right) - d\left( {P,{F}_{2}}\right) }\right| = {2a}\left( {{2c} > {2a} > 0}\right)$ ，则点 $P$ 的轨迹与直线 $y = k$ ( $k$ 为常数) 有且仅有 2 个公共点.

# 第十二讲圆

## 一、圆基本概念一览

$>$ 圆的方程

(1)圆的标准方程为 ${\left( x - a\right) }^{2} + {\left( y - b\right) }^{2} = {r}^{2}$ ，其中 $\left( {a, b}\right)$ 为圆心， $r$ 为半径；

(2)圆的一般方程为 ${x}^{2} + {y}^{2} + {Dx} + {Ey} + F = 0$ ，且 $\Delta = {D}^{2} + {E}^{2} - {4F} > 0$ 。其中 $\left( {-\frac{D}{2}, - \frac{E}{2}}\right)$ 为圆心， $\frac{\sqrt{\Delta }}{2}$ 为半径。

(3)圆的参数方程为 $\left\{ \begin{array}{l} x = a + r\cos \theta \\ y = b + r\sin \theta \end{array}\right.$ ，其中 $\left( {a, b}\right)$ 为圆心， $r$ 为半径。

### 圆的位置关系

(1)点 $P$ 与 $\odot O$ 位置关系判定为:圆外 $\Leftrightarrow {PO} > r$ ；圆上 $\Leftrightarrow {PO} = r$ ；圆内 $\Leftrightarrow {PO} < r$

(2)直线 $l$ 与 $\odot O$ 位置关系判定为:相离 $\Leftrightarrow {d}_{O - l} > r$ ；相切 $\Leftrightarrow {d}_{O - l} = r$ ；相交 $\Leftrightarrow {d}_{O - l} < r$

(3) $\odot P$ 与 $\odot Q$ 位置关系判定为:相离 $\Leftrightarrow {PQ} > {R}_{p} + {R}_{Q}$ ；外切 $\Leftrightarrow {PQ} = {R}_{p} + {R}_{Q}$ ；

相交 $\Leftrightarrow \left| {{R}_{p} - {R}_{Q}}\right| < {PQ} < {R}_{p} + {R}_{Q}$ ；内切 $\Leftrightarrow {PQ} = \left| {{R}_{p} - {R}_{Q}}\right|$ ；内含 $\Leftrightarrow {PQ} < \left| {{R}_{p} - {R}_{Q}}\right|$

圆的切线: 若 $\left( {a, b}\right)$ 为圆心, $r$ 为半径

(1)已知切点为 $\left( {{x}_{0},{y}_{0}}\right)$ ,过该切点的切线方程为 $\left( {{x}_{0} - a}\right) \left( {x - a}\right) + \left( {{y}_{0} - b}\right) \left( {y - b}\right) = {r}^{2}$

(2)已知切线倾斜角为 $\alpha$ ，则切线方程为 $\left( {x - a}\right) \sin \alpha - \left( {y - b}\right) \cos \alpha \pm r = 0$

(3)已知切线斜率为 $k$ ，则切线方程为 $y - b = k\left( {x - a}\right) \pm r\sqrt{1 + {k}^{2}}$

$>$ 外接圆与内切:

(1) $\bigtriangleup {ABC}$ 外接圆半径为 $R = \frac{a}{2\sin A} = \frac{b}{2\sin B} = \frac{c}{2\sin C}$

(2) $\bigtriangleup {ABC}$ 内切圆半径为 $r = \frac{2S}{C}$

圆的弦: 垂径定理

## 二、圆与直线相关问题

1. 设圆 $C$ 与 $x$ 轴相切,圆心在直线 ${3x} - y = 0$ 上,且被直线 $x - y = 0$ 截得的弦长为 $2\sqrt{7}$ ,求圆 $C$ 的方程.

2. 已知坐标平面上有两点 $B\left( {3,3}\right) \text{ 、 }C\left( {0, - 1}\right)$ ，若直线 ${l}_{1} : {ax} + \left( {1 - a}\right) y - 3 = 0$ 与直线 ${l}_{2} : {ax} + y + 1 = 0$ 相交于点 $A$ ,则 $\bigtriangleup {ABC}$ 的外接圆半径的最小值为\_\_\_.

3. 设 $a\text{ 、 }b$ 是 $\sin \theta \cdot {x}^{2} + \cos \theta \cdot x - 1 = 0$ 两个不等实根,则过 $A\left( {a,{a}^{2}}\right) \text{ 、 }B\left( {b,{b}^{2}}\right)$ 的直线与单位圆的位置关系为 ( ).

::: choices
- (A) 相离
- (B) 相切
- (C) 相交
- (D) 随 $\theta$ 的值变化
:::


4. 已知圆满足:① 截 $y$ 轴所得弦长为 2；② 被 $x$ 轴分成两段圆弧，弧长之比为 3:1；③ 圆心到直线 $l : x - {2y} = 0$ 的距离最小,求此时圆的方程.

5. 在平面直角坐标系 ${xOy}$ 中,已知向量 $\overrightarrow{a} \cdot \overrightarrow{b},\left| \overrightarrow{a}\right| = \left| \overrightarrow{b}\right| = 1,\overrightarrow{a} \cdot \overrightarrow{b} = 0$ ,点 $Q$ 满足 $\overrightarrow{OQ} = \sqrt{2}\left( {\overrightarrow{a} + \overrightarrow{b}}\right)$ . 曲线 $C = \left\{ {P\left| {\;\overline{OP} = \overrightarrow{a}\cos \theta + \overrightarrow{b}\sin \theta }\right. ,0 \leq \theta \leq {2\pi }}\right\}$ ,区域 $\Omega = \{ P\left| {0 < r \leq }\right| \overline{PQ} \mid \leq R, r < R\}$ . 若 $C \cap \Omega$ 为两段分离的曲线, 则 ( ).

::: choices
- (A) $1 < r < R < 3$
- (B) $1 < r < 3 \leq R$
- (C) $r \leq 1 < R < 3$
- (D) $1 < r < R < R$
:::


6. 若点 $P\left( {x, y}\right)$ 的坐标满足方程 $x\cos \alpha + y\sin \alpha = 4$ ，则当 $\alpha$ 在实数范围内变换时， $P$ 点的轨迹是( ).

::: choices
- (A) 圆
- (B) 圆周及圆内部分
- (C) 圆周及圆外部分
- (D) 整个坐标平面
:::


7. 若 $\odot O$ 以 $\left( {a, b}\right)$ 为圆心, $r$ 为半径。过 $\odot O$ 外一点 $P\left( {{x}_{0},{y}_{0}}\right)$ 作圆的两条切线,设切点为 $A$ 和 $B$ ,则直线 ${AB}$ 的方程为\_\_\_

8. 如图， ${l}_{1},{l}_{2}$ 是过点 $M$ 的夹角为 $\frac{\pi }{3}$ 的两条直线，且均与圆心为 $O$ ，半径为 1 的圆相切，设圆周上一点 $P$ 到 ${l}_{1},{l}_{2}$ 的距离分别为 ${d}_{1},{d}_{2}$ ,则 $2{d}_{1} + {d}_{2}$ 的最小值为\_\_\_

![](images/bo_d68j3a77aajc739aivpg_102_1222_1096_338_367_0.jpg)

9. 圆 $C$ 分别与 $x$ 轴、 $y$ 轴相切于点 $A$ 、 $B$ ，过劣弧 ${AB}$ 上一点 $T$ 作圆 $C$ 的切线，分别交 $x$ 正半轴， $y$ 正半轴于点 $M, N$ 。若点 $Q\left( {2,1}\right)$ 是切线上的一点，则 $\bigtriangleup {MON}$ 周长的最小值为\_\_\_

# 第十三讲曲线与圆

## 一、曲线到圆的动点距离

1. 设一椭圆的中心是坐标原点,长轴在 $x$ 轴上,离心率为 $\frac{\sqrt{3}}{2}$ ,若圆 $C : {x}^{2} + {\left( y - \frac{3}{2}\right) }^{2} = 1$ 上的点与这个椭圆上的点的最大距离为 $1 + \sqrt{7}$ ，则这个椭圆的方程为\_\_\_

2. 若 $P$ 是双曲线 $\frac{{x}^{2}}{9} - \frac{{y}^{2}}{16} = 1$ 的右支上的动点, $M\text{ 、 }N$ 分别是圆 ${\left( x + 5\right) }^{2} + {y}^{2} = 4$ 和 ${\left( x - 5\right) }^{2} + {y}^{2} = 4$ 上的动点, 则 $\left| {PM}\right| - \left| {PN}\right|$ 的取值范围为\_\_\_.

## 二、曲线轨迹

3. 已知动圆 $P$ 过定点 $A\left( {-3,0}\right)$ ，并且在定圆 $B : {\left( x - 3\right) }^{2} + {y}^{2} = {64}$ 的内部与其相内切，求动圆圆心 $P$ 的轨迹方程.

4. 已知圆 ${\left( x - 2\right) }^{2} + {y}^{2} = 9$ 的圆心为 $C$ ,过 $M\left( {-2,0}\right)$ 且与 $x$ 轴不重合的直线 $l$ 交圆于 $A, B$ 两点,点 $A$ 在 $M$ 与 $B$ 之间，过点 $M$ 作直线 ${AC}$ 的平行线交直线 ${BC}$ 于点 $P$ ，则点 $P$ 的轨迹为( )

::: choices
- A. 圆的一部分
- B. 椭圆的一部分
- D. 抛物线的一部分
:::


5. 已知曲线 ${C}_{1} : y = \sqrt{1 - {x}^{2}}$ 与曲线 ${C}_{2} : y = \sqrt{2 - {x}^{2}}$ ，长度为 1 的线段 ${AB}$ 的两端点 $A$ ， $B$ 分别在曲线 ${C}_{1}$ ， ${C}_{2}$ 上沿顺时针方向运动，若点 $A$ 从点 $\left( {-1,0}\right)$ 开始运动，点 $B$ 到达点 $\left( {\sqrt{2},0}\right)$ 时停止运动，则线段 ${AB}$ 所扫过的区域的面积为\_\_\_

## 三、特殊代数式的几何意义

6. 设 $A\left( {{x}_{1},{y}_{1}}\right) , B\left( {{x}_{2},{y}_{2}}\right)$ 是曲线 ${x}^{2} + {y}^{2} = {2x} - {4y}$ 上的两点，则 ${x}_{1}{y}_{2} - {x}_{2}{y}_{1}$ 的最大值为\_\_\_

7. 已知 $A\left( {{x}_{1},{y}_{1}}\right) , B\left( {{x}_{2},{y}_{2}}\right)$ 是圆 ${x}^{2} + {y}^{2} = 1$ 上的两个不同的动点,且 ${x}_{1}{y}_{2} = {x}_{2}{y}_{1}$ ,则 $\mu = 2{x}_{1} + {x}_{2} + 2{y}_{1} + {y}_{2}$ 的最大值为\_\_\_

8. 已知实数 $a$ 、 $b$ 使得不等式 $\left| {a{x}^{2} + {bx} + a}\right| \leq x$ 对任意 $x \in \left\lbrack {1,2}\right\rbrack$ 都成立，在平面直角坐标系 ${xOy}$ 中，点 $\left( {a, b}\right)$ 形成的区域记为 $\Omega$ ，若圆 ${x}^{2} + {y}^{2} = {r}^{2}$ 上的任一点都在 $\Omega$ 中，则 $r$ 的最大值为\_\_\_

9. 若点 $A = \left\{ {\left( {x, y}\right) \mid {x}^{2} + {y}^{2} \leq 1}\right\} , B = \left\{ {\left( {x, y}\right) \mid - 2 \leq x \leq 2, - 1 \leq y \leq 1}\right\}$ ，则点集 $Q = \left\{ {\left( {x, y}\right) \mid x = {x}_{1} + {x}_{2}, y = {y}_{1} + {y}_{2},\left( {{x}_{1},{y}_{1}}\right) \in A,\left( {{x}_{2},{y}_{2}}\right) \in B}\right\}$ 所表示的区域的面积是\_\_\_

10. 在平面直角坐标系 ${xOy}$ 中,过点 $P\left( {-3, a}\right)$ 作圆 ${x}^{2} + {y}^{2} - {2x} = 0$ 的两条切线,切点分别为 $M\left( {{x}_{1},{y}_{1}}\right)$ 、 $N\left( {{x}_{2},{y}_{2}}\right)$ ，若 $\left( {{x}_{2} - {x}_{1}}\right) \left( {{x}_{2} + {x}_{1}}\right) + \left( {{y}_{2} - {y}_{1}}\right) \left( {{y}_{2} + {y}_{1} - 2}\right) = 0$ ，则实数 $a$ 的值等于\_\_\_

## 四、图形极限

11. 设 ${P}_{n}\left( {{x}_{n},{y}_{n}}\right)$ 是直线 ${2x} - y = \frac{n}{n + 1}\left( {n \in {N}^{ * }}\right)$ 与圆 ${x}^{2} + {y}^{2} = 1$ 在第一象限的交点,

则 $\mathop{\lim }\limits_{{n \rightarrow + \infty }}\frac{{y}_{n} - 1}{{x}_{n} - 1} =$ \_\_\_，$\mathop{\lim }\limits_{{n \rightarrow + \infty }}\frac{{y}_{n} - \frac{3}{5}}{{x}_{n} - \frac{4}{5}} =$ \_\_\_

12. 已知点 ${A}_{n}\text{ 、 }{B}_{n}\left( {n \in {\mathbf{N}}^{ * }}\right)$ 在双曲线 ${xy} = 1$ 上，且点 ${A}_{n}$ 的横坐标为 $\frac{n}{n + 1}$ ，点 ${B}_{n}$ 的横坐标为 $\frac{n + 1}{n}$ ，记 $M$ 点的坐标为 $\left( {1,1}\right) ,{P}_{n}\left( {{x}_{n},{y}_{n}}\right)$ 是 $\bigtriangleup {A}_{n}{B}_{n}M$ 的外心，则 $\mathop{\lim }\limits_{{n \rightarrow \infty }}{x}_{n} =$

# 第十四讲椭圆与双曲线 $I$

## 一、圆、椭圆与双曲线基础知识汇总

<table><tr><td rowspan="4" colspan="2">统一标准式: $\frac{{x}^{2}}{{\lambda }^{2}} + \frac{{y}^{2}}{{\mu }^{2}} = 1$</td><td>圆: $\lambda ,\mu$ 为相等实数</td><td>$\lambda = \mu = r$</td></tr><tr><td>椭圆: $\lambda ,\mu$ 为不等实数</td><td>大的为 $a$ ,小的为 $b$</td></tr><tr><td>双曲线: $\lambda ,\mu$ 一虚一实</td><td>实数为 $a$ ,虚数 (模长) 为 $b$ <br> 渐近线: $y = \pm \left| \frac{\mu }{\lambda }\right| x$</td></tr><tr><td colspan="2">$c = \sqrt{\left| {\lambda }^{2} - {\mu }^{2}\right| },\;e = \frac{c}{a}$</td></tr><tr><td>内部: $\frac{{x}^{2}}{{\lambda }^{2}} + \frac{{y}^{2}}{{\mu }^{2}} < 1$</td><td colspan="3"><img src="images/bo_d68j3a77aajc739aivpg_109_539_1031_281_220_0.jpg"/>  <img src="images/bo_d68j3a77aajc739aivpg_109_836_1037_283_215_0.jpg"/>  <img src="images/bo_d68j3a77aajc739aivpg_109_1115_1038_262_213_0.jpg"/></td></tr><tr><td rowspan="2">切线</td><td colspan="2">已知切点坐标 $\left( {{x}_{0},{y}_{0}}\right)$</td><td>$\frac{{x}_{0}x}{{\lambda }^{2}} + \frac{{y}_{0}y}{{\mu }^{2}} = 1$</td></tr><tr><td colspan="2">已知切线斜率 $k$</td><td>$y = {kx} \pm \sqrt{\left| {\lambda }^{2}{k}^{2} + {\mu }^{2}\right| }$</td></tr><tr><td rowspan="2">焦半径</td><td colspan="2">焦点在 $x$ 轴</td><td>左焦半径 $P{F}_{1} = \left| {\lambda + e{x}_{P}}\right|$ ,右焦半径 $P{F}_{2} = \left| {\lambda - e{x}_{P}}\right|$</td></tr><tr><td colspan="2">焦点在 $y$ 轴</td><td>下焦半径 $P{F}_{1} = \left| {\mu + e{y}_{P}}\right|$ ,上焦半径 $P{F}_{2} = \left| {\mu - e{y}_{P}}\right|$</td></tr><tr><td>顶点斜率积</td><td colspan="2">曲线上任一动点 $P$ <br> 到两对称顶点斜率</td><td rowspan="2">${k}_{1}{k}_{2} = - \frac{{\mu }^{2}}{{\lambda }^{2}}$</td></tr><tr><td>斜径定理</td><td colspan="2">弦斜率 ${k}_{1}$ <br> 弦中点与原点连线斜率 ${k}_{2}$</td></tr></table>

### 圆锥曲线动点轨迹汇总

### 动点距离和差

(1)动点 $P$ 到两定点 $A, B$ 的距离平方和 $P{A}^{2} + P{B}^{2}$ 为大于 $\frac{A{B}^{2}}{2}$ 的定值时， $P$ 的轨迹为圆

(2)动点 $P$ 到两定点 $A, B$ 的距离和 ${PA} + {PB}$ 为大于 ${AB}$ 线段长的定值时， $P$ 的轨迹为椭圆

(3)动点 $P$ 到两定点 $A, B$ 的距离差值 $\left| {{PA} - {PB}}\right|$ 为小于 ${AB}$ 线段长的定值时， $P$ 的轨迹为双曲线

### 动点距离比

(1)动点 $P$ 到两定点 $A, B$ 的距离比 $\frac{PA}{PB}$ 为定值，且该定值不等于 1 时， $P$ 的轨迹为圆(阿波罗尼斯圆)

(2)动点 $P$ 到定点 $A$ 的距离，与到不过 $A$ 的定直线 $l$ 的距离比 $\frac{PA}{{d}_{P - l}}$ 为小于 1 的定值时， $P$ 的轨迹为椭圆

(3)动点 $P$ 到定点 $A$ 的距离，与到不过 $A$ 的定直线 $l$ 的距离比 $\frac{PA}{{d}_{P - l}}$ 为定值 1 时， $P$ 的轨迹为抛物线

(4)动点 $P$ 到定点 $A$ 的距离，与到不过 $A$ 的定直线 $l$ 的距离比 $\frac{PA}{{d}_{P - l}}$ 为大于 1 的定值时， $P$ 的轨迹为双曲线。在(2)(3)(4)中，定点 $A$ 为曲线的焦点，定直线 $l$ 为曲线的准线，比值 $\frac{PA}{{d}_{P - l}}$ 为曲线的离心率

### 斜率积

(1)动点 $P$ 到两定点 $A, B$ 的斜率积为定值 -1 时， $P$ 的轨迹为圆

(2)动点 $P$ 到两定点 $A, B$ 的斜率积为 $\left( {-\infty , - 1}\right) \cup \left( {-1,0}\right)$ 范围内的定值时， $P$ 的轨迹为椭圆

(3)动点 $P$ 到两定点 $A, B$ 的斜率积为 $\left( {0, + \infty }\right)$ 的定值时， $P$ 的轨迹为双曲线

## 二、椭圆与双曲线的几何性质

1. 设点 $P$ 是曲线 $y = \sqrt{{x}^{2} + 1}$ 上的动点，点 $F\left( {0, - \sqrt{2}}\right)$ ， $A\left( {\sqrt{2},0}\right)$ ，满足 $\left| {PF}\right| + \left| {PA}\right| = 4$ ，则点 $P$ 的坐标是(B)。 标为\_\_\_.

2. 已知 ${F}_{1},{F}_{2}$ 是双曲线 $C : \frac{{x}^{2}}{{a}^{2}} - \frac{{y}^{2}}{{b}^{2}} = 1\left( {a, b > 0}\right)$ 的左、右焦点,过 ${F}_{2}$ 的直线交双曲线的右支于 $A, B$ 两点，且 $\left| {A{F}_{1}}\right| = 2\left| {A{F}_{2}}\right|$ ， $\angle A{F}_{1}{F}_{2} = \angle {F}_{1}B{F}_{2}$ ，则在下列结论中，所有正确结论的序号为\_\_\_.

① 双曲线 $C$ 的离心率为 2; ② 双曲线 $C$ 的一条渐近线的斜率为 $\sqrt{2}$ ；

③ 线段 ${AB}$ 的长为 ${6a}$ ；④ $\bigtriangleup A{F}_{1}{F}_{2}$ 的面积为 $\sqrt{15}{a}^{2}$ .

![](images/bo_d68j3a77aajc739aivpg_111_1270_1215_239_293_0.jpg)

3. 如图,已知 ${F}_{1},{F}_{2}$ 分别是椭圆 $C : \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 的左、右焦点, $M, N$ 为椭圆上两点,满足 ${F}_{1}M//{F}_{2}N$ ，且 $\left| {{F}_{2}N}\right| : \left| {{F}_{2}M}\right| : \left| {{F}_{1}M}\right| = 1 : 2 : 3$ ，则椭圆 $C$ 的离心率为\_\_\_.

![](images/bo_d68j3a77aajc739aivpg_112_1190_375_349_262_0.jpg)

4. 已知 ${F}_{1}\text{ 、 }{F}_{2}$ 是双曲线 $\Gamma : \frac{{x}^{2}}{{a}^{2}} - \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > 0, b > 0}\right)$ 的左、右焦点， $l$ 是 $\Gamma$ 的一条渐近线，以 ${F}_{2}$ 为圆心的圆与 $l$ 相切于点 $P$ . 若双曲线 $\Gamma$ 的离心率为 2,则 $\sin \angle P{F}_{1}{F}_{2} =$

5. 已知平面直角坐标系中的直线 ${l}_{1} : y = {3x}$ 、 ${l}_{2} : y = {-{3x}}$ . 设到 ${l}_{1}\text{ 、 }{l}_{2}$ 距离之和为 $2{p}_{1}$ 的点的轨迹是曲线 ${C}_{1}$ ,到 ${l}_{1}\text{ 、 }{l}_{2}$ 距离平方和为 $2{p}_{2}$ 的点的轨迹是曲线 ${C}_{2}$ ,其中 ${p}_{1}\text{ 、 }{p}_{2} > 0$ . 则 ${C}_{1}\text{ 、 }{C}_{2}$ 公共点的个数不可能为( )个

::: choices
- A. 0
- B. 4
- C. 8
- D. 12
:::


6. 已知曲线 ${C}_{1} : \frac{{x}^{2}}{m} + {y}^{2} = 1\left( {m > 1}\right)$ 和 ${C}_{2} : \frac{{x}^{2}}{n} - {y}^{2} = 1\left( {n > 0}\right)$ 有相同的焦点,分别为 ${F}_{1},{F}_{2}$ ,点 $M$ 是 ${C}_{1}$ 和 ${C}_{2}$ 的一个交点，则 ${\Delta M}{F}_{1}{F}_{2}$ 的形状是\_\_\_

## 三、焦半径

7. 已知点 $F$ 是椭圆 $\frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 的右焦点， $A$ 、 $B$ 、 $C$ 是椭圆上的三点，使得 $\overrightarrow{FA} + \overrightarrow{FB} + \overrightarrow{FC} = \overrightarrow{0}$ ， 则 $\left| \overrightarrow{FA}\right| + \left| \overrightarrow{FB}\right| + \left| \overrightarrow{FC}\right| =$ \_\_\_.

8. 双曲线 ${x}^{2} - {y}^{2} = 2$ 的左、右焦点分别为 ${F}_{1}\text{ 、 }{F}_{2}$ ,点 $P\left( {{x}_{n},{y}_{n}}\right) \left( {n \in {\mathbf{N}}^{ * }}\right)$ 在其右支上,且满足 $\left| {{P}_{n + 1}{F}_{2}}\right| = \left| {{P}_{n}{F}_{1}}\right|$ , 若 ${P}_{1}{F}_{2} \bot {F}_{1}{F}_{2}$ ,则 ${x}_{100} =$ \_\_\_.

# 课后练习 9

1. 在正三棱柱 ${ABC} - {A}_{1}{B}_{1}{C}_{1}$ 中， ${AB} = {A{A}_{1}}$ ，则 ${A{C}_{1}}$ 与平面 $B{B}_{1}{C}_{1}C$ 所成的角的正弦值为()

::: choices
- A. $\frac{\sqrt{2}}{2}$
- B. $\frac{\sqrt{6}}{4}$
- C. $\frac{\sqrt{15}}{54}$
- D. $\frac{\sqrt{6}}{3}$
:::


2. 三条射线 ${OA},{OB},{OC}$ 两两成 ${60}^{ \circ }$ 角,则直线 ${OA}$ 与平面 ${OBC}$ 的成角为( )

::: choices
- A. 60°
- B. 45°
- C. $\arccos \frac{\sqrt{3}}{3}$
- D. $\arccos \frac{\sqrt{6}}{3}$
:::


3. 已知正方形 ${ABCD}$ 折成直二面角 $A - {BD} - C$ ，则二面角 $B - {CD} - A$ 的大小为( )

::: choices
- A. 60°
- B. 45°
- C. $\arccos \frac{1}{3}$
- D. $\arctan \sqrt{2}$
:::


4. 二面角 $\alpha - l - \beta$ 的度数为 ${120}^{ \circ }, A, B \in l,{AC} \subset \alpha ,{BD} \subset \beta ,{AC} \bot l,{BD} \bot l$ ,若 ${AB} = {AC} = {BD} = 1$ , 则 ${CD}$ 等于\_\_\_。

5. 【23 上海高考 17】直四棱柱 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ ， ${AB}//{DC}$ ， ${AB}\bot {AD}$ ， ${AB} = 2$ ， ${AD} = 3$ ， ${DC} = 4$ .

(1)求证: ${A}_{1}B \bot$ 平面 ${DC}{C}_{1}{D}_{1}$ ；

(2)若四棱柱 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 的体积为 36，求二面角 ${A}_{1} - {BD} - A$ 的大小.

![](images/bo_d68j3a77aajc739aivpg_115_1127_1554_334_278_0.jpg)

6. 如图，已知四棱锥 $P - {ABCD}$ ， ${PB}\bot {AD}$ ，侧面 ${PAD}$ 为边长等于 2 的正三角形，底面 ${ABCD}$ 为菱形,侧面 ${PAD}$ 与底面 ${ABCD}$ 所成的二面角为 ${120}^{ \circ }$ 。

(1)求点 $P$ 到平面 ${ABCD}$ 的距离；(2)求面 ${APB}$ 与面 ${CPB}$ 所成锐二面角的大小。

![](images/bo_d68j3a77aajc739aivpg_116_1113_393_396_288_0.jpg)

# 课后练习 10

1. 已知正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ ，空间一动点 $P$ 满足 ${A}_{1}P \bot A{B}_{1}$ ，且 $\angle {AP}{B}_{1} = \angle {AD}{B}_{1}$ ，则点 $P$ 的轨迹为 ( )

::: choices
- A. 直线
- B. 圆
- C. 椭圆
- D. 抛物线
:::


![](images/bo_d68j3a77aajc739aivpg_117_1077_487_358_335_0.jpg)

在一个棱长为 10 的密封正方体盒子中, 放一个半径为 1 的小球, 任意摇动盒子, 则小球在盒子中不能接触到的内壁面积为\_\_\_；

3. 如图:棱长为 2 的正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 的内切球为球 $O$ ， $E$ 、 $F$ 分别是棱 ${AB}$ 和棱 ${C{C}_{1}}$ 的中点， $G$ 在棱 ${BC}$ 上移动，则下列命题正确的有\_\_\_

① 存在点 $G$ ，使 ${OD}$ 垂直于平面 ${EFG}$ ；

② 对于任意点 $G,{OA}$ 平行于平面 ${EFG}$

③ 直线 ${EF}$ 被球 $O$ 截得的弦长为 $\sqrt{2}$ ；

③ 过直线 ${EF}$ 的平面截球 $O$ 所得的所有截面圆中,半径最小的圆的面积为 $\frac{\pi }{2}$ .

![](images/bo_d68j3a77aajc739aivpg_117_1109_1565_343_315_0.jpg)

4. 已知 $A{A}_{1}$ 是圆柱的一条母线， ${AB}$ 是圆柱下底面的直径， $C$ 是圆柱下底面圆周上异于 $A$ ， $B$ 的点，若圆柱的侧面积为 ${4\pi }$ ，则三棱锥 ${A}_{1} - {ABC}$ 外接球体积的最小值为\_\_\_

5. 【2024 崇明一模 15】已知点 $M$ 为正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 内部(不包含表面)的一点. 给出下列两个命题:

${q}_{1}$ : 过点 $M$ 有且只有一个平面与 $A{A}_{1}$ 和 ${B}_{1}{C}_{1}$ 都平行;

${q}_{2}$ : 过点 $M$ 至少可以作两条直线与 $A{A}_{1}$ 和 ${B}_{1}{C}_{1}$ 所在的直线都相交.

则以下说法正确的是( )

::: choices
- A. 命题 ${q}_{1}$ 是真命题,命题 ${q}_{2}$ 是假命题
- B. 命题 ${q}_{1}$ 是假命题,命题 ${q}_{2}$ 是真命题
- C. 命题 ${q}_{1}\text{ 、 }{q}_{2}$ 都是真命题
- D. 命题 ${q}_{1}\text{ 、 }{q}_{2}$ 都是假命题
:::


6. 【2024 金山一模 15】如图，在正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 中， $E$ 、 $F$ 为正方体内(含边界)不重合的两个动点, 下列结论错误的是 ( )

::: choices
- A. 若 $E \in B{D}_{1}, F \in {BD}$ ,则 ${EF} \bot {AC}$
- B. 若 $E \in B{D}_{1}, F \in {BD}$ ,则平面 ${BEF} \bot$ 平面 ${A}_{1}B{C}_{1}$
- C. 若 $E \in {AC}, F \in C{D}_{1}$ ,则 ${EF}//$ 平面 ${A}_{1}B{C}_{1}$
- D. 若 $E \in {AC}, F \in C{D}_{1}$ ,则 ${EF}//A{D}_{1}$
:::


![](images/bo_d68j3a77aajc739aivpg_118_1265_1570_285_278_0.jpg)

7. 正三棱锥 $P - {ABC}$ 的侧棱两两成 ${40}^{ \circ }$ 角，侧棱长为 $1, D, E$ 分别为 ${PB},{PC}$ 上的点，则 $\bigtriangleup {ADE}$ 的周长的最小值为\_\_\_.

![](images/bo_d68j3a77aajc739aivpg_119_1245_309_229_291_0.jpg)

8. 如图，已知正方体 ${ABCD} - {A}_{1}{B}_{1}{C}_{1}{D}_{1}$ 的棱长为 1，点 $M$ 为棱 ${AB}$ 的中点，点 $P$ 在侧面 ${BC}{C}_{1}{B}_{1}$ 及其边界上运动,则 ${2PM} + P{D}_{1}$ 的最小值为\_\_\_

![](images/bo_d68j3a77aajc739aivpg_119_1161_857_317_284_0.jpg)

9. 在四棱锥 $S - {ABCD}$ 中,已知 ${SA} \bot$ 底面 ${ABCD},{AB}//{CD},{AB} \bot {AD},{AB} = 2\sqrt{2},{AD} = {CD} = 4, M$ 是平面 ${SAD}$ 内的动点，且满足 $\angle {CMD} = \angle {BMA}$ ，则当四棱锥 $M - {ABCD}$ 的体积最大时，三棱锥 $M - {ACD}$ 外接球的表面积为\_\_\_

![](images/bo_d68j3a77aajc739aivpg_119_1211_1515_273_326_0.jpg)

# 课后练习 11

1、已知直线 $y = x + 1$ 上有两个点 $A\left( {{a}_{1},{b}_{1}}\right) , B\left( {{a}_{2},{b}_{2}}\right)$ ，已知 ${a}_{1},{b}_{1},{a}_{2},{b}_{2}$ 满足: $\sqrt{2}\left| {{a}_{1}{a}_{2} + {b}_{1}{b}_{2}}\right| = \sqrt{{a}_{1}^{2} + {b}_{1}^{2}} \cdot \sqrt{{a}_{2}^{2} + {b}_{2}^{2}}$ ，若 ${a}_{1} > {a}_{2}$ ， $\left| {AB}\right| = 2 + \sqrt{2}$ ，则这样的点 $A$ 有\_\_\_个.

1. 已知直线 ${l}_{1} : {a}_{1}x + {b}_{1}y + 1 = 0,{l}_{2} : {a}_{2}x + {b}_{2}y + 1 = 0$ 交于点 $\left( {3,4}\right)$ ，则过点 $P\left( {{a}_{1},{b}_{1}}\right)$ 和点 $Q\left( {{a}_{2},{b}_{2}}\right)$ 的直线方程是\_\_\_.

2. 对于直线 $l$ 上的任意一点 $P\left( {x, y}\right)$ ,点 $Q\left( {x + {3y},{8x} - y}\right)$ 也在直线 $l$ 上,求直线 $l$ 的方程为\_\_\_

3. 已知 $A\left( {1,1}\right)$ 、 $B\left( {2, - 1}\right)$ ，若直线 $l : x + {ay} + 1 = 0$ 与线段 ${AB}$ 相交，则实数 $a$ 的取值范围是\_\_\_.

4. 已知直线 ${l}_{1} : {ax} - {2y} - {2a} + 4 = 0,{l}_{2} : {2x} + {a}^{2}y - 2{a}^{2} - 4 = 0$ ，其中 $0 < a < 2$ ，若 ${l}_{1},{l}_{2}$ 与坐标轴围成一个四边形，则该四边形面积的最小值为\_\_\_。

5. 在平面直角坐标系中,对于任意两个点 $P\left( {{x}_{1},{y}_{1}}\right) \text{ 、 }{P}_{2}\left( {{x}_{2},{y}_{2}}\right)$ 的“非常距离”定义如下: 若 $\left| {{x}_{1} - {x}_{2}}\right| \geq \left| {{y}_{1} - {y}_{2}}\right|$ ,则点 $P\left( {{x}_{1},{y}_{1}}\right) \text{ 、 }{P}_{2}\left( {{x}_{2},{y}_{2}}\right)$ 的“非常距离”为 $\left| {{x}_{1} - {x}_{2}}\right|$ ,若 $\left| {{x}_{1} - {x}_{2}}\right| < \left| {{y}_{1} - {y}_{2}}\right|$ ,则点 $P\left( {{x}_{1},{y}_{1}}\right) \text{ 、 }{P}_{2}\left( {{x}_{2},{y}_{2}}\right)$ 的“非常距离”为 $\left| {{y}_{1} - {y}_{2}}\right|$ . 已知点 $C$ 是直线 $y = \frac{3}{4}x + 3$ 的一个动点，则点 $C$ 和点 $D\left( {0,1}\right)$ 的“非常距离”的最小值是\_\_\_.

6. 设已知直线 $l : {kx} - y + 1 + {2k} = 0, k \in \mathbf{R}$ .

(1)证明:直线 $l$ 过定点；

(2)若直线 $l$ 不经过第四象限，求 $k$ 的取值范围；

(3)若直线 $l$ 交 $x$ 轴负半轴于点 $A$ ，交 $y$ 轴正半轴于点 $B$ ， $O$ 为坐标原点，设 $\bigtriangleup {AOB}$ 的面积为 $S$ ，求 $S$ 的最小值及此时直线 $l$ 的方程.

7. 在直角坐标系 ${xOy}$ 中，定义点 $A\left( {{x}_{1},{y}_{1}}\right)$ ， $B\left( {{x}_{2},{y}_{2}}\right)$ 的 “直角距离” 为(A, B)为: $d\left( {A, B}\right) = \left| {{x}_{1} - {x}_{2}}\right| + \left| {{y}_{1} - {y}_{2}}\right|$ ,设 $M\left( {1,1}\right) , N\left( {-1, - 1}\right)$ .

(1)点 $C$ 满足 $d\left( {C, M}\right) = d\left( {C, N}\right)$ ，在所给坐标系中画出点 $C$ 所在区域；(只需画图,无需说明理由

(2)分别过点 $M, N$ 作斜率为 2 的直线 ${l}_{1},{l}_{2}$ ，点 $Q, R$ 分别是直线 ${l}_{1},{l}_{2}$ 上的动点,求 $d\left( {Q, R}\right)$ 的最小值；

(3)设 $P\left( {x, y}\right)$ ，记方程 $d\left( {P, M}\right) + d\left( {P, N}\right) = 8$ 的曲线为 $\Gamma$ ，类比椭圆研究曲线 $\Gamma$ 的性质(结论不要求证明), 并在所给坐标系中画出该曲线.

# 课后练习 12

1. 直线 $x\cos \theta + y\sin \theta + c = 0\left( {\theta \in \mathbf{R}}\right)$ 必 ( ).

::: choices
- (A) 过某个定点
- (B) 与某个定圆相切
- (C) 与某定直线平行
- (D) 与某定直线垂直
:::


2. 设集合 $P = \left\{ {\left( {x, y}\right) \mid {\left( x + 2\right) }^{2} + {\left( y - 3\right) }^{2} \leq 4}\right\} , Q = \left\{ {\left( {x, y}\right) \mid {\left( x + 1\right) }^{2} + {\left( y - m\right) }^{2} < \frac{1}{4}}\right\}$ ,且 $P \cap Q = Q$ ,则实数 $m$ 的取值范围为\_\_\_。

3. 过点 $P\left( {\frac{1}{2}, - 2}\right)$ 作圆 $C : {\left( x - \frac{4}{3}m\right) }^{2} + {\left( y - m + 1\right) }^{2} = 1,\left( {m \in R}\right)$ 的切线,切点分别为 $A$ 和 $B$ ,则 $\overrightarrow{PA} \cdot \overrightarrow{PB}$ 的最小值为\_\_\_

4. 如图，已知点 $P\left( {2,0}\right)$ ，且正方形 ${ABCD}$ 内接于圆 $O : {x}^{2} + {y}^{2} = 1$ ， $M$ 、 $N$ 分别为边 ${AB}$ 、 ${BC}$ 的中点. 当正方形 ${ABCD}$ 绕圆心 $O$ 旋转时， $\overrightarrow{PM} \cdot \overrightarrow{ON}$ 的取值范围是\_\_\_.

![](images/bo_d68j3a77aajc739aivpg_123_950_1324_514_359_0.jpg)

5. 设圆 $O$ 是单位圆，正方形边 ${AB}$ 垂直于 $x$ 轴且为圆 $O$ 的一条弦，则 $\left| {OD}\right|$ 的取值范围是 \_\_\_.

![](images/bo_d68j3a77aajc739aivpg_123_1057_1880_411_293_0.jpg)

6. 如图，正方形 ${ABCD}$ 的边长为 20 米，圆 $O$ 的半径为 1 米，圆心是正方形的中心，点 $P, Q$ 分别在线段 ${AD},{CB}$ 上,若线段 ${PQ}$ 与圆 $O$ 有公共点,则称点 $Q$ 在点 $P$ 的 “盲区” 中,已知点 $P$ 以 ${1.5}\mathrm{\;m}/\mathrm{s}$ 的速度从 $A$ 出发向 $D$ 移动。同时,点 $Q$ 以 $1\mathrm{m}/\mathrm{s}$ 的速度从 $C$ 出发向 $B$ 移动,则在点 $P$ 从 $A$ 移动到 $D$ 的过程中,点 $Q$ 在点 $P$ 的盲区中的时长约\_\_\_秒(精确到 0.1)

![](images/bo_d68j3a77aajc739aivpg_124_1206_456_305_279_0.jpg)

7. 如图，已知满足条件 $\left| {z - {3i}}\right| = \left| {\sqrt{3} - i}\right|$ 的复数 $z$ 在复平面 ${xOy}$ 对应点的轨迹为圆 $C$ (圆心为 $C$ )，设复平面 ${xOy}$ 上的复数 $z = x + {yi}\left( {x \in R, y \in R}\right)$ 对应的点为 $\left( {x, y}\right)$ ,定直线 $m$ 的方程为 $x + {3y} + 6 = 0$ ,过 $A\left( {-1,0}\right)$ 的一条动直线 $l$ 与直线 $m$ 相交于 $N$ 点，于圆 $C$ 相交于 $P, Q$ 两点， $M$ 是弦 ${PQ}$ 的中点；

(1)若直线 $l$ 经过圆心 $C$ ，求证: $l$ 与 $m$ 垂直；

(2)当 $\left| {PQ}\right| = 2\sqrt{3}$ 时，求直线 $l$ 的方程；

(3)设 $t = \overrightarrow{AM} \cdot \overrightarrow{AN}$ ，试问 $t$ 是否为定值？若为定值，请求出 $t$ 的值；若不是定值，请说明理由

![](images/bo_d68j3a77aajc739aivpg_124_1012_1283_520_410_0.jpg)

# 第十五讲椭圆与双曲线 II

## 一、到直线距离

1. 已知实数 $x, y$ 满足: $x\left| x\right| + y\left| y\right| = 1$ ,则 $\mu = \left| {x + y + \sqrt{2}}\right|$ 的取值范围为\_\_\_.

2. 已知实数 $x, y$ 满足 $\frac{x\left| x\right| }{4} + y\left| y\right| = 1$ ，则 $\left| {x + {2y} - 4}\right|$ 的取值范围为\_\_\_.

3. 已知: $\sqrt{{x}^{2} + {y}^{2}} + \sqrt{{\left( x - 8\right) }^{2} + {\left( y - 6\right) }^{2}} = {20}$ ,则 $\left| {{3x} - {4y} - {100}}\right|$ 的最大值为\_\_\_.

## 二、弦中点

4. 将曲线 $\frac{{x}^{2}}{16} + \frac{{y}^{2}}{9} = 1\left( {x \geq 0}\right)$ 与曲线 $\frac{{x}^{2}}{7} + \frac{{y}^{2}}{9} = 1\left( {x \leq 0}\right)$ 合成的曲线记作 $C$ . 设 $k$ 为实数，斜率为 $k$ 的直线与 $C$ 交于 $A, B$ 两点， $P$ 为线段 ${AB}$ 的中点，有下列两个结论:① 存在 $k$ ，使得点 $P$ 的轨迹总落在某个椭圆上；② 存在 $k$ ，使得点 $P$ 的轨迹总落在某条直线上，则下列选项正确的是( )

::: choices
- (A)①② 均正确
- (B)①② 均错误
- (C)① 正确，② 错误
- (D)① 错误，② 正确
:::


5. 已知直线 $l$ 与椭圆 $\frac{{x}^{2}}{6} + \frac{{y}^{2}}{3} = 1$ 在第一象限交于 $A, B$ 两点， $l$ 与 $x$ 轴， $y$ 轴分别交于 $M, N$ 两点，且 $\left| {MA}\right| = \left| {NB}\right|$ ， $\left| {MN}\right| = 2\sqrt{3}$ ，则 $l$ 的方程为\_\_\_

## 三、双曲线的焦点三角形

6. 已知双曲线 ${x}^{2} - {y}^{2} = 4, A\text{ 、 }B$ 分别是其左、右顶点. 若 $P$ 是双曲线上一点,满足 $4\angle {PAB} = \angle {PBA}$ ,则 $\angle {APB} =$ \_\_\_.

7. 已知双曲线 ${x}^{2} - {y}^{2} = {a}^{2}\left( {a > 0}\right)$ 的左、右顶点分别为 $A$ 、 $B$ ，双曲线在第一象限的图像上有一点 $P$ ， $\angle {PAB} = \alpha ,\angle {PBA} = \beta ,\angle {APB} = \gamma$ ，则( ).

::: choices
- (A) $\tan \alpha + \tan \beta + \tan \gamma = 0$
- (B) $\tan \alpha + \tan \beta - \tan \gamma = 0$
- (C) $\tan \alpha + \tan \beta + 2\tan \gamma = 0$
- (D) $\tan \alpha + \tan \beta - 2\tan \gamma = 0$
:::


8. 已知点 $P\left( {{x}_{P},{y}_{P}}\right)$ 是双曲线 $C : \frac{{x}^{2}}{{a}^{2}} - \frac{{y}^{2}}{{b}^{2}} = 1$ 上的动点,设直线 $l$ 是 $\angle {F}_{1}P{F}_{2}$ 的平分线,交 $x$ 轴于点 $Q\left( {{x}_{Q},0}\right)$ ,

(1)试表出示 ${x}_{Q}$ ；(用 $a$ 、 $b$ 、 $c$ 、 ${x}_{P}$ 表示)

(2)设 $\bigtriangleup {F}_{1}P{F}_{2}$ 的内心为 $I\left( {{x}_{I},{y}_{I}}\right)$ ，求 ${x}_{I}$ (用 $a$ 、 $b$ 、 $c$ 、 ${x}_{P}$ 表示)

9. 已知一簇双曲线 ${E}_{n} : {x}^{2} - {y}^{2} = {\left( \frac{n}{2025}\right) }^{2}\left( {n \in {N}^{ * }, n \leq {2025}}\right)$ ,设双曲线 ${E}_{n}$ 的左、右焦点分别为 ${F}_{n}$ , ${F}_{{n}_{2}},{P}_{n}$ 是双曲线 ${E}_{n}$ 右支上一动点, $\bigtriangleup {P}_{n}{F}_{{n}_{1}}{F}_{{n}_{2}}$ 的内切圆 ${G}_{n}$ 与 $x$ 轴切于点 ${A}_{n}\left( {{a}_{n},0}\right)$ ,则 ${a}_{1} + {a}_{2} + \cdots + {a}_{2025} =$ \_\_\_.

# 第十六讲椭圆与双曲线 III

### 必背公式回顾

<table><tr><td rowspan="5">统一标准式 $\frac{{x}^{2}}{{\lambda }^{2}} + \frac{{y}^{2}}{{\mu }^{2}} = 1$</td><td>圆: $\lambda ,\mu$ 为相等实数</td><td colspan="2">$\lambda = \mu = r$</td></tr><tr><td>椭圆: $\lambda ,\mu$ 为不等实数</td><td colspan="2">大的为 $a$ ,小的为 $b$</td></tr><tr><td>双曲线: $\lambda ,\mu$ 一虚一实</td><td colspan="2">实数为 $a$ ,虚数 (模长) 为 $b$ <br> 渐近线: $y = \pm \left| \frac{\mu }{\lambda }\right| x$</td></tr><tr><td colspan="3">$c = \sqrt{\left| {\lambda }^{2} - {\mu }^{2}\right| },\;e = \frac{c}{a}$</td></tr><tr><td colspan="2">设 $y = {kx} + m$</td><td>直线过 $x$ 轴定点，或表达式用 $y$ 更方便时设 $x = {ty} + n \; \lambda ,\mu$ 互换、 $x, y$ 互换、 $k$ 变 t、 $m$ 变 n</td></tr><tr><td>联立方程</td><td colspan="2">$\left( {{\lambda }^{2}{k}^{2} + {\mu }^{2}}\right) {x}^{2} + 2{\lambda }^{2}{kmx} + {\lambda }^{2}\left( {{m}^{2} - {\mu }^{2}}\right) = 0$</td><td>$\left( {{\mu }^{2}{t}^{2} + {\lambda }^{2}}\right) {y}^{2} + 2{\mu }^{2}{tny} + {\mu }^{2}\left( {{n}^{2} - {\lambda }^{2}}\right) = 0$</td></tr><tr><td>$\Delta$</td><td colspan="2">$\Delta = {\left( 2\lambda \mu \right) }^{2}\left( {{\lambda }^{2}{k}^{2} + {\mu }^{2} - {m}^{2}}\right)$</td><td>$\Delta = {\left( 2\mu \lambda \right) }^{2}\left( {{\mu }^{2}{t}^{2} + {\lambda }^{2} - {n}^{2}}\right)$</td></tr><tr><td>$\left| {{x}_{1} - {x}_{2}}\right|$</td><td colspan="2">$\left| {{x}_{1} - {x}_{2}}\right| = \frac{\sqrt{\Delta }}{\left| {\lambda }^{2}{k}^{2} + {\mu }^{2}\right| }$</td><td>$\left| {{y}_{1} - {y}_{2}}\right| = \frac{\sqrt{\Delta }}{\left| {\mu }^{2}{t}^{2} + {\lambda }^{2}\right| }$</td></tr><tr><td>弦长</td><td colspan="2">$\sqrt{1 + {k}^{2}}\frac{\sqrt{\Delta }}{\left| {\lambda }^{2}{k}^{2} + {\mu }^{2}\right| }$</td><td>$\sqrt{1 + {t}^{2}}\frac{\sqrt{\Delta }}{\left| {\mu }^{2}{t}^{2} + {\lambda }^{2}\right| }$</td></tr><tr><td>弦中点 $M$</td><td colspan="2">$k \cdot {k}_{OM} = - \frac{{\mu }^{2}}{{\lambda }^{2}}$</td><td>$t \cdot {t}_{OM} = - \frac{{\lambda }^{2}}{{\mu }^{2}}$</td></tr><tr><td>极线</td><td colspan="3">$\frac{{x}_{0}x}{{\lambda }^{2}} + \frac{{y}_{0}y}{{\mu }^{2}} = 1$</td></tr></table>

## 一、目标函数: 面积

1. 已知 ${F}_{1},{F}_{2}$ 分别是椭圆 $E : \frac{{x}^{2}}{12} + \frac{{y}^{2}}{3} = 1$ 的左，右焦点， $A$ 为 $E$ 的左顶点， $B$ 为 $E$ 的上顶点， $M$ 是 $E$ 上第四象限内一点， ${AM}$ 与 $y$ 轴交于点 $C,{BM}$ 与 $x$ 轴交于点 $D$ .

(1)证明:四边形 ${ABDC}$ 的面积是定值.

(2)求 $\bigtriangleup {CDM}$ 的面积的最大值.

2. 已知椭圆 $\Gamma : \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right) , A\text{ 、 }B$ 分别为 $\Gamma$ 的右顶点、上顶点.

(1)求以原点 $O$ 为圆心，且与直线 ${AB}$ 相切的圆的方程；

(2)过 $A\text{ 、 }B$ 作直线 ${AB}$ 的垂线，分别交椭圆 $\Gamma$ 于点 $D\text{ 、 }C$ ，若 ${BC} = {3AD}$ ，求 $\frac{a}{b}$ 的值；

(3)设 $a = 2, b = 1, P$ 是椭圆 $\Gamma$ 上非顶点的任意一点， $Q$ 是 $P$ 关于原点的对称点，直线 ${AQ}$ 与 ${BP}$ 交于点 $R$ ,求 $\bigtriangleup {PQR}$ 面积的最大值.

![](images/bo_d68j3a77aajc739aivpg_132_348_555_469_275_0.jpg)

20(2)图

![](images/bo_d68j3a77aajc739aivpg_132_931_554_431_264_0.jpg)

20(3)图

## 二、目标函数: 线段长

3. 曲线 ${x}^{2} - \frac{{y}^{2}}{a} = 1$ 与曲线 $\frac{{x}^{2}}{49} + \frac{{y}^{2}}{a} = 1\left( {a > 0}\right)$ 在第一象限的交点为 $A$ ,曲线 $C$ 是 ${x}^{2} - \frac{{y}^{2}}{a} = 1\left( {1 \leq x \leq {x}_{A}}\right)$ 和 $\frac{{x}^{2}}{49} + \frac{{y}^{2}}{a} = 1\left( {x \geq {x}_{A}}\right)$ 组成的封闭图形,曲线 $C$ 与 $x$ 轴的左交点为 $M$ ,右交点为 $N$ .

(1)设曲线 ${x}^{2} - \frac{{y}^{2}}{a} = 1$ 与曲线 $\frac{{x}^{2}}{49} + \frac{{y}^{2}}{a} = 1\left( {a > 0}\right)$ 具有相同的右焦点 $F$ ，求线段 ${AF}$ 的方程；

(2)在 1 )的条件下，曲线 $C$ 上存在多少个点 $S$ ，使得 $\left| {NS}\right| = \left| {NF}\right|$ ，请说明理由；

(3)设过原点 $O$ 的直线 $l$ 与以 $D\left( {t,0}\right) \left( {t > 0}\right)$ 为圆心的圆相切，其中圆的半径小于 1，切点为 $T$ ，直线 $l$ 与曲线 $C$ 在第一象限的两个交点为 $P, Q$ ,当 $\frac{1}{{\overrightarrow{OP}}^{2}} + \frac{1}{{\overrightarrow{OQ}}^{2}} = {\overrightarrow{OT}}^{2}$ 对任意直线 $l$ 恒成立,求 $t$ 的值.

4. 已知椭圆 $C : \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 的右顶点为 $\mathrm{A}$

(1)当 $a = 2, b = 1$ ，椭圆 $C$ 上存在点 $P$ ，使得 $\angle {OPA} = {90}^{ \circ }$ ，求点 $P$ 的横坐标；

(2)若椭圆 $C$ 上存在点 $P$ ，使得 $\angle {OPA} = {90}^{ \circ }$ ，求 $a$ 、 $b$ 满足的条件；

(3)当 $a = 2$ ， $b = 1$ ，椭圆 $C$ 上存在点 $P$ ，过点 $Q\left( {-4\text{ , }0}\right)$ 任作一动直线 $l$ 交椭圆 $C$ 于 $M$ 、 $N$ 两点，记 $\overrightarrow{QM} = \lambda \overrightarrow{QN}$ ，若在线段 ${MN}$ 上取一点 $R$ ，使得 $\overrightarrow{MR} = \lambda \overrightarrow{RN}$ ，求证:当直线 $l$ 转动时，点 $R$ 在某一直线上运动, 并求该定直线的方程。

# 第十七讲椭圆与双曲线 IV

## 三、目标函数: 斜率

1. 在平面直角坐标系 ${xOy}$ 中,已知椭圆 $\Gamma : \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 的左右顶点分别为 $A, B$ ,右焦点为 $F$ ,且椭圆 $\Gamma$ 过点 $\left( {0,\sqrt{5}}\right) ,\left( {2,\frac{5}{3}}\right)$ ,过点 $F$ 的直线 $l$ 与椭圆 $\Gamma$ 交于 $P, Q$ 两点 (点 $P$ 在 $x$ 轴的上方).

(1)求椭圆 $\Gamma$ 的标准方程；

(2)若 $\overline{PF} + 2\overline{QF} = \overline{0}$ ，求点 $P$ 的坐标；

(3)设直线 ${AP},{BQ}$ 的斜率分别为 ${k}_{1},{k}_{2}$ ，是否存在常数 $\lambda$ ，使得 ${k}_{1} + \lambda {k}_{2} = 0$ ？若存在，求出 $\lambda$ 的值；若不存在, 说明理由.

![](images/bo_d68j3a77aajc739aivpg_135_1179_945_372_299_0.jpg)

2. 已知 $A, B$ 为椭圆 $\frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 和双曲线 $\frac{{x}^{2}}{{a}^{2}} - \frac{{y}^{2}}{{b}^{2}} = 1$ 的公共顶点， $P, Q$ 分别为双曲线和椭圆上不同于 $A, B$ 的动点,且满足 $\overrightarrow{AP} + \overrightarrow{BP} = \lambda \left( {\overrightarrow{AQ} + \overrightarrow{BQ}}\right) ,\lambda \in R,\left| \lambda \right| > 1$ ,设直线 ${AP},{BP},{AQ}$ , ${BQ}$ 的斜率分别为 ${k}_{1},{k}_{2},{k}_{3},{k}_{4}$ .

1) 求证: 点 $P, Q, O$ 三点共线;

2) 求 ${k}_{1} + {k}_{2} + {k}_{3} + {k}_{4}$ 的值;

3) 若 ${F}_{1},{F}_{2}$ 分别为椭圆和双曲线的右焦点,且 $Q{F}_{1}//P{F}_{2}$ ,求 ${k}_{1}^{2} + {k}_{2}^{2} + {k}_{3}^{2} + {k}_{4}^{2}$ 的值.

![](images/bo_d68j3a77aajc739aivpg_136_892_691_652_395_0.jpg)

## 四、目标函数: 弦中点与弦中垂线

3. 已知椭圆 ${C}_{1} : \frac{{x}^{2}}{2} + \frac{{y}^{2}}{{b}^{2}} = 1$ 的左右焦点分别为 ${F}_{1},{F}_{2}$ ,离心率为 ${e}_{1}$ ; 双曲线 ${C}_{2} : \frac{{x}^{2}}{2} - \frac{{y}^{2}}{{b}^{2}} = 1$ 的左右焦点分别为 ${F}_{3},{F}_{4}$ ,离心率为 ${e}_{2}$ ,且 ${e}_{1}{e}_{2} = \frac{\sqrt{3}}{2}$ . 过点 ${F}_{1}$ 作不垂直于 $y$ 轴的直线 $l$ 交椭圆 ${C}_{1}$ 于 $A, B$ 两点,点 $M$ 为线段 ${AB}$ 的中点,直线 ${OM}$ 交双曲线 ${C}_{2}$ 于 $P, Q$ 两点.

(1)求 ${C}_{1}$ ， ${C}_{2}$ 的方程；

( 2 )若 $\overrightarrow{A{F}_{1}} = 3\overrightarrow{{F}_{1}B}$ ，求直线 ${PQ}$ 的方程；

(3)求四边形 ${APBQ}$ 面积的最小值.

![](images/bo_d68j3a77aajc739aivpg_137_965_788_524_322_0.jpg)

4. 0 为坐标原点，曲线 ${C}_{1} : \frac{{x}^{2}}{{a}^{2}} - {y}^{2} = 1\left( {a > 0}\right)$ 和曲线 ${C}_{2} : \frac{{x}^{2}}{4} + \frac{{y}^{2}}{2} = 1$ 有公共点，直线 ${l}_{1} : y = {k}_{1}x + {b}_{1}$ 与曲线 ${C}_{1}$ 的左支相交于 $A, B$ 两点,线段 ${AB}$ 的中点为 $M$ .

(1)若曲线 ${C}_{1}$ 和 ${C}_{2}$ 有且仅有两个公共点，求曲线 ${C}_{1}$ 的离心率和渐近线方程；

(2)若直线 ${OM}$ 经过曲线 ${C}_{2}$ 上的点 $T\left( {\sqrt{2}, - 1}\right)$ ，且 ${a}^{2}$ 为正整数，求 $a$ 的值；

(3)若直线 ${l}_{2} : y = {k}_{2}X + {b}_{2}$ 与曲线 ${C}_{2}$ 相交于 $C, D$ 两点，且直线 ${OM}$ 经过线段 ${CD}$ 中点 $N$ ，且直线 ${OM}$ 经过线段 ${CD}$ 中点 $N$ ,证明: ${k}_{1}^{2} + {k}_{2}^{2} > 1$ .

![](images/bo_d68j3a77aajc739aivpg_138_1238_742_326_241_0.jpg)

5. 已知椭圆 $\frac{{x}^{2}}{6} + \frac{{y}^{2}}{3} = 1$ 上有两点 $P\left( {-2,1}\right)$ 及 $Q\left( {2, - 1}\right)$ ，直线 $l : y = {kx} + m$ 与椭圆交于 $A$ ， $B$ 两点，与线段 ${PQ}$ 交于点 $C$ (异于 $P, Q$ ).

(1)当 $k = 1$ 且 $\overrightarrow{PC} = \frac{1}{2}\overrightarrow{CQ}$ 时，求直线 $l$ 的方程；

(2)当 $k = 2$ 时，求四边形 ${PAQB}$ 面积的取值范围；

(3)记直线 ${PA},{PB},{QA},{QB}$ 的斜率依次为 ${k}_{1},{k}_{2},{k}_{3},{k}_{4}$ ，当 $m \neq 0$ 且线段 ${AB}$ 的中点 $M$ 在直线 $y = - x$ 上时,计算 ${k}_{1} \cdot {k}_{2}$ 的值,并证明: ${k}_{1}^{2} + {k}_{2}^{2} > 2{k}_{3}{k}_{4}$ .

# 第十八讲抛物线 I

## 一、抛物线中的常规问题

1. 已知平面内一动点 $P$ 到点 $F\left( {1,0}\right)$ 的距离与点 $P$ 到 $y$ 轴的距离的差等于 1,设点 $P$ 的轨迹为 $C$ ,过点 $F$ 作两条斜率存在且互相垂直的直线 ${l}_{1},{l}_{2}$ ,设 ${l}_{1}$ 与轨迹 $C$ 相交于点 $A, B,{l}_{2}$ 与轨迹 $C$ 相交于点 $D, E$ ,求 $\overrightarrow{AD} \cdot \overrightarrow{EB}$ 的最小值。

2. 设 ${C}_{1}$ 是以 $F$ 为焦点的抛物线 ${y}^{2} = {2px}\left( {p > 0}\right) ,{C}_{2}$ 是以直线 ${2x} - \sqrt{3}y = 0$ 与 ${2x} + \sqrt{3}y = 0$ 为渐近线，以 $\left( {0,\sqrt{7}}\right)$ 为焦点的双曲线.

(1)求双曲线 ${C}_{2}$ 的标准方程；(2)若 ${C}_{1}$ 与 ${C}_{2}$ 在第一象限有两个公共点 $A$ 、 $B$ ；

① 求 $p$ 的取值范围，并求 $\overrightarrow{FA} \cdot \overrightarrow{FB}$ 的最大值；

② 是否存在正数 $p$ ，使得此时 $\bigtriangleup {FAB}$ 的重心 $G$ 恰好在双曲线 ${C}_{2}$ 的渐近线上？若存在，求出 $p$ 的值；若不存在, 请说明理由.

3. 【2018 上海高考 20 题】设常数 $t > 2$ ，在平面直角坐标系 ${xOy}$ 中，已知点 $F\left( {2,0}\right)$ ，直线 $l : x = t$ ，曲线 $\Gamma : {y}^{2} = {8x}\left( {0 \leq x \leq t, y \geq 0}\right) , l$ 与 $x$ 轴交于点 $A$ 、与 $\Gamma$ 交于点 $B, P\text{ 、 }Q$ 分别是曲线 $\Gamma$ 与线段 ${AB}$ 上的动点.

(1)用 $t$ 表示点 $B$ 到点 $F$ 的距离；

(2)设 $t = 3,\left| {FQ}\right| = 2$ ，线段 ${OQ}$ 的中点在直线 ${FP}$ 上，求 $\bigtriangleup {AQP}$ 的面积；

(3)设 $t = 8$ ，是否存在以 ${FP}\text{ 、 }{FQ}$ 为邻边的矩形 ${FPEQ}$ ，使得点 $E$ 在 $\Gamma$ 上？若存在，求点 $P$ 的坐标；若不存在, 说明理由.

4. 已知椭圆 ${C}_{1} : \frac{{x}^{2}}{2} + {y}^{2} = 1$ ，抛物线 ${C}_{2} : {y}^{2} = {2px}\left( {p > 0}\right)$ ，点 $A$ 是椭圆 ${C}_{1}$ 与抛物线 ${C}_{2}$ 在第一象限的交点， 若存在过点 $A$ 且不过原点的直线 $l$ 交椭圆 ${C}_{1}$ 于点 $B$ ,交抛物线 ${C}_{2}$ 于 $M$ ,使得 $M$ 为线段 ${AB}$ 的中点，求 $p$ 的最大值和 $p$ 取到最大值时直线 $l$ 的方程.

![](images/bo_d68j3a77aajc739aivpg_143_1176_481_377_320_0.jpg)

## 二、抛物线中的面积

5. 已知 ${AB}\text{ 、 }{CD}$ 都过抛物线 ${y}^{2} = {2px}$ 焦点且 ${AB} \bot {CD},{AC} \bot {BD}$ ,求 ${ABCD}$ 面积。

6. 已知抛物线 $C$ 顶点在原点，焦点在 $y$ 轴上，抛物线 $C$ 上一点 $Q\left( {a,2}\right)$ 到焦点的距离为 3,线段 ${AB}$ 的两端点 $A\left( {{x}_{1},{y}_{1}}\right) \text{ 、 }B\left( {{x}_{2},{y}_{2}}\right)$ 在抛物线 $C$ 上.

(1)求抛物线 $C$ 的方程；

(2)若 $y$ 轴上存在一点 $M\left( {0, m}\right)$ ( $m > 0$ )，使线段 ${AB}$ 经过点 $M$ 时，以 ${AB}$ 为直径的圆经过原点，求 $m$ 的值;

(3)在抛物线 $C$ 上存在点 $N\left( {{x}_{3},{y}_{3}}\right)$ ，满足 ${x}_{3} < {x}_{1} < {x}_{2}$ ，若 $\bigtriangleup {ABN}$ 是以角 $A$ 为直角的等腰直角三角形，求 $\bigtriangleup {ABN}$ 面积的最小值.

# 第十九讲抛物线 II

## 三、抛物线与切线

1. 已知 $A, B, C$ 是抛物线 ${\Gamma }_{1} : {x}^{2} = y$ 上的三个点,且直线 ${CA},{CB}$ 分别与抛物线 ${\Gamma }_{2} : {y}^{2} = {4x}$ 相切, $F$ 为抛物线 ${\Gamma }_{1}$ 的焦点.

(1)若点 $C$ 的横坐标为 ${x}_{3}$ ，用 ${x}_{3}$ 表示线段 ${CF}$ 的长；

(2)若 ${CA}\bot {CB}$ ，求点 $C$ 的坐标；

(3)证明:直线 ${AB}$ 与抛物线 ${\Gamma }_{2}$ 相切.

![](images/bo_d68j3a77aajc739aivpg_146_1215_843_310_301_0.jpg)

2. 已知点 $P$ 在抛物线 $C : {y}^{2} = {4x}$ 上,过点 $P$ 作圆 $M : {\left( x - 3\right) }^{2} + {y}^{2} = {r}^{2}\left( {0 < r \leq \sqrt{2}}\right)$ 的两条切线,与抛物线 $C$ 分别交于 $A, B$ 两点，切线 ${PA},{PB}$ 与圆 $M$ 分别相切于点 $E, F$ .

1)若点 $P$ 到圆心 $M$ 的距离与它到抛物线 $C$ 的准线的距离相等，求点 $P$ 的坐标；

2. 若点 $P$ 的坐标为 $\left( {1,2}\right)$ ,且 $r = \sqrt{2}$ 时,求 $\overrightarrow{PE} \cdot \overrightarrow{PF}$ 的值;

3. 若点 $P$ 的坐标为 $\left( {1,2}\right)$ ,设线段 ${AB}$ 中点的纵坐标为 $t$ ,求 $t$ 的取值范围.

3) 已知抛物线 ${C}_{1} : {y}^{2} = {4ax}\left( {a > 0}\right)$ 和 ${C}_{2} : {x}^{2} = {4y}$ 在第一象限内的交点为 $P,{C}_{1}$ 和 ${C}_{2}$ 在点 $P$ 处的切线分别为 ${l}_{1}$ 和 ${l}_{2}$ ,定义 ${l}_{1}$ 和 ${l}_{2}$ 的夹角为曲线 ${C}_{1},{C}_{2}$ 的夹角.

1. 求点 $P$ 的坐标;

2. 若 ${C}_{1},{C}_{2}$ 的夹角为 $\arctan \frac{3}{4}$ ,求 $a$ 的值;

3. 若直线 ${l}_{3}$ 既是 ${C}_{1}$ 也是 ${C}_{2}$ 的切线,切点分别为 $Q, R$ ,当 $\bigtriangleup {PQR}$ 为直角三角形时,求出相应的 $a$ 的值.

4) 在平面直角坐标系 ${xOy}$ 中,一动圆经过点 $A\left( {\frac{1}{2},0}\right)$ 且与直线 $x = - \frac{1}{2}$ 相切,设该动圆圆心的轨迹为曲线 $M, P$ 是曲线 $M$ 上一点.

1)求曲线 $M$ 的方程；

2. 过点 $A$ 且斜率为 $k$ 的直线 $l$ 与曲线 $M$ 交于 $B, C$ 两点，若 $l//{OP}$ 且直线 ${OP}$ 与直线 $x = l$ 交于 $Q$ 点，求 $\frac{\left| {AB}\right| \cdot \left| {AC}\right| }{\left| {OP}\right| \cdot \left| {OQ}\right| }$ 的值;

3. 若点 $D, E$ 在 $y$ 轴上, $\bigtriangleup {PDE}$ 的内切圆的方程为 ${\left( x - 1\right) }^{2} + {y}^{2} = 1$ ,求 $\bigtriangleup {PDE}$ 面积的最小值.

# 第二十讲常见定点、定值、定直线问题 I

1. 已知椭圆 $C : \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 的左、右焦点分别为 ${F}_{1}\text{ 、 }{F}_{2}$ ，设过 ${F}_{2}$ 且不与坐标轴垂直的直线 $l$ 与 $C$ 交于 $P\text{ 、 }Q$ 两点 $M$ 是点 $P$ 关于 $x$ 轴的对称点. 在 $x$ 轴上是否存在一个定点 $N$ ,使得 $M\text{ 、 }Q\text{ 、 }N$ 三点共线,若存在,求出点 $N$ 的坐标; 若不存在,请说明理由.

2. 已知椭圆 $\Gamma : \frac{{x}^{2}}{2} + {y}^{2} = 1$ 的右焦点为 $F$ ，直线 $x = t$ ( $t \in \left( {-\sqrt{2},\sqrt{2}}\right)$ )与该椭圆交于点 $A$ 、 $B$ (点 $A$ 位于 $x$ 轴上方)， $x$ 轴上有一定点 $C\left( {2,0}\right)$ ，直线 ${AF}$ 与直线 ${BC}$ 交于点 $P$ 。求证:点 $P$ 在椭圆 $\Gamma$ 上.

3. 已知椭圆 $C$ 为 $\frac{{x}^{2}}{4} + \frac{{y}^{2}}{1} = 1$ ，设直线 $x = {my} + 1$ 与椭圆交于 $P\text{ 、 }Q$ 点，直线 ${A}_{1}P$ 与 ${A}_{2}Q$ 交于点 $S$ ，试问: $m$ 变化时， $S$ 是否在定直线上。

4. 已知双曲线 $\frac{{x}^{2}}{9} - \frac{{y}^{2}}{16} = 1$ 的左、右顶点为 $A\text{ 、 }B$ ,右焦点为 $F$ 。设过直 $T\left( {9, m}\right)$ 的直线 ${TA}\text{ 、 }{TB}$ 与此双曲线分别交于点 $M\left( {{x}_{1},{y}_{1}}\right) \text{ 、 }N\left( {{x}_{2},{y}_{2}}\right)$ ,求证: 直线 ${MN}$ 过定点。

5. 已知椭圆 $C : \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 过点 $\left( {1,\frac{\sqrt{2}}{2}}\right)$ ，离心率为 $\frac{\sqrt{2}}{2}$ ，点 $A$ 、 $B$ 分别是椭圆 $C$ 的上、下顶点，点 $M$ 是椭圆 $C$ 上异于 $A$ 、 $B$ 的一点.

(1)求椭圆 $C$ 的方程；

(2)若点 $P$ 在直线 $x - y + 2 = 0$ 上，且 $\overrightarrow{BP} = 3\overrightarrow{BM}$ ，求 $\bigtriangleup {PMA}$ 的面积；

(3)过点 $M$ 作斜率为 $k$ 的直线分别交椭圆 $C$ 于另一点 $N$ ，交 $y$ 轴于点 $D$ ，且点 $D$ 在线段 ${OA}$ 上(不包括端点)，直线 ${NA}$ 与直线 ${BM}$ 交于点 $P$ ，求 $\overrightarrow{OD} \cdot \overrightarrow{OP}$ 的值.

![](images/bo_d68j3a77aajc739aivpg_154_1165_603_324_351_0.jpg)

# 第二十一讲常见定点、定值、定直线问题 II

1. 已知动点 $M$ 到直线 $x + 2 = 0$ 的距离比到点 $F\left( {1,0}\right)$ 的距离大 1.

1)求动点 $M$ 所在的曲线 $C$ 的方程；

2. 已知点 $P\left( {1,2}\right)$ ， $A$ ， $B$ 是曲线 $C$ 上的两个动点，如果直线 ${PA}$ 的斜率与直线 ${PB}$ 的斜率互为相反数，证明: 直线 ${AB}$ 的斜率为定值，并求出这个定值；

3. 已知点 $P\left( {1,2}\right) , A, B$ 是曲线 $C$ 上的两个动点，如果直线 ${PA}$ 的斜率与直线 ${PB}$ 的斜率之和为 2,证明: 直线 ${AB}$ 过定点.

2) 已知抛物线 $\Gamma : {y}^{2} = {4x}$ .

1. 求抛物线 $\Gamma$ 的焦点 $F$ 的坐标和准线 $l$ 的方程:

2. 过焦点 $F$ 且斜率为 $\frac{1}{2}$ 的直线与抛物线 $\Gamma$ 交于两个不同的点 $A, B$ ,求线段 ${AB}$ 的长;

3. 已知点 $P\left( {1,2}\right)$ ，是否存在定点 $Q$ ，使得过点 $Q$ 的直线与抛物线 $\Gamma$ 交于两个不同的点 $M$ ， $N$ (均不与点 $P$ 重合),且以线段 ${MN}$ 为直径的圆恒过点 $P$ ? 若存在,求出点 $Q$ 的坐标; 若不存在,请说明理由.

3) 已知抛物线 $\Gamma : {y}^{2} = {4x}$ 的焦点为 $F$ ，准线为 $l$ .

1. 若 $F$ 为双曲线 $C : \frac{{x}^{2}}{{a}^{2}} - 2{y}^{2} = 1\left( {a > 0}\right)$ 的一个焦点,求双曲线 $C$ 的离心率 $e$ :

2. 设 $l$ 与 $x$ 轴的交点为 $E$ ,点 $P$ 在第一象限,且在 $\Gamma$ 上,若 $\frac{\left| PF\right| }{\left| PE\right| } = \frac{\sqrt{2}}{2}$ ,求直线 ${EP}$ 的方程;

3. 经过点 $F$ 的直线 ${l}^{\prime }$ 与 $\Gamma$ 相交于 $A, B$ 两点， $O$ 为坐标原点，直线 ${OA},{OB}$ 分别与 $l$ 相交于点 $M, N$ ，试问以线段 ${MN}$ 为直径的圆是否过定点? 若是,求出定点的坐标; 若不是,说明理由.

4) 已知抛物线 $l$ : ${y}^{2} = {4x}$ 的焦点为 $F$ ，准线为 $l$ ，直线 $l$ ² 经过点 $F$ 且与 $\Gamma$ 交于 $A, B$ 两点.

1)求以 $F$ 为焦点，坐标轴为对称轴，离心率为 $\frac{1}{2}$ 的椭圆的标准方程；

2. 若 $\left| {AB}\right| = 5$ ，求线段 ${AB}$ 的中点到 $x$ 轴的距离；

3. 设 $O$ 为坐标原点， $M$ 为 $\Gamma$ 上的动点，直线 ${AM}$ ， ${BM}$ 分别与准线 $l$ 交于 $C$ ， $D$ 两点，证明: $\overrightarrow{OC} \cdot \overrightarrow{OD}$ 为常数.

5) 已知 ${y}^{2} = x$ 上有一动点 $M\left( {{x}_{0},{y}_{0}}\right)$ ,过 $M$ 分别作两直线交抛物线于 $P\text{ 、 }Q$ ,交 $x = t$ 于 $A\text{ 、 }B$ 。是否存在 $t$ ,使 ${y}_{A} \cdot {y}_{B} = 1$ 且 ${y}_{P} \cdot {y}_{Q}$ 为常数。若存在则求出 $t$ 的值,若不存在,请说明理由。

# 课后练习 18

1. 从抛物线 ${y}^{2} = {ax}$ 外一点 $A\left( {\cdot 2, - 4}\right)$ 做倾斜角为 ${45}^{ \circ }$ 的直线，与抛物线交于两个不同的点 $P\text{ 、 }Q$ ，若 $\left| {AP}\right|$ 、 $\left| {PQ}\right| \text{ 、 }\left| {AQ}\right|$ 成等比数列,求抛物线的方程.

2. 已知抛物线 ${y}^{2} = {4x}$ 的焦点为 $F$ ， $A, B$ 为抛物线上两点，且 ${AF}\bot {BF}$ ，求 $\bigtriangleup {AFB}$ 面积的取值范围。

3. 如图，由半圆 ${x}^{2} + {y}^{2} = {r}^{2}\left( {r \leq 0, r > 0}\right)$ 和部分抛物线 $y = a\left( {{x}^{2} - 1}\right) \left( {y \geq 0, a > 0}\right)$ 合成的曲线 $C$ 称为“羽毛球形线",曲线 $C$ 与 $x$ 轴有 $A\text{ 、 }B$ 两个交点,且经过点 $\left( {2,3}\right)$ ;

(1)求 $a\text{ 、 }r$ 的值；

(2)设 $N\left( {0,2}\right)$ ， $M$ 为曲线 $C$ 上的动点，求 $\left| {MN}\right|$ 的最小值；

(3)过 $A$ 且斜率为 $k$ 的直线 $l$ 与“羽毛球形线”相交于 $P$ 、 $A$ 、 $Q$ 三点，问是否存在实数 $k$ ，使得 $\angle {QBA} = \angle {PBA}$ ？ 若存在,求出 $k$ 的值,若不存在,请说明理由.

![](images/bo_d68j3a77aajc739aivpg_161_1170_611_355_378_0.jpg)

4. 在平面直角坐标系 ${xOy}$ 中,点 $A\left( {-2,0}\right)$ ,过动点 $P$ 作直线 $x = - 4$ 的垂线,垂足为 $M$ ,且 $\overrightarrow{AM} \cdot \overrightarrow{AP} = - 4$ , 记动点 $P$ 的轨迹为曲线 $E$ .

(1)求曲线 $E$ 的方程；

(2)过点 $A$ 的直线 $l$ 交曲线 $E$ 于不同的两点 $B\text{ 、 }C$ ；

① 若 $B$ 为线段 ${AC}$ 的中点，求直线 $l$ 的方程；② 设 $B$ 关于 $x$ 轴的对称点为 $D$ ，求 $\bigtriangleup {ACD}$ 面积 $S$ 的取值范围.

5. 已知抛物线 ${y}^{2} = {2px}\left( {p > 0}\right)$ ,过动点 $M\left( {a,0}\right)$ 且斜率为 1 的直线 $l$ 与该抛物线交于不同两点 $A, B$ , $\left| {AB}\right| \leq {2p}$ 。

(1)求 $a$ 取值范围:

(2)若线段 ${AB}$ 垂直平分线交 $x$ 轴于点 $N$ ，求 $\bigtriangleup {NAB}$ 面积的最大值。

# 课后练习 19

1. 已知抛物线 $C : {x}^{2} = {2py}\left( {p > 0}\right)$ 的焦点坐标为 $\left( {0,1}\right)$

(1)求抛物线方程；

(2)过直线 $y = x - 2$ 上一点 $P\left( {t, t - 2}\right)$ 作抛物线的切线切点为 $A, B$

① 设直线 ${PA}\text{ 、 }{AB}\text{ 、 }{PB}$ 的斜率分别为 ${k}_{1},{k}_{2},{k}_{3}$ ,求证: ${k}_{1},{k}_{2},{k}_{3}$ 成等差数列;

② 若以切点 $B$ 为圆心 $r$ 为半径的圆与抛物线 $C$ 交于 $D, E$ 两点且 $D, E$ 关于直线 ${AB}$ 对称，求点 $P$ 横坐标的取值范围.

![](images/bo_d68j3a77aajc739aivpg_164_1095_680_413_375_0.jpg)

2. 的已知点 $R\left( {{x}_{0},{y}_{0}}\right)$ 在 $\Gamma : {y}^{2} = {2px}$ 上，以 $R$ 为切点的 $\Gamma$ 的切线的斜率为 $\frac{p}{{y}_{0}}$ ，过 $\Gamma$ 外一点 $A$ (不在 $x$ 轴上) 作 $\Gamma$ 的切线 ${AB},{AC}$ ,点 $B\text{ 、 }C$ 为切点,作平行于 ${BC}$ 的切线 ${MN}$ (切点为 $D$ ),点 $M\text{ 、 }N$ 分别是与 ${AB}$ 、 ${AC}$ 的交点 (如图)；

(1)用 $B\text{ 、 }C$ 的纵坐标 $s\text{ 、 }t$ 表示直线 ${BC}$ 的斜率；

(2)若直线 ${AD}$ 与 ${BC}$ 的交点为 $E$ ，证明 $D$ 是 ${AE}$ 的中点；

(3)设三角形 $\bigtriangleup {ABC}$ 面积为 $S$ ，若将由过 $\Gamma$ 外一点的两条切线及第三条切线(平行于两切线切点的连线) 围成的三角形叫做“切线三角形”，如 $\bigtriangleup {AMN}$ ，再由 $M$ 、 $N$ 作“切线三角形”，并依这样的方法不断作切线二角形……，试利用“切线三角形”的面积和计算由抛物线及 ${BC}$ 所围成的阴影部分的面积 $T$ ；

![](images/bo_d68j3a77aajc739aivpg_165_1097_626_433_405_0.jpg)

3. 若 $A, B$ 是曲线 ${y}^{2} = {4x}$ 上的不同两点,弦 ${AB}$ (不平行于 $y$ 轴) 的垂直平分线与 $x$ 轴相交于点 $P$ ,则称弦 ${AB}$ 是点 $P$ 的一条“相关弦”。给定 ${x}_{0} > 2$ 。

(1)证明:点 $P\left( {{x}_{0},0}\right)$ 的所有“相关弦”的中点的横坐标相同；

(2)点 $P\left( {{x}_{0},0}\right)$ 的“相关弦”的弦长中是否存在最大值？设明理由。

4. 已知抛物线 ${y}^{2} = x, O$ 为坐标原点.

(1)过抛物线焦点 $F$ 的直线交抛物线于 $A, B$ 两点，求 $\overrightarrow{OA} \cdot \overrightarrow{OB}$ 的值；

(2)过抛物线上的一点 $C\left( {{x}_{0},{y}_{0}}\right)$ ，分别作两条直线交抛物线于另外两点 $P\left( {{x}_{P},{y}_{P}}\right)$ ， $Q\left( {{x}_{Q},{y}_{Q}}\right)$ ，交直线 $x = - 1$ 于 ${A}_{1}\left( {-1,1}\right) ,{B}_{1}\left( {-1, - 1}\right)$ 两点,证明: ${y}_{P} \cdot {y}_{Q}$ 为常数;

(3)已知点 $D\left( {1,1}\right)$ ，在抛物线上是否存在异于点 $D$ 的两个不同的点 $M, N$ ，使得 ${DM}\bot {MN}?$ 若存在，求 $N$ 点纵坐标的取值范围；若不存在，请说明理由.

5. 【2019 年上海春考 20 题】已知抛物线 ${y}^{2} = {4x}$ ， $F$ 为焦点， $P$ 为准线 $l$ 上一动点，线段 ${PF}$ 与抛物线交于点 $Q$ ,定义 $d\left( P\right) = \frac{\left| FP\right| }{\left| FQ\right| }$ .

(1)若点 $P$ 坐标为 $\left( {-1, - \frac{8}{3}}\right)$ ，求 $d\left( P\right)$ ；

(2)求证:存在常数 $a$ ，使得 ${2d}\left( P\right) = \left| {FP}\right| + a$ 恒成立；

(3)设 ${P}_{1}\text{ 、 }{P}_{2}\text{ 、 }{P}_{3}$ 为准线 $l$ 上的三点，且 $\left| {{P}_{1}{P}_{2}}\right| = \left| {{P}_{2}{P}_{3}}\right|$ ，试比较 $d\left( {P}_{1}\right) + d\left( {P}_{3}\right)$ 与 ${2d}\left( {P}_{2}\right)$ 的大小.

# 课后练习 20

1. 已知椭圆 $C : \frac{{x}^{2}}{4} + \frac{{y}^{2}}{3} = 1$ 的左、右焦点分别为 ${F}_{1}\text{ 、 }{F}_{2}$ ,设过 ${F}_{2}$ 且不与坐标轴垂直的直线 $l$ 与 $C$ 交于 $P\text{ 、 }Q$ 两点, $M$ 是点 $P$ 关于 $x$ 轴的对称点. 在 $x$ 轴上是否存在一个定点 $N$ ,使得 $M\text{ 、 }Q\text{ 、 }N$ 三点共线,若存在,求出点 $N$ 的坐标; 若不存在,请说明理由.

2. 已知椭圆 $\Gamma : \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 的右焦点坐标为 $\left( {2,0}\right)$ ，且长轴长为短轴长的 $\sqrt{2}$ 倍，直线 $l$ 交椭圆 $\Gamma$ 于不同的两点 $M,{N.1}$ ) 求椭圆 $\Gamma$ 的方程；

(1)若直线 $l$ 经过点 $T\left( {0,4}\right)$ ，且 $\bigtriangleup {OMN}$ 的面积为 $2\sqrt{2}$ ，求直线 $l$ 的方程；

(2)若直线 $l$ 的方程为 $y = {kx} + t\left( {k \neq 0}\right)$ ，点 $M$ 关于 $x$ 轴的对称点为 ${M}_{1}$ ，直线 ${MN}$ ， ${M}_{1}N$ 分别与 $x$ 轴相交于 $P, Q$ 两点,证明: $\left| {OP}\right| \cdot \left| {OQ}\right|$ 为定值.

![](images/bo_d68j3a77aajc739aivpg_170_1099_598_407_334_0.jpg)

3. 知椭圆 $\Gamma : \frac{{x}^{2}}{8} + \frac{{y}^{2}}{4} = 1$ 的上、下顶点分别为 $A\text{ 、 }B$ ,经过点 $P\left( {0,4}\right)$ 的直线 $l$ 与椭圆 $\Gamma$ 相交于 $M\text{ 、 }N$ 两点 (不同于 $A\text{ 、 }B$ 两点) 。设直线 ${AN}\text{ 、 }{BM}$ 相交于点 $Q\left( {m, n}\right)$ ,求证: $n$ 是定值.

4. 设 ${A}_{1},{A}_{2}$ 分别是相圆 $\Gamma : \frac{{x}^{2}}{{a}^{2}} + {y}^{2} = 1\left( {a > 1}\right)$ 的左右顶点,点 $B$ 为椭圆的上顶点.

(1)若 $\overrightarrow{{A}_{1}B} \cdot \overrightarrow{{A}_{2}B} = - 4$ ，求椭圆 $\Gamma$ 的方程；

(2)设 $a = \sqrt{2}$ ， ${F}_{2}$ 是椭圆的右焦点，点 $Q$ 是椭圆第二象限部分上一点，若线段 ${F}_{2}Q$ 的中点 $M$ 在 $y$ 轴上，求 $\bigtriangleup {F}_{2}{BQ}$ 的面积;

(3)设 $a = 3$ ，点 $P$ 是直线 $x = 6$ 上的动点，点 $C, D$ 是椭圆上异于左右顶点的两点，且 $C, D$ 分别在直线 $P{A}_{1}, P{A}_{2}$ 上,证明: 直线 ${CD}$ 恒过一定点.

![](images/bo_d68j3a77aajc739aivpg_172_1069_723_444_362_0.jpg)

# 课后练习 21

1. 已知椭圆 $\Gamma : \frac{{x}^{2}}{12} + \frac{{y}^{2}}{8} = 1$ 的左、右焦点分别为 ${F}_{1},{F}_{2}$ ,过点 ${F}_{1}$ 的直线 $l$ 交椭圆于 $A, B$ 两点,交 $y$ 轴于点 $P\left( {0, t}\right)$ .

(1)若 ${F}_{1}P \bot {F}_{2}P$ ，求 $t$ 的值；

(2)若点 $A$ 在第一象限，满足 $\overrightarrow{{F}_{1}A} \cdot \overrightarrow{{F}_{2}A} = 7$ ，求 $t$ 的值；

(3)在平面内是否存在定点 $Q$ ，使得 $\overrightarrow{QA} \cdot \overrightarrow{QB}$ 为定值？若存在，求出点 $Q$ 的坐标；若不存在，说明理由.

![](images/bo_d68j3a77aajc739aivpg_173_1190_786_312_257_0.jpg)

2. 知椭圆 $C : \frac{{x}^{2}}{t} + {y}^{2} = 1\left( {t > 1}\right)$ 的左右焦点分别为 ${F}_{1},{F}_{2}$ ,直线 $l : y = {kx} + m\left( {m \neq 0}\right)$ 与椭圆 $C$ 交于 $M$ , $N$ 两点 ( $M$ 点在 $N$ 点的上方),与 $y$ 轴交于点 $E$ .

1) 当 $t = 2$ 时,点 $A$ 为椭圆 $C$ 除顶点外任一点,求 $\bigtriangleup A{F}_{1}{F}_{2}$ 的周长;

2) 当 $t = 3$ 且直线 $l$ 过点 $D\left( {-1,0}\right)$ 时,设 $\overline{EM} = \lambda \overline{DM},\overrightarrow{EN} = \mu \overrightarrow{DN}$ ,证明: $\lambda + \mu$ 为定值,并求出该值;

3) 若椭圆 $C$ 的离心率为 $\frac{\sqrt{3}}{2}$ ，求 $k$ 的值，使 ${\left| OM\right| }^{2} + {\left| ON\right| }^{2}$ 为定值，并求此时 $\bigtriangleup {MON}$ 面积的最大值.

3. 已知双曲线 $\Gamma : \frac{{x}^{2}}{4} - \frac{{y}^{2}}{12} = 1, F$ 为左焦点， $P$ 为直线 $x = 1$ 上一动点， $Q$ 为线段 ${PF}$ 与 $\Gamma$ 的交点. 定义:

$$
d\left( P\right)  = \frac{\left| FP\right| }{\left| FQ\right| }
$$

1. 若点 $Q$ 的纵坐标为 $\sqrt{15}$ ,求 $d\left( P\right)$ 的值;

2. 设 $d\left( P\right) = \lambda$ ,点 $P$ 的纵坐标为 $t$ ,试将 ${t}^{2}$ 表示成 $\lambda$ 的函数并求其定义域:

3. 证明: 存在常数 $m, n$ ,使得 ${md}\left( P\right) = \left| {FP}\right| + n$ .

4) 已知椭圆 $E : \frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ 的左右焦点分别为 ${F}_{1},{F}_{2}$ ,短轴两个端点为 $A, B$ ,且四边形 ${F}_{1}A{F}_{2}B$ 是边长为 2 的正方形。

(1)求椭圆方程；

(2)若 $C, D$ 分别是椭圆长轴的左右端点，动点 $M$ 满足 ${MD}\bot {CD}$ ，连接 ${CM}$ ，交椭圆于点 $P$ 。证明: $\overrightarrow{OM} \cdot \overrightarrow{OP}$ 为定值。

5. 已知椭圆 $\frac{{x}^{2}}{{a}^{2}} + \frac{{y}^{2}}{{b}^{2}} = 1\left( {a > b > 0}\right)$ ，直线 $l$ 与椭圆交于 $P, Q$ 两点，与 $x$ 轴交于点 $N$ 。若 $A$ 为该椭圆上的点，且 ${k}_{AP} \cdot {k}_{AQ}$ 为定值。请证明: $N$ 为定点是 $A$ 为椭圆左右顶点的充要条件。
