## 数列通项与求和

<table><tr><td>教学目标</td><td>1、掌握由常见数列递推关系式求通项公式的方法, 由数列递推关系式的特点, 选择合适的方法; <br> 2、掌握等差数列与等比数列前 $\mathrm{n}$ 项和公式,并能够应用这些知识解决一些简单的问题</td></tr><tr><td>重点</td><td>1、根据数列的递推公式求解数列通项公式； <br> 2、掌握求一些特殊数列前 n 项和的方法:公式、分组、倒序相加、裂项、错位; <br> 3、理解求数列通项及数列求和中蕴含的数学思想方法.</td></tr><tr><td>难 点</td><td>理解求数列通项及数列求和中蕴含的数学思想方法</td></tr></table>

## (一) 求数列通项

## 知识梳理

## 1、定义法 (等差数列、等比数列通项公式)

2、运用 ${a}_{n} = \left\{  \begin{matrix} {S}_{1} & , n = 1 \\  {S}_{n} - {S}_{n - 1} & , n \geq  2 \end{matrix}\right.$ 求数列通项公式:

数列的通项 ${a}_{n}$ 与前 $n$ 项和 ${S}_{n}$ 的关系是 ${a}_{n} = \left\{  \begin{matrix} {S}_{1} & , n = 1 \\  {S}_{n} - {S}_{n - 1} & , n \geq  2 \end{matrix}\right.$ ,当 $n = 1$ 时, ${a}_{1}$ 若适合 ${S}_{n} - {S}_{n - 1}$ ,则 $n = 1$ 的情况可并入 $n \geq  2$ 时的通项 ${a}_{n}$ ; 当 $n = 1$ 时, ${a}_{1}$ 若不适合 ${S}_{n} - {S}_{n - 1}$ ,则用分段函数的形式表示.

## 3、由递推公式求通项公式

如果已知数列 $\left\{  {a}_{n}\right\}$ 的首项 (或前几项),且任何一项 ${a}_{n}$ 与它的前一项 ${a}_{n - 1}$ (或前几项)间的关系可以用一个式子来表示,即 ${a}_{n} = f\left( {a}_{n - 1}\right)$ 或 ${a}_{n} = f\left( {{a}_{n - 1},{a}_{n - 2}}\right)$ ,那么这个式子叫作数列 $\left\{  {a}_{n}\right\}$ 的递推公式.

已知递推公式求通项公式, 一般用代数的变形技巧整理变形, 然后采用累加法、累乘法、待定系数法 ( 构造法)、取倒数、取对数等转化为等差数列或等比数列求通项公式. 常见方法如下:

(1)累加法:型如 ${a}_{n + 1} = {a}_{n} + f\left( n\right)$ 的一阶递推式，

运用 “累加法” (或 “迭加法”) 求通项公式, 即

$$
{a}_{n} = {a}_{1} + \left( {{a}_{2} - {a}_{1}}\right)  + \left( {{a}_{3} - {a}_{2}}\right)  + \cdots  + \left( {{a}_{n} - {a}_{n - 1}}\right)  = {a}_{1} + \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}f\left( k\right) .
$$

(2)累乘法: ${\text{ 型 }\text{ 如 }}{a}_{n + 1} = {a}_{n} \cdot  f\left( n\right)$ 的递推式，

运用 “累乘法” (或 “迭乘法”) 求通项公式,

即 ${a}_{n} = {a}_{1} \cdot  \frac{{a}_{2}}{{a}_{1}} \cdot  \frac{{a}_{3}}{{a}_{2}}\cdots \frac{{a}_{n}}{{a}_{n - 1}} = {a}_{1} \cdot  f\left( 1\right)  \cdot  f\left( 2\right) \cdots f\left( {n - 1}\right) \left( {n \geq  2}\right)$ .

(3)构造法:

①、型如 ${a}_{n + 1} = p{a}_{n} + q\left( {p \neq  1, q \neq  0}\right)$

可由下面两种方法求通项公式.

方法一: 由 ${a}_{n + 1} = p{a}_{n} + q$ 及 ${a}_{n} = p{a}_{n - 1} + q$ ,两式相减得 ${a}_{n + 1} - {a}_{n} = p\left( {{a}_{n} - {a}_{n - 1}}\right)$ ,有 $\left\{  {{a}_{n + 1} - {a}_{n}}\right\}$ 是首项为 ${a}_{2} - {a}_{1}$ ,公比为 $p$ 的等比数列,先求出 ${a}_{n + 1} - {a}_{n}$ ,再利用 “累加法” 求出 ${a}_{n}$ .

方法二: 构造数列 $\left\{  {{a}_{n} + \lambda }\right\}$ ,满足 ${a}_{n + 1} + \lambda  = p\left( {{a}_{n} + \lambda }\right)$ ,运用 “待定系数法”,解得 $\lambda  = \frac{q}{p - 1}$ ,则 $\left\{  {{a}_{n} + \frac{q}{p - 1}}\right\}$ 是首项为 ${a}_{1} + \frac{q}{p - 1}$ ,公比为 $p$ 的等比数列.

②、型如 ${a}_{n + 1} = p{a}_{n} + {qn} + r\left( {p \neq  1, p \neq  0, q \neq  0}\right)$ 可构造数列 $\left\{  {{a}_{n} + {\lambda n} + \mu }\right\}$ ,满足 ${a}_{n + 1} + \lambda \left( {n + 1}\right)  + \mu  = p\left( {{a}_{n} + {\lambda n} + \mu }\right)$ ,运用待定系数法解得 $\lambda  = \frac{q}{p - 1},\mu  = \frac{r}{p - 1} + \frac{q}{{\left( p - 1\right) }^{2}}$ ,从而由等比数列求出通项公式; 进一步推广,若其中包含 $n$ 的二次 、三次, 则构造的数列中也同样包含对应次数项.

③、型如 ${a}_{n + 1} = p{a}_{n} + f\left( n\right) \left( {p \neq  1, p \neq  0}\right)$ 可在等式两边同除以 ${p}^{n + 1}$ ，构造数列 $\left\{  \frac{{a}_{n}}{{p}^{n}}\right\}$ ，满足 $\frac{{a}_{n + 1}}{{p}^{n + 1}} = \frac{{a}_{n}}{{p}^{n}} + \frac{f\left( n\right) }{{p}^{n + 1}}$ ，令 ${b}_{n} = \frac{{a}_{n}}{{p}^{n}}$ ，则转化为 ${b}_{n + 1} = {b}_{n} + \frac{f\left( n\right) }{{p}^{n + 1}}$ ,即类型(1),利用 “累加法” 求通项公式.

④、型如 ${a}_{n + 1} = \frac{p{a}_{n}}{{a}_{n} + q}\left( {p \neq  0, q \neq  0,{a}_{n} \neq  0}\right)$

运用取倒数,构造数列 $\left\{  \frac{1}{{a}_{n}}\right\}$ ,满足 $\frac{1}{{a}_{n + 1}} = \frac{q}{p{a}_{n}} + \frac{1}{p}$ ,若 $p = q$ 时,则数列 $\left\{  \frac{1}{{a}_{n}}\right\}$ 为等差数列; 若 $p \neq  q$ 时, 转换为类型(3)- I, 再运用 “待定系数法”.

或型如 ${a}_{n} - {a}_{n + 1} = \lambda {a}_{n} \cdot  {a}_{n + 1}$

两边同除 ${a}_{n} \cdot  {a}_{n + 1}$ 得 $\frac{1}{{a}_{n + 1}} - \frac{1}{{a}_{n}} = \lambda$ ,构造数列 $\left\{  \frac{1}{{a}_{n}}\right\}$ 为等差数列.

⑤、型如 ${a}_{n + 1} = p{a}^{r}$

运用两边取对数法得 $\lg {a}_{n + 1} = r\lg {a}_{n} + \lg p$ ,令 ${b}_{n} = \lg {a}_{n}$ ,化为 ${b}_{n + 1} = r{b}_{n} + \lg p$ 型,再用 “待定系数法”.

## (4)周期数列:

和年份有关，代几项，看周期.

①形如 ${a}_{n + 1} =  - \frac{1}{1 + {a}_{n}}\left( {n \in  {N}^{ * }}\right)$ 的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 3$ 的数列.

②形如 ${a}_{n + 1} = 1 - \frac{1}{{a}_{n}}\left( {n \in  {N}^{ * }}\right)$ 的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 3$ 的数列.

③形如 ${a}_{n + 2} = {a}_{n + 1} - {a}_{n}\left( {n \in  {N}^{ * }}\right)$ 的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 6$ 的数列.

④形如 ${a}_{n + 1} = \frac{1 + {a}_{n}}{1 - {a}_{n}}\left( {n \in  {N}^{ * }}\right)$ 的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 4$ 的数列.

⑤形如 ${a}_{n + 1} = C - {a}_{n}\left( {n \in  {N}^{ * }}\right)$ (等和数列)的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 2$ 的数列.

4、除了上述方法还有数学归纳法(归纳一猜想一证明)等.

## 例题精讲

【例1】(1)已知单调递增数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 0,{\left( {a}_{n + 1} + {a}_{n} - 1\right) }^{2} = 4{a}_{n + 1} \cdot  {a}_{n}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ ，则 ${a}_{n} =$ ___.

(2)已知数列 $\left\{  {a}_{n}\right\}$ 的各项均为正数，且 $\frac{{{a}_{n + 1}}^{2}}{{a}_{n}} - 6{a}_{n} - {a}_{n + 1} = 0\left( {n \in  {N}^{ * }}\right)$ ，则 $\frac{{a}_{4} + {a}_{7}}{{a}_{2} + {a}_{5}} =$ ___.

【例2】(1)设数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，若 ${a}_{1} = 1$ ， ${S}_{n} - \frac{1}{2}{a}_{n + 1} = 0\left( {n \in  {N}^{ * }}\right)$ ，则 $\left\{  {a}_{n}\right\}$ 的通项公式为___.

(2)数列 $\left\{  {a}_{n}\right\}$ 满足 $\frac{1}{2}{a}_{1} + \frac{1}{{2}^{2}}{a}_{2} + \cdots  + \frac{1}{{2}^{n}}{a}_{n} = {2n} + 5, n \in  {N}^{ * }$ ，则 ${a}_{n} =$ ___.

(3)设 ${S}_{n}$ 是数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和， ${a}_{1} = 1,{S}_{n}^{2} = {a}_{n}\left( {{S}_{n} - \frac{1}{2}}\right) \left( {n \geq  2}\right)$ ，求 $\left\{  {a}_{n}\right\}$ 的通项。

【例3】(1)已知数列 $\left\{  {a}_{n}\right\}$ 满足: ${a}_{1} = 1,{a}_{n + 1} = \frac{n + 1}{n}{a}_{n} + \frac{n + 1}{{2}^{n}}$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式。

(2)已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 2,\frac{{a}_{n}}{{a}_{n + 1} - {a}_{n}} = \frac{n}{2}$ ，求通项公式 ${a}_{n}$ .

【例4】(1)在数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 2$ ， $3{a}_{n + 1} - 2{a}_{n} - 1 = 0$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

(2)已知数列 $\left\{  {a}_{n}\right\}$ 的首项 ${a}_{1} = 1$ ，前 $n$ 项和为 ${S}_{n}$ ，且 ${S}_{n + 1} = {2{S}_{n}} + n + 1\left( {n \in  {N}^{ * }}\right)$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

(3)已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 1,{a}_{n + 1} = m{a}_{n} + {3}^{n}\left( {m \neq  0}\right)$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【例 5】(1)已知数列 $\left\{  {a}_{n}\right\}$ 满足:对任意的 $n \in  {\mathrm{N}}^{ * }$ 均有 ${a}_{n + 1} = k{a}_{n} + {3k} - 3$ ，其中 $k$ 为不等于 0 与 1 的常数， 若 ${a}_{i} \in  \{  - {678}, - {78}, - 3,{22},{222},{2222}\} , i = 2,3,4,5$ ，则满足条件的 ${a}_{1}$ 所有可能值的和为___.

(2)已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 2,{a}_{n + 1} = 3{a}_{n} + {3}^{n + 1} - {2}^{n}\left( {n \in  {N}^{ * }}\right)$ . 设 ${b}_{n} = \frac{{a}_{n} - {2}^{n}}{{3}^{n}}$ ，证明:数列 $\left\{  {b}_{n}\right\}$ 为等差数列,并求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【例6】已知 ${a}_{1} = 4,{a}_{n + 1} = \frac{2 \cdot  {a}_{n}}{2{a}_{n} + 1}$ ,求 ${a}_{n}$ .

【例 7】设正项数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,\sqrt{{a}_{n}} = 2{a}_{n - 1}\left( {n \geq  2}\right)$ ,求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【例8】(1)数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 0,{a}_{n + 1} + {a}_{n} = {2n}$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

(2)已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 3,{a}_{n} \cdot  {a}_{n + 1} = {\left( \frac{1}{2}\right) }^{n},\left( {n \in  {N}^{ * }}\right)$ ，求此数列的通项公式.

【例9】(1)数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{n + 1} = \left\{  \begin{array}{ll} 2{a}_{n}, & 0 \leq  {a}_{n} \leq  \frac{1}{2} \\  2{a}_{n} - 1, & \frac{1}{2} < {a}_{n} < 1 \end{array}\right.$ ， ${a}_{1} = \frac{3}{5}$ ，则数列的第 2021 项为___.

(2)若数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 2,{a}_{n + 1} = \frac{{a}_{n} + 1}{1 - {a}_{n}},{a}_{2020} =$ ___.

【例10】已知数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n}$ 满足: ${S}_{n} = \frac{{a}_{n}}{2} + \frac{1}{{a}_{n}} - 1$ ,且 ${a}_{n} > 0, n \in  {N}^{ * }$ .

(1)求 ${a}_{1},{a}_{2},{a}_{3}$ ；

(2)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【例11】(1)已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,{a}_{2} = 4$ ,且 $2{a}_{n} = \frac{n - 1}{n}{a}_{n - 1} + \frac{n + 1}{n}{a}_{n + 1}\left( {n \geq  2, n \in  N}\right)$ ，则 $\frac{{a}_{n}}{n}$ 的最大值为( )

A. $\frac{49}{24}$ B. 1 C. 2

D. $\frac{5}{3}$

(2)已知数列 $\left\{  {a}_{n}\right\}$ 是共有 $k$ 个项的有限数列,且满足 ${a}_{n + 1} = {a}_{n - 1} - \frac{n}{{a}_{n}}\left( {n = 2,\cdots , k - 1}\right)$ ,若 ${a}_{1} = {24},{a}_{2} = {51},{a}_{k} = 0$ ,则 $k =$

(3)已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,{a}_{2} = 3,{a}_{n + 2} = 3{a}_{n + 1} - 2{a}_{n}\left( {n \in  {N}^{ * }}\right)$ .

(I) 证明: 数列 $\left\{  {{a}_{n + 1} - {a}_{n}}\right\}$ 是等比数列;

(II) 求数列 $\left\{  {a}_{n}\right\}$ 的通项公式;

(III) 若数列 $\left\{  {b}_{n}\right\}$ 满足 ${4}^{{b}_{1} - 1}{4}^{{b}_{2} - 1}\ldots {4}^{{b}_{n} - 1} = {\left( {a}_{n} + 1\right) }^{{b}_{n}}\left( {n \in  {N}^{ * }}\right)$ ,证明 $\left\{  {b}_{n}\right\}$ 是等差数列。

【例12】已知数列 $\left\{  {a}_{n}\right\}  ,\left\{  {b}_{n}\right\}$ 满足 ${a}_{1} = 2,{b}_{1} = 1$ ,且 $\left\{  {\begin{array}{l} {a}_{n} = \frac{3}{4}{a}_{n - 1} + \frac{1}{4}{b}_{n - 1} + 1, \\  {b}_{n} = \frac{1}{4}{a}_{n - 1} + \frac{3}{4}{b}_{n - 1} + 1, \end{array}\left( {n \geq  2}\right) }\right.$ .

(1)令 ${c}_{n} = {a}_{n} + {b}_{n}$ ，求数列 $\left\{  {c}_{n}\right\}$ 的通项公式；

(2)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【例 13】设 ${a}_{1} = 2,{a}_{n + 1} = \frac{2}{{a}_{n} + 1},{b}_{n} = \left| \frac{{a}_{n} + 2}{{a}_{n} - 1}\right| , n \in  {N}^{ * }$ ，则数列 $\left\{  {b}_{n}\right\}$ 的通项公式 ${b}_{n} =$ ___.

*【例 14】(1)数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = \frac{1}{2},{a}_{n + 1} = \frac{{a}_{n} + 3}{2{a}_{n} - 4}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ ，求通项公式 ${a}_{n}$ .

(2)数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 5,{a}_{n + 1} = \frac{{a}_{n} - 4}{{a}_{n} - 3}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ ，求通项公式 ${a}_{n}$ .

## 巩固训练

1、已知正项数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,\left( {n + 2}\right) {a}_{n + 1}^{2} - \left( {n + 1}\right) {a}_{n}^{2} + {a}_{n}{a}_{n + 1} = 0$ ，则它的通项公式为( )

A. ${a}_{n} = \frac{1}{n + 1}$ B. ${a}_{n} = \frac{2}{n + 1}$ C. ${a}_{n} = \frac{n + 1}{2}$ D. ${a}_{n} = n$

2、设正数数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,数列 $\left\{  {S}_{n}\right\}$ 的前 $n$ 项之积为 ${T}_{n}$ ,且 ${S}_{n} + {T}_{n} = 1$ ,则数列 $\left\{  {a}_{n}\right\}$ 的通项公式是___.

3、已知各项都是正数的数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = \frac{3}{2},{a}_{n + 1} = \frac{1}{2}{a}_{n}\left( {4 - {a}_{n}}\right)$ ,求通项公式 ${a}_{n}$ .

4、某生物病毒繁殖规则如图，现有一个这种生物病毒，初始状态为 $t = 0$ ( $t$ 表示时间，单位:小时)，请写出4小时后此病毒的个数___，由此推测n小时后此病毒的个数为___

![7_527_958_196_180_0.jpg](images/7_527_958_196_180_0.jpg)

![7_860_946_222_206_0.jpg](images/7_860_946_222_206_0.jpg)

$t = 0$ t=1 t=2 t=3

5、已知数列 $\left\{  {a}_{n}\right\}$ 的前 $\mathrm{n}$ 项和 $\mathrm{{Sn}}$ 满足: 当 $\mathrm{n} \in  \mathrm{N} *$ 时, $\mathrm{{Sn}} \neq  0$ ; 当 $\mathrm{n} > 1$ 时, ${a}_{n} + 2{S}_{n}{S}_{n - 1} = 0$ ,且 ${a}_{1} = 1$ . 求数列 $\left\{  {a}_{n}\right\}$ 的通项公式。

6、陈先生买了一套总价为 80 万元住房，首付 30 万元，其余 50 万元向银行申请贷款，贷款月利率 0.5%，从贷款后的第一个月后开始还款，每月还款数额相等，30年还清. 问程先生每月应还款多少元(精确到0.01 元).

(注: 如果上个月欠银行贷款 $a$ 元,则一个月后,程先生应还给银行固定数额 $x$ 元,此时贷款余额为 $a\left( {1 + {0.5}\% }\right)  - x$ 元)

7、在数列 $\left\{  {a}_{n}\right\}$ 中，已知 ${a}_{1} = 2,{a}_{2} = 7,{a}_{n + 2}$ 等于 ${a}_{n}{a}_{n + 1}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ 的个位数，则 ${a}_{2013}$ 的值是 ( )

A. 8 B. 6 C. 4 D. 2

8、意大利著名数学家斐波那契在研究兔子繁殖问题时，发现有这样一列数:1，1，2，3，5，8，13，21， $\ldots$ ,其中从第三项开始,每个数都等于它前面两个数的和,后来人们把这样的一列数组成的数列 $\left\{  {a}_{n}\right\}$ 称为 “斐波那契数列”, 那么 $\frac{{a}_{1}^{2} + {a}_{2}^{2} + {a}_{3}^{2} + \ldots  + {a}_{n}^{2}}{{a}_{n}}\left( {n \geq  3}\right)$ ,是斐波那契数列的第___项.

9、已知数列 $\left\{  {a}_{n}\right\}$ 满足:① ${a}_{1} = 0$ ，②对任意的 $n \in  {N}^{ * }$ 都有 ${a}_{n + 1} > {a}_{n}$ 成立.

函数 ${f}_{n}\left( x\right)  = \left| {\sin \frac{1}{n}\left( {x - {a}_{n}}\right) }\right| , x \in  \left\lbrack  {{a}_{n},{a}_{n + 1}}\right\rbrack$ 满足: 对于任意的实数 $m \in  \lbrack 0,1),{f}_{n}\left( x\right)  = m$ 总有两个不同的根,

10、已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 2,{a}_{n + 1} = 3{a}_{n} + {2}^{n - 1}, n \in  {\mathbf{N}}^{ * }$ .

(1)求证:数列 $\left\{  {{a}_{n} + {2}^{n - 1}}\right\}$ 是等比数列，并求 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)设 ${b}_{n} = {\log }_{\sqrt{3}}\left( {{a}_{n} + {2}^{n - 1}}\right)  + 1$ ，若不等式 ${15}\left( {1 + \frac{1}{{b}_{1}}}\right) \left( {1 + \frac{1}{{b}_{2}}}\right) \cdots \left( {1 + \frac{1}{{b}_{n}}}\right)  \geq  k\sqrt{{10n} + {15}}$ 对于任意 $n \in  {\mathbf{N}}^{ * }$ 都成立,求正数 $k$ 的最大值.

## (二)数列求和

## 知识梳理

求数列前 $\mathrm{n}$ 项和:

1、公式法求和

① 等差数列求和公式: ${S}_{n} = \frac{n\left( {{a}_{1} + {a}_{n}}\right) }{2} = n{a}_{1} + \frac{n\left( {n - 1}\right) }{2}d$

② 等比数列求和公式: ${S}_{n} = \left\{  \begin{matrix} n{a}_{1} & \left( {q = 1}\right) \\  \frac{{a}_{1}\left( {1 - {q}^{n}}\right) }{1 - q} = \frac{{a}_{1} - {a}_{n}q}{1 - q} & \left( {q \neq  1}\right)  \end{matrix}\right.$

③ ${S}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}k = \frac{1}{2}n\left( {n + 1}\right) \;$ ④ ${S}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}{k}^{2} = \frac{1}{6}n\left( {n + 1}\right) \left( {{2n} + 1}\right) \;$ ⑤ ${S}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}{k}^{3} = {\left\lbrack  \frac{1}{2}n\left( n + 1\right) \right\rbrack  }^{2}$

公式法求和注意事项:(1)弄准求和项数 $n$ 的值；

(2)等比数列公比 $q$ 未知时，运用前 $n$ 项和公式要分类.

## 2、分组求和法

分组求和有两种情况, 一种是将数列适当拆开, 可分为几个等差、等比或常见的数列, 然后分别求和, 再将其合并即可; 另一种是将数列相邻的两项 (或若干项) 并成一项 (或一组) 得到一个新数列 (容易求和).

3、裂项相消法

裂项法的实质是将数列中的每项(通项)分解，然后重新组合，使之能消去一些项，最终达到求和的目的, 如:

(1) ${a}_{n} = f\left( {n + 1}\right)  - f\left( n\right)$

(2) ${a}_{n} = \frac{1}{n\left( {n + 1}\right) } = \frac{1}{n} - \frac{1}{n + 1}\xrightarrow[]{\text{ 推广 }}\frac{1}{n\left( {n + k}\right) } = \frac{1}{k}\left( {\frac{1}{n} - \frac{1}{n + k}}\right)$

(3) $\frac{1}{\sqrt{n + 1} + \sqrt{n}} = \sqrt{n + 1} - \sqrt{n}\xrightarrow[]{\text{ 推广 }}\frac{1}{\sqrt{n + k} + \sqrt{n}} = \frac{1}{k}\left( {\sqrt{n + k} - \sqrt{n}}\right)$

(4) $\frac{{a}^{n}}{\left( {{a}^{n} - b}\right) \left( {{a}^{n + 1} - b}\right) } = \frac{1}{a - 1}\left( {\frac{1}{{a}^{n} - b} - \frac{1}{{a}^{n + 1} - b}}\right)$

(5) ${a}_{n} = \frac{{\left( 2n\right) }^{2}}{\left( {{2n} - 1}\right) \left( {{2n} + 1}\right) } = 1 + \frac{1}{2}\left( {\frac{1}{{2n} - 1} - \frac{1}{{2n} + 1}}\right)$

(6) ${a}_{n} = \frac{1}{n\left( {n + 1}\right) \left( {n + 2}\right) } = \frac{1}{2}\left\lbrack  {\frac{1}{n\left( {n + 1}\right) } - \frac{1}{\left( {n + 1}\right) \left( {n + 2}\right) }}\right\rbrack$

(7) ${a}_{n} = \frac{n + 2}{n\left( {n + 1}\right) } \cdot  \frac{1}{{2}^{n}} = \frac{2\left( {n + 1}\right)  - n}{n\left( {n + 1}\right) } \cdot  \frac{1}{{2}^{n}} = \frac{1}{n \cdot  {2}^{n - 1}} - \frac{1}{\left( {n + 1}\right) {2}^{n}}$ ,则 ${S}_{n} = 1 - \frac{1}{\left( {n + 1}\right) {2}^{n}}$

(8) $\frac{\sin {1}^{ \circ  }}{\cos {n}^{ \circ  }\cos {\left( n + 1\right) }^{ \circ  }} = \tan {\left( n + 1\right) }^{ \circ  } - \tan {n}^{ \circ  }$

(9) $\frac{n}{\left( {n + 1}\right) !} = \frac{1}{n!} - \frac{1}{\left( {n + 1}\right) !}$

用裂项相消法求和时,要对通项进行变换,如: $\frac{1}{\sqrt{n + k} + \sqrt{n}} = \frac{1}{k}\left( {\sqrt{n + k} - \sqrt{n}}\right) ,\frac{1}{n\left( {n + k}\right) } = \frac{1}{k}\left( {\frac{1}{n} - \frac{1}{n + k}}\right)$ 裂项后可以产生连续可以相互抵消的项. 抵消后并不一定只剩下第一项和最后一项, 也有可能前面剩两项, 后面也剩两项.

4、倒序相加法

这是推导等差数列的前 $n$ 项和公式时所用的方法,就是将一个数列倒过来排列 (倒序),再把它与原数列相加,就可以得到 $n$ 个 $\left( {{a}_{1} + {a}_{n}}\right)$ .

5、错位相减法

这种方法是在推导等比数列的前 $n$ 项和公式时所用的方法,这种方法主要用于求数列 $\left\{  {{a}_{n} \cdot  {b}_{n}}\right\}$ 的前 $n$ 项和,其中 $\left\{  {a}_{n}\right\}  \text{ 、 }\left\{  {b}_{n}\right\}$ 分别是等差数列和等比数列.

用错位相减法求和时, 应注意:

(1)要善于识别题目类型，特别是等比数列公比为负数的情形；

(2)在写出 “ ${S}_{n}$ ” 与 “ $q{S}_{n}$ ” 的表达式时应特别注意将两式 “错项对齐” 以便下一步准确写出 “ ${S}_{n} - q{S}_{n}$ ”的表达式;

(3)在应用错位相减法求和时，若等比数列的公比为参数，应分公比等于 1 和不等于 1 两种情况求解.

## 例题精讲

【例 15】(1)已知各项均为正数的数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，且 ${a}_{1} = 1,{a}_{n + 1}\left( {{a}_{n + 1} - 1}\right)  = {a}_{n}\left( {{a}_{n} + 1}\right)$ . 若 $\left\lbrack  x\right\rbrack$ 表示不超过 $x$ 的最大整数， ${b}_{n} = \left\lbrack  \frac{{\left( n + 1\right) }^{2}}{2{S}_{n}}\right\rbrack$ ，则数列 $\left\{  {b}_{n}\right\}$ 的前 2021 项和 ${T}_{2021} =$ (   )

A. 1010 B. 1011 C. 2021 D. 2022

(2)“中国剩余定理”又称 “孙子定理”，讲的是关于整除的问题 (如 7 被 3 除余 1:1 被 2 除余 1). 现有这样一个整除问题: 将 1 到 100 这 100 个正整数中能被 2 除余 1 且被 3 除余 1 的数按从小到大的顺序排成一列,构成数列 $\left\{  {a}_{n}\right\}$ ,则数列 $\left\{  {a}_{n}\right\}$ 各项的和为(   )

A. 736 B. 816 C. 833 D. 29800

【例 16】已知数列 $\left\{  {a}_{n}\right\}$ 和 $\left\{  {b}_{n}\right\}$ 满足 ${a}_{1} = 1,{b}_{1} = 0,4{a}_{n + 1} = 3{a}_{n} - {b}_{n} + 4,4{b}_{n + 1} = 3{b}_{n} - {a}_{n} - 4$ .

(1)证明: $\left\{  {{a}_{n} + {b}_{n}}\right\}$ 是等比数列， $\left\{  {{a}_{n} - {b}_{n}}\right\}$ 是等差数列；

(2)求 $\left\{  {a}_{n}\right\}$ 和 $\left\{  {b}_{n}\right\}$ 的通项公式；

(3)令 ${c}_{n} = \left\{  \begin{array}{ll} {a}_{n} & n\text{ 是奇数 } \\  {b}_{n} & n\text{ 是偶数 } \end{array}\right.$ ，求数列 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n}$ 的通项公式，并求数列 $\left\{  \frac{1}{{S}_{n}}\right\}$ 的最大值、最小值，并指出分别是第几项.

【例 17】求证: ${C}_{n}^{0} + 3{C}_{n}^{1} + 5{C}_{n}^{2} + \cdots  + \left( {{2n} + 1}\right) {C}_{n}^{n} = \left( {n + 1}\right)  \cdot  {2}^{n}$ ;

【例 18】数列 $\left\{  {b}_{n}\right\}$ 满足 ${b}_{n + 1} = \frac{{b}_{n}}{2} + \frac{1}{{2}^{n + 1}}$ ,若 ${b}_{1} = \frac{1}{2}$ ,则 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为(   )

A. $1 - \frac{n + 2}{{2}^{n + 1}}$ B. $1 - \frac{n + 1}{{2}^{n + 1}}$ C. $2 - \frac{n + 2}{{2}^{n}}$ D. $2 - \frac{{3n} + 3}{{2}^{n + 1}}$

【例 19】已知数列 $\left\{  {a}_{n}\right\}$ : 满足 ${a}_{1} = 2,{a}_{n + 1} = {a}_{n}^{2} + 6{a}_{n} + 6\left( {n \in  {N}^{ * }}\right)$ .

(1)设 ${C}_{n} = {\log }_{5}\left( {{a}_{n} + 3}\right)$ ，求证是等比数列；

(2)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式

(3)设 ${b}_{n} = \frac{1}{{a}_{n} - 6} - \frac{1}{{a}_{n}^{2} + 6{a}_{n}}$ ，数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ，求证: $- \frac{5}{16} \leq  {T}_{n} <  - \frac{1}{4}$ .

【例 20】已知等差数列 $\left\{  {a}_{n}\right\}$ 的公差为 2,前 $n$ 项和为 ${S}_{n}$ ,且 ${S}_{1},{S}_{2},{S}_{4}$ 成等比数列.

(I) 求数列 $\left\{  {a}_{n}\right\}$ 的通项公式;

(II) 令 ${b}_{n} = {\left( -1\right) }^{n - 1}\frac{4n}{{a}_{n}{a}_{n + 1}}$ ,求数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和 ${T}_{n}$ .

## 巩固训练

1、记 ${a}_{m}$ 为数列 $\left\{  {3}^{n}\right\}$ 在区间 $(0, m\rbrack \left( {n \in  {N}^{ * }}\right)$ 中的项的个数,则数列 $\left\{  {a}_{m}\right\}$ 的前 100 项的和 ${S}_{100} =$ ___.

2、已知等差数列 $\left\{  {a}_{n}\right\}$ 中 ${a}_{1} = d = 1$ ， ${b}_{n} = \tan {a}_{n} \cdot  \tan {a}_{n + 1}\left( {n \in  {N}^{ * }}\right)$ ，则数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n} =$ ___.

3. 已知 ${a}_{1} = 2$ ，点 $\left( {{a}_{n},{a}_{n + 1}}\right)$ 在函数 $f\left( x\right)  = {x}^{2} + {2x}$ 的图象上 $\left( {n \in  {N}^{ * }}\right)$ ， ${b}_{n} = \frac{1}{{a}_{n}} + \frac{1}{{a}_{n} + 2}$ ，则数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n} =$ ___.

4. $\frac{1}{0!{10}!} + \frac{1}{1!9!} + \frac{1}{2!8!} + \frac{1}{3!7!} + \frac{1}{4!6!} + \frac{1}{5!5!} + \frac{1}{6!4!} + \frac{1}{7!3!} + \frac{1}{8!2!} + \frac{1}{9!1!} + \frac{1}{{10}!0!} =$

5、已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = {24},{a}_{n + 1} = \frac{n + 3}{n}{a}_{n} + \left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right)$ .

(1)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)用适当的组合数形式表示 ${a}_{n}$ ，并求数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n}$ ；

(3)若 ${b}_{n} = \frac{{a}_{n} \cdot  {2}^{n + 1}}{{\left( n + 2\right) }^{2}\left( {n + 3}\right) }$ ，记数列 $\left\{  \frac{1}{{b}_{n}}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ，求 $\mathop{\lim }\limits_{{x \rightarrow  \infty }}{T}_{n}$ .

6、在数列 $\left\{  {a}_{n}\right\}$ 中,已知 ${a}_{1} = 2,{a}_{n + 1}{a}_{n} = 2{a}_{n} - {a}_{n + 1}\left( {n \in  {N}^{ * }}\right)$ .

(1)证明:数列 $\left\{  {\frac{1}{{a}_{n}} - 1}\right\}$ 为等比数列；

(2)记 ${b}_{n} = \frac{{a}_{n}{a}_{n + 1}}{{2}^{n}}$ ，数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，求使得 ${S}_{n} > {1.999}$ 的整数 $n$ 的最小值；

(3)是否存在正整数 $m\text{ 、 }n\text{ 、 }k$ ，且 $m < n < k$ ，使得 ${a}_{m}\text{ 、 }{a}_{n}\text{ 、 }{a}_{k}$ 成等差数列？若存在，求出 $m\text{ 、 }n\text{ 、 }k$ 的值; 若不存在, 请说明理由.

## 实战演练

## 一、填空题

1、已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 3$ ，且 $n \in  {N}^{ * }$ 时， ${a}_{n + 1} = \frac{n}{n + 2}{a}_{n}$ ，求通项 ${a}_{n} =$ ___.

2、已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,3{a}_{n + 1}{a}_{n} = {a}_{n} - {a}_{n + 1}$ ，则通项 ${a}_{n} =$ ___.

3、设 ${S}_{n}$ 是数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和且 ${a}_{1} = 2,{a}_{n + 1} = {S}_{n} \cdot  {S}_{n + 1}$ ，则 ${S}_{n} =$ ___.

4、若数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1$ ， $n{a}_{n + 1} - \left( {n + 1}\right) {a}_{n} = 2$ ，则数列 $\left\{  {a}_{n}\right\}$ 的通项公式为___.

5、已知数列 $\left\{  {a}_{n}\right\}  ,\left\{  {b}_{n}\right\}$ 满足 ${a}_{1} = {b}_{1} = 1$ ，对任何正整数 $n$ 均有 ${a}_{n + 1} = {a}_{n} + {b}_{n} + \sqrt{{a}_{n}^{2} + {b}_{n}^{2}}$ ， ${b}_{n + 1} = {a}_{n} + {b}_{n} - \sqrt{{a}_{n}^{2} + {b}_{n}^{2}}$ ， 设 ${c}_{n} = {3}^{n}\left( {\frac{1}{{a}_{n}} + \frac{1}{{b}_{n}}}\right)$ ,则数列 $\left\{  {c}_{n}\right\}$ 的前 2020 项之和为___.

6、我们知道: $\frac{n + p}{n\left( {n + q}\right) } = \frac{p}{q} \cdot  \frac{1}{n} - \frac{p - q}{q} \cdot  \frac{1}{n + q}$ .

已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 1$ ， ${a}_{n} = 2{a}_{n - 1} + \frac{n + 2}{n\left( {n + 1}\right) }$ ， $\left( {n \geq  2\text{ ， }n \in  {N}^{ * }}\right)$ ，则数列 $\left\{  {a}_{n}\right\}$ 的通项公式 ${a}_{n} =$ ___.

## 二、选择题

7、已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 1$ ， ${a}_{n + 1} - {a}_{n} = \frac{1}{n\left( {n + 1}\right) }$ ，则 ${a}_{2020}$ 等于( )

A. $\frac{2019}{2020}$ B. $\frac{4039}{2020}$ C. $\frac{2020}{2021}$ D. $\frac{4041}{2021}$

8、在各项均为正数的数列 $\left\{  {a}_{n}\right\}$ 中, ${S}_{n}$ 是其前 $n$ 项和, $n{a}_{n + 1}^{2} = \left( {n + 1}\right) {a}_{n}^{2} + {a}_{n}{a}_{n + 1}$ 且 ${a}_{3} = \pi$ ,则 $\tan {S}_{4}$ 的值等于 ( )

A. $- \sqrt{3}$

B. $- \frac{\sqrt{3}}{3}$ C. $\frac{\sqrt{3}}{3}$ D. $\sqrt{3}$

9、已知正数数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{n + 1} \geq  2{a}_{n} + 1$ ，且 ${a}_{n} < {2}^{n + 1}$ 对 $n \in  {N}^{ * }$ 恒成立，则 ${a}_{1}$ 的范围为( )

A. $\left\lbrack  {1,3}\right\rbrack$ B. $\left( {1,3}\right)$ C. $(0,3\rbrack$ D. $\left( {0,4}\right)$

10、已知“整数对”按如下规律排列:(1,1),(1,2),(2,1),(1,3),(2,2),(3,1),(1,4),(2,3),(3,2),(4,1),...,则第 68 个“整数对”为( )

A. $\left( {1,{12}}\right)$ B. $\left( {3,{10}}\right)$ C. $\left( {2,{11}}\right)$ D. $\left( {3,9}\right)$

## 三、解答题

11、等差数列 $\left\{  {a}_{n}\right\}$ 的首项为 1,公差 $d \neq  0$ ,且 ${a}_{1}\text{ 、 }{a}_{2}\text{ 、 }{a}_{5}$ 成等比数列,数列 $\left\{  {b}_{n}\right\}$ 满足 ${b}_{1} = 1$ 且 $\frac{1}{{b}_{n + 1}} = \frac{1}{{b}_{n}} - \frac{1}{{2}^{n}}\left( {n \in  {N}^{ * }}\right) .$

(1)求 ${a}_{n}$ 、 ${b}_{n}$ ；

(2)若 ${c}_{n} = \frac{{a}_{n}}{{b}_{n}}$ ，数列 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ .

① 求 ${S}_{n}$ ；

② 求使 ${S}_{n} > \frac{35}{8}$ 的最小正整数 $n$ .

12、已知 $\overrightarrow{a} = \left( {{S}_{n},2}\right) ,\overrightarrow{b} = \left( {1,1 - {a}_{n}}\right)$ ,对任意 $n \in  {N}^{ * }$ ,有 $\overrightarrow{a} \bot  \overrightarrow{b}$ 成立.

(1)求 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)设 ${b}_{n + 1} = 2{b}_{n} - {2}^{n + 1},{b}_{1} = 8,{T}_{n}$ 是数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和，求正整数 $k$ ，使得对任意 $n \in  {N}^{ * }$ ， ${T}_{k} \geq  {T}_{n}$ 恒成立;

(3)设 ${c}_{n} = \frac{{a}_{n + 1}}{\left( {1 + {a}_{n}}\right) \left( {1 + {a}_{n + 1}}\right) },{R}_{n}$ 是数列 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项和，若对任意 $n \in  {N}^{ * }$ 均有 ${R}_{n} < \lambda$ 恒成立，求 $\lambda$ 的最小值.
