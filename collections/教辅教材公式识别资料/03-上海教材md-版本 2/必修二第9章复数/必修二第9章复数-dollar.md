---
title: 必修二第9章复数-dollar
来源: 沪教版教材
---
### 9.1 复数及其四则运算

复数

实系数一元二次方程并不是总有实数解的, 这是因为在实数范围内负数不能进行开平方运算. 在数学的发展史上有一件有意思的事: 数学家在研究三次方程求解的过程中, 即使最终得到实根, 过程中却常常要对一些负数开平方, 遇到了难以自圆其说的尴尬. 于是, 一种被称作为“虚数”的新数于 16 世纪开始被引入了数学. 实数与虚数合称为复数.

复数是人类理性思维的演绎成果, 它的产生首先是因为数学家解决数学自身问题的需要, 在很长的一段时间内, 人们并不清楚它与现实世界到底有怎样的联系. 后来，数学家建立了复数与向量, 即复数与几何的关联, 在大学学习力学和电磁学时, 会看到复数在其中的重要作用, 复数在数学及其他科学领域中也越来越体现出它的重要性. 现在, 复数已经成为数学工作者与许多领域的科技人员熟练掌握并广泛应用的基本数学工具.

## 1 复数的引入与复数的四则运算

为了解决负数的开平方问题, 数学家引入了一个不同于实数的新数 i, 称为虚数单位 (imaginary unit), 并规定

$$
{\mathrm{i}}^{2} =  - 1,
$$

即规定 $\mathrm{i}$ 是 -1 的一个平方根. 更一般地,把任意 $b \in  \mathbf{R}$ 与虚数单位 $\mathrm{i}$ 的乘积记为 $b\mathrm{i}$ ,并规定虚数单位与实数间的乘法满足交换律与结合律. 对于 $b\mathrm{i}$ ,我们有,

$$
{\left( b\mathrm{i}\right) }^{2} = \left( {b\mathrm{i}}\right) \left( {b\mathrm{i}}\right)  = {b}^{2}{\mathrm{i}}^{2} =  - {b}^{2},
$$

即 $b\mathrm{i}$ 是 $- {b}^{2}$ 的一个平方根. 只要 $b \neq  0, - {b}^{2}$ 就是一个负数,而且任何负数都具有这个形式. 因此, 引进虚数单位后, 我们得到了所有负数的平方根.

一个实数 $a$ 可以与形如 $b\mathrm{i}\left( {b \in  \mathbf{R}}\right)$ 的数相加,规定把它们的和用实系数二项式的形式表示成 $a + b\mathrm{i}$ .

定义 形如 $a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 的数称为一个复数 (complex number).

全体复数构成的集合用字母 $\mathbf{C}$ 表示.

我们约定:

(1)复数 $a + b\mathrm{i} = 0\left( {a\text{ 、 }b \in  \mathbf{R}}\right)  \Leftrightarrow  a = 0$ 且 $b = 0$ ；

(2)复数 $a + b\mathrm{i} = c + d\mathrm{i}\left( {a\text{ 、 }b\text{ 、 }c\text{ 、 }d \in  \mathbf{R}}\right)  \Leftrightarrow  a = c$ 且 $b = d$ .

在前面规定的实数与虚数单位之间的乘法以及实数与 $b\mathrm{i}$ 形式的复数的加法基础上, 可以定义两个复数之间的加法、减法和乘法.

两个复数的相加或相减, 按多项式相加或相减, 再进行去括号与合并同类项. 因此, 我们有如下的公式:

$$
\left( {a + b\mathrm{i}}\right)  \pm  \left( {c + d\mathrm{i}}\right)  = \left( {a \pm  c}\right)  + \left( {b \pm  d}\right) \mathrm{i}
$$

$$
\left( {a\text{ 、 }b\text{ 、 }c\text{ 、 }d \in  \mathbf{R}}\right) \text{ . }
$$

两个复数相乘，可按多项式相乘，再用条件 ${\mathrm{i}}^{2} =  - 1$ 化简整理所得的结果. 因此,如果 $a\text{ 、 }b\text{ 、 }c\text{ 、 }d \in  \mathbf{R}$ ,那么

$$
\left( {a + b\mathrm{i}}\right) \left( {c + d\mathrm{i}}\right)  = {ac} + {bc}\mathrm{i} + {ad}\mathrm{i} + {bd}{\mathrm{i}}^{2}
$$

$$
= \left( {{ac} - {bd}}\right)  + \left( {{bc} + {ad}}\right) \mathrm{i}.
$$

这样, 我们得到了如下复数乘法的公式:

$$
\left( {a + b\mathrm{i}}\right) \left( {c + d\mathrm{i}}\right)  = \left( {{ac} - {bd}}\right)  + \left( {{bc} + {ad}}\right) \mathrm{i}
$$

$$
\left( {a\text{ 、 }b\text{ 、 }c\text{ 、 }d \in  \mathbf{R}}\right) \text{ . }
$$

复数加法与乘法满足交换律、结合律与乘法对加法的分配律.

虽然这里列出了复数加法、减法和乘法的公式, 但在实际计算中, 其实不必硬记并套用公式, 用多项式运算的方式直接解题也是非常简洁的.

例 1 计算:

(1)(1+3i)+(-4+2i)；

(2)(3-2i)-(3+2i)；

(3) $\left( {2 - {3i}}\right) \left( {4 + {2i}}\right)$ ；

(4) $\left( {1 + {2i}}\right) \left( {3 + {4i}}\right) \left( {-2 + i}\right)$ .

解 (1) $\left( {1 + {3i}}\right)  + \left( {-4 + {2i}}\right)  = \left( {1 - 4}\right)  + \left( {3 + 2}\right) i =  - 3 + {5i}$ .

(2) $\left( {3 - {2i}}\right)  - \left( {3 + {2i}}\right)  = \left( {3 - 3}\right)  + \left( {-2 - 2}\right) i =  - {4i}$ ，

(3) $\left( {2 - 3\mathrm{i}}\right) \left( {4 + 2\mathrm{i}}\right)  = 2 \times  4 + 2 \times  2\mathrm{i} - 4 \times  3\mathrm{i} - \left( {2\mathrm{i}}\right)  \times  \left( {3\mathrm{i}}\right)$

$$
= 8 + 4\mathrm{i} - {12}\mathrm{i} - 6 \times  \left( {-1}\right)  = {14} - 8\mathrm{i}.
$$

(4) $\left( {1 + {2i}}\right) \left( {3 + {4i}}\right) \left( {-2 + i}\right) \; = \left( {1 \times  3 + 1 \times  4\mathrm{i} + 3 \times  2\mathrm{i} + 2 \times  4{\mathrm{i}}^{2}}\right) \left( {-2 + \mathrm{i}}\right)$

$$
= \left( {-5 + {10}\mathrm{i}}\right) \left( {-2 + \mathrm{i}}\right)
$$

$= \left( {-5}\right)  \times  \left( {-2}\right)  - 5\mathrm{i} - 2 \times  {10}\mathrm{i} + {10}{\mathrm{i}}^{2} =  - {25}\mathrm{i}.$

下面讨论复数系中的除法运算.

就像在实数系中一样,复数系中的除法也是作为乘法的逆运算定义的. 复数 $a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 除以非零复数 $c + d\mathrm{i}(c\text{ 、 }d \in$ R),就是求一个复数 $x + y\mathrm{i}\left( {x\text{ 、 }y \in  \mathbf{R}}\right)$ ,使得

$$
\left( {c + d\mathrm{i}}\right) \left( {x + y\mathrm{i}}\right)  = a + b\mathrm{i}.
$$

为了找出 $x + y\mathrm{i}$ ,我们把上式两边同乘 $c - d\mathrm{i}$ ,得到

$$
\left( {c - d\mathrm{i}}\right) \left( {c + d\mathrm{i}}\right) \left( {x + y\mathrm{i}}\right)  = \left( {c - d\mathrm{i}}\right) \left( {a + b\mathrm{i}}\right) ,
$$

即 $\;\left( {{c}^{2} + {d}^{2}}\right) \left( {x + y\mathrm{i}}\right)  = \left( {{ac} + {bd}}\right)  + \left( {{bc} - {ad}}\right) \mathrm{i}$ .

由于 $c + d\mathrm{i}$ 是一个非零复数,实数 ${c}^{2} + {d}^{2} \neq  0$ ,从而可以在等式两边同乘 $\frac{1}{{c}^{2} + {d}^{2}}$ ,得到

$$
x + y\mathrm{i} = \frac{{ac} + {bd}}{{c}^{2} + {d}^{2}} + \frac{{bc} - {ad}}{{c}^{2} + {d}^{2}}\mathrm{i}.
$$

---

与初中学过的形如 $a + b\sqrt{2}$ 的根式之间的运算作个类比.

---

下一步,我们用复数乘法公式不难验证求出的 $x + y\mathrm{i}$ 确实满足 $\left( {c + d\mathrm{i}}\right) \left( {x + y\mathrm{i}}\right)  = a + b\mathrm{i}$ (留作习题). 这就证明了 $x + y\mathrm{i}$ 的存在性及唯一性. 因此,在复数系中可以做除法,且如果把 $a + b\mathrm{i}$ 除以 $c + d\mathrm{i}$ 的商以分式形式记为 $\frac{a + b\mathrm{i}}{c + d\mathrm{i}}$ ,就有如下复数除法公式:

$$
\frac{a + b\mathrm{i}}{c + d\mathrm{i}} = \frac{{ac} + {bd}}{{c}^{2} + {d}^{2}} + \frac{{bc} - {ad}}{{c}^{2} + {d}^{2}}\mathrm{i}
$$

$$
\left( {a\text{ 、 }b\text{ 、 }c\text{ 、 }d \in  \mathbf{R}, c + d\mathrm{i} \neq  0}\right) .
$$

与做复数的加减法及乘法类似, 同学们并不需要死记这个除法公式,实际要做的只是化简分式 $\frac{a + b\mathrm{i}}{c + d\mathrm{i}}$ . 我们可以把分子与分母同乘 $c - d\mathrm{i}$ 后再化简整理,即得

$$
\frac{a + b\mathrm{i}}{c + d\mathrm{i}} = \frac{\left( {a + b\mathrm{i}}\right) \left( {c - d\mathrm{i}}\right) }{\left( {c + d\mathrm{i}}\right) \left( {c - d\mathrm{i}}\right) } = \frac{\left( {{ac} + {bd}}\right)  + \left( {{bc} - {ad}}\right) \mathrm{i}}{{c}^{2} + {d}^{2}}
$$

$$
= \frac{{ac} + {bd}}{{c}^{2} + {d}^{2}} + \frac{{bc} - {ad}}{{c}^{2} + {d}^{2}}\mathrm{i}.
$$

例 2 计算:

(1) $\frac{3 + \mathrm{i}}{2 - \mathrm{i}}$ ；

(2) $\frac{1 + \sqrt{2}\mathrm{i}}{1 - \sqrt{2}\mathrm{i}}$ .

解 (1) $\frac{3 + \mathrm{i}}{2 - \mathrm{i}} = \frac{\left( {3 + \mathrm{i}}\right) \left( {2 + \mathrm{i}}\right) }{\left( {2 - \mathrm{i}}\right) \left( {2 + \mathrm{i}}\right) } = \frac{\left( {6 - 1}\right)  + \left( {3 + 2}\right) \mathrm{i}}{4 - \left( {-1}\right) } = \frac{5 + 5\mathrm{i}}{5} = 1 + \mathrm{i}$ .

(2) $\frac{1 + \sqrt{2}\mathrm{i}}{1 - \sqrt{2}\mathrm{i}} = \frac{{\left( 1 + \sqrt{2}\mathrm{i}\right) }^{2}}{\left( {1 - \sqrt{2}\mathrm{i}}\right) \left( {1 + \sqrt{2}\mathrm{i}}\right) } = \frac{1 + 2\sqrt{2}\mathrm{i} - 2}{1 + 2} =  - \frac{1}{3} + \frac{2\sqrt{2}}{3}\mathrm{i}.$

我们还约定若干个相同复数相乘可以写成幂的形式: 对任意复数 $a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 与任何正整数 $n,{\left( a + b\mathrm{i}\right) }^{n}$ 表示 $n$ 个 $a + b\mathrm{i}$ 相乘.

非零复数的负指数幂也是有意义的: 当 $a + b\mathrm{i} \neq  0$ 时,对任何正整数 $n,{\left( a + b\mathrm{i}\right) }^{-n} = \frac{1}{{\left( a + b\mathrm{i}\right) }^{n}}$ ; 当 $a + b\mathrm{i} \neq  0$ 时,还约定 ${\left( a + b\mathrm{i}\right) }^{0} = 1.$

同底数幂的运算规则同样适用于复数,如 ${\left( a + b\mathrm{i}\right) }^{m}{\left( a + b\mathrm{i}\right) }^{n} \; = {\left( a + b\mathrm{i}\right) }^{m + n},{\left\lbrack  {\left( a + b\mathrm{i}\right) }^{m}\right\rbrack  }^{n} = {\left( a + b\mathrm{i}\right) }^{mn}$ (这里 $m\text{ 、 }n$ 都是整数).

---

这个方法是否似曾相识? 与分母有理化过程做一比较.

---

此外, 因为复数关于加法和乘法的运算律都成立, 所以两实数和(差)的完全平方公式以及平方差公式等常用的乘法公式在复数范围内也都适用.

例 3 (1)计算虚数单位 i 的整数次幂，并找出规律；

(2)对任意整数 $m$ ，计算 ${\mathrm{i}}^{m} + {\mathrm{i}}^{m + 1} + {\mathrm{i}}^{m + 2} + {\mathrm{i}}^{m + 3}$ .

解(1)我们有

$$
{\mathrm{i}}^{1} = \mathrm{i},{\mathrm{i}}^{2} =  - 1,{\mathrm{i}}^{3} = {\mathrm{i}}^{2} \times  \mathrm{i} =  - 1 \times  \mathrm{i} =  - \mathrm{i},{\mathrm{i}}^{4} = {\left( {\mathrm{i}}^{2}\right) }^{2} = {\left( -1\right) }^{2} = 1.
$$

由最后一个等式,推知对任意整数 $n,{\mathrm{i}}^{4n} = {\left( {\mathrm{i}}^{4}\right) }^{n} = {1}^{n} = 1$ . 因此,

i 的幂的一般规律是:对任意给定的整数 $n$ ，均有

$$
{\mathrm{i}}^{4n} = 1,{\mathrm{i}}^{{4n} + 1} = \mathrm{i},{\mathrm{i}}^{{4n} + 2} =  - 1,{\mathrm{i}}^{{4n} + 3} =  - \mathrm{i}.
$$

(2) ${\mathrm{i}}^{m} + {\mathrm{i}}^{m + 1} + {\mathrm{i}}^{m + 2} + {\mathrm{i}}^{m + 3} = {\mathrm{i}}^{m}\left( {1 + \mathrm{i} + {\mathrm{i}}^{2} + {\mathrm{i}}^{3}}\right)$

$$
= {\mathrm{i}}^{m}\left\lbrack  {1 + \mathrm{i} + \left( {-1}\right)  + \left( {-\mathrm{i}}\right) }\right\rbrack   = 0.
$$

例 4 计算: ${\left( a + b\mathrm{i}\right) }^{2} - {\left( a - b\mathrm{i}\right) }^{2}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ .

解 ${\left( a + b\mathrm{i}\right) }^{2} - {\left( a - b\mathrm{i}\right) }^{2}$

$= \left\lbrack  {\left( {a + b\mathrm{i}}\right)  + \left( {a - b\mathrm{i}}\right) }\right\rbrack  \left\lbrack  {\left( {a + b\mathrm{i}}\right)  - \left( {a - b\mathrm{i}}\right) }\right\rbrack$

$= \left( {2a}\right)  \times  \left( {{2b}\mathrm{i}}\right)  = {4ab}\mathrm{i}.$

## 练习 9.1(1)

1. 已知 $\left( {x + {2y}}\right)  + \left( {{5x} - y}\right) \mathrm{i} = 9 + \mathrm{i}$ ，其中 $x$ 、 $y \in  \mathbf{R}$ . 求 $x$ 、 $y$ 的值.

2. 计算:

(1) $\left( {-1 + {3i}}\right)  + \left( {2 + {6i}}\right)$ ； (2) $\left( {3 - {2i}}\right)  - \left( {4 + i}\right)$ ；

(3) $\left( {\frac{1}{2} - \frac{\sqrt{3}}{2}\mathrm{i}}\right) \left( {\sqrt{3} + \mathrm{i}}\right)$ ；___ (4) ${\left( 1 + \mathrm{i}\right) }^{6}$ ；

(5) $\frac{2}{1 - \mathrm{i}}$ ； (6) $\frac{-1 + 2\mathrm{i}}{-1 - 2\mathrm{i}}$ .

## 2 复数的实部、虚部与共轭

我们已经引入了复数并介绍了复数的四则运算, 本小节将进一步介绍与复数有关的一些概念, 以期对复数及其运算有更好的把握与理解.

复数的表达方式 $a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 称为它的代数形式,其中的实数 $a$ 和 $b$ 分别叫做该复数的实部 (real part) 和虚部 (imaginary part). 为了行文的简洁与方便, 复数也常常用单个字母(常用 $z$ )来表示，此时它的实部和虚部分别记作 $\operatorname{Re}z$ 与 $\operatorname{Im}z$ . 即,若复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ ,则 $\operatorname{Re}z = a,\operatorname{Im}z = b$ . 若复数 $z = a + b\mathrm{i}$ 的虚部为零,即 $b = 0$ ,则 $z = a$ 是个实数; 当 $b \neq  0$ 时, $z$ 称为虚数 (imaginary number). 特别地,当 $a = 0$ 但 $b \neq  0$ 时, $z = b\mathrm{i}$ 称为纯虚数 (pure imaginary number). 我们已经知道, $z = 0$ 当且仅当 $a = 0$ 且 $b = 0$ ,此时 $z$ 是一个实数.

实数是虚部等于零的复数, 因此, 实数集合是复数集合的子集,并且是一个真子集,即 $\mathbf{R} \subset  \mathbf{C}$ .

复数可以按以下方式分类:

$$
\text{ 复数 }\left( {z = a + b\mathrm{i}, a\text{ 、 }b \in  \mathbf{R}}\right) \left\{  \begin{array}{l} \text{ 实数 }\left( {b = 0}\right) \\  \text{ 虚数 }\left( {b \neq  0}\right) \\  \text{ 一纯虚数 }\left( {b \neq  0, a = 0}\right)  \end{array}\right.
$$

例 5 填写下表:

<table><tr><td>$z$</td><td>是否复数</td><td>是否实数</td><td>是否虚数</td><td>是否纯虚数</td><td>$\operatorname{Re}z$</td><td>$\operatorname{Im}z$</td></tr><tr><td>-0.5i</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>$- \frac{1}{2} - \sqrt{2}\mathrm{i}$</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>$\pi$</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>$\sqrt{3}$</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2i-5</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

解

<table><tr><td>$z$</td><td>是否复数</td><td>是否实数</td><td>是否虚数</td><td>是否纯虚数</td><td>$\operatorname{Re}z$</td><td>$\operatorname{Im}z$</td></tr><tr><td>-0.5i</td><td>是</td><td>否</td><td>是</td><td>是</td><td>0</td><td>-0.5</td></tr><tr><td>$- \frac{1}{2} - \sqrt{2}\mathrm{i}$</td><td>是</td><td>否</td><td>是</td><td>否</td><td>$- \frac{1}{2}$</td><td>$- \sqrt{2}$</td></tr><tr><td>$\pi$</td><td>是</td><td>是</td><td>否</td><td>否</td><td>$\pi$</td><td>0</td></tr><tr><td>0</td><td>是</td><td>是</td><td>否</td><td>否</td><td>0</td><td>0</td></tr><tr><td>$\sqrt{3}$</td><td>是</td><td>是</td><td>否</td><td>否</td><td>✓3</td><td>0</td></tr><tr><td>2i-5</td><td>是</td><td>否</td><td>是</td><td>否</td><td>-5</td><td>2</td></tr></table>

例 6 求实数 $m$ 的值或取值范围,使得复数

$$
z = {m}^{2} + m - 2 + \left( {{m}^{2} - 1}\right) \mathrm{i}
$$

分别是:

(1)实数； (2)虚数；

(3)纯虚数； (4) 0 .

解 (1) $z$ 为实数当且仅当 ${m}^{2} - 1 = 0$ ,即 $m = 1$ 或 $m =  - 1$ . 所以,当 $m = 1$ 或 $m =  - 1$ 时,复数 $z = {m}^{2} + m - 2 + \left( {{m}^{2} - 1}\right) \mathrm{i}$ 是实数.

(2) $z$ 是虚数当且仅当 ${m}^{2} - 1 \neq  0$ ，即 $m \neq  1$ 且 $m \neq   - 1$ . 所以,当 $m <  - 1$ 或 $- 1 < m < 1$ 或 $m > 1$ 时,复数 $z = {m}^{2} + m - 2 + \; \left( {{m}^{2} - 1}\right) \mathrm{i}$ 是虚数.

(3) $z$ 是纯虚数当且仅当 $\left\{  \begin{array}{l} {m}^{2} + m - 2 = 0, \\  {m}^{2} - 1 \neq  0, \end{array}\right.$ 即 $\left\{  \begin{array}{l} \left( {m + 2}\right) \left( {m - 1}\right)  = 0, \\  \left( {m + 1}\right) \left( {m - 1}\right)  \neq  0, \end{array}\right.$ 唯一满足此条件的 $m$ 的值是 $m =  - 2$ . 所以,当 $m =  - 2$ 时,复数 $z = {m}^{2} + m - 2 + \left( {{m}^{2} - 1}\right) \mathrm{i}$ 是纯虚数.

(4) $z = 0$ 当且仅当 $\left\{  \begin{array}{l} {m}^{2} + m - 2 = 0, \\  {m}^{2} - 1 = 0, \end{array}\right.$ 即 $\left\{  \begin{array}{l} \left( {m + 2}\right) \left( {m - 1}\right)  = 0, \\  \left( {m + 1}\right) \left( {m - 1}\right)  = 0, \end{array}\right.$ 唯一满足此条件的 $m$ 的值是 $m = 1$ . 所以,当 $m = 1$ 时,复数 $z = {m}^{2} + m - 2 + \left( {{m}^{2} - 1}\right) \mathrm{i}$ 等于 0 .

在推导复数除法公式时, 如果除数 (如果把除法写成分式, 就是分母)是 $c + d\mathrm{i}\left( {c\text{ 、 }d \in  \mathbf{R}}\right)$ ,我们把被除数与除数 (分子与分母) 同乘复数 $c - {di}$ ,就可把除数 (分母) 化为实数 ${c}^{2} + {d}^{2}$ . 像 $c + {di}$ 与 $c - {di}\left( {c\text{ 、 }d \in  \mathbf{R}}\right)$ 这样实部相同而虚部互为相反数的一对复数叫做共轭复数 (conjugate complex number), 也称这两个复数互为共轭, 或者说其中的一个数是另一个数的共轭复数. 共轭复数是复数理论中的一个重要概念. 一对共轭复数的积必为实数, 用此性质可以把分母的虚数化为实数, 从而把除法的结果写成复数的代数形式. 共轭复数的更多性质和应用在进一步的学习中还会见到.

一个复数 $z$ 的共轭复数记为 $\bar{z}$ . 因此,若 $z = a + b\mathrm{i}(a\text{ 、 }b \in$ R),则 $\bar{z} = a - b\mathrm{i}$ . 共轭复数具有如下性质:

(1)一个复数的共轭复数的共轭复数是它自己, 即对任何复数 $z,\bar{z} = z$ ;

(2)取共轭复数的过程与复数的四则运算可交换，即对复数 ${z}_{1}$ 与 ${z}_{2}$ ,

$$
\overline{{z}_{1} \pm  {z}_{2}} = \overline{{z}_{1}} \pm  \overline{{z}_{2}},\overline{{z}_{1}{z}_{2}} = \overline{{z}_{1}}\overline{{z}_{2}},
$$

且当 ${z}_{2} \neq  0$ 时, $\overline{\left( \frac{{z}_{1}}{{z}_{2}}\right) } = \overline{\frac{{z}_{1}}{{z}_{2}}}$ .

性质 (1) 从共轭复数的定义即得.

---

性质 (2) 的含义是, 两个过程 (“取共轭”与 “作四则运算”) 的先后次序可以交换, 即对一个四则运算的结果取共轭, 与先对参与四则运算的各数取共轭后再作四则运算, 所得的结果是一样的.

---

性质(2)对加法与减法，验证是直截了当的，留作练习. 下面对乘法与除法分别验证这个性质.

设 ${z}_{1} = a + b\mathrm{i},{z}_{2} = c + d\mathrm{i}\left( {a\text{ 、 }b\text{ 、 }c\text{ 、 }d \in  \mathbf{R}}\right)$ ,则

$$
\overline{{z}_{1}}\overline{{z}_{2}} = \left( {a - b\mathrm{i}}\right) \left( {c - d\mathrm{i}}\right)  = \left( {{ac} - {bd}}\right)  - \left( {{ad} + {bc}}\right) \mathrm{i}
$$

$$
= \overline{\left( {{ac} - {bd}}\right)  + \left( {{ad} + {bc}}\right) \mathrm{i}} = \overline{{z}_{1}{z}_{2}},
$$

从而乘法的情况得证.

现设 ${z}_{2} \neq  0$ ,则由乘法情形的结果,有 $\overline{\left( \frac{{z}_{1}}{{z}_{2}}\right) } \cdot  \overline{{z}_{2}} = \overline{\left( \frac{{z}_{1}}{{z}_{2}} \cdot  {z}_{2}\right) } = \; \overline{{z}_{1}}$ . 由于 $\overline{{z}_{2}}$ 也不等于 0,等式两边同除以 $\overline{{z}_{2}}$ ,便得到 $\overline{\left( \frac{{z}_{1}}{{z}_{2}}\right) } = \frac{\overline{{z}_{1}}}{\overline{{z}_{2}}}$ , 这就是除法时的结论.

例 7 设 $z$ 是复数,求证: $\bar{z} = z$ 是 $z \in  \mathbf{R}$ 的充要条件.

证明 必要性: 由 $z \in  \mathbf{R}$ ,可知 $z$ 的代数形式 $a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 中 $b = 0$ ,所以 $\bar{z} = z$ .

充分性: 设复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 满足 $z = \bar{z}$ ,即 $a + b\mathrm{i} \; = a - b\mathrm{i}$ . 由复数相等的充要条件,得 $b =  - b$ ,从而 $b = 0$ ,即 $z \in  \mathbf{R}$ .

例 8 设 ${z}_{1} = 1 + 3\mathrm{i},{z}_{2} = 1 - \mathrm{i}$ . 求复数 $z$ ,使得 $\bar{z} = \frac{{z}_{1}}{{z}_{2}}$ .

解 根据条件, 并由共轭复数的性质, 得到

$$
z = \overline{\bar{z}} = \frac{\overline{{z}_{1}}}{\overline{{z}_{2}}} = \frac{1 - 3\mathrm{i}}{1 + \mathrm{i}} = \frac{\left( {1 - 3\mathrm{i}}\right) \left( {1 - \mathrm{i}}\right) }{\left( {1 + \mathrm{i}}\right) \left( {1 - \mathrm{i}}\right) }
$$

$$
= \frac{\left( {1 - 3}\right)  + \left( {-3 - 1}\right) \mathrm{i}}{1 + 1} = \frac{-2 - 4\mathrm{i}}{2} =  - 1 - 2\mathrm{i}.
$$

## 练习 9.1(2)

1. 对复数 ${z}_{1}\text{ 、 }{z}_{2} \in  \mathbf{C}$ ,验证: $\overline{{z}_{1} + {z}_{2}} = \overline{{z}_{1}} + \overline{{z}_{2}},\overline{{z}_{1} - {z}_{2}} = \overline{{z}_{1}} - \overline{{z}_{2}}$ .

2. 在下列复数中, 哪些是实数? 哪些是虚数? 哪些是纯虚数? 各数的实部和虚部分别是什么?

$$
- 5 + 6\mathrm{i}\text{ 、 }\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}\mathrm{i}\text{ 、 } - \sqrt{3}\text{ 、 }\mathrm{i}\text{ 、 }0\text{ 、 }\cos \frac{\pi }{5} + \mathrm{i}\sin \frac{\pi }{5}.
$$

3. 下列关于复数 $z$ 和 $\bar{z}$ 的命题是真命题还是假命题? 请给出结论并说明理由.

(1) $z + \bar{z}$ 一定是实数； (2) $z - \bar{z}$ 一定是纯虚数；

(3)若 $z - \bar{z} = 0$ ，则 $z$ 是实数； (4)若 $z + \bar{z} = 0$ ，则 $z$ 是纯虚数.

4. 求实数 $m$ 的值或取值范围,使得复数 $z = \left( {m + 2}\right)  + \left( {m - 1}\right) \mathrm{i}$ 分别是:

(1)实数； (2)虚数； (3)纯虚数.

## 习题 9.1

A 组

1. 已知复数 $\left( {\frac{1}{2}x + y}\right)  + \left( {{5x} + \frac{2}{3}y - {16}}\right) \mathrm{i} =  - 4$ ，其中 $x\text{ 、 }y \in  \mathbf{R}$ . 求 $x\text{ 、 }y$ 的值.

2. 已知 $\left( {x + y}\right)  - {xy}\mathrm{i} =  - 5 + {24}\mathrm{i}$ ,其中 $x\text{ 、 }y \in  \mathbf{R}$ . 求 $x\text{ 、 }y$ 的值.

3. 计算:

(1) $\left( {\frac{1}{4} - \frac{13}{5}\mathrm{i}}\right)  + \left( {\frac{2}{3} + \frac{5}{2}\mathrm{i}}\right)$ ；___ (2) $- \left( {3 - {4i}}\right)  + \left( {2 + \mathrm{i}}\right)  - \left( {1 - {5i}}\right)$ ；

(3) $\left\lbrack  {\left( {a + b}\right)  + \left( {a - b}\right) \mathrm{i}}\right\rbrack   - \left\lbrack  {\left( {a - b}\right)  - \left( {a + b}\right) \mathrm{i}}\right\rbrack  \left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ ；

(4) $\left( {4 - {3i}}\right) \left( {3 + {4i}}\right)$ ； (5) $\left( {-2 + {3i}}\right) \left( {5 - {4i}}\right)$ ；

(6) ${\left( \frac{\sqrt{2}}{2} - \frac{\sqrt{2}}{2}\mathrm{i}\right) }^{2}$ ； (7) $\frac{7 + 9\mathrm{i}}{1 + 2\mathrm{i}}$ ；

(8) $\frac{6 - {5i}}{2 + {3i}}$ ； (9) $\frac{\sqrt{5} + \sqrt{3}\mathrm{i}}{\sqrt{5} - \sqrt{3}\mathrm{i}} - \frac{\sqrt{3} + \sqrt{5}\mathrm{i}}{\sqrt{3} - \sqrt{5}\mathrm{i}}$ .

4. 用复数乘法公式验证: 若 $c + d\mathrm{i} \neq  0$ ,则 $\left( {c + d\mathrm{i}}\right) \left( {\frac{{ac} + {bd}}{{c}^{2} + {d}^{2}} + \frac{{bc} - {ad}}{{c}^{2} + {d}^{2}}\mathrm{i}}\right)  = a + b\mathrm{i}$ .

5. 已知复数 ${z}_{1} = \left( {{a}^{2} + 2}\right)  + \left( {-{2a} - 1}\right) \mathrm{i},{z}_{2} = \left( {a - 6}\right)  + \left( {{a}^{2} + a}\right) \mathrm{i}$ ，其中 $a \in  \mathbf{R}$ . 若 ${z}_{1} \; + {z}_{2} = 2 + \mathrm{i}$ ,求 $a$ 的值.

6. 设实数 $x\text{ 、 }y$ 使得 $\left( {x + y\mathrm{i}}\right) \mathrm{i} - 2 + 4\mathrm{i} = \left( {x - y\mathrm{i}}\right) \left( {1 + \mathrm{i}}\right)$ ,求 $x\text{ 、 }y$ 的值.

7. 已知实数 $x\text{ 、 }y$ 使得 $\frac{x}{1 - \mathrm{i}} + \frac{y}{1 - 2\mathrm{i}} = \frac{5}{1 - 3\mathrm{i}}$ ,求 $x\text{ 、 }y$ 的值.

8. 求复数 $- 3 + 2\mathrm{i}$ 与复数 $2 + 3\mathrm{i}$ 的乘积的共轭复数.

9. 若复数 ${z}_{1} = a + 2\mathrm{i}\left( {a \in  \mathbf{R}}\right) ,{\bar{z}}_{2} = 3 + 4\mathrm{i}$ ,且 $\frac{{z}_{1}}{{z}_{2}}$ 为纯虚数,求 $a$ 的值.

10. 已知复数 $z = 1 + \mathrm{i}$ ，求 $\frac{{\bar{z}}^{2} - \bar{z} + 1}{{\bar{z}}^{2} + \bar{z} + 1}$ 的值.

11. 求实数 $m$ 的值,使得复数 $\left( {{m}^{2} - {3m} - 4}\right)  + \left( {{m}^{2} - {5m} - 6}\right) \mathrm{i}$ 分别是:

(1)实数； (2)纯虚数； (3)零.

12. 已知 $\left( {2{x}^{2} - {5x} + 2}\right)  + \left( {{y}^{2} + y - 2}\right) \mathrm{i} = 0$ ,其中 $x\text{ 、 }y \in  \mathbf{R}$ . 求 $x\text{ 、 }y$ 的值.

B 组

1. 计算:

(1) ${\left( \frac{1 - \mathrm{i}}{1 + \mathrm{i}}\right) }^{3}$ ； (2) $\frac{-2 + 2\sqrt{3}\mathrm{i}}{{\left( \sqrt{3} + \mathrm{i}\right) }^{2}}$ ；

(3) ${\left( 1 + \mathrm{i}\right) }^{10} - {\left( 1 - \mathrm{i}\right) }^{10}$ .

2. 已知复数 ${z}_{1} = 5 + {10}\mathrm{i}$ 及 ${z}_{2} = 3 - 4\mathrm{i}$ ，且复数 $z$ 满足 $\frac{1}{z} = \frac{1}{\overline{{z}_{1}}} + \frac{1}{\overline{{z}_{2}}}$ . 求 $z$ .

3. 已知复数 $\left( {{x}^{2} - {y}^{2} - 7}\right)  + \left( {x - y - 3}\right) \mathrm{i}$ 等于 $- 2\mathrm{i}$ ,其中 $x\text{ 、 }y \in  \mathbf{R}$ . 求 $x\text{ 、 }y$ 的值.

4. 已知 $\left( {{2x} + {3y}}\right)  + \left( {{x}^{2} - {y}^{2}}\right) \mathrm{i} = y + 2 + 4\mathrm{i}$ ,其中 $x\text{ 、 }y \in  \mathbf{R}$ . 求 $x\text{ 、 }y$ 的值.

5. 是否存在实数 $m$ ,使得复数 $z = {m}^{2} + {2m} - {15} + \frac{{m}^{2} - {5m} + 6}{{m}^{2} - {25}}\mathrm{i}$ 分别满足下列条件? 若存在,求出 $m$ 的值或取值范围; 若不存在,请说明理由.

(1) $z$ 是实数； (2) $z$ 是虚数；

(3) $z$ 是纯虚数； (4)z 是零.

6. 选择题:

(1)设 ${z}_{1}\text{ 、 }{z}_{2} \in  \mathbf{C}$ ，则 “ ${z}_{1}\text{ 、 }{z}_{2}$ 中至少有一个虚数” 是 “ ${z}_{1} - {z}_{2}$ 为虚数” 的(C) ( )

A. 充分非必要条件; B. 必要非充分条件;

C. 充要条件; D. 既非充分也非必要条件.

(2)若实数 $a$ 使得(1-i)+(1+i) $a \neq  0$ ，则 ( )

A. $a \neq  1$ ; B. $a \neq   - 1$ ;

C. $a \neq  1$ 且 $a \neq   - 1$ ; D. $a$ 可以是任意实数.

7. 如果复数 $z$ 满足 $\left( {1 + {2i}}\right) \bar{z} = 4 + {3i}$ ,求 $z$ .

8. 设复数 $z = a + b\mathrm{i}$ ，其中 $a\text{ 、 }b \in  \mathbf{R}, a \neq  0$ 且 $b \neq  0$ . 求证: $\frac{z + \bar{z}}{z - \bar{z}}$ 是纯虚数.

### 9.2 复数的几何意义

## 1 复平面与复数的坐标表示

复数 $a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 一一对应于有序实数对 $\left( {a, b}\right)$ ,而有序实数对 $\left( {a, b}\right)$ 与平面直角坐标系中的点 $Z\left( {a, b}\right)$ 又是一一对应的. 因此,可以用平面直角坐标系中的点 $Z\left( {a, b}\right)$ 表示复数 $z = \; a + b\mathrm{i}$ .

如图 9-2-1,在平面上建立直角坐标系,以坐标为 $\left( {a, b}\right)$ 的点 $Z$ 表示复数 $z = a + b\mathrm{i}$ ,就可在平面上的点的集合与复数集合之间建立一个一一对应. 这样用来表示复数的平面叫做复平面 (complex plane).

![bo_d4sll53ef24c73be0n1g_10_1180_899_236_256_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_10_1180_899_236_256_0.jpg)

图 9-2-1

在复平面上, $x$ 轴上的点具有 $\left( {a,0}\right)$ 形式的坐标,从而对应的都是实数,所以把 $x$ 轴叫做实轴 (real axis); 同理, $y$ 轴上的点 (除坐标原点外) 都对应纯虚数,所以把 $y$ 轴叫做虚轴 (imaginary axis). 坐标原点表示实数 0 .

![bo_d4sll53ef24c73be0n1g_10_1182_1303_239_407_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_10_1182_1303_239_407_0.jpg)

图 9-2-2

如图 9-2-2,共轭复数 $z = a + b\mathrm{i}$ 和 $\bar{z} = a - b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 在复平面上所对应的点 $Z\left( {a, b}\right)$ 和 ${Z}^{\prime }\left( {a, - b}\right)$ 关于 $x$ 轴对称; 反之, 如果复平面上的两个点关于 $x$ 轴对称,那么这两个点所对应的复数互为共轭. 特别地,如果 $b = 0$ ,即 $z$ 是实数,则 $z = \bar{z}$ ,此时 $z\text{ 、 }\bar{z}$ 在复平面上所对应的点是位于实轴上的同一点.

例 1 在复平面上有点 $A\left( {2,0}\right) \text{ 、 }B\left( {0, - 1}\right) \text{ 、 }C\left( {-2,3}\right)$ 、 $D\left( {4, - 3}\right)$ ,分别写出这四个点所对应的复数 ${z}_{A}\text{ 、 }{z}_{B}\text{ 、 }{z}_{C}\text{ 、 }{z}_{D}$ , 并求这些复数的共轭复数在复平面上所对应的点的坐标.

解 ${z}_{A} = 2,{z}_{B} =  - \mathrm{i},{z}_{C} =  - 2 + 3\mathrm{i},{z}_{D} = 4 - 3\mathrm{i}$ .

这些复数的共轭复数分别是 ${\bar{z}}_{A} = 2,{\bar{z}}_{B} = \mathrm{i},{\bar{z}}_{C} =  - 2 - 3\mathrm{i}$ , ${\bar{z}}_{D} = 4 + 3\mathrm{i}$ ,它们在复平面上所对应的点分别是 ${A}^{\prime }\left( {2,0}\right) \text{ 、 }{B}^{\prime }\left( {0,1}\right)$ 、 ${C}^{\prime }\left( {-2, - 3}\right) \text{ 、 }{D}^{\prime }\left( {4,3}\right)$ .

## 2 复数的向量表示

上一章我们学过平面向量的坐标表示, 知道通过平面直角坐标系, 可在平面向量与平面上的点之间建立一一对应. 现在, 我们以平面直角坐标系为媒介, 又可以通过复数与平面上的点的一一对应, 在复数与平面向量之间建立一一对应. 如图 9-2-3, 复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 在复平面上对应坐标为 $\left( {a, b}\right)$ 的点 $Z$ ,而点 $Z$ 又对应于平面向量 $\overrightarrow{OZ} = \left( {a, b}\right)$ ,从而复数 $z = a + b\mathrm{i}$ 对应于平面向量 $\overrightarrow{OZ} = \left( {a, b}\right)$ . 有了这些对应,我们可以把复数 $z = a + b\mathrm{i}$ 方便地看作是复平面上的点 $Z\left( {a, b}\right)$ 或向量 $\overrightarrow{OZ}$ .

![bo_d4sll53ef24c73be0n1g_11_229_231_234_255_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_11_229_231_234_255_0.jpg)

图 9-2-3

![bo_d4sll53ef24c73be0n1g_11_136_600_363_308_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_11_136_600_363_308_0.jpg)

图 9-2-4

例 2 在复平面上作出表示下列复数的向量:

${z}_{1} = 2 + 2\mathrm{i},{z}_{2} =  - 3 - 2\mathrm{i},{z}_{3} = 2\mathrm{i},{z}_{4} =  - 4,{z}_{5} = 2 - 2\mathrm{i}.$

解 在复平面上,表示复数 ${z}_{1} = 2 + 2\mathrm{i},{z}_{2} =  - 3 - 2\mathrm{i}$ , ${z}_{3} = 2\mathrm{i},{z}_{4} =  - 4,{z}_{5} = 2 - 2\mathrm{i}$ 的向量分别为图 9-2-4 中的向量 $\overrightarrow{OA}\text{ 、 }\overrightarrow{OB}\text{ 、 }\overrightarrow{OC}\text{ 、 }\overrightarrow{OD}\text{ 、 }\overrightarrow{OE}.$

例 3 设复平面上的点 $A$ 和点 $B$ 所对应的复数分别为 ${z}_{A} = {x}_{A} + {y}_{A}\mathrm{i}\left( {{x}_{A}\text{ 、 }{y}_{A} \in  \mathbf{R}}\right)$ 和 ${z}_{B} = {x}_{B} + {y}_{B}\mathrm{i}\left( {{x}_{B}\text{ 、 }{y}_{B} \in  \mathbf{R}}\right)$ ,试用 ${z}_{A}$ 和 ${z}_{B}$ 表示复平面上的向量 $\overrightarrow{AB}$ 所对应的复数 $z$ .

解 复平面上的点 $A$ 与点 $B$ 的坐标分别为 $\left( {{x}_{A},{y}_{A}}\right)$ 与 $\left( {{x}_{B},{y}_{B}}\right)$ ,故向量 $\overrightarrow{AB} = \left( {{x}_{B} - {x}_{A},{y}_{B} - {y}_{A}}\right)$ ,它所对应的复数是 $z = \left( {{x}_{B} - {x}_{A}}\right)  + \left( {{y}_{B} - {y}_{A}}\right) \mathrm{i}$ . 再由复数减法法则,可得 $z = \; {z}_{B} - {z}_{A}$ .

注意, 平面上起点不在原点的向量所表示的复数是该向量相应的位置向量所表示的复数. 上例说明, 这个复数是向量终点对应的复数与起点对应的复数之差.

例 4 设 $z \in  \mathbf{C}$ ,复平面上的点 $Z$ 与 ${Z}^{\prime }$ 分别表示 $z$ 与 $z\mathrm{i}$ . 求证: $\overrightarrow{OZ} \bot  \overrightarrow{O{Z}^{\prime }}$ .

证明 令 $z = x + y\mathrm{i}\left( {x\text{ 、 }y \in  \mathbf{R}}\right)$ ,则 $z\mathrm{i} =  - y + x\mathrm{i}$ ,从而 $\overrightarrow{OZ} = \; \left( {x, y}\right) ,\overrightarrow{O{Z}^{\prime }} = \left( {-y, x}\right)$ ,它们的数量积是 $\overrightarrow{OZ} \cdot  \overrightarrow{O{Z}^{\prime }} = x\left( {-y}\right)  + \; {yx} = 0$ ,所以 $\overrightarrow{OZ} \bot  \overrightarrow{O{Z}^{\prime }}$ .

## 3 复数加法的平行四边形法则

我们已经知道向量的加法适用平行四边形法则, 在将复数与平面向量建立一一对应后, 两个复数的和是否与对应的向量的和一致呢? 也就是说, 在复平面上是否也可以用平行四边形法则表述复数的加法呢?

![bo_d4sll53ef24c73be0n1g_12_1127_223_399_278_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_12_1127_223_399_278_0.jpg)

图 9-2-5

如图 9-2-5,复数 ${z}_{1} = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 对应向量 $\overrightarrow{O{Z}_{1}} = \left( {a, b}\right)$ , 复数 ${z}_{2} = c + d\mathrm{i}\left( {c\text{ 、 }d \in  \mathbf{R}}\right)$ 对应向量 $\overrightarrow{O{Z}_{2}} = \left( {c, d}\right)$ . 由于复数 $z = {z}_{1} + {z}_{2} = \left( {a + c}\right)  + \left( {b + d}\right) \mathrm{i}$ ,因此 $z$ 对应于向量

$$
\overrightarrow{OZ} = \left( {a + c, b + d}\right)  = \overrightarrow{O{Z}_{1}} + \overrightarrow{O{Z}_{2}}.
$$

这说明, 两个复数的和所对应的向量就是原来两个复数所对应向量的和,即以 $\overrightarrow{O{Z}_{1}}$ 与 $\overrightarrow{O{Z}_{2}}$ 为邻边的平行四边形的对角线所表示的向量. 这就是复数加法的平行四边形法则. 同样, 两个复数的差 ${z}_{1} - {z}_{2}$ 所对应向量是两个向量 $\overrightarrow{O{Z}_{1}}\text{ 、 }\overrightarrow{O{Z}_{2}}$ 的差 $\overrightarrow{O{Z}_{1}} - \overrightarrow{O{Z}_{2}}$ .

例 5 如图 9-2-6,在复平面上给定平行四边形 ${OABC}$ , 其中点 $A$ 与点 $C$ 分别对应于复数 ${z}_{A} =  - 1 + \mathrm{i}$ 与 ${z}_{C} = 3 + 2\mathrm{i}$ . 求点 $B$ 所对应的复数.

![bo_d4sll53ef24c73be0n1g_12_1142_624_318_243_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_12_1142_624_318_243_0.jpg)

图 9-2-6

解 由平行四边形 ${ABCD}$ ,根据复数加法的平行四边形法则,点 $B$ 所对应的复数为 ${z}_{A} + {z}_{C} = 2 + 3\mathrm{i}$ .

## 练习 9.2(1)

1. 当复数 $z$ 满足下列条件时,分别指出 $z$ 在复平面上所对应的点 $Z$ 的位置:

(1) $z$ 是正实数； (2) $z$ 是负实数；

(3) $z$ 是实部小于零、虚部大于零的虚数；(4) $z$ 是虚部小于零的纯虚数.

2. 如果复数 $z = \left( {m - 2}\right)  + \left( {{m}^{2} - {16}}\right) \mathrm{i}\left( {m \in  \mathbf{R}}\right)$ 在复平面上所对应的点在第四象限,求 $m$ 的取值范围.

3. 设复数 $3 - 4\mathrm{i}$ 与 $5 - 6\mathrm{i}$ 在复平面上所对应的向量分别为 $\overrightarrow{OA}$ 与 $\overrightarrow{OB}$ ( $O$ 为坐标原点), 求向量 $\overrightarrow{AB}$ 及 $\overrightarrow{BA}$ 所对应的复数.

4. 已知复平面上有点 $C\left( {2,4}\right)$ 和点 $D$ ,使得向量 $\overrightarrow{CD}$ 所对应的复数是 $- 3 - \mathrm{i}$ . 求点 $D$ 的坐标.

## 4 复数的模

复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 在复平面上所对应的点 $Z\left( {a, b}\right)$ 到原点的距离 $\sqrt{{a}^{2} + {b}^{2}}$ ,叫做复数 $z$ 的模 (modulus),记作 $\left| z\right|$ . 这样,复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 的模是

$$
\left| z\right|  = \left| {a + b\mathrm{i}}\right|  = \sqrt{{a}^{2} + {b}^{2}}.
$$

---

复数的模也称为它的绝对值.

---

由于复数 $z = a + b\mathrm{i}$ 的模与该复数所对应的向量 $\overrightarrow{OZ}$ 的模是一致的, 因此复数的模也可以说成是其对应的向量的模.

例 6 求下列复数的模:

(1) ${z}_{1} = 3 + {4i}$ ；

(2) ${z}_{2} =  - \frac{1}{2} - \sqrt{2}\mathrm{i}.$

解 (1) $\left| {z}_{1}\right|  = \sqrt{{3}^{2} + {4}^{2}} = 5$ .

(2) $\left| {z}_{2}\right|  = \sqrt{{\left( -\frac{1}{2}\right) }^{2} + {\left( -\sqrt{2}\right) }^{2}} = \frac{3}{2}$ .

复数的模有如下性质:

$$
\left| z\right|  = \left| \bar{z}\right| , z\bar{z} = {\left| z\right| }^{2};
$$

$$
\left| {{z}_{1}{z}_{2}}\right|  = \left| {z}_{1}\right| \left| {z}_{2}\right|
$$

$$
\left| \frac{{z}_{1}}{{z}_{2}}\right|  = \frac{\left| {z}_{1}\right| }{\left| {z}_{2}\right| }
$$

其中, $z\text{ 、 }{z}_{1}\text{ 、 }{z}_{2} \in  \mathbf{C}$ ,并在关于除法的性质中需假设 ${z}_{2} \neq  0$ .

证明 设 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ ,则

$$
\left| z\right|  = \sqrt{{a}^{2} + {b}^{2}} = \sqrt{{a}^{2} + {\left( -b\right) }^{2}} = \left| \bar{z}\right| ,
$$

$$
z\bar{z} = \left( {a + b\mathrm{i}}\right) \left( {a - b\mathrm{i}}\right)  = {a}^{2} - {\left( b\mathrm{i}\right) }^{2} = {a}^{2} + {b}^{2} = {\left| z\right| }^{2}.
$$

为证关于乘法的性质,设有两个复数 ${z}_{1} = a + b\mathrm{i}$ 与 ${z}_{2} = c + \; d\mathrm{i}\left( {a\text{ 、 }b\text{ 、 }c\text{ 、 }d \in  \mathbf{R}}\right)$ ,则

$$
\left| {{z}_{1}{z}_{2}}\right|  = \left| {\left( {a + b\mathrm{i}}\right) \left( {c + d\mathrm{i}}\right) }\right|
$$

$$
= \left| {\left( {{ac} - {bd}}\right)  + \left( {{ad} + {bc}}\right) \mathrm{i}}\right|
$$

$$
= \sqrt{{\left( ac - bd\right) }^{2} + {\left( ad + bc\right) }^{2}}
$$

$$
= \sqrt{{a}^{2}{c}^{2} - {2abcd} + {b}^{2}{d}^{2} + {a}^{2}{d}^{2} + {2abcd} + {b}^{2}{c}^{2}}
$$

$$
= \sqrt{\left( {{a}^{2} + {b}^{2}}\right) \left( {{c}^{2} + {d}^{2}}\right) }
$$

$$
= \sqrt{{a}^{2} + {b}^{2}} \cdot  \sqrt{{c}^{2} + {d}^{2}}
$$

$$
= \left| {z}_{1}\right| \left| {z}_{2}\right| \text{ . }
$$

现在,进一步设 ${z}_{2} \neq  0$ ,则 ${z}_{1} = {z}_{2} \cdot  \frac{{z}_{1}}{{z}_{2}}$ ,于是 $\left| {z}_{1}\right|  = \; \left| {{z}_{2} \cdot  \frac{{z}_{1}}{{z}_{2}}}\right|  = \left| {z}_{2}\right|  \cdot  \left| \frac{{z}_{1}}{{z}_{2}}\right|$ . 两边除以 $\left| {z}_{2}\right|$ ,就得到 $\left| \frac{{z}_{1}}{{z}_{2}}\right|  = \frac{\left| {z}_{1}\right| }{\left| {z}_{2}\right| }$ .

例 7 已知复数 $z$ 满足 $\left| z\right|  = 1$ ,求证: $z + \frac{1}{z}$ 是实数.

证明 由 $\left| z\right|  = 1$ ,得 $z\bar{z} = {\left| z\right| }^{2} = 1$ ,所以 $\bar{z} = \frac{1}{z}$ ,由此得到 $z + \frac{1}{z} = z + \bar{z}$ ,从而可知 $z + \frac{1}{z}$ 是实数.

例 8 求下列复数的模:

(1) $\frac{\left( {1 - i}\right) \left( {1 + {2i}}\right) }{4 + {3i}}$ ；

(2) $\frac{\left( {7 - {3i}}\right) \left( {5 + {4i}}\right) }{\left( {7 + {3i}}\right) \left( {-4 - {5i}}\right) }$ .

解 (1) $\left| \frac{\left( {1 - \mathrm{i}}\right) \left( {1 + 2\mathrm{i}}\right) }{4 + 3\mathrm{i}}\right|  = \frac{\left| {1 - \mathrm{i}}\right|  \times  \left| {1 + 2\mathrm{i}}\right| }{\left| 4 + 3\mathrm{i}\right| }$

$$
= \frac{\sqrt{{1}^{2} + {\left( -1\right) }^{2}} \times  \sqrt{{1}^{2} + {2}^{2}}}{\sqrt{{4}^{2} + {3}^{2}}}
$$

$$
= \frac{\sqrt{10}}{5}\text{ . }
$$

(2)将原式分子分母都乘 $\mathrm{i}$ ，就得到 $\frac{\left( {7 - 3\mathrm{i}}\right) \left( {5 + 4\mathrm{i}}\right) \mathrm{i}}{\left( {7 + 3\mathrm{i}}\right) \left( {5 - 4\mathrm{i}}\right) }$ ，其中 $7 - 3\mathrm{i}$ 与 $7 + 3\mathrm{i},5 + 4\mathrm{i}$ 与 $5 - 4\mathrm{i}$ 是两对共轭复数,它们都分别有相同的模,所以 $\left| \frac{\left( {7 - 3\mathrm{i}}\right) \left( {5 + 4\mathrm{i}}\right) }{\left( {7 + 3\mathrm{i}}\right) \left( {-4 - 5\mathrm{i}}\right) }\right|  = \left| \mathrm{i}\right|  = 1$ .

---

第(2)小题虽可以像第(1)小题那样直接计算, 但这里的解法提供一个思路: 可以利用一些已知的性质简化计算过程.

---

复数的模还有如下性质: 对 ${z}_{1}\text{ 、 }{z}_{2} \in  \mathbf{C}$ ,

$$
\left| {z}_{1}\right|  + \left| {z}_{2}\right|  \geq  \left| {{z}_{1} + {z}_{2}}\right| .
$$

这不过是 “三角形两边之和大于第三边” 这个性质的另一种表达方式, 即必修课程第 2 章所述的 “三角不等式”. 如图 9-2-7, 若复平面上 ${Z}_{1}\text{ 、 }{Z}_{2}$ 是复数 ${z}_{1}\text{ 、 }{z}_{2}$ 所对应的点,则平行四边形 $O{Z}_{2}Z{Z}_{1}$ 的顶点 $Z$ 就是复数 ${z}_{1} + {z}_{2}$ 对应的点. 因此,有

$$
\left| {z}_{1}\right|  + \left| {z}_{2}\right|  = \left| {O{Z}_{1}}\right|  + \left| {O{Z}_{2}}\right|
$$

$$
= \left| {O{Z}_{1}}\right|  + \left| {{Z}_{1}Z}\right|
$$

$$
\geq  \left| {OZ}\right|
$$

$$
= \left| {{z}_{1} + {z}_{2}}\right| \text{ . }
$$

![bo_d4sll53ef24c73be0n1g_14_1141_1262_316_230_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_14_1141_1262_316_230_0.jpg)

图 9-2-7

复平面上两点的距离可以简洁地用对应复数差的模表示出来: 设 ${Z}_{1}\left( {a, b}\right) \text{ 、 }{Z}_{2}\left( {c, d}\right)$ 是复平面上的两个点,其对应的复数为 ${z}_{1} = a + b\mathrm{i},{z}_{2} = c + d\mathrm{i}$ ,则由平面上两点间距离公式可知

$$
\left| {{z}_{1} - {z}_{2}}\right|  = \sqrt{{\left( a - c\right) }^{2} + {\left( b - d\right) }^{2}} = \left| {{Z}_{1}{Z}_{2}}\right|  = \left| \overrightarrow{{Z}_{1}{Z}_{2}}\right| .
$$

例 9 设复数 $- \sqrt{5} + {2\mathrm{i}}$ 和复数 $2 + \sqrt{5}\mathrm{i}$ 在复平面上分别对应点 $A$ 和点 $B$ ,求 $A\text{ 、 }B$ 两点间的距离.

解 $A\text{ 、 }B$ 两点间的距离是

$$
\left| {AB}\right|  = \sqrt{{\left( -\sqrt{5} - 2\right) }^{2} + {\left( 2 - \sqrt{5}\right) }^{2}}
$$

$$
= \sqrt{\left( {5 + 4\sqrt{5} + 4}\right)  + \left( {4 - 4\sqrt{5} + 5}\right) }
$$

$$
= 3\sqrt{2}\text{ . }
$$

## 练习 9.2(2)

1. 计算下列复数的模:

(1) $\left( {4 - {3i}}\right)  + \left( {-{12} - {5i}}\right)$ ； (2) $\left( {2 - \sqrt{3}\mathrm{i}}\right) {\left( \sqrt{6} - \mathrm{i}\right) }^{2}$ ；

(3) $\frac{7 + \mathrm{i}}{{\left( 3 - 4\mathrm{i}\right) }^{2}}$ .

2. 设复数 ${z}_{1} = 6 + 8\mathrm{i}$ 与 ${z}_{2} = 9 - 4\mathrm{i}$ 在复平面上所对应的点为 ${Z}_{1}$ 与 ${Z}_{2}$ ,试指出 ${Z}_{1}\text{ 、 }{Z}_{2}$ 与以原点为圆心、 10 为半径的圆 $C$ 的位置关系.

3. 设复平面上平行四边形 ${OMNP}$ 的顶点 $O\text{ 、 }M\text{ 、 }P$ 的坐标分别为 $\left( {0,0}\right) \text{ 、 }\left( {3,4}\right)$ 、 $\left( {-2, - 3}\right)$ ,求 ${ON}$ 的长度.

4. 求复数 $8 + 5\mathrm{i}$ 与 $4 - 2\mathrm{i}$ 在复平面上所对应的点之间的距离.

## 习题 9.2

## A 组

1. 设复数 ${z}_{A} =  - 4\text{ 、 }{z}_{B} = 2\mathrm{i}\text{ 、 }{z}_{C} = 2 - 3\mathrm{i}\text{ 、 }{z}_{D} = 3 + 2\mathrm{i}\text{ 、 }{z}_{E} =  - 1 - \mathrm{i}$ .

(1)在复平面上分别作出这些复数所对应的点 $A\text{ 、 }B\text{ 、 }C\text{ 、 }D\text{ 、 }E$ ；

(2)在复平面上分别作出这些复数的共轭复数所对应的向量.

2. 求实数 $m$ 的值或取值范围,使得复数 $z = \left( {{m}^{2} - {8m} + {15}}\right)  + \left( {{m}^{2} - {5m} - {14}}\right) \mathrm{i}$ 在复平面上所对应的点 $Z$ 分别位于

(1)实轴上; (2)虚轴上; (3)第四象限.

3. 设在复平面上的点 $A$ 与点 $B$ 所对应的复数分别为 ${z}_{A}$ 与 ${z}_{B}$ ,对于下列各组复数,分别求向量 $\overrightarrow{AB}$ 和向量 $\overrightarrow{BA}$ 所对应的复数:

(1) ${z}_{A} = 2 - {3\mathrm{i}},{z}_{B} = 4 + {5\mathrm{i}}$ ； (2) ${z}_{A} = \frac{1}{2} - \frac{\sqrt{3}}{2}\mathrm{i},{z}_{B} = \frac{\sqrt{3}}{2} + \frac{1}{2}\mathrm{i}.$

4. 已知复平面上有点 $A$ 和点 $B$ ,向量 $\overrightarrow{OA}$ 与向量 $\overrightarrow{AB}$ 所对应的复数分别为 $- 1 - {2\mathrm{i}}$ 与 4-i. 求点 $B$ 的坐标.

5. 设复数 $1 + 2\mathrm{i}$ 、 $- 2 + \mathrm{i}$ 、 $- 1 - 2\mathrm{i}$ 在复平面上所对应的点分别为 $A$ 、 $B$ 、 $C$ ,求 $\bigtriangleup {ABC}$ 的面积.

6. 计算:

(1) ${\left| 3 - 4i\right| }^{4}$ ； (2) $\left| {\left( {1 + i}\right) {\left( -2\sqrt{2} + i\right) }^{3}}\right|$ ；

(3) $\left| \frac{\left( {\sqrt{5} - 2\mathrm{i}}\right) {\left( 1 + \sqrt{3}\mathrm{i}\right) }^{2}}{\sqrt{13} + \sqrt{23}\mathrm{i}}\right|$ ; (4) $\left| \frac{{\left( 1 + 3\mathrm{i}\right) }^{3}\left( {4 - \mathrm{i}}\right) }{{\left( 1 - 3\mathrm{i}\right) }^{2}}\right|$ .

7. 已知 $\left| {1 - {4ki}}\right|  = 5$ ,其中 $k \in  \mathbf{R}$ . 求 $k$ 的值.

8. 设复数 $\left( {m - 1}\right)  + \left( {{2m} - 3}\right) \mathrm{i}\left( {m \in  \mathbf{R}}\right)$ 的模为 1,求 $m$ 的值.

9. 已知复数 $z = \frac{m + \left( {{3m} - 1}\right) \mathrm{i}}{2 - \mathrm{i}}\left( {m \in  \mathbf{R}}\right)$ 的实部与虚部互为相反数，求 $\left| z\right|$ .

10. 若复数 ${z}_{1} = 5 + {12}\mathrm{i}$ ,复数 ${z}_{2}$ 满足 $\left| {z}_{2}\right|  = {13}$ ,且 ${z}_{1}{z}_{2}$ 是纯虚数,求复数 ${z}_{2}$ .

## B 组

1. 选择题:

(1)设复平面上表示 $2 - \mathrm{i}$ 和 $3 + 4\mathrm{i}$ 的点分别为点 $A$ 和点 $B$ ，则表示向量 $\overrightarrow{AB}$ 的复数在复平面上所对应的点位于 ( )

A. 第一象限; B. 第二象限; C. 第三象限; D. 第四象限.

(2)复平面上平行于虚轴的非零向量所对应的复数一定是 ( )

A. 正数; B. 负数;

C. 纯虚数; D. 实部不为零的虚数.

2. 已知复平面上平行四边形 ${ABCD}$ 的顶点 $A\text{ 、 }B\text{ 、 }C$ 的坐标分别是 $\left( {-2, - 1}\right) \text{ 、 }\left( {7,3}\right)$ 、 $\left( {{12},9}\right)$ ,求点 $D$ 的坐标和向量 $\overrightarrow{AD}$ 所对应的复数.

3. 设复数 ${z}_{1}$ 与 ${z}_{2}$ 分别对应复平面上的向量 $\overrightarrow{O{Z}_{1}}$ 与 $\overrightarrow{O{Z}_{2}}$ ,已知 $\left| \overrightarrow{O{Z}_{1}}\right|  = \left| \overrightarrow{O{Z}_{2}}\right|  = 1$ , $\overrightarrow{O{Z}_{1}} \bot  \overrightarrow{O{Z}_{2}}$ . 求 $\left| {{z}_{1} + {z}_{2}}\right|$ 与 $\left| {{z}_{1} - {z}_{2}}\right|$ .

4. 已知复数 $z$ 满足 $\left| z\right|  = 1$ ,且 $z$ 不是纯虚数. 求证: $\frac{z + \mathrm{i}}{z - \mathrm{i}}$ 是纯虚数.

5. 证明: 集合 $M = \{ z \mid  z = \cos \theta  + \mathrm{i}\sin \theta ,\theta  \in  \mathbf{R}\}$ 中的所有复数在复平面上所对应的点在同一个圆上.

6. 设 ${z}_{1}\text{ 、 }{z}_{2} \in  \mathbf{C}$ ,求证: ${\left| {z}_{1} + {z}_{2}\right| }^{2} + {\left| {z}_{1} - {z}_{2}\right| }^{2} = 2\left( {{\left| {z}_{1}\right| }^{2} + {\left| {z}_{2}\right| }^{2}}\right)$ .

7. 若复数 $z$ 满足 $\left| {z - 2}\right|  = \left| {z - 2\mathrm{i}}\right|  = 2$ ,求 $z$ .

### 9.3 实系数一元二次方程

在初中课程中已学过了实系数一元二次方程, 它具有标准形式

$$
a{x}^{2} + {bx} + c = 0\left( {a\text{ 、 }b\text{ 、 }c \in  \mathbf{R}, a \neq  0}\right) .
$$

我们已经知道可用判别式 $\Delta  = {b}^{2} - {4ac}$ 来判定这个方程实根的存在性. 具体地说, 在实数范围内考虑:

(1)当 $\Delta  > 0$ 时，该方程有两个不相等的实根 $\frac{-b \pm  \sqrt{\Delta }}{2a}$ ；

(2)当 $\Delta  = 0$ 时，该方程有两个相等的实根(二重根) $- \frac{b}{2a}$ ；

(3)当 $\Delta  < 0$ 时，该方程没有实根.

我们现在再来讨论实系数一元二次方程的求根问题，但将根的取值范围从实数拓广到复数. 也就是说, 我们不仅要讨论实根, 还要讨论虚根. 我们要解决的问题实际上有两个:

(A) 当 $\Delta  \geq  0$ 时,除了已经找到的实根外,方程在复数范围还有其他的根吗?

(B) 当 $\Delta  < 0$ 时,方程在复数范围有根吗? 怎样求出它的根?

回答这两个问题,关键是对 $\Delta$ (它是一个实数) 在复数范围的平方根问题有个准确的把握.

## 1 实数的平方根

设 $c \in  \mathbf{R}$ ,并设 $a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 是它的一个平方根,即 ${\left( a + b\mathrm{i}\right) }^{2} = c$ . 将上式左边展开,得到 $\left( {{a}^{2} - {b}^{2}}\right)  + {2ab}\mathrm{i} = c$ ,再根据复数相等的条件, 就得到

$$
\left\{  \begin{array}{l} {a}^{2} - {b}^{2} = c, \\  {2ab} = 0. \end{array}\right.
$$

从第二个等式可知, $a$ 与 $b$ 中至少有一个为零.

当 $c \geq  0$ 时,必须 $b = 0$ ,否则 $a = 0$ ,从而推出 $c =  - {b}^{2} < 0$ , 与假设矛盾. 于是, $a + b\mathrm{i} = a$ 必是 $c$ 的一个实平方根. 这说明, 除了已知的实平方根 $a =  \pm  \sqrt{c}$ ,非负实数 $c$ 在复数范围没有其他的平方根.

而当 $c < 0$ 时,必须 $a = 0$ ,否则 $b = 0$ ,从而推出 $c = {a}^{2} > 0$ , 与假设矛盾. 于是, ${b}^{2} =  - c > 0$ ,从而 $b =  \pm  \sqrt{-c}$ . 此时 $c$ 的平方根有两个: $\pm  \sqrt{-c}\mathrm{i}$ ,它们是两个共轭的纯虚数.

例 1 在复数范围求 25 与 -25 的平方根.

解 因为 ${25} > 0$ ,它在复数范围的平方根与实数范围的平方根是一样的,都是 $\pm  5$ ; 因为 $- {25} < 0$ ,它没有实平方根,而在复数范围其平方根是 $\pm  \sqrt{-\left( {-{25}}\right) }\mathrm{i} =  \pm  5\mathrm{i}$ .

## 2 实系数一元二次方程

我们现在在复数范围求解实系数一元二次方程 $a{x}^{2} + {bx} + c \; = 0\left( {a \neq  0}\right)$ . 用配方法,得到

$$
{\left( x + \frac{b}{2a}\right) }^{2} = \frac{\Delta }{4{a}^{2}}\text{ ,即 }{\left( 2ax + b\right) }^{2} = \Delta \text{ ,其中 }\Delta  = {b}^{2} - {4ac}.
$$

这就是说, ${2ax} + b$ 是实数 $\Delta$ 的平方根. 由前面关于实数平方根的讨论, 就可以回答本节引言中所提的两个问题了, 其答案是: 在复数范围内,

(1)当 $\Delta  > 0$ 时,方程有两个不相等的实根 $\frac{-b \pm  \sqrt{\Delta }}{2a}$ ;

(2)当 $\Delta  = 0$ 时,方程有两个相等的实根 (二重根) $- \frac{b}{2a}$ ;

(3)当 $\Delta  < 0$ 时,方程有一对共轭虚根 $\frac{-b \pm  \sqrt{-\Delta }\mathrm{i}}{2a}$ .

例 2 在复数范围内解方程: $2{x}^{2} - {4x} + 5 = 0$ .

解 该方程的判别式 $\Delta  = {\left( -4\right) }^{2} - 4 \times  2 \times  5 =  - {24} < 0$ ,所以此方程有一对共轭虚根

$$
x = \frac{-\left( {-4}\right)  \pm  \sqrt{24}\mathrm{i}}{4} = 1 \pm  \frac{\sqrt{6}}{2}\mathrm{i}.
$$

如果实系数一元二次方程 $a{x}^{2} + {bx} + c = 0\left( {a \neq  0}\right)$ 有实根 ${x}_{1}$ 与 ${x}_{2}$ ,由必修课程第 2 章已经知道这两个根与方程的系数有如下关系(韦达定理):

$$
{x}_{1} + {x}_{2} =  - \frac{b}{a},{x}_{1}{x}_{2} = \frac{c}{a}.
$$

实系数一元二次方程的根与系数的关系在虚根的情况下仍然成立, 这只要直接把根代入验证就可以了.

---

有兴趣的同学可以写出在复数范围内求解实系数一元二次方程的完整算法, 并上机加以实现.

请同学们自行完成这一验证过程.

---

例 3 如果 $p\text{ 、 }q$ 都是实数,而关于 $x$ 的方程 $2{x}^{2} + {px} + \; q = 0$ 有一个根 $- 2 + 3\mathrm{i}$ ,求 $p\text{ 、 }q$ 的值.

解 方程 $2{x}^{2} + {px} + q = 0$ 有一个虚根 $- 2 + 3\mathrm{i}$ ,则它的另一个根必为其共轭复数 $- 2 - 3\mathrm{i}$ . 由根与系数的关系,有

$$
\left( {-2 + 3\mathrm{i}}\right)  + \left( {-2 - 3\mathrm{i}}\right)  =  - \frac{p}{2},\left( {-2 + 3\mathrm{i}}\right) \left( {-2 - 3\mathrm{i}}\right)  = \frac{q}{2},
$$

从而 $p = 8, q = {26}$ .

例 4 在复数范围将 $2{x}^{2} - {4x} + 5$ 分解因式.

解 例 2 中已经求出方程 $2{x}^{2} - {4x} + 5 = 0$ 的两个根 $1 + \frac{\sqrt{6}}{2}\mathrm{i}$ 与 $1 - \frac{\sqrt{6}}{2}\mathrm{i}$ ,所以

$$
2{x}^{2} - {4x} + 5 = 2\left( {x - 1 - \frac{\sqrt{6}}{2}\mathrm{i}}\right) \left( {x - 1 + \frac{\sqrt{6}}{2}\mathrm{i}}\right) .
$$

## 练习 9.3

1. 已知 $k$ 是一个实常数，而关于 $x$ 的一元二次方程 ${x}^{2} - {2kx} - k = 0$ 有两个虚根. 求 $k$ 的取值范围.

2. 在复数范围内解方程:

(1) ${x}^{2} + 2 = 0$ ； (2) ${x}^{2} + {2x} + 3 = 0$ ；

(3) $2\left( {{x}^{2} + 4}\right)  = {5x}$ .

3. 若 ${x}_{1}$ 和 ${x}_{2}$ 是方程 $2{x}^{2} + x + 3 = 0$ 的两个根,求 $\frac{1}{{x}_{1}} + \frac{1}{{x}_{2}}$ 的值.

## 习题 9.3

## A 组

1. 在复数范围内解下列一元二次方程:

(1) $4{x}^{2} + {25} = 0$ ； (2) ${x}^{2} - {2x} - 2 = 0$ ；

(3) ${x}^{2} - x + 1 = 0$ ； (4) $\left( {x - 3}\right) \left( {x - 5}\right)  = 2$ .

2. 已知 $2 + 3\mathrm{i}$ 是实系数一元二次方程 ${x}^{2} + {bx} + c = 0$ 一个根,求 $b\text{ 、 }c$ 的值.

3. 已知关于 $x$ 的实系数一元二次方程 ${x}^{2} + {kx} + 3 = 0$ 有两个虚根 ${x}_{1}$ 和 ${x}_{2}$ ,且 $\left| {{x}_{1} - {x}_{2}}\right|  = 2\sqrt{2}$ . 求 $k$ 的值.

## B 组

1. 在复数范围内解方程:

(1) ${x}^{4} - {16} = 0$ ； (2) ${x}^{4} + 3{x}^{2} - {10} = 0$ .

2. 已知两个复数的和为 4 、积为 6 ，求这两个复数.

3. 在复数范围内分解因式:

(1) ${a}^{2} + {2ab} + {b}^{2} + {c}^{2}$ ; (2) ${x}^{2} + 5{y}^{2}$ ；

(3) $2{x}^{2} - {6x} + 5$ .

4. 已知关于 $x$ 的实系数一元二次方程 ${x}^{2} + {kx} + {k}^{2} - {2k} = 0$ 有两个虚根 ${x}_{1}$ 和 ${x}_{2}$ ，且 ${x}_{1}^{2} + {x}_{2}^{2} = 3$ . 求 $k$ 的值.

## 探究与实践

同学们也许会注意到,用配方法导出 ${\left( 2ax + b\right) }^{2} = \Delta$ 时并不在乎原来的一元二次方程 $a{x}^{2} + {bx} + c = 0\left( {a \neq  0}\right)$ 是否具有实系数. 当方程不局限于实系数时,判别式 $\Delta  = {b}^{2} - {4ac}$ 可能为虚数. 如果我们有方法能够找出任意复数的平方根, 那么一般复系数一元二次方程就可解了. 要得到一个复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 的平方根,可以从假设 ${\left( c + d\mathrm{i}\right) }^{2} = a + b\mathrm{i}$ ( $c\text{ 、 }d \in  \mathbf{R}$ )开始,令等式两边的实部、虚部分别相等,得到关于 $c\text{ 、 }d$ 的方程组并求解. 这个方法是可行的, 有兴趣的同学不妨一试.

### 9.4 复数的三角形式

本章第 1 节讲了用复数的代数形式所表达的复数运算公式. 这时, 复数的加减运算公式比较简洁. 但是, 复数的乘除, 特别是复数的除法, 相应的公式比较复杂, 计算比较繁琐. 本节将介绍复数的另外一种表示形式——三角形式，在这种形式下，复数的乘除有比较简洁的计算公式, 相应运算的意义也会更明显地表现出来.

## 1 复数的三角形式

如图 9-4-1,复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 对应着复平面上的一个点 $Z\left( {a, b}\right)$ . 我们把以原点 $O$ 为顶点、 $x$ 轴的正半轴为始边、 射线 ${OZ}$ 为终边的角 $\theta$ ,叫做复数 $z$ 的辐角 (argument),记作 Arg $z$ . 这里的角是 6.1 节意义下的任意角,即它是从原点出发的一条射线从始边位置旋转到终边位置所形成的角, 逆时针旋转时其度量取正值, 顺时针旋转时其度量取负值, 不旋转时其度量为 0 .

![bo_d4sll53ef24c73be0n1g_21_216_1019_262_255_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_21_216_1019_262_255_0.jpg)

图 9-4-1

因为一个角的终边绕原点 $O$ 旋转 ${2\pi }$ 仍回到原来的位置,所以任意一个非零复数 $z$ 的辐角都有无穷多个,其任意两个辐角的大小的差一定是 ${2\pi }$ 的整数倍. 例如,虚数单位 $\mathrm{i}$ 的辐角可以是任何 $\frac{\pi }{2} + {2k\pi }, k \in  \mathbf{Z}$ .

规定:复数 0 的辐角的大小是任意的值.

---

两个非零复数相等，当且仅当它们的模与辐角主值分别相等.

---

在复数 $z$ 的所有辐角中,满足 $0 \leq  \theta  < {2\pi }$ 的辐角 $\theta$ 称为 $z$ 的辐角主值,记作 $\arg z$ . 复数的辐角虽不是唯一确定的,但非零复数的辐角主值则是唯一确定的.

复数的任意一个辐角 $\theta$ 与复数的模 $r = \left| z\right|  = \sqrt{{a}^{2} + {b}^{2}}$ 一起, 就完全确定了复数 $z = a + b\mathrm{i}$ . 事实上,如图9-4-1,我们有

$$
a = r\cos \theta , b = r\sin \theta .
$$

于是

$$
z = r\left( {\cos \theta  + \mathrm{i}\sin \theta }\right) .
$$

复数的这种表示形式叫做它的三角形式.

例 1 分别写出下列复数的模 $r$ 与辐角主值 $\theta$ ,并把这些复数用三角形式表示:

(1) $\sqrt{3} + \mathrm{i}$ ；

(2)-1+i;

(3)-1；

(4) $- 3 - {4i}$ .

解 (1) $r = \sqrt{{\left( \sqrt{3}\right) }^{2} + {1}^{2}} = 2,\cos \theta  = \frac{\sqrt{3}}{2},\sin \theta  = \frac{1}{2},\theta$ 为第一象限角,故辐角主值为 $\theta  = \arg \left( {\sqrt{3} + \mathrm{i}}\right)  = \frac{\pi }{6}$ ,从而 $\sqrt{3} + \mathrm{i}$ 的三角形式为 $2\left( {\cos \frac{\pi }{6} + \mathrm{i}\sin \frac{\pi }{6}}\right)$ ,即

$$
\sqrt{3} + \mathrm{i} = 2\left( {\cos \frac{\pi }{6} + \mathrm{i}\sin \frac{\pi }{6}}\right) .
$$

(2) $r = \sqrt{{\left( -1\right) }^{2} + {1}^{2}} = \sqrt{2},\cos \theta  =  - \frac{1}{\sqrt{2}} =  - \frac{\sqrt{2}}{2},\sin \theta  = \frac{1}{\sqrt{2}} \; = \frac{\sqrt{2}}{2},\theta$ 为第二象限角,故辐角主值为 $\theta  = \arg \left( {-1 + \mathrm{i}}\right)  = \frac{3\pi }{4}$ . 因此, 用三角形式表示-1+i, 有

$$
- 1 + \mathrm{i} = \sqrt{2}\left( {\cos \frac{3\pi }{4} + \mathrm{i}\sin \frac{3\pi }{4}}\right) .
$$

(3)-1 的模 $r = \sqrt{{\left( -1\right) }^{2} + {0}^{2}} = 1$ ， -1 所对应的点 $\left( {-1,0}\right)$ 在 $x$ 轴的负半轴上,故辐角主值为 $\theta  = \arg \left( {-1}\right)  = \pi$ . 因此,用三角形式表示-1，有

$$
- 1 = \cos \pi  + \mathrm{i}\sin \pi .
$$

(4) $r = \sqrt{{\left( -3\right) }^{2} + {\left( -4\right) }^{2}} = 5,\cos \theta  =  - \frac{3}{5},\sin \theta  =  - \frac{4}{5},\theta$ 为第三象限角,且 $\tan \theta  = \frac{4}{3}$ ,故辐角主值为 $\theta  = \arg \left( {-3 - 4\mathrm{i}}\right)  = \; \pi  + \arctan \frac{4}{3}$ . 因此,用三角形式表示 $- 3 - 4\mathrm{i}$ ,有

$$
- 3 - 4\mathrm{i} = 5\left\lbrack  {\cos \left( {\pi  + \arctan \frac{4}{3}}\right)  + \mathrm{i}\sin \left( {\pi  + \arctan \frac{4}{3}}\right) }\right\rbrack  .
$$

例 2 把下列复数用三角形式表示:

(1) $\cos \theta  - \mathrm{i}\sin \theta$ ;

(2) $- 2\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right)$ .

解(1)因为 $\cos \left( {-\theta }\right)  = \cos \theta ,\sin \left( {-\theta }\right)  =  - \sin \theta$ ,所以 $\cos \theta  - \mathrm{i}\sin \theta$ 的三角形式是 $\cos \left( {-\theta }\right)  + \mathrm{i}\sin \left( {-\theta }\right)$ .

(2) $- 2\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right)$ 的模是 2 又因为 $\cos \left( {\pi  + \alpha }\right)  = \; - \cos \alpha ,\sin \left( {\pi  + \alpha }\right)  =  - \sin \alpha$ ,所以 $- 2\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right)$ 的三角形式是2[cos $\left( {\pi  + \alpha }\right)  + \mathrm{i}$ sin $\left( {\pi  + \alpha }\right) \rbrack$ .

## 练习 9.4(1)

1. 下列复数是否用三角形式来表示的? 为什么?

(1)3π(cos 0.5+i sin 0.5)； (2) $2\left( {\sin 1 + \mathrm{i}\cos 1}\right)$ ；

(3) $\cos {131\pi } + \mathrm{i}\sin {131\pi }$ ； (4) $\sqrt{2}\left( {\cos {0.3\pi } + \mathrm{i}\sin {0.2\pi }}\right)$ ；

(5) $- 2\left( {\cos \frac{\pi }{4} + \mathrm{i}\sin \frac{\pi }{4}}\right)$ ； (6) $3\left( {\cos \frac{\pi }{5} - \mathrm{i}\sin \frac{\pi }{5}}\right)$ .

2. 把下列复数用三角形式表示(用辐角主值):

(1) 3; (2)-2i;

(3) $1 + \mathrm{i}$ ； (4)-1+ $\sqrt{3}\mathrm{i}$ .

## 2 三角形式下复数的乘除运算

现在我们讨论三角形式下的复数乘除运算公式.

设有两个用三角形式表示的复数 ${z}_{1} = r\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right)$ 与 ${z}_{2} = s\left( {\cos \beta  + \mathrm{i}\sin \beta }\right)$ ,其中 $r = \left| {z}_{1}\right|  \geq  0, s = \left| {z}_{2}\right|  \geq  0$ ,则

Q

$$
{z}_{1}{z}_{2} = {rs}\left\lbrack  {\cos \left( {\alpha  + \beta }\right)  + \mathrm{i}\sin \left( {\alpha  + \beta }\right) }\right\rbrack  ;
$$

$$
\frac{{z}_{1}}{{z}_{2}} = \frac{r}{s}\left\lbrack  {\cos \left( {\alpha  - \beta }\right)  + \mathrm{i}\sin \left( {\alpha  - \beta }\right) }\right\rbrack  \left( {{z}_{2} \neq  0}\right) .
$$

---

三角形式下的复数乘除运算公式称为棣莫弗公式.

---

![bo_d4sll53ef24c73be0n1g_23_251_1624_193_214_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_23_251_1624_193_214_0.jpg)

棣莫弗 (A. De Moivre, 1667-1754), 法国数学家.

也就是说，两个复数相乘，其积的模等于模的积，积的辐角等于辐角的和；两个复数相除(除数不为零)，其商的模等于模的商, 商的辐角等于辐角的差.

证明 乘积的公式的推导是两角和的正弦、余弦公式的直接应用:

$$
{z}_{1}{z}_{2} = {rs}\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right) \left( {\cos \beta  + \mathrm{i}\sin \beta }\right)
$$

$$
= {rs}\left\lbrack  {\left( {\cos \alpha \cos \beta  - \sin \alpha \sin \beta }\right)  + \mathrm{i}\left( {\sin \alpha \cos \beta  + \cos \alpha \sin \beta }\right) }\right\rbrack
$$

$$
= {rs}\left\lbrack  {\cos \left( {\alpha  + \beta }\right)  + \mathrm{i}\sin \left( {\alpha  + \beta }\right) }\right\rbrack  ,
$$

乘积公式得证.

现在设 ${z}_{2} \neq  0$ (从而 $s \neq  0$ ),用乘积公式计算复数 ${z}_{2}$ 与 $\frac{r}{s}\left\lbrack  {\cos \left( {\alpha  - \beta }\right)  + \mathrm{i}\sin \left( {\alpha  - \beta }\right) }\right\rbrack$ 的乘积,就得到

$$
{z}_{2} \cdot  \frac{r}{s}\left\lbrack  {\cos \left( {\alpha  - \beta }\right)  + \mathrm{i}\sin \left( {\alpha  - \beta }\right) }\right\rbrack
$$

$$
= s \cdot  \frac{r}{s}\left\lbrack  {\cos \left( {\beta  + \alpha  - \beta }\right)  + \mathrm{i}\sin \left( {\beta  + \alpha  - \beta }\right) }\right\rbrack
$$

$$
= r\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right)  = {z}_{1},
$$

再把等式两边同除以 ${z}_{2}$ ,就得到所求的除法公式.

例 3 计算, 并用复数的代数形式表示计算结果:

(1) $\sqrt{3}\left( {\cos \frac{\pi }{12} + \mathrm{i}\sin \frac{\pi }{12}}\right)  \cdot  \sqrt{2}\left( {\cos \frac{\pi }{4} + \mathrm{i}\sin \frac{\pi }{4}}\right)$ ；

(2) $\frac{4\left( {\cos \frac{4\pi }{3} + \mathrm{i}\sin \frac{4\pi }{3}}\right) }{2\left( {\cos \frac{5\pi }{6} + \mathrm{i}\sin \frac{5\pi }{6}}\right) }$ .

解 $\left( 1\right) \sqrt{3}\left( {\cos \frac{\pi }{12} + \mathrm{i}\sin \frac{\pi }{12}}\right)  \cdot  \sqrt{2}\left( {\cos \frac{\pi }{4} + \mathrm{i}\sin \frac{\pi }{4}}\right)$

$$
= \sqrt{3} \times  \sqrt{2}\left\lbrack  {\cos \left( {\frac{\pi }{12} + \frac{\pi }{4}}\right)  + \mathrm{i}\sin \left( {\frac{\pi }{12} + \frac{\pi }{4}}\right) }\right\rbrack
$$

$$
= \sqrt{6}\left( {\cos \frac{\pi }{3} + \mathrm{i}\sin \frac{\pi }{3}}\right)
$$

$$
= \sqrt{6}\left( {\frac{1}{2} + \frac{\sqrt{3}}{2}\mathrm{i}}\right)
$$

$$
= \frac{\sqrt{6}}{2} + \frac{3\sqrt{2}}{2}\mathrm{i}.
$$

(2) $\frac{4\left( {\cos \frac{4\pi }{3} + \mathrm{i}\sin \frac{4\pi }{3}}\right) }{2\left( {\cos \frac{5\pi }{6} + \mathrm{i}\sin \frac{5\pi }{6}}\right) }$

$$
= 2\left\lbrack  {\cos \left( {\frac{4\pi }{3} - \frac{5\pi }{6}}\right)  + \mathrm{i}\sin \left( {\frac{4\pi }{3} - \frac{5\pi }{6}}\right) }\right\rbrack
$$

$$
= 2\left( {\cos \frac{\pi }{2} + \mathrm{i}\sin \frac{\pi }{2}}\right)
$$

$$
= 2\mathrm{i}\text{ . }
$$

我们现在来分析复数乘法的几何意义.

在复平面上,把复数 ${z}_{1} = r\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right)$ (其中 $r = \left| {z}_{1}\right|  \geq  0$ ) 对应的向量记为 $\overrightarrow{O{Z}_{1}}$ ,则 $\left| \overrightarrow{O{Z}_{1}}\right|  = r$ ,而从 $x$ 轴正向到 $\overrightarrow{O{Z}_{1}}$ 方向需旋转 $\alpha$ 角 (当 $\alpha  > 0$ 时,逆时针旋转; 当 $\alpha  < 0$ 时,顺时针旋转).

把 ${z}_{1}$ 乘一个非负实数 $s$ ,就是把向量 $\overrightarrow{O{Z}_{1}}$ 伸缩为原来的 $s$ 倍,成为向量 $\overrightarrow{O{Z}_{1}^{\prime }} = s\overrightarrow{O{Z}_{1}}$ (向量与实数的乘积),使它的模 $\left| \overrightarrow{O{Z}_{1}^{\prime }}\right|  = {sr}$ ,而其辐角不变 (图 9-4-2(1)).

![bo_d4sll53ef24c73be0n1g_25_579_402_887_307_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_25_579_402_887_307_0.jpg)

图 9-4-2

把 ${z}_{1}$ 乘一个模为 1 的复数 $\cos \beta  + \mathrm{i}\sin \beta$ ，就是把 ${z}_{1}$ 的辐角从 $\alpha$ 变成了 $\alpha  + \beta$ ，将向量 $\overrightarrow{O{Z}_{1}}$ 变成为向量 $\overrightarrow{O{Z}_{1}}$ ，而其模 $\left| \overrightarrow{O{Z}_{1}}\right|  = \; r$ 不变 (图 9-4-2(2)). 也就是说,这个乘法就是让向量 $\overrightarrow{O{Z}_{1}}$ 绕坐标原点旋转 $\beta$ 角成为向量 $\overrightarrow{O{Z}_{1}}$ ，使得以 $x$ 轴正半轴为始边、以 $\overrightarrow{O{Z}_{1}}$ 为终边的角是 $\alpha  + \beta$ . 这样，“旋转”这一重要的几何变换可以用复数乘法得到准确的表达. 例如，由于 $\mathrm{i}$ 的辐角主值是 $\frac{\pi }{2}$ ，因此把 ${z}_{1}$ 乘 $\mathrm{i}$ 就是让向量 $\overrightarrow{O{Z}_{1}}$ 绕坐标原点逆时针旋转 $\frac{\pi }{2}$ . Q

---

当 $\beta  > 0$ 时,逆时针旋转; 当 $\beta  < 0$ 时, 顺时针旋转.

---

一般地,把复数 ${z}_{1}$ 乘任意一个复数 ${z}_{2} = s\left( {\cos \beta  + \mathrm{i}\sin \beta }\right)$ , 在几何上就是对 $\overrightarrow{O{Z}_{1}}$ 作上述两个变换的合成: 先伸缩,再旋转, 或者先旋转, 后伸缩 (图 9-4-2(3)). 从复数乘法的结果我们知道, 这两个不同顺序会得到同样的结果.

$$
{z}^{\prime } = \left( {-2 + 2\mathrm{i}}\right) \left( {\cos {120}^{ \circ  } + \mathrm{i}\sin {120}^{ \circ  }}\right)
$$

$$
= \left( {-2 + 2\mathrm{i}}\right) \left( {-\frac{1}{2} + \frac{\sqrt{3}}{2}\mathrm{i}}\right)
$$

$$
= \left( {1 - \sqrt{3}}\right)  - \left( {1 + \sqrt{3}}\right) \mathrm{i}.
$$

![bo_d4sll53ef24c73be0n1g_25_221_1468_255_315_0.jpg](attachments/bo_d4sll53ef24c73be0n1g_25_221_1468_255_315_0.jpg)

图 9-4-3

例 4 如图 9-4-3,设复数 $- 2 + 2\mathrm{i}$ 在复平面上所对应的向量是 $\overrightarrow{OZ}$ ,将 $\overrightarrow{OZ}$ 绕原点 $O$ 逆时针旋转 ${120}^{ \circ  }$ 得到向量 $\overrightarrow{O{Z}^{\prime }}$ . 求向量 $\overrightarrow{O{Z}^{\prime }}$ 所对应的复数. (结果用复数的代数形式表示)

解 设向量 $\overrightarrow{O{Z}^{\prime }}$ 对应的复数为 ${z}^{\prime }$ ,则

## 3 三角形式下复数的乘方与开方

复数的 $n$ 次幂 ( $n$ 是正整数) 是 $n$ 个相同复数的连乘,因此, 根据复数乘法公式,一个复数的 $n$ 次幂的模是底数模的 $n$ 次幂, 而其辐角是底数辐角的 $n$ 倍.

作为乘方的逆运算,自然会想到,一个复数开 $n$ 次方,方根的模是被开方数模的 $n$ 次方根,而方根的辐角是被开方数辐角的 $n$ 分之一. 这个规则原则上没错,但要注意的是: 由于被开方数不同辐角的 $n$ 分之一所得出的辐角可能有不同的主值, 在这个过程中被开方数的辐角不能只取主值. 事实上,如果 $\alpha$ 是被开方数的辐角之一,以下 $n$ 个值都可以作为被开方数 $n$ 次方根的辐角:

$$
\frac{\alpha }{n},\frac{\alpha  + {2\pi }}{n},\frac{\alpha  + {4\pi }}{n},\cdots ,\frac{\alpha  + 2\left( {n - 1}\right) \pi }{n}.
$$

这 $n$ 个值之间的差都不是 ${2\pi }$ 的整数倍,它们都给出了不同的 $n$ 次方根; 而其余可能的辐角 $\frac{\alpha  + {2k\pi }}{n}\left( {k \in  \mathbf{Z}}\right)$ 都与上述辐角之一相差 ${2\pi }$ 的整数倍,它们不会再给出更多不同的 $n$ 次方根了.

现在可把复数的乘方与开方的公式总结如下:

设 $z = r\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right) \left( {r = \left| z\right|  \geq  0}\right)$ ,则对任何正整数 $n$ ,有

${z}^{n} = {r}^{n}\left( {\cos {n\alpha } + \mathrm{i}\sin {n\alpha }}\right) ;$

$z$ 的 $n$ 次方根为

$\sqrt[n]{r}\left( {\cos \frac{\alpha  + {2k\pi }}{n} + \mathrm{i}\sin \frac{\alpha  + {2k\pi }}{n}}\right) , k = 0,1,2,\cdots , n - 1.$

例 5 计算 ${\left( 1 - \mathrm{i}\right) }^{20}$ .

解 将 $1 - \mathrm{i}$ 写成三角形式 $1 - \mathrm{i} = \sqrt{2}\left( {\cos \frac{7\pi }{4} + \mathrm{i}\sin \frac{7\pi }{4}}\right)$ ，就可以得到

${\left( 1 - \mathrm{i}\right) }^{20} = {2}^{10}\left( {\cos {35\pi } + \mathrm{i}\sin {35\pi }}\right)  = {1024}\left( {\cos \pi  + \mathrm{i}\sin \pi }\right)  =  - {1024}$ .

例 6 求 1 的三次方根.

解 因为 $1 = \cos 0 + \mathrm{i}\sin 0$ ,所以它的三次方根是 $\cos \frac{2k\pi }{3} + \; \mathrm{i}\sin \frac{2k\pi }{3}\left( {k = 0,1,2}\right)$ ,即

$$
1 = \cos 0 + \mathrm{i}\sin 0,
$$

$$
\omega  = \cos \frac{2\pi }{3} + \mathrm{i}\sin \frac{2\pi }{3} =  - \frac{1}{2} + \frac{\sqrt{3}}{2}\mathrm{i},
$$

$$
{\omega }^{2} = \cos \frac{4\pi }{3} + \mathrm{i}\sin \frac{4\pi }{3} =  - \frac{1}{2} - \frac{\sqrt{3}}{2}\mathrm{i}.
$$

## 练习 9.4(2)

1. 计算:

(1) $8\left( {\cos \frac{\pi }{6} + \mathrm{i}\sin \frac{\pi }{6}}\right)  \cdot  2\left( {\cos \frac{\pi }{3} + \mathrm{i}\sin \frac{\pi }{3}}\right)$ ;

(2) $\frac{6\left( {\cos \frac{3\pi }{5} + \mathrm{i}\sin \frac{3\pi }{5}}\right) }{2\left( {\cos \frac{\pi }{10} + \mathrm{i}\sin \frac{\pi }{10}}\right) }$ ;

(3) ${\left\lbrack  \sqrt{2}\left( \cos \frac{\pi }{6} + \mathrm{i}\sin \frac{\pi }{6}\right) \right\rbrack  }^{5}$ .

2. 求 1 的所有四次方根.

## 习题 9.4

## A 组

1. 把下列复数用三角形式表示 (用辐角主值):

(1)4-4i; (2) $- 3\sqrt{3} - {3i}$ ；

(3) $\sin \frac{\pi }{8} + \mathrm{i}\cos \frac{\pi }{8}$ ; (4) $\frac{\pi }{\cos \frac{\pi }{7} + \mathrm{i}\sin \frac{\pi }{7}}$ .

2. 计算,并将结果用复数的代数形式表示:

(1) $\sqrt{2}\left( {\cos {240}^{ \circ  } + \mathrm{i}\sin {240}^{ \circ  }}\right)  \cdot  \frac{\sqrt{3}}{2}\left( {\cos {60}^{ \circ  } + \mathrm{i}\sin {60}^{ \circ  }}\right)$ ;

(2) $\frac{{12}\left( {\cos \frac{11\pi }{6} + \mathrm{i}\sin \frac{11\pi }{6}}\right) }{6\left( {\cos \frac{2\pi }{3} + \mathrm{i}\sin \frac{2\pi }{3}}\right) }$ ; (3) $\frac{\sqrt{3}\left( {\cos {150}^{ \circ  } + \mathrm{i}\sin {150}^{ \circ  }}\right) }{\sqrt{2}\left( {\cos {300}^{ \circ  } + \mathrm{i}\sin {300}^{ \circ  }}\right) }$ ;

(4) ${\left\lbrack  \sqrt{2}\left( \sin \frac{\pi }{6} + \mathrm{i}\cos \frac{\pi }{6}\right) \right\rbrack  }^{3}$ ； (5) ${\left( \sqrt{3} - \mathrm{i}\right) }^{12}$ .

3. 求 $- \mathrm{i}$ 的所有三次方根.

B 组

1. 计算,并将结果用复数的代数形式表示:

(1) ${\left( \cos \frac{11\pi }{6} + \mathrm{i}\sin \frac{11\pi }{6}\right) }^{2} \cdot  \sqrt{2}\left( {\cos \frac{5\pi }{3} + \mathrm{i}\sin \frac{5\pi }{3}}\right)$ ;

(2) $\frac{\sqrt{5}{\left( \cos \frac{5\pi }{4} + \mathrm{i}\sin \frac{5\pi }{4}\right) }^{2} \cdot  \sqrt{2}\left( {\cos \frac{7\pi }{3} + \mathrm{i}\sin \frac{7\pi }{3}}\right) }{\sqrt{3}\left( {\cos \frac{7\pi }{3} + \mathrm{i}\sin \frac{7\pi }{3}}\right)  \cdot  \sqrt{5}\left( {\cos \frac{7\pi }{3} - \mathrm{i}\sin \frac{7\pi }{3}}\right) }$ .

2. 设复数 $- 3 - 4\mathrm{i}$ 在复平面上所对应的向量是 $\overrightarrow{OZ}$ ,将 $\overrightarrow{OZ}$ 绕原点 $O$ 顺时针旋转 ${810}^{ \circ  }$ 得到向量 $\overrightarrow{O{Z}^{\prime }}$ . 求向量 $\overrightarrow{O{Z}^{\prime }}$ 所对应的复数. (结果用复数的代数形式表示)

3. 求复数 $3 + 4\mathrm{i}$ 与复数 $- 1 + 7\mathrm{i}$ 在复平面上所对应的两个向量的夹角的大小.

## 课后阅读

## 三次方程求根公式与复数的起源

现代教科书在引进复数时往往从引入负数的平方根开始, 但历史上复数的思想却是从寻找实系数一元三次方程求根公式中萌芽的.

对一般的实系数一元三次方程 $a{x}^{3} + b{x}^{2} + {cx} + d = 0\left( {a \neq  0}\right)$ ,由于总可以通过代换 $x = y - \frac{b}{3a}$ 消去其二次项,因此如何求解形如 ${x}^{3} + {px} + q = 0$ 的三次方程就成为关注的重点.

在一些数学工具书中,我们可以找到方程 ${x}^{3} + {px} + q = 0$ 的求根公式,这一公式被称为卡尔丹公式, 它是以 16 世纪意大利数学家卡尔丹 (J. Cardan) 的名字命名的. 这里用现代数学的语言来介绍一下卡尔丹公式的获得过程.

三次方程 ${x}^{3} + {px} + q = 0$ 可以变形为 ${x}^{3} =  - {px} + \left( {-q}\right)$ ,即把 ${x}^{3}$ 写成了两数之和. 受此启发,设想所求的未知数 $x$ 也可以写成两数之和: $x = m + n$ ,再把等式 ${x}^{3} = {\left( m + n\right) }^{3}$ 的右边展开,就得到 ${x}^{3} = {m}^{3} + {n}^{3} + {3mn}\left( {m + n}\right)$ ,即 ${x}^{3} = {3mnx} + \left( {{m}^{3} + {n}^{3}}\right)$ . 将上式与 ${x}^{3} =  - {px} + \left( {-q}\right)$ 相对照,不妨令

$$
\left\{  \begin{array}{l} {3mn} =  - p, \\  {m}^{3} + {n}^{3} =  - q. \end{array}\right.
$$

把此方程组中的第一个方程两边同时作三次方,并把 ${m}^{3}$ 与 ${n}^{3}$ 看成未知数,由上述方程组可解出

$$
\left\{  \begin{array}{l} {m}^{3} =  - \frac{q}{2} + \sqrt{{\left( \frac{q}{2}\right) }^{2} + {\left( \frac{p}{3}\right) }^{3}}, \\  {n}^{3} =  - \frac{q}{2} - \sqrt{{\left( \frac{q}{2}\right) }^{2} + {\left( \frac{p}{3}\right) }^{3}}. \end{array}\right.
$$

于是,似乎可以顺理成章地把方程 ${x}^{3} + {px} + q = 0$ 的一个根写成

$$
x = \sqrt[3]{-\frac{q}{2} + \sqrt{{\left( \frac{q}{2}\right) }^{2} + {\left( \frac{p}{3}\right) }^{3}}} + \sqrt[3]{-\frac{q}{2} - \sqrt{{\left( \frac{q}{2}\right) }^{2} + {\left( \frac{p}{3}\right) }^{3}}}.
$$

三次方程求根公式的研究推进至此, 看似大功告成. 但是, 将此公式用于另一位意大利数学家邦贝利(R. Bombelli)曾关注过的方程 ${x}^{3} - {15x} - 4 = 0$ ，得到该方程的一个根是 $x = \sqrt[3]{2 + \sqrt{-{121}}} + \sqrt[3]{2 - \sqrt{-{121}}}$ ,在认为负数不能进行开平方运算的 16 世纪,这是一个不知作何解释的结果. 另外,由 ${64} = {15} \times  4 + 4$ 就可以看到方程 ${x}^{3} = {15x} + 4$ 有一个根是 $x = 4$ ,进而可求得该方程另外两个实根为 $x =  - 2 \pm  \sqrt{3}$ . 如何把这两个结果统一起来,让当时的数学家们不知所措了.

其实,只要用现代的复数理论是可以把 $x = \sqrt[3]{2 + \sqrt{-{121}}} + \sqrt[3]{2 - \sqrt{-{121}}}$ 与 $x = 4$ 统一起来的. 事实上,若把 $\sqrt{-{121}}$ 解释为 -121 的一个平方根 (比方说 11i),则

$$
x = \sqrt[3]{2 + {11}\mathrm{i}} + \sqrt[3]{2 - {11}\mathrm{i}}.
$$

可以直接验证 $2 \pm  \mathrm{i}$ 是 $2 \pm  {11}\mathrm{i}$ 的三次方根,于是卡尔丹公式确实给出了方程 ${x}^{3} - {15x} - 4 = 0$ 的一个根 $x = \left( {2 + \mathrm{i}}\right)  + \left( {2 - \mathrm{i}}\right)  = 4$ .

这样的演绎和解释在数学上不够严谨, 如二次和三次根号的使用会有歧义, 解方程过程中会产生增根等. 在这些方面做些严格化后, 卡尔丹公式就是一个有效的求三次方程根的公式. 在实际求根过程中,一旦找到了 ${m}^{3}$ 与 ${n}^{3}$ 的一对三次方根 ${m}_{1}$ 与 ${n}_{1}$ ,并验证其满足 $3{m}_{1}{n}_{1} =  - p$ ,则方程 ${x}^{3} + {px} + q = 0$ 的三个根就是

$$
{x}_{1} = {m}_{1} + {n}_{1},{x}_{2} = \omega {m}_{1} + {\omega }^{2}{n}_{1},{x}_{3} = {\omega }^{2}{m}_{1} + \omega {n}_{1},
$$

这里 $\omega  =  - \frac{1}{2} + \frac{\sqrt{3}}{2}\mathrm{i}$ 是 1 的一个三次方根 (参看本章 9.4 节例 6). 例如,对方程 ${x}^{3} - {15x} - 4 \; = 0$ ,我们前面找到的 ${m}_{1} = 2 + \mathrm{i},{n}_{1} = 2 - \mathrm{i}$ ,恰满足 $3{m}_{1}{n}_{1} = {15} =  - p$ ,于是,经过简单的计算就得到方程的三个实根:

$$
{x}_{1} = {m}_{1} + {n}_{1} = 4,{x}_{2} = \omega {m}_{1} + {\omega }^{2}{n}_{1} =  - 2 - \sqrt{3},{x}_{3} = {\omega }^{2}{m}_{1} + \omega {n}_{1} =  - 2 + \sqrt{3}.
$$

为了从卡尔丹的研究走到得以公认的三次方程求根公式, 有许多数学家曾作出了巨大的努力，关键就是从卡尔丹工作中所隐含的复数思想的萌芽逐步发展成完善的复数理论， 使得解方程过程中每一步都落在坚实的数学基础上.

因此, 通常认为, 求解三次方程的研究是现代复数理论的起点.

## 内容提要

复数是我们继自然数、整数、有理数和实数的学习之后，新认识的一种数.

1. 复数系与相关概念

(1)虚数单位i，满足 ${\mathrm{i}}^{2} =  - 1$ .

(2)复数的代数形式: $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ .

(3)复数的相等: $a + b\mathrm{i} = 0\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 的充要条件是 $a\text{ 、 }b$ 同时为 0；复数 $a + b\mathrm{i} = \; c + d\mathrm{i}\left( {a\text{ 、 }b\text{ 、 }c\text{ 、 }d \in  \mathbf{R}}\right)$ 的充要条件是 $a = c$ 且 $b = d$ .

(4)复数的实部与虚部:复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 的实部是 $a$ ，虚部是 $b$ ；虚部为 0 的复数是实数，虚部不为 0 的复数称为虚数，实部为 0 的虚数称为纯虚数.

(5) 复数的模:复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 的模是 $\left| z\right|  = \sqrt{{a}^{2} + {b}^{2}}$ .

(6)复数的共轭:复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 的共轭复数是 $\bar{z} = a - b\mathrm{i}$ .

2. 复数的四则运算

(1)两个复数进行相加、相减或相乘时，仿照两个二项式进行相加、相减或相乘的规则计算，并用条件 ${\mathrm{i}}^{2} =  - 1$ 及合并同类项以化简结果.

(2)两个复数进行除法(除数不为 0)运算时，将分子和分母同时乘分母的共轭复数， 然后分子和分母分别做复数的乘法而得到运算结果.

(3)复数模对乘、除的分配性:复数积(商)的模等于模的积(商).

3. 复数的坐标表示

(1)复平面:表示复数的直角坐标平面叫做复平面，其中 $x$ 轴叫做实轴， $y$ 轴叫做虚轴.

(2)复数的坐标表示与向量表示:复数 $z = a + b\mathrm{i}$ ( $a$ 、 $b \in  \mathbf{R}$ )可用复平面上坐标为 $\left( {a, b}\right)$ 的点 $Z\left( {a, b}\right)$ 来表示，也可以用从坐标原点 $O$ 出发的向量 $\overrightarrow{OZ} = \left( {a, b}\right)$ 来表示.

(3)复数模的几何意义:复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ 的模 $\left| z\right|$ 等于点 $Z\left( {a, b}\right)$ 与原点的距离，也等于向量 $\overrightarrow{OZ}$ 的模 $\left| \overrightarrow{OZ}\right|$ .

(4)两个复数的和在复平面上所对应的向量就是两个复数对应的向量按平行四边形法则所得到的和向量.

(5)两复数差的模的几何意义:两复数差的模是这两个复数在复平面上对应点之间的距离.

4. 实系数一元二次方程

给定方程 $a{x}^{2} + {bx} + c = 0\left( {a\text{ 、 }b\text{ 、 }c \in  \mathbf{R}, a \neq  0}\right)$ ,并令 $\Delta  = {b}^{2} - {4ac}$ 为其判别式,则

(1)当 $\Delta  > 0$ 时，方程有两个不相等的实根 $\frac{-b \pm  \sqrt{\Delta }}{2a}$ ；

(2)当 $\Delta  = 0$ 时，方程有两个相等的实根(二重根) $- \frac{b}{2a}$ ；

(3)当 $\Delta  < 0$ 时，方程有一对共轭虚根 $\frac{-b \pm  \sqrt{-\Delta }\mathrm{i}}{2a}$ .

*5. 复数的三角形式

(1)复数的辐角:设复数 $z$ 对应复平面上的点 $Z$ ，则以原点为顶点、 $x$ 轴的正半轴为始边、射线 ${OZ}$ 为终边的角 $\theta$ 称为 $z$ 的辐角，记作 $\operatorname{Arg}z$ ；满足 $0 \leq  \theta  < {2\pi }$ 的辐角称为 $z$ 的辐角主值，记为 $\arg z$ .

(2)复数的三角形式:设复数 $z$ 的模为 $r$ ，辐角为 $\theta$ ，则 $z = r\left( {\cos \theta  + \mathrm{i}\sin \theta }\right)$ ，复数的这种表示形式称为它的三角形式.

(3)三角形式下复数的乘法与除法公式:给定三角形式的复数 ${z}_{1} = r\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right)$ 与 ${z}_{2} = s\left( {\cos \beta  + \mathrm{i}\sin \beta }\right)$ ,则

${z}_{1}{z}_{2} = {rs}\left\lbrack  {\cos \left( {\alpha  + \beta }\right)  + \mathrm{i}\sin \left( {\alpha  + \beta }\right) }\right\rbrack  ,$

$\frac{{z}_{1}}{{z}_{2}} = \frac{r}{s}\left\lbrack  {\cos \left( {\alpha  - \beta }\right)  + \mathrm{i}\sin \left( {\alpha  - \beta }\right) }\right\rbrack  \left( {{z}_{2} \neq  0}\right) .$

(4)三角形式下复数的乘方与开方公式:给定三角形式的复数 $r\left( {\cos \alpha  + \mathrm{i}\sin \alpha }\right)$ ，则对任何正整数 $n$ ,有

${z}^{n} = {r}^{n}\left( {\cos {n\alpha } + \mathrm{i}\sin {n\alpha }}\right) ,$

$z$ 的 $n$ 次方根为 $\sqrt[n]{r}\left( {\cos \frac{\alpha  + {2k\pi }}{n} + \mathrm{i}\sin \frac{\alpha  + {2k\pi }}{n}}\right) , k = 0,1,2,\cdots , n - 1$ .

## 复习题

## A 组

1. 选择题:

(1)虚数的平方一定是 ( )

A. 正实数； B. 负实数；

C. 虚数; D. 虚数或负实数.

(2)如果复平面上的向量 $\overrightarrow{AB}$ 所对应的复数是 $- 3 + {2i}$ ，那么向量 $\overrightarrow{BA}$ 所对应的复数是( )

A. $3 - 2\mathrm{i}$ ； B. $3 + 2\mathrm{i}$ ；

C. $- 3 + 2\mathrm{i}$ ; D. $- 3 - 2\mathrm{i}$ .

2. 填空题:

(1)设 $z = {{11} - {60}\mathrm{i}}$ ，则 $\operatorname{Re}z =$ ___； $\left| z\right|  =$ ___； $\left| z\right|  =$ ___； $\bar{z} =$ ___.

(2)下列三个命题中，真命题是___.

① 在复平面上，表示实数的点都在实轴上，表示虚数的点都在虚轴上；

② 任何一个表示虚数的点一定在某一个象限内;

③ 复数的模表示该复数在复平面上所对应的点到原点的距离.

3. 已知复数 $z = \left( {{a}^{2} - {2a} - 3}\right)  + \left( {{a}^{2} - {4a} + 3}\right) \mathrm{i}$ ,其中 $a$ 是实数.

(1)若 $z \in  \mathbf{R}$ ，求 $a$ 的值；

(2)若 $z$ 在复平面上所对应的点位于第一象限，求 $a$ 的取值范围.

4. 已知复数 ${z}_{1} = \left( {{a}^{2} - a - 6}\right)  + \left( {1 - {2a}}\right) \mathrm{i},{z}_{2} = \left( {a - 3}\right)  + \left( {{a}^{2} - {2a} + 2}\right) \mathrm{i}$ ，其中 $a \in  \mathbf{R}$ . 若 $\overline{{z}_{1}} = {z}_{2}$ ,求 $a$ 的值.

5. 计算:

(1) $\left( {4 + i}\right) \left( {3 + {2i}}\right)$ ；

(2) $\left( {\sqrt{2} + \sqrt{3}i}\right) \left( {\sqrt{2} - \sqrt{3}i}\right) \left( {-\sqrt{3} + \sqrt{2}i}\right) \left( {-\sqrt{3} - \sqrt{2}i}\right)$ ；

(3) $\frac{-3 + {29i}}{1 + {2i}}$ ；

(4) $\frac{{\left( 1 + i\right) }^{4}}{1 + {2i}} + \frac{{\left( 1 - i\right) }^{4}}{1 - {2i}}$ ；

(5) ${\left\lbrack  \left( \sqrt{3} + 1\right)  + \left( \sqrt{3} - 1\right) \mathrm{i}\right\rbrack  }^{2}$ .

6. 已知复数 $z = \frac{{\left( -3 - \mathrm{i}\right) }^{2}\left( {2 - \mathrm{i}}\right) }{{\left( 1 + 2\mathrm{i}\right) }^{3}}$ ,求 $\left| z\right|$ .

7. 在复数范围内解下列方程:

(1) ${x}^{2} - {4x} + 8 = 0$ ；

(2) $3{x}^{2} + {2x} - 3 = 0$ .

B 组

1. 选择题:

(1)设 ${z}_{1}\text{ 、 }{z}_{2} \in  \mathbf{C}$ ，则 “ $\left| {z}_{1}\right|  = \left| {z}_{2}\right|$ ” 是 “ ${z}_{1} = {z}_{2}$ ” 的 ( )

A. 充分非必要条件; B. 必要非充分条件;

C. 充要条件; D. 既非充分也非必要条件.

(2)设复数 $z = a + b\mathrm{i}\left( {a\text{ 、 }b \in  \mathbf{R}}\right)$ ，则 ${z}^{2}$ 是纯虚数的充要条件是 ( )

A. ${a}^{2} = {b}^{2}$ ; B. ${a}^{2} + {b}^{2} = 0$ ;

C. $\left| a\right|  = \left| b\right|  \neq  0$ ; D. ${ab} \neq  0$ .

2. 若复数 $z$ 满足 $z + \bar{z} = 2,\left( {z - \bar{z}}\right) \mathrm{i} = 2$ ,求 $\left| z\right|$ .

3. 若复数 ${z}_{1}$ 和复数 ${z}_{2}$ 满足 ${z}_{1}{z}_{2} = 3 - 4\mathrm{i},\left| {z}_{1}\right|  = 2$ ,求 $\left| {z}_{2}\right|$ .

4. 若 ${x}_{1}$ 和 ${x}_{2}$ 是方程 ${x}^{2} - {5x} + 8 = 0$ 的两个根,求 $\left| {x}_{1}\right|  + \left| {x}_{2}\right|$ 的值.

## 拓展与思考

1. 若复数 ${z}_{1}$ 和复数 ${z}_{2}$ 满足 $\left| {z}_{1}\right|  = 3,\left| {z}_{2}\right|  = 4,\left| {{z}_{1} + {z}_{2}}\right|  = 5$ ,求 $\left| {{z}_{1} - {z}_{2}}\right|$ .

2. 已知复数 ${z}_{1}$ 和复数 ${z}_{2}$ 满足 ${z}_{1} + {z}_{2} = 3 - 5\mathrm{i},\overline{{z}_{1}} - \overline{{z}_{2}} =  - 2 + 3\mathrm{i}$ . 求 ${z}_{1}^{2} - {z}_{2}^{2}$ .
