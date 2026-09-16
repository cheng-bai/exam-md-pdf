## 数列通项与求和

<table><tr><td>教学目标</td><td>1、掌握由常见数列递推关系式求通项公式的方法，由数列递推关系式的特点，选择合适的方法; <br> 2、掌握等差数列与等比数列前 $\mathrm{n}$ 项和公式，并能够应用这些知识解决一些简单的问题</td></tr><tr><td>重点</td><td>1、根据数列的递推公式求解数列通项公式； <br> 2、掌握求一些特殊数列前 $\mathrm{n}$ 项和的方法: 公式、分组、倒序相加、裂项、错位; <br> 3、理解求数列通项及数列求和中蕴含的数学思想方法.</td></tr><tr><td>难 点</td><td>理解求数列通项及数列求和中蕴含的数学思想方法</td></tr></table>

## (一) 求数列通项

## 知识梳理

## 1、定义法(等差数列、等比数列通项公式)

2、运用 ${a}_{n} = \left\{  \begin{matrix} {S}_{1} & , n = 1 \\  {S}_{n} - {S}_{n - 1} & , n \geq  2 \end{matrix}\right.$ 求数列通项公式:

数列的通项 ${a}_{n}$ 与前 $n$ 项和 ${S}_{n}$ 的关系是 ${a}_{n} = \left\{  \begin{array}{ll} {S}_{1} & , n = 1 \\  {S}_{n} - {S}_{n - 1} & , n \geq  2 \end{array}\right.$ ,当 $n = 1$ 时, ${a}_{1}$ 若适合 ${S}_{n} - {S}_{n - 1}$ ,则 $n = 1$ 的情况可并入 $n \geq  2$ 时的通项 ${a}_{n}$ ; 当 $n = 1$ 时, ${a}_{1}$ 若不适合 ${S}_{n} - {S}_{n - 1}$ ,则用分段函数的形式表示.

## 3、由递推公式求通项公式

如果已知数列 $\left\{  {a}_{n}\right\}$ 的首项 (或前几项),且任何一项 ${a}_{n}$ 与它的前一项 ${a}_{n - 1}$ (或前几项) 间的关系可以用一个式子来表示,即 ${a}_{n} = f\left( {a}_{n - 1}\right)$ 或 ${a}_{n} = f\left( {{a}_{n - 1},{a}_{n - 2}}\right)$ ,那么这个式子叫作数列 $\left\{  {a}_{n}\right\}$ 的递推公式.

已知递推公式求通项公式, 一般用代数的变形技巧整理变形, 然后采用累加法、累乘法、待定系数法 ( 构造法)、取倒数、取对数等转化为等差数列或等比数列求通项公式. 常见方法如下:

(1)累加法:型如 ${a}_{n + 1} = {a}_{n} + f\left( n\right)$ 的一阶递推式,

运用 “累加法” (或 “迭加法”) 求通项公式, 即

$$
{a}_{n} = {a}_{1} + \left( {{a}_{2} - {a}_{1}}\right)  + \left( {{a}_{3} - {a}_{2}}\right)  + \cdots  + \left( {{a}_{n} - {a}_{n - 1}}\right)  = {a}_{1} + \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}f\left( k\right) .
$$

(2)累乘法:型如 ${a}_{n + 1} = {a}_{n} \cdot  f\left( n\right)$ 的递推式，

运用“累乘法” (或 “迭乘法”) 求通项公式,

即 ${a}_{n} = {a}_{1} \cdot  \frac{{a}_{2}}{{a}_{1}} \cdot  \frac{{a}_{3}}{{a}_{2}}\cdots \frac{{a}_{n}}{{a}_{n - 1}} = {a}_{1} \cdot  f\left( 1\right)  \cdot  f\left( 2\right) \cdots f\left( {n - 1}\right) \left( {n \geq  2}\right)$ .

(3)构造法:

①、型如 ${a}_{n + 1} = p{a}_{n} + q\left( {p \neq  1, q \neq  0}\right)$

可由下面两种方法求通项公式.

方法一: 由 ${a}_{n + 1} = p{a}_{n} + q$ 及 ${a}_{n} = p{a}_{n - 1} + q$ ,两式相减得 ${a}_{n + 1} - {a}_{n} = p\left( {{a}_{n} - {a}_{n - 1}}\right)$ ,有 $\left\{  {{a}_{n + 1} - {a}_{n}}\right\}$ 是首项为 ${a}_{2} - {a}_{1}$ ,公比为 $p$ 的等比数列,先求出 ${a}_{n + 1} - {a}_{n}$ ,再利用 “累加法” 求出 ${a}_{n}$ .

方法二: 构造数列 $\left\{  {{a}_{n} + \lambda }\right\}$ ,满足 ${a}_{n + 1} + \lambda  = p\left( {{a}_{n} + \lambda }\right)$ ,运用 “待定系数法”,解得 $\lambda  = \frac{q}{p - 1}$ ,则 $\left\{  {{a}_{n} + \frac{q}{p - 1}}\right\}$ 是首项为 ${a}_{1} + \frac{q}{p - 1}$ ,公比为 $p$ 的等比数列.

②、型如 ${a}_{n + 1} = p{a}_{n} + {qn} + r\left( {p \neq  1, p \neq  0, q \neq  0}\right)$ 可构造数列 $\left\{  {{a}_{n} + {\lambda n} + \mu }\right\}$ ,满足 ${a}_{n + 1} + \lambda \left( {n + 1}\right)  + \mu  = p\left( {{a}_{n} + {\lambda n} + \mu }\right)$ ,运用待定系数法解得 $\lambda  = \frac{q}{p - 1},\mu  = \frac{r}{p - 1} + \frac{q}{{\left( p - 1\right) }^{2}}$ ,从而由等比数列求出通项公式; 进一步推广,若其中包含 $n$ 的二次 、三次, 则构造的数列中也同样包含对应次数项.

③、型如 ${a}_{n + 1} = p{a}_{n} + f\left( n\right) \left( {p \neq  1, p \neq  0}\right)$

可在等式两边同除以 ${p}^{n + 1}$ ，构造数列 $\left\{  \frac{{a}_{n}}{{p}^{n}}\right\}$ ，满足 $\frac{{a}_{n + 1}}{{p}^{n + 1}} = \frac{{a}_{n}}{{p}^{n}} + \frac{f\left( n\right) }{{p}^{n + 1}}$ ，令 ${b}_{n} = \frac{{a}_{n}}{{p}^{n}}$ ，则转化为 ${b}_{n + 1} = {b}_{n} + \frac{f\left( n\right) }{{p}^{n + 1}}$ ,即类型(1),利用 “累加法” 求通项公式.

④、型如 ${a}_{n + 1} = \frac{p{a}_{n}}{{a}_{n} + q}\left( {p \neq  0, q \neq  0,{a}_{n} \neq  0}\right)$

运用取倒数,构造数列 $\left\{  \frac{1}{{a}_{n}}\right\}$ ,满足 $\frac{1}{{a}_{n + 1}} = \frac{q}{p{a}_{n}} + \frac{1}{p}$ ,若 $p = q$ 时,则数列 $\left\{  \frac{1}{{a}_{n}}\right\}$ 为等差数列; 若 $p \neq  q$ 时, 转换为类型(3)-I, 再运用 “待定系数法”.

或型如 ${a}_{n} - {a}_{n + 1} = \lambda {a}_{n} \cdot  {a}_{n + 1}$

两边同除 ${a}_{n} \cdot  {a}_{n + 1}$ 得 $\frac{1}{{a}_{n + 1}} - \frac{1}{{a}_{n}} = \lambda$ ,构造数列 $\left\{  \frac{1}{{a}_{n}}\right\}$ 为等差数列.

⑤、型如 ${a}_{n + 1} = p{a}^{r}$

运用两边取对数法得 $\lg {a}_{n + 1} = r\lg {a}_{n} + \lg p$ ,令 ${b}_{n} = \lg {a}_{n}$ ,化为 ${b}_{n + 1} = r{b}_{n} + \lg p$ 型,再用 “待定系数法”.

## (4)周期数列:

和年份有关，代几项，看周期.

① 形如 ${a}_{n + 1} =  - \frac{1}{1 + {a}_{n}}\left( {n \in  {N}^{ * }}\right)$ 的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 3$ 的数列.

② 形如 ${a}_{n + 1} = 1 - \frac{1}{{a}_{n}}\left( {n \in  {N}^{ * }}\right)$ 的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 3$ 的数列.

③ 形如 ${a}_{n + 2} = {a}_{n + 1} - {a}_{n}\left( {n \in  {N}^{ * }}\right)$ 的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 6$ 的数列.

④形如 ${a}_{n + 1} = \frac{1 + {a}_{n}}{1 - {a}_{n}}\left( {n \in  {N}^{ * }}\right)$ 的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 4$ 的数列.

⑤形如 ${a}_{n + 1} = C - {a}_{n}\left( {n \in  {N}^{ * }}\right)$ (等和数列)的数列 $\left\{  {a}_{n}\right\}$ 是周期为 $T = 2$ 的数列.

4、除了上述方法还有数学归纳法(归纳一猜想一证明)等.

## 例题精讲

【例1】(1)已知单调递增数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 0,{\left( {a}_{n + 1} + {a}_{n} - 1\right) }^{2} = 4{a}_{n + 1} \cdot  {a}_{n}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ ，则 ${a}_{n} =$ ___

【难度】 $\star   \star   \star   \star$

【答案】 ${\left( n - 1\right) }^{2}$

【解析】解: $\because {a}_{1} = 0,{\left( {a}_{n + 1} + {a}_{n} - 1\right) }^{2} = 4{a}_{n + 1} \cdot  {a}_{n},\therefore {\left( {a}_{2} + {a}_{1} - 1\right) }^{2} = 4{a}_{2} \cdot  {a}_{1}$ ,即 ${\left( {a}_{2} - 1\right) }^{2} = 0$ ,所以 ${a}_{2} = 1$

，由于数列 $\left\{  {a}_{n}\right\}$ 是递增数列，则 ${a}_{n + 1} + {a}_{n} \geq  {a}_{1} + {a}_{2} = 1$ ，且 $4{a}_{n + 1} \cdot  {a}_{n} \geq  0$ ， $\therefore {a}_{n + 1} + {a}_{n} - 1 \geq  0$ ，由于

${\left( {a}_{n + 1} + {a}_{n} - 1\right) }^{2} = 4{a}_{n + 1} \cdot  {a}_{n}$ ,则 ${a}_{n + 1} + {a}_{n} - 1 = 2\sqrt{{a}_{n}{a}_{n + 1}}$ ,即 ${a}_{n + 1} + {a}_{n} - 2\sqrt{{a}_{n}{a}_{n + 1}} = 1,\therefore {\left( \sqrt{{a}_{n + 1}} - \sqrt{{a}_{n}}\right) }^{2} = 1$

,而数列 $\left\{  {a}_{n}\right\}$ 是递增数列,则 $\sqrt{{a}_{n + 1}} - \sqrt{{a}_{n}} > 0,\therefore \sqrt{{a}_{n + 1}} - \sqrt{{a}_{n}} = 1,\therefore$ 数列 $\left\{  \sqrt{{a}_{n}}\right\}$ 是首项为 0,公差为 1 的等差数列, $\therefore \sqrt{{a}_{n}} = 0 + \left( {n - 1}\right)  \times  1 = n - 1,\therefore {a}_{n} = {\left( n - 1\right) }^{2}\left( {n \in  {N}^{ * }}\right)$ . 故答案为: ${\left( n - 1\right) }^{2}$ .

(2)已知数列 $\left\{  {a}_{n}\right\}$ 的各项均为正数，且 $\frac{{{a}_{n + 1}}^{2}}{{a}_{n}} - 6{a}_{n} - {a}_{n + 1} = 0\left( {n \in  {N}^{ * }}\right)$ ，则 $\frac{{a}_{4} + {a}_{7}}{{a}_{2} + {a}_{5}} =$ ___.

【难度】★★★★

【答案】 9

【解析】解: $\because \frac{{a}_{n + 1}{}^{2}}{{a}_{n}} = 6{a}_{n} + {a}_{n + 1}\left( {n \in  {N}^{ * }}\right) ,\therefore {a}_{n + 1}{}^{2} - {a}_{n}{a}_{n + 1} - 6{a}_{n}{}^{2} = 0,\therefore \left( {{a}_{n + 1} - 3{a}_{n}}\right) \left( {{a}_{n + 1} + 2{a}_{n}}\right)  = 0$ , $\because$ 数列 $\left\{  {a}_{n}\right\}$ 的各项均为正数, $\therefore {a}_{n + 1} = 3{a}_{n}$ 或 ${a}_{n + 1} =  - 2{a}_{n}$ (舍去), $\therefore$ 数列 $\left\{  {a}_{n}\right\}$ 是公比为 $q = 3$ 的等比数列, $\therefore \frac{{a}_{4} + {a}_{7}}{{a}_{2} + {a}_{5}} = \frac{{q}^{2}\left( {{a}_{2} + {a}_{5}}\right) }{{a}_{2} + {a}_{5}} = 9$ ,故答案为: 9 .

【例2】(1)设数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，若 ${a}_{1} = 1$ ， ${S}_{n} - \frac{1}{2}{a}_{n + 1} = 0\left( {n \in  {N}^{ * }}\right)$ ，则 $\left\{  {a}_{n}\right\}$ 的通项公式为___.

【难度】 $\star   \star   \star   \star$

【答案】 ${a}_{n} = \left\{  \begin{matrix} 1 & , n = 1 \\  2 \cdot  {3}^{n - 2} & , n \geq  2 \end{matrix}\right.$

【解析】方法一: 令 $n = 1$ ,可得 ${S}_{1} - \frac{1}{2}{a}_{2} = 0$ ,即 ${a}_{2} = 2$ .

由题可得, $\left\{  \begin{array}{ll} {S}_{n} = \frac{1}{2}{a}_{n + 1}\left( 1\right) & n \geq  1, n \in  {N}^{ * } \\  {S}_{n - 1} = \frac{1}{2}{a}_{n}\left( 2\right) & n \geq  2, n \in  {N}^{ * } \end{array}\right.$

①-②，可得 ${a}_{n + 1} = 3{a}_{n}, n \geq  2$ .

$\therefore$ 数列 $\left\{  {a}_{n}\right\}$ 是以 ${a}_{2} = 2$ 为首选,3 为公比的等比数列

$\therefore {a}_{n} = 2 \cdot  {3}^{n - 2}, n \geq  2$ .

经验证, ${a}_{1} = 1$ 不符合 ${a}_{n} = 2 \cdot  {3}^{n - 2}$

所以该数列的通项公式为 ${a}_{n} = \left\{  \begin{array}{ll} 1 & , n = 1 \\  2 \cdot  {3}^{n - 2} & , n \geq  2 \end{array}\right.$

方法二: 先利用 ${S}_{n} = \frac{1}{2}{a}_{n + 1} = \frac{1}{2}\left( {{S}_{n + 1} - {S}_{n}}\right)$ 先求出数列 $\left\{  {S}_{n}\right\}$ ,后在求出 $\left\{  {a}_{n}\right\}$ .

(2)数列 $\left\{  {a}_{n}\right\}$ 满足 $\frac{1}{2}{a}_{1} + \frac{1}{{2}^{2}}{a}_{2} + \cdots  + \frac{1}{{2}^{n}}{a}_{n} = {2n} + 5, n \in  {N}^{ * }$ ，则 ${a}_{n} =$ ___.

【难度】 $\star   \star   \star   \star$

【答案】 ${a}_{n} = \left\{  \begin{array}{ll} {14} & n = 1 \\  {2}^{n + 1}, & n \geq  2, n \in  {N}^{ * } \end{array}\right.$

【解析】令 $n = 1$ ,可得 $\frac{1}{2}{a}_{1} = 7$ ,即 ${a}_{1} = {14}$ .

由题可得, $\left\{  \begin{array}{ll} \frac{1}{2}{a}_{1} + \frac{1}{{2}^{2}}{a}_{2} + \cdots  + \frac{1}{{2}^{n}}{a}_{n} = {2n} + 5\left( 1\right) & n \geq  1, n \in  {N}^{ * } \\  \frac{1}{2}{a}_{1} + \frac{1}{{2}^{2}}{a}_{2} + \cdots  + \frac{1}{{2}^{n - 1}}{a}_{n - 1} = 2\left( {n - 1}\right)  + 5\left( 2\right) & n \geq  2, n \in  {N}^{ * } \end{array}\right.$ .

①-②，可得 ${a}_{n} = {2}^{n + 1}$ ， $n \geq  2$ .

经验证, ${a}_{1} = {14}$ 不符合 ${a}_{n} = {2}^{n + 1}\; \leftarrow$ 该步很重要,7

所以该数列的通项公式为 ${a}_{n} = \left\{  \begin{array}{ll} {14} & n = 1 \\  {2}^{n + 1}, & n \geq  2, n \in  {N}^{ * } \end{array}\right.$ .

(3)设 ${S}_{n}$ 是数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和， ${a}_{1} = 1$ ， ${S}_{n}^{2} = {a}_{n}\left( {{S}_{n} - \frac{1}{2}}\right) \left( {n \geq  2}\right)$ ，求 $\left\{  {a}_{n}\right\}$ 的通项。

【难度】 $\star   \star   \star   \star$

【答案】 ${a}_{n} = \frac{2}{{\left( 2n - 1\right) }^{2}}$

【解析】 $\because {S}_{n}^{2} = {a}_{n}\left( {{S}_{n} - \frac{1}{2}}\right) ,\therefore n \geq  2$ 时, ${S}_{n}^{2} = \left( {{S}_{n} - {S}_{n - 1}}\right) \left( {{S}_{n} - \frac{1}{2}}\right)$ ,

整理得, ${S}_{n - 1} - {S}_{n} = 2{S}_{n - 1}{S}_{n} \Rightarrow  \frac{1}{{S}_{n}} - \frac{1}{{S}_{n - 1}} = 2$ ,

$\therefore$ 数列 $\left\{  {a}_{n}\right\}$ 是以 2 为公差的等差数列,其首项为 $\frac{1}{{S}_{1}} = 1$ .

$\therefore \frac{1}{{S}_{n}} = 1 + 2\left( {n - 1}\right)  \Rightarrow  {S}_{n} = \frac{1}{{2n} - 1},\therefore {a}_{n} = \frac{2{S}_{n}^{2}}{2{S}_{n} - 1} = \frac{2}{{\left( 2n - 1\right) }^{2}}$ ;

【例3】(1)已知数列 $\left\{  {a}_{n}\right\}$ 满足: ${a}_{1} = 1,{a}_{n + 1} = \frac{n + 1}{n}{a}_{n} + \frac{n + 1}{{2}^{n}}$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式。

【难度】 $\star   \star   \star$

【答案】 ${a}_{n} = {2n} - \frac{n}{{2}^{n - 1}}$

【解析】由 ${a}_{n + 1} = \frac{n + 1}{n}{a}_{n} + \frac{n + 1}{{2}^{n}}$ ,可得 $\frac{{a}_{n + 1}}{n + 1} = \frac{{a}_{n}}{n} + \frac{1}{{2}^{n}}$ ,

又 ${b}_{n} = \frac{{a}_{n}}{n},\therefore {b}_{n + 1} - {b}_{n} = \frac{1}{{2}^{n}}$ ，由 ${a}_{1} = 1$ ，得 ${b}_{1} = 1$ ，

由累加法可得 $\left( {{b}_{2} - {b}_{1}}\right)  + \left( {{b}_{3} - {b}_{2}}\right)  + \ldots  + \left( {{b}_{n} - {b}_{n - 1}}\right)  = \frac{1}{{2}^{1}} + \frac{1}{{2}^{2}} + \ldots  + \frac{1}{{2}^{n - 1}}$ ,

即 ${b}_{n} - {b}_{1} = \frac{\frac{1}{2}\left( {1 - \frac{1}{{2}^{n - 1}}}\right) }{1 - \frac{1}{2}} = 1 - \frac{1}{{2}^{n - 1}},\therefore {b}_{n} = 2 - \frac{1}{{2}^{n - 1}}$ . $\left( {n = 1\text{ 时也满足 }}\right) ,{a}_{n} = {2n} - \frac{n}{{2}^{n - 1}}$ ,

(2)已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 2$ ， $\frac{{a}_{n}}{{a}_{n + 1} - {a}_{n}} = \frac{n}{2}$ ，求通项公式式 6 。

【难度】 $\star   \star   \star   \star$

【答案】 ${a}_{n} = n\left( {n + 1}\right)$

【解析】 $\frac{{a}_{n}}{{a}_{n + 1} - {a}_{n}} = \frac{n}{2} \Rightarrow  \frac{{a}_{n + 1}}{{a}_{n}} = \frac{n + 2}{n}$

法一: $\therefore$ 当 $n \geq  2$ 时， ${a}_{n} = {a}_{1} \cdot  \frac{{a}_{2}}{{a}_{1}} \cdot  \frac{{a}_{3}}{{a}_{2}}\cdots \frac{{a}_{n}}{{a}_{n - 1}} = 2 \times  \frac{3}{1} \times  \frac{4}{2} \times  \frac{5}{3} \times  \cdots  \times  \frac{n + 2}{n} = n\left( {n + 1}\right)$ ；

当 $n = 1$ 时, ${a}_{1} = 2$ 符合上式;

$\therefore {a}_{n} = n\left( {n + 1}\right)$ .

法二: $\frac{{a}_{n}}{{a}_{n + 1} - {a}_{n}} = \frac{n}{2} \Rightarrow  \frac{{a}_{n + 1}}{{a}_{n}} = \frac{n + 2}{n} \Rightarrow  \frac{{a}_{n + 1}}{\left( {n + 2}\right) \left( {n + 1}\right) } = \frac{{a}_{n}}{n\left( {n + 1}\right) } \; \therefore \left\{  \frac{{a}_{n}}{n\left( {n + 1}\right) }\right\}$ 为常值数列, $\frac{{a}_{n}}{n\left( {n + 1}\right) } = \frac{{a}_{1}}{2} = 1 \Rightarrow  {a}_{n} = n\left( {n + 1}\right)$

【例4】( 1 )在数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 2$ ， $3{a}_{n + 1} - 2{a}_{n} - 1 = 0$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【难度】 $m \neq  m$

【答案】 ${a}_{n} = {2}^{n} - 1$

【解析】解法一: $3{a}_{n + 1} = 2{a}_{n} + {1.3}{a}_{n} = 2{a}_{n - 1} + 1$ ,两式相减可得: $3\left( {{a}_{n + 1} - {a}_{n}}\right)  = 2\left( {{a}_{n} - {a}_{n - 1}}\right)$ ,即 $\left\{  {{a}_{n + 1} - {a}_{n}}\right\}$ 为等比数列,且首项为 ${a}_{2} - {a}_{1} =  - \frac{1}{3}$ ,公比为 $\frac{2}{3}$ ,即 ${a}_{n + 1} - {a}_{n} =  - \frac{1}{3} \cdot  {\left( \frac{2}{3}\right) }^{n - 1}$ ,

再用累加法,即可得到 ${a}_{n} = 1 + {\left( \frac{2}{3}\right) }^{n - 1}$ 。

解法二: $3{a}_{n + 1} = 2{a}_{n} + 1 \Rightarrow  {a}_{n + 1} - 1 = \frac{2}{3}\left( {{a}_{n} - 1}\right)$ ,所以 $\left\{  {{a}_{n} - 1}\right\}$ 为等比数列且

${a}_{n} - 1 = {\left( \frac{2}{3}\right) }^{n - 1} \Rightarrow  {a}_{n} = 1 + {\left( \frac{2}{3}\right) }^{n - 1}$ ,

(2)已知数列 $\left\{  {a}_{n}\right\}$ 的首项 ${a}_{1} = 1$ ，前 $n$ 项和为 ${S}_{n}$ ，且 ${S}_{n + 1} = 2{S}_{n} + n + 1\left( {n \in  {N}^{ * }}\right)$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【难度】 $\star   \star   \star$

【答案】 ${a}_{n} = {2}^{n} - 1\left( {n \in  {N}^{ * }}\right)$ .

【解析】由已知, ${S}_{n + 1} = 2{S}_{n} + n + 1\left( {n \in  {N}^{ * }}\right)$ ,当 $n \geq  2$ 时, ${S}_{n} = 2{S}_{n - 1} + n$ ,

两式相减得, ${a}_{n + 1} = 2{a}_{n} + 1$ ,于是 ${a}_{n + 1} + 1 = 2\left( {{a}_{n} + 1}\right)$ ,

当 $n = 1$ 时， ${S}_{2} = 2{S}_{1} + 1 + 1$ ，即 ${a}_{1} + {a}_{2} = 2{a}_{1} + 1 + 1$ ，所以 ${a}_{2} = 3$ .

此时 ${a}_{2} + 1 = 2\left( {{a}_{1} + 1}\right)$ ，且 ${a}_{1} + 1 = 2 \neq  0$ ，

所以，数列 $\left\{  {{a}_{n} + 1}\right\}$ 是首项为 ${a}_{1} + 1 = 2$ ，公比为 2 的等比数列

所以, ${a}_{n} + 1 = 2 \cdot  {2}^{n - 1}$ ,即 ${a}_{n} = {2}^{n} - 1\left( {n \in  {N}^{ * }}\right)$ .

(3)已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 1,{a}_{n + 1} = m{a}_{n} + {3}^{n}\left( {m \neq  0}\right)$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【难度】 $\star   \star   \star   \star$

【答案】当 $m = 3$ 时, ${a}_{n} = n \cdot  {3}^{n - 1}$ ; 当 $m \neq  3$ 时, ${a}_{n} = \frac{{m}^{n} - {3}^{n}}{m - 3}$

【解析】当 $m = 3$ 时, $\because {a}_{n + 1} = 3{a}_{n} + {3}^{n},\therefore \frac{{a}_{n + 1}}{{3}^{n}} = \frac{{a}_{n}}{{3}^{n - 1}} + 1$ ,令 $\frac{{a}_{n}}{{3}^{n - 1}} = {b}_{n}$

$\therefore$ 数列 $\left\{  {b}_{n}\right\}$ 是等差数列, ${b}_{n} = 1 + 1\left( {n - 1}\right)  = n,\therefore {a}_{n} = n \cdot  {3}^{n - 1}$ .

当 $m \neq  3$ 时, ${a}_{n + 1} = m{a}_{n} + {3}^{n} \Rightarrow  \frac{{a}_{n + 1}}{{m}^{n}} = \frac{{a}_{n}}{{m}^{n - 1}} + {\left( \frac{3}{m}\right) }^{n}$ ,后面再用累加法即可得到 ${a}_{n} = \frac{{m}^{n} - {3}^{n}}{m - 3}$ 。

(或 ${a}_{n + 1} = m{a}_{n} + {3}^{n} \Rightarrow  \frac{{a}_{n + 1}}{{3}^{n}} = \frac{m}{3} \cdot  \frac{{a}_{n}}{{3}^{n - 1}} + 1$ ,后面再利用待定系数法构造等比数列可得 ${a}_{n} = \frac{{m}^{n} - {3}^{n}}{m - 3}$ 。

或 ${a}_{n + 1} = m{a}_{n} + {3}^{n} \Rightarrow  {a}_{n + 1} + A \cdot  {3}^{n + 1} = m\left( {{a}_{n} + A \cdot  {3}^{n}}\right)$ 待定系数法构造等比数列,后略)

【例 5】(1) 已知数列 $\left\{  {a}_{n}\right\}$ 满足: 对任意的 $n \in  {\mathrm{N}}^{ * }$ 均有 ${a}_{n + 1} = k{a}_{n} + {3k} - 3$ ，其中 $k$ 为不等于 0 与 1 的常数， 若 ${a}_{i} \in  \{  - {678}, - {78}, - 3,{22},{222},{2222}\} , i = 2,3,4,5$ ，则满足条件的 ${a}_{1}$ 所有可能值的和为___.

【难度】 $\star   \star   \star   \star$

【答案】 $- 3 - \frac{34}{3} + {2022} = \frac{6023}{3}$

【解析】 ${a}_{i} + 3 \in  \{  - {653}, - {75},0,{25},{225},{2225}\}$

(2)已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 2,{a}_{n + 1} = 3{a}_{n} + {3}^{n + 1} - {2}^{n}\left( {n \in  {N}^{ * }}\right)$ . 设 ${b}_{n} = \frac{{a}_{n} - {2}^{n}}{{3}^{n}}$ ，证明:数列 $\left\{  {b}_{n}\right\}$ 为等差数列,并求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【难度】 $\star   \star   \star   \star$

【答案】 ${a}_{n} = \left( {n - 1}\right) {3}^{n} + {2}^{n}$

【解析】 ${b}_{n + 1} - {b}_{n} = 1$ ,所以数列 $\left\{  {b}_{n}\right\}$ 为等差数列, ${a}_{n} = \left( {n - 1}\right) {3}^{n} + {2}^{n}$ .

【例6】已知 ${a}_{1} = 4,{a}_{n + 1} = \frac{2 \cdot  {a}_{n}}{2{a}_{n} + 1}$ ,求 ${a}_{n}$ .

【难度】 $\star   \star   \star   \star$

【解析】两边取倒数得: $\frac{1}{{a}_{n + 1}} - \frac{1}{2{a}_{n}} = 1$ ,设 $\frac{1}{{a}_{n}} = {b}_{n}$ ,则 ${b}_{n + 1} - \frac{1}{2}{b}_{n} = 1$ ;

令 ${b}_{n + 1} + t = \frac{1}{2}\left( {{b}_{n} + t}\right)$ ; 展开后得, $t =  - 2;\therefore \frac{{b}_{n + 1} - 2}{{b}_{n} - 2} = \frac{1}{2}$ ;

$\therefore \left\{  {{b}_{n} - 2}\right\}$ 是以 ${b}_{1} - 2 = \frac{1}{{a}_{1}} - 2 =  - \frac{7}{4}$ 为首项, $\frac{1}{2}$ 为公比的等比数列.

$\therefore {b}_{n} - 2 = \left( {-\frac{7}{4}}\right) {\left( \frac{1}{2}\right) }^{n - 1}$ ; 即 $\frac{1}{{a}_{n}} - 2 = \left( {-\frac{7}{4}}\right) {\left( \frac{1}{2}\right) }^{n - 1}$ ,得 ${a}_{n} = \frac{{2}^{n + 1}}{{2}^{n + 2} - 7}$ .

【例 7】设正项数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,\sqrt{{a}_{n}} = 2{a}_{n - 1}\left( {n \geq  2}\right)$ ,求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【难度】 $\star   \star   \star   \star$

【答案】 ${a}_{n} = {2}^{{2}^{n - 1} - 1}$

【解析】 ${a}_{n} = 2{a}_{n - 1}^{2}$ 两边同时取以 2 为底的对数,可得到 ${\log }_{2}{a}_{n} = 2{\log }_{2}{a}_{n - 1} + 1$ ,转化为 “ ${a}_{n + 1} = p{a}_{n} + q$ ”类型 (解法略).

【例8】(1)数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 0,{a}_{n + 1} + {a}_{n} = {2n}$ ,求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【难度】 $\star   \star   \star$

【答案】 ${a}_{n} = \left\{  \begin{array}{l} n - 1, n\text{ 为奇数, } \\  n, n\text{ 为偶数. } \end{array}\right.$

【解析】方法一: 令 ${b}_{n} = {\left( -1\right) }^{n}{a}_{n}$

则 ${b}_{n + 1} - {b}_{n} = {\left( -1\right) }^{n + 1}{a}_{n + 1} - {\left( -1\right) }^{n}{a}_{n} = {\left( -1\right) }^{n + 1}\left( {{a}_{n + 1} + {a}_{n}}\right)  = {\left( -1\right) }^{n + 1} \cdot  {2n}$ .

$n \geq  2$ 时, $\left\{  \begin{array}{l} {b}_{n} - {b}_{n - 1} = {\left( -1\right) }^{n} \cdot  2\left( {n - 1}\right) \\  {b}_{n - 1} - {b}_{n - 2} = {\left( -1\right) }^{n - 1} \cdot  2\left( {n - 2}\right) \\  \cdots \cdots \\  {b}_{2} - {b}_{1} = {\left( -1\right) }^{2} \cdot  2 \times  1 \\  {b}_{1} =  - {a}_{1} = 0 \end{array}\right.$

各式相加: ${b}_{n} = 2\left\lbrack  {{\left( -1\right) }^{n}\left( {n - 1}\right)  + {\left( -1\right) }^{n - 1}\left( {n - 2}\right)  + \cdots  + {\left( -1\right) }^{3} \cdot  2 + {\left( -1\right) }^{2} \cdot  1}\right\rbrack$

当 $n$ 为偶数时, ${b}_{n} = 2\left\lbrack  {\left( {n - 1}\right)  + \left( {-1}\right)  \cdot  \frac{n - 2}{2}}\right\rbrack   = n$ . 此时 ${a}_{n} = {b}_{n} = n$

当 $\mathrm{n}$ 为奇数时, ${b}_{n} = 2\left( {-\frac{n - 1}{2}}\right)  =  - n + 1$ 此时 ${b}_{n} =  - {a}_{n}$ ,所以 ${a}_{n} = n - 1$ .

故 ${a}_{n} = \left\{  \begin{array}{l} n - 1, n\text{ 为奇数, } \\  n, n\text{ 为偶数. } \end{array}\right.$

方法二: $\because {a}_{n + 1} + {a}_{n} = {2n}$

$\therefore n \geq  2$ 时, ${a}_{n} + {a}_{n - 1} = 2\left( {n - 1}\right)$ ,

两式相减得: ${a}_{n + 1} - {a}_{n - 1} = 2$ .

$\therefore {a}_{1},{a}_{3},{a}_{5},\cdots$ ,构成以 ${a}_{1}$ 为首项,以 2 为公差的等差数列;

${a}_{2},{a}_{4},{a}_{6},\cdots$ ,构成以 ${a}_{2}$ 为首项,以 2 为公差的等差数列

$\therefore {a}_{{2k} - 1} = {a}_{1} + \left( {k - 1}\right) d = {2k} - 2$

${a}_{2k} = {a}_{2} + \left( {k - 1}\right) d = {2k}.$

$\therefore {a}_{n} = \left\{  \begin{array}{l} n - 1, n\text{ 为奇数, } \\  n, n\text{ 为偶数. } \end{array}\right.$

(2)已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 3,{a}_{n} \cdot  {a}_{n + 1} = {\left( \frac{1}{2}\right) }^{n},\left( {n \in  {N}^{ * }}\right)$ ，求此数列的通项公式.

【难度】 $\star   \star   \star$

【答案】 ${a}_{n} = \left\{  \begin{array}{l} 3 \cdot  {\left( \frac{1}{2}\right) }^{\frac{n - 1}{2}}, n\text{ 为奇数 } \\  6 \cdot  {\left( \frac{1}{2}\right) }^{\frac{n}{2} - 1}, n\text{ 为偶数 } \end{array}\right.$

【解析】 ${a}_{n} \cdot  {a}_{n + 1} = {\left( \frac{1}{2}\right) }^{n},{a}_{n - 1} \cdot  {a}_{n} = {\left( \frac{1}{2}\right) }^{n - 1}$ ,两式相除可得 $\frac{{a}_{n + 1}}{{a}_{n - 1}} = \frac{1}{2}$ ,所以数列 $\left\{  {a}_{n}\right\}$ 是分奇数项和偶数项都成等比数列,且 ${a}_{1} = 3,{a}_{2} = \frac{1}{6}$ ,公比都是 $\frac{1}{2}$ ,即 ${a}_{n} = \left\{  \begin{array}{l} 3 \cdot  {\left( \frac{1}{2}\right) }^{\frac{n - 1}{2}}, n\text{ 为奇数 } \\  6 \cdot  {\left( \frac{1}{2}\right) }^{\frac{n}{2} - 1}, n\text{ 为偶数 } \end{array}\right.$ .

【例9】(1)数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{n + 1} = \left\{  \begin{array}{l} 2{a}_{n},\;0 \leq  {a}_{n} \leq  \frac{1}{2} \\  2{a}_{n} - 1,\frac{1}{2} < {a}_{n} < 1 \end{array}\right.$ ， ${a}_{1} = \frac{3}{5}$ ，则数列的第2021项为___.

【难度】 $\star   \star   \star$

【答案】 $\frac{3}{5}$

【解析】由已知可得, ${a}_{2} = 2 \times  \frac{3}{5} - 1 = \frac{1}{5},{a}_{3} = 2 \times  \frac{1}{5} - \frac{2}{5},{a}_{4} = 2 \times  \frac{2}{5} = \frac{4}{5},{a}_{5} = 2 \times  \frac{4}{5} - 1 = \frac{3}{5}$ ,

$\therefore \left\{  {a}_{n}\right\}$ 为周期数列且 $T = 4,\therefore {a}_{2021} = {a}_{1} = \frac{3}{5}$ .

(2)若数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 2,{a}_{n + 1} = \frac{{a}_{n} + 1}{1 - {a}_{n}},{a}_{2020} =$ ___.

【难度】 $\star   \star   \star$

【答案】 $\frac{1}{3}$

【解析】 $\because$ 数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 2,{a}_{n + 1} = \frac{{a}_{n} + 1}{1 - {a}_{n}}$ ,

$\therefore {a}_{2} = \frac{{a}_{1} + 1}{1 - {a}_{1}} =  - 3$ ,同理可得: ${a}_{3} = \frac{-3 + 1}{1 - \left( {-3}\right) } =  - \frac{1}{2},{a}_{4} = \frac{-\frac{1}{2} + 1}{1 - \left( {-\frac{1}{2}}\right) } = \frac{1}{3},{a}_{5} = \frac{\frac{1}{3} + 1}{1 - \frac{1}{3}} = 2,\ldots$

$\therefore$ 数列 $\left\{  {a}_{n}\right\}$ 是周期为 4 的数列,

又 ${2020} = {505} \times  4,\therefore {a}_{2020} = {a}_{4} = \frac{1}{3}$ ,

故答案为: $\frac{1}{3}$ .

【例10】已知数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n}$ 满足: ${S}_{n} = \frac{{a}_{n}}{2} + \frac{1}{{a}_{n}} - 1$ ,且 ${a}_{n} > 0, n \in  {N}^{ * }$ .

(1)求 ${a}_{1},{a}_{2},{a}_{3}$ ；

(2)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【难度】 $\star   \star   \star   \star$

【答案】(1) ${a}_{1} = \sqrt{3} - 1;{a}_{2} = \sqrt{5} - \sqrt{3};{a}_{3} = \sqrt{7} - \sqrt{5}$ ;

(2)猜想 ${a}_{n} = \sqrt{{2n} + 1} - \sqrt{{2n} - 1}\left( {n \in  {N}^{ * }}\right)$ ，证明见解析。

【解析】(1) 当 $n = 1$ 时,由已知得 ${a}_{1} = \frac{{a}_{1}}{2} + \frac{1}{{a}_{1}} - 1$ ,即 ${a}_{1}^{2} + 2{a}_{1} - 2 = 0\therefore {a}_{1} = \sqrt{3} - 1\left( {{a}_{1} > 0}\right)$

当 $n = 2$ 时,由已知得 ${a}_{1} + {a}_{2} = \frac{{a}_{2}}{2} + \frac{1}{{a}_{2}} - 1$ ,

将 ${a}_{1} = \sqrt{3} - 1$ 代入并整理得 ${a}_{2}{}^{2} + 2\sqrt{3}{a}_{2} - 2 = 0;\therefore {a}_{2} = \sqrt{5} - \sqrt{3}\left( {{a}_{2} > 0}\right)$ .

同理可得 ${a}_{3} = \sqrt{7} - \sqrt{5}$ .

(2)猜想 ${a}_{n} = \sqrt{{2n} + 1} - \sqrt{{2n} - 1}\left( {n \in  {N}^{ * }}\right)$ .

证明: ①由 (1) 知，当 $n = 1,2,3$ 时，通项公式成立.

②假设当 $n = k\left( {k \geq  3, k \in  {N}^{ * }}\right)$ 时，通项公式成立，

即 ${a}_{k} = \sqrt{{2k} + 1} - \sqrt{{2k} - 1}$ .

由于 ${a}_{k + 1} = {S}_{k + 1} - {S}_{k} = \frac{{a}_{k} + 1}{2} + \frac{1}{{a}_{k + 1}} - \frac{{a}_{k}}{2} - \frac{1}{{a}_{k}}$ ,

将 ${a}_{k} = \sqrt{{2k} + 1} - \sqrt{{2k} - 1}$ 代入上式,整理得

${a}_{k + 1}^{2} + 2\sqrt{{2k} + 1}{a}_{k + 1} - 2 = 0,$

$\therefore {a}_{k + 1} = \sqrt{{2k} + 3} - \sqrt{{2k} + 1}$ ,

即 $n = k + 1$ 时通项公式成立.

根据①②可知，对所有 $n \in  {N}^{ * }$ ， ${a}_{n} = \sqrt{{2n} + 1} - \sqrt{{2n} - 1}$ 成立.

【例11】(1)已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,{a}_{2} = 4$ ,且 $2{a}_{n} = \frac{n - 1}{n}{a}_{n - 1} + \frac{n + 1}{n}{a}_{n + 1}\left( {n \geq  2, n \in  N}\right)$ ,则 $\frac{{a}_{n}}{n}$ 的最大值为( )

A. $\frac{49}{24}$ B. 1 C. 2

D. $\frac{5}{3}$

【难度】

【答案】C

【解析】因为 $2{a}_{n} = \frac{n - 1}{n}{a}_{n - 1} + \frac{n + 1}{n}{a}_{n + 1}\left( {n \geq  2, n \in  N}\right)$ ,所以

${2n}{a}_{n} = \left( {n - 1}\right) {a}_{n - 1} + \left( {n + 1}\right) {a}_{n + 1},\left( {n \geq  2, n \in  N}\right)$

所以数列 $\left\{  {n{a}_{n}}\right\}$ 是等差数列,

又 ${a}_{1} = 1,{a}_{2} = 4$ ,所以数列 $\left\{  {n{a}_{n}}\right\}$ 是以 1 为首项, $\frac{2{a}_{2} - {a}_{1}}{2 - 1} = 7$ 为公差的等差数列,所以 $n{a}_{n} = {7n} - 6$ , 所以 $\frac{{a}_{n}}{n} = \frac{{7n} - 6}{{n}^{2}} = \frac{7}{n} - \frac{6}{{n}^{2}} =  - 6{\left( \frac{1}{n} - \frac{7}{12}\right) }^{2} + \frac{49}{24}, n \in  {N}^{ * }$ ,

所以当 $n = 2$ 时, $\frac{{a}_{n}}{n}$ 取最大值,最大值为 $\frac{7}{2} - \frac{6}{4} = 2$ .

故选: C.

(2)已知数列 $\left\{  {a}_{n}\right\}$ 是其有 $k$ 个项的有限数列,且满足 ${a}_{n + 1} = {a}_{n - 1} - \frac{n}{{a}_{n}}\left( {n = 2,\cdots , k - 1}\right)$ ,若 ${a}_{1} = {24},{a}_{2} = {51},{a}_{k} = 0$ ，则 $k =$ ___

【难度】 $\star   \star   \star   \star$

【答案】 50

【解析】两边同时乘 ${a}_{n}$ 得: ${a}_{n + 1}{a}_{n} - {a}_{n}{a}_{n - 1} =  - n,\therefore {a}_{3}{a}_{2} - {a}_{2}{a}_{1} =  - 2,{a}_{4}{a}_{3} - {a}_{3}{a}_{2} =  - 3$ ,

……, ${a}_{k}{a}_{k - 1} - {a}_{k - 1}{a}_{k - 2} =  - \left( {k - 1}\right)$ ,累加得, ${a}_{k}{a}_{k - 1} - {a}_{2}{a}_{1} =  - \frac{\left( {k + 1}\right) \left( {k - 2}\right) }{2},\because {a}_{k} = 0$ ,

$\therefore {24} \times  {51} \times  2 = \left( {k + 1}\right) \left( {k - 2}\right) ,\because k > 0$ ,解得 $k = {50}$

(3)已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,{a}_{2} = 3,{a}_{n + 2} = 3{a}_{n + 1} - 2{a}_{n}\left( {n \in  {N}^{ * }}\right)$ .

(I) 证明: 数列 $\left\{  {{a}_{n + 1} - {a}_{n}}\right\}$ 是等比数列;

(II)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(III)若数列 $\left\{  {b}_{n}\right\}$ 满足 ${4}^{{b}_{1} - 1}{4}^{{b}_{2} - 1}\ldots {4}^{{b}_{n} - 1} = {\left( {a}_{n} + 1\right) }^{{b}_{n}}\left( {n \in  {N}^{ * }}\right)$ ，证明 $\left\{  {b}_{n}\right\}$ 是等差数列.

【难度】★★★★

【答案】见解析

【解析】(I) 证明: $\because {a}_{n + 2} = 3{a}_{n + 1} - 2{a}_{n}$ ,

$\therefore {a}_{n + 2} - {a}_{n + 1} = 2\left( {{a}_{n + 1} - {a}_{n}}\right)$ ,

$\because {a}_{1} = 1,{a}_{2} = 3$ ,

$\therefore \frac{{a}_{n + 2} - {a}_{n + 1}}{{a}_{n + 1} - {a}_{n}} = 2\left( {n \in  {N}^{ * }}\right)$ .

$\therefore \left\{  {{a}_{n + 1} - {a}_{n}}\right\}$ 是以 ${a}_{2} - {a}_{1} = 2$ 为首项,2 为公比的等比数列.

(II) 解: 由 (I) 得 ${a}_{n + 1} - {a}_{n} = {2}^{n}\left( {n \in  {N}^{ * }}\right)$ ,

$\therefore {a}_{n} = \left( {{a}_{n} - {a}_{n - 1}}\right)  + \left( {{a}_{n - 1} - {a}_{n - 2}}\right)  + \ldots  + \left( {{a}_{2} - {a}_{1}}\right)  + {a}_{1} \; = {2}^{n - 1} + {2}^{n - 2} + \ldots  + 2 + 1 \; = {2}^{n} - 1\left( {n \in  {N}^{ * }}\right)$ .

(III) 证明: $\because {4}^{{b}_{1} - 1}{4}^{{b}_{2} - 1}\ldots {4}^{{b}_{n} - 1} = {\left( {a}_{n} + 1\right) }^{{b}_{n}}$ ,

$\therefore {4}^{\left( {b}_{1} + {b}_{2} + \ldots  + {b}_{n}\right) } = {2}^{n{b}_{n}}$ ,

$\therefore 2\left\lbrack  {\left( {{b}_{1} + {b}_{2} + \ldots  + {b}_{n}}\right)  - n}\right\rbrack   = n{b}_{n}$ ,①

$2\left\lbrack  {\left( {{b}_{1} + {b}_{2} + \ldots  + {b}_{n} + {b}_{n + 1}}\right)  - \left( {n + 1}\right) }\right\rbrack   = \left( {n + 1}\right) {b}_{n + 1}$ .②

②-①，得 $2\left( {{b}_{n + 1} - 1}\right)  = \left( {n + 1}\right) {b}_{n + 1} - n{b}_{n}$ ，

即 $\left( {n - 1}\right) {b}_{n + 1} - n{b}_{n} + 2 = 0$ .③

$$
n{b}_{n + 2} - \left( {n + 1}\right) {b}_{n + 1} + 2 = 0.
$$

④

④-③，得 $n{b}_{n + 2} - {2n}{b}_{n + 1} + n{b}_{n} = 0$ ，

即 ${b}_{n + 2} - 2{b}_{n + 1} + {b}_{n} = 0$ ,

$\therefore {b}_{n + 2} - {b}_{n + 1} = {b}_{n + 1} - {b}_{n}\left( {n \in  {N}^{ * }}\right)$ ,

$\therefore \left\{  {b}_{n}\right\}$ 是等差数列,

【例12】已知数列 $\left\{  {a}_{n}\right\}  ,\left\{  {b}_{n}\right\}$ 满足 ${a}_{1} = 2,{b}_{1} = 1$ ,且 $\left\{  {\begin{array}{l} {a}_{n} = \frac{3}{4}{a}_{n - 1} + \frac{1}{4}{b}_{n - 1} + 1, \\  {b}_{n} = \frac{1}{4}{a}_{n - 1} + \frac{3}{4}{b}_{n - 1} + 1, \end{array}\left( {n \geq  2}\right) }\right.$ .

(1)令 ${c}_{n} = {a}_{n} + {b}_{n}$ ，求数列 $\left\{  {c}_{n}\right\}$ 的通项公式；

(2)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式.

【难度】 $\star   \star   \star   \star$

【答案】( 1 ) ${c}_{n} = {2n} + 1$ ( 2 ) ${a}_{n} = \frac{1}{{2}^{n}} + n + \frac{1}{2}$

【解析】解: (1) 由题可知, $\left\{  {\begin{array}{l} {a}_{n} = \frac{3}{4}{a}_{n - 1} + \frac{1}{4}{b}_{n - 1} + 1, \\  {b}_{n} = \frac{1}{4}{a}_{n - 1} + \frac{3}{4}{b}_{n - 1} + 1, \end{array}\left( {n \geq  2}\right) ,{c}_{n} = {a}_{n} + {b}_{n}}\right.$ ,

则 ${a}_{n} + {b}_{n} = \left( {{a}_{n - 1} + {b}_{n - 1}}\right)  + 2\left( {n \geq  2}\right)$ ,

即 ${c}_{n} = {c}_{n - 1} + 2\left( {n \geq  2}\right)$ ,得: ${c}_{n} - {c}_{n - 1} = 2\left( {n \geq  2}\right)$ ,易知 $\left\{  {c}_{n}\right\}$ 是首项为 ${a}_{1} + {b}_{1} = 3$ ,公差为 2 的等差数列,

则通项公式为: ${c}_{n} = {2n} + 1$ .

(2)由题可得: ${a}_{n} - {b}_{n} = \frac{1}{2}\left( {{a}_{n - 1} - {b}_{n - 1}}\right) \left( {n \geq  2}\right)$ ，

令 ${d}_{n} = {a}_{n} - {b}_{n}$ ,则 ${d}_{n} = \frac{1}{2}{d}_{n - 1}\left( {n \geq  2}\right)$ ,易知 $\left\{  {d}_{n}\right\}$ 是首项为 ${a}_{1} - {b}_{1} = 1$ ，公比为 $\frac{1}{2}$ 的等比数列，

则通项公式为: ${d}_{n} = \frac{1}{{2}^{n - 1}}$ ,

由 $\left\{  \begin{array}{l} {a}_{n} + {b}_{n} = {2n} + 1, \\  {a}_{n} - {b}_{n} = \frac{1}{{2}^{n - 1}}, \end{array}\right.$ ,解得: ${a}_{n} = \frac{1}{{2}^{n}} + n + \frac{1}{2}$ .

【例 13】设 ${a}_{1} = 2,{a}_{n + 1} = \frac{2}{{a}_{n} + 1},{b}_{n} = \left| \frac{{a}_{n} + 2}{{a}_{n} - 1}\right| , n \in  {N}^{ * }$ ，则数列 $\left\{  {b}_{n}\right\}$ 的通项公式 ${b}_{n} =$ ___.

【难度】 $\star   \star   \star   \star$

【答案】 ${2}^{n + 1}$

【解析】 $\because {a}_{k + 1} = \frac{2}{{a}_{k} + 1},\;{b}_{k} = \left| \frac{{a}_{k} + 2}{{a}_{k} - 1}\right|$ ,

$\therefore {b}_{k + 1} = \left| \frac{{a}_{k + 1} + 2}{{a}_{k + 1} - 1}\right|  = \left| \frac{\frac{2}{{a}_{k} + 1} + 2}{\frac{2}{{a}_{k} + 1} - 1}\right|  = \left| \frac{2\left( {{a}_{k} + 2}\right) }{{a}_{k} - 1}\right|  = 2{b}_{k} = {2}^{k + 2}$ ,

故答案为: ${2}^{n + 1}, n \in  {N}^{ * }$ .

*【例 14】(1)数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = \frac{1}{2},{a}_{n + 1} = \frac{{a}_{n} + 3}{2{a}_{n} - 4}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ ，求通项公式 ${a}_{n}$ .

【难度】 $\star   \star   \star   \star   \star$

【答案】 ${a}_{n} = \frac{-{5}^{n} + {\left( -1\right) }^{n - 1} \cdot  3 \cdot  {2}^{n + 1}}{2 \cdot  {5}^{n} + {\left( -1\right) }^{n - 1} \cdot  {2}^{n + 1}}$

【解析】作函数 $f\left( x\right)  = \frac{x + 3}{{2x} - 4}$ ,解方程 $f\left( x\right)  = x$ ,即 $\frac{x + 3}{{2x} - 4} = x$ 得 ${x}_{1} =  - \frac{1}{2},{x}_{2} = 3$ .

由于 ${a}_{n + 1} - \left( {-\frac{1}{2}}\right)  = \frac{{a}_{n} + 3}{2{a}_{n} - 4} + \frac{1}{2} = \frac{2\left( {{a}_{n} + \frac{1}{2}}\right) }{2{a}_{n} - 4}$ ,①

${a}_{n + 1} - 3 = \frac{{a}_{n} + 3}{2{a}_{n} - 4} - 3 = \frac{-5\left( {{a}_{n} - 3}\right) }{2{a}_{n} - 4}$ ,②

且 ${a}_{n} \neq  3$ (否则由式②得到 ${a}_{1} = 3$ ，矛盾).

$\therefore$ ①、②两式相除，得 $\frac{{a}_{n + 1} + \frac{1}{2}}{2{a}_{n + 1} - 3} =  - \frac{2}{5} \cdot  \frac{{a}_{n} + \frac{1}{2}}{{a}_{n} - 3}$ .

结合初始条件及等比数列的通项公式,可知 $\frac{{a}_{n} + \frac{1}{2}}{{a}_{n} - 3} = {\left( -\frac{2}{3}\right) }^{n}$ .

$\therefore {a}_{n} = \frac{-{5}^{n} + {\left( -1\right) }^{n - 1} \cdot  3 \cdot  {2}^{n + 1}}{2 \cdot  {5}^{n} + {\left( -1\right) }^{n - 1} \cdot  {2}^{n + 1}}$ .

(2)数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 5,{a}_{n + 1} = \frac{{a}_{n} - 4}{{a}_{n} - 3}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ ，求通项公式 ${a}_{n}$ .

【难度】 $\star   \star   \star   \star$

【答案】 ${a}_{n} = \frac{{6n} - {11}}{{3n} - 4}$

【解析】方法一: 作函数 $f\left( x\right)  = \frac{x - 4}{x - 3}$ ,解方程 $f\left( x\right)  = x$ ,即 $\frac{x - 4}{x - 3} = x$ 得 ${x}_{1} = {x}_{2} = 2$ .

由于 ${a}_{n + 1} - 2 = \frac{{a}_{n} - 4}{{a}_{n} - 3} - 2 = \frac{-{a}_{n} + 4}{{a}_{n} - 3}$ ,①

且 ${a}_{n} \neq  2$ (否则由式②得到 ${a}_{1} = 2$ ，矛盾).

$\therefore$ 两边取倒数,得 $\frac{1}{{a}_{n + 1} - 2} = \frac{{a}_{n} - 3}{-{a}_{n} + 2} = \frac{1}{{a}_{n} - 2} - 1$ .

$\therefore$ 数列 $\left\{  \frac{1}{{a}_{n} - 2}\right\}$ 为等差数列 $\frac{1}{{a}_{n} - 2} = \frac{4 - {3n}}{3}$ ,从而 ${a}_{n} = \frac{{6n} - {11}}{{3n} - 4}$ .

方法二: ${a}_{n + 1} + m = \frac{n\left( {{a}_{n} + m}\right) }{{a}_{n} - 3} \Rightarrow  \left\{  {\begin{array}{l} m =  - 2 \\  n =  - 1 \end{array} \Rightarrow  {a}_{n + 1} - 2 =  - \frac{\left( {a}_{n} - 2\right) }{{a}_{n} - 3}}\right.$

$\therefore$ 两边取倒数,得 $\frac{1}{{a}_{n + 1} - 2} = \frac{{a}_{n} - 3}{-{a}_{n} + 2} = \frac{1}{{a}_{n} - 2} - 1$ .

$\therefore$ 数列 $\left\{  \frac{1}{{a}_{n} - 2}\right\}$ 为等差数列 $\frac{1}{{a}_{n} - 2} = \frac{4 - {3n}}{3}$ ,从而 ${a}_{n} = \frac{{6n} - {11}}{{3n} - 4}$ .

## 巩固训练

1、已知正项数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,\left( {n + 2}\right) {a}_{n + 1}^{2} - \left( {n + 1}\right) {a}_{n}^{2} + {a}_{n}{a}_{n + 1} = 0$ ，则它的通项公式为( )

A. ${a}_{n} = \frac{1}{n + 1}$ B. ${a}_{n} = \frac{2}{n + 1}$ C. ${a}_{n} = \frac{n + 1}{2}$ D. ${a}_{n} = n$

【难度】 $\star   \star   \star   \star$

【答案】B

【解析】

由 $\left( {n + 2}\right) {a}_{n + 1}^{2} - \left( {n + 1}\right) {a}_{n}^{2} + {a}_{n}{a}_{n + 1} = 0$ ,得 $\left\lbrack  {\left( {n + 2}\right) {a}_{n + 1} - \left( {n + 1}\right) {a}_{n}}\right\rbrack   \cdot  \left( {{a}_{n + 1} + {a}_{n}}\right)  = 0$ ,

又 ${a}_{n} > 0$ ，所以 $\left( {n + 2}\right) {a}_{n + 1} = \left( {n + 1}\right) {a}_{n}$ ，即数列 $\left\{  {\left( {n + 1}\right) {a}_{n}}\right\}$ 为常数列，

因为 ${a}_{1} = 1$ ,所以 $\left( {n + 1}\right) {a}_{n} = 2$ ,于是所求通项公式为 ${a}_{n} = \frac{2}{n + 1}$ .

故选: B

2、设正数数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，数列 $\left\{  {S}_{n}\right\}$ 的前 $n$ 项之积为 ${T}_{n}$ ，且 ${S}_{n} + {T}_{n} = 1$ ，则数列 $\left\{  {a}_{n}\right\}$ 的通项公式是___.

【难度】 $\bigstar \bigstar \bigstar$

【答案】 ${a}_{n} = \frac{1}{n\left( {n + 1}\right) }$

【解析】 ${T}_{1} = {S}_{1} = {a}_{1},\therefore 2{a}_{1} = 1,{a}_{1} = \frac{1}{2}$ ,即 ${S}_{1} = {T}_{1} = \frac{1}{2}$ ,

${S}_{n} = \frac{{T}_{n}}{{T}_{n - 1}}\left( {n \geq  2}\right) ,\therefore \frac{{T}_{n}}{{T}_{n - 1}} + {T}_{n} = 1,\therefore \frac{1}{{T}_{n}} - \frac{1}{{T}_{n - 1}} = 1$ ,即 $\left\{  {T}_{n}\right\}$ 是以 2 为首项,1 为公差的等差数列,故 $\frac{1}{{T}_{n}} = 2 + n - 1 = n + 1,{T}_{n} = \frac{1}{n + 1},{S}_{n} = \frac{n}{n + 1},{S}_{1} = \frac{1}{2}$ 也符合此式, ${S}_{n} = \frac{n}{n + 1},\therefore$ 当 $n \geq  2$ 时,

${a}_{n} = {S}_{n} - {S}_{n - 1} = \frac{n}{n + 1} - \frac{n - 1}{n} = \frac{1}{n\left( {n + 1}\right) }$ ,又 ${a}_{1} = \frac{1}{2},\therefore {a}_{n} = \frac{1}{n\left( {n + 1}\right) }$ ,

故答案为: ${a}_{n} = \frac{1}{n\left( {n + 1}\right) }$ .

3、已知各项都是正数的数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = \frac{3}{2},{a}_{n + 1} = \frac{1}{2}{a}_{n}\left( {4 - {a}_{n}}\right)$ ,求通项公式 ${a}_{n}$ .

【难度】

【答案】 ${a}_{n} = 2 - {2}^{1 - {2}^{n}}$

【解析】由已知得 ${a}_{n + 1} =  - \frac{1}{2}{\left( {a}_{n} - 2\right) }^{2} + 2$ ,令 $2 - {a}_{n} = {b}_{n}$ ,则有 ${b}_{1} = \frac{1}{2},{b}_{n + 1} = \frac{1}{2}{b}_{n}^{2}$ .

$\because {a}_{n} > 0,\therefore 0 < {a}_{n + 1} < 2$ ,又 $0 < {a}_{1} < 2,\therefore 0 < {a}_{n} < 2$ ,从而 ${b}_{n} > 0$ .

取对数得 $\lg {b}_{n + 1} = 2\lg {b}_{n} - \lg 2$ ,即 $\lg {b}_{n + 1} - \lg 2 = 2\left( {\lg {b}_{n} - \lg 2}\right)$ .

$\therefore \left\{  {\lg {b}_{n} - \lg 2}\right\}$ 是首项为 $- 2\lg 2$ ,公比为 2 的等比数列,

$\therefore \lg {b}_{n} - \lg 2 =  - {2}^{n}\lg 2,\therefore {b}_{n} = {2}^{1 - {2}^{n}},\therefore {a}_{n} = 2 - {2}^{1 - {2}^{n}}$ .

![14_524_206_202_192_0.jpg](images/14_524_206_202_192_0.jpg)

![14_858_190_225_220_0.jpg](images/14_858_190_225_220_0.jpg)

t=0 t=1 t=2 t=3

【难度】★★★★

【答案】 ${61}\;{2}^{n + 2} - 3$

【解析】解: 根据图分析可知,

$t = 0$ ,病毒的个数是 1 个;

$t = 1$ ,病毒的个数是 5 个;

$t = 2$ ,病毒的个数是 13 个;

$t = 3$ ,病毒的个数是 29 个;

可推出 $t = 4$ ,病毒的个数是 ${29} + \left( {{29} - {13}}\right)  \times  2 = {61}$ 个;

可得 $5 - 1 = 4 = {2}^{2},{13} - 5 = 8 = {2}^{3},{29} - {13} = {16} = {2}^{4},\cdots \cdots$ ,可得 ${a}_{n + 1} - {a}_{n} = {2}^{n + 1}$

所以 $n\left( {n \geq  2}\right)$ 小时后病毒的个数: ${a}_{n} = {a}_{1} + \left( {{a}_{2} - {a}_{1}}\right)  + \left( {{a}_{3} - {a}_{2}}\right)  + \cdots  + \left( {{a}_{n} - {a}_{n - 1}}\right)$

$= 1 + {2}^{2} + {2}^{3} + \cdots  + {2}^{n} = 1 + \frac{4\left( {1 - {2}^{-1}}\right) }{1 - 2} = {2}^{n + 2} - 3$

故答案为: ${61};{2}^{n + 2} - 3$

5、已知数列 $\left\{  {a}_{n}\right\}$ 的前 $\mathrm{n}$ 项和 $\mathrm{{Sn}}$ 满足:当 $\mathrm{n} \in  \mathrm{N} *$ 时， $\mathrm{{Sn}} \neq  0$ ；当 $\mathrm{n} > 1$ 时， ${a}_{n} + 2{S}_{n}{S}_{n - 1} = 0$ ，且 ${a}_{1} = 1$ . 求数列 $\left\{  {a}_{n}\right\}$ 的通项公式。

【难度】 $\star   \star   \star   \star$

【答案】 ${a}_{n} = \left\{  \begin{matrix} 1, n = 1 \\  \frac{-2}{\left( {{2n} - 1}\right) \left( {{2n} - 3}\right) }, n \geq  2 \end{matrix}\right.$

【解析】当 $\mathrm{n} > 1$ 时, ${a}_{n} + 2{S}_{n}{S}_{n - 1} = 0$ ,则: ${S}_{n} - {S}_{n - 1} + 2{S}_{n - 1}{S}_{n} = 0$ ,整理得 $\frac{1}{{S}_{n}} - \frac{1}{{S}_{n - 1}} = 2$ (常数). 所以数列 $\left\{  \frac{1}{{S}_{n}}\right\}$ 是等差数列,且 $\frac{1}{{S}_{1}} = 1$ ,公差为 2 . 所以 $\frac{1}{{S}_{n}} = 1 + 2\left( {n - 1}\right)  = {2n} - 1$ ,整理得 ${S}_{n} = \frac{1}{{2n} - 1}$ ,所以当 $n \geq  2$ 时, ${a}_{n} = {S}_{n} - {S}_{n - 1} = \frac{1}{{2n} - 1} - \frac{1}{{2n} - 3} = \frac{-2}{\left( {{2n} - 1}\right) \left( {{2n} - 3}\right) }$ ; 当 $n = 1$ 时, ${a}_{1} = 1$ 不满足此式子. 所以 ${a}_{n} = \left\{  {\begin{matrix} 1, n = 1 \\  \frac{-2}{\left( {{2n} - 1}\right) \left( {{2n} - 3}\right) } \end{matrix}, n \geq  2}\right.$

6、陈先生买了一套总价为 80 万元住房，首付 30 万元，其余50 万元向银行申请贷款，贷款月利率 0.5%，从贷款后的第一个月后开始还款，每月还款数额相等，30年还清. 问程先生每月应还款多少元(精确到0.01 元).

(注: 如果上个月欠银行贷款 $a$ 元,则一个月后,程先生应还给银行固定数额 $x$ 元,此时贷款 $a\left( {1 + {0.5}\% }\right)  - x$ 元)

【难度】

【答案】见解析

【解析】解: 设陈先生在第 $n$ 个月时还欠银行贷款 ${a}_{n}$ 万元,每月固定还款 $x$ 万元,则

${a}_{n} = {a}_{n - 1}\left( {1 + {0.5}\% }\right)  - x,\;{a}_{0} = {50},\;{a}_{n} + k = {1.005}\left( {{a}_{n - 1} + k}\right) ,\;{a}_{n} = {1.005}{a}_{n - 1} + {0.005k}$

所以 $k =  - {200x},\left\{  {{a}_{n} - {200x}}\right\}$ 是公比为 1.005 的等比数列

即 ${a}_{n} - {200x} = \left( {{a}_{0} - {200x}}\right)  \cdot  {1.005}^{n}$ .

由 ${a}_{360} = 0$ 得 $\;0 - {200x} = \left( {{50} - {200x}}\right)  \cdot  {1.005}^{360}$ .

利用计算器可以求得 $x = {0.299775}$ 万元，即每月还款2997.75元

7、在数列 $\left\{  {a}_{n}\right\}$ 中，已知 ${a}_{1} = 2,{a}_{2} = 7,{a}_{n + 2}$ 等于 ${a}_{n}{a}_{n + 1}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ 的个位数，则 ${a}_{2013}$ 的值是 ( )

A. 8 B. 6 C. 4 D. 2

【难度】 $\star   \star   \star$

【答案】C

【解析】 ${a}_{1}{a}_{2} = 2 \times  7 = {14},\therefore {a}_{3} = 4,4 \times  7 = {28},\therefore {a}_{4} = 8,4 \times  8 = {32}$ ,

$\therefore {a}_{5} = 2,2 \times  8 = {16},\therefore {a}_{6} = 6,{a}_{7} = 2,{a}_{8} = 2,{a}_{9} = 4,{a}_{10} = 8,{a}_{11} = 2$ ,

$\therefore$ 从第三项起, ${a}_{n}$ 的值成周期排列,周期数为 $6,{2013} = {335} \times  6 + 3,\therefore {a}_{2013} = {a}_{3} = 4$ .

8、意大利著名数学家斐波那契在研究兔子繁殖问题时，发现有这样一列数:1，1，2，3，5，8，13，21， $\ldots$ ,其中从第三项开始,每个数都等于它前面两个数的和,后来人们把这样的一列数组成的数列 $\left\{  {a}_{n}\right\}$ 称为 “斐波那契数列”，那么 $\frac{{a}_{1}^{2} + {a}_{2}^{2} + {a}_{3}^{2} + \ldots  + {a}_{n}^{2}}{{a}_{n}}\left( {n \geq  3}\right)$ ，是斐波那契数列的第___项.

【难度】 $\star   \star   \star   \star   \star$

【答案】 $n + 1$

【解析】解: $\because {a}_{n + 2} = {a}_{n + 1} + {a}_{n},\therefore {a}_{n} \cdot  {a}_{n + 1} = {a}_{n}^{2} + {a}_{n - 1} \cdot  {a}_{n}$ ,

${a}_{n - 1} \cdot  {a}_{n} = {a}_{n - 1}^{2} + {a}_{n - 2} \cdot  {a}_{n - 1},$

...

${a}_{3} \cdot  {a}_{2} = {a}_{2}^{2} + {a}_{2}{a}_{1},$

$\therefore {a}_{n} \cdot  {a}_{n + 1} = {a}_{n}^{2} + {a}_{n - 1}^{2} + \ldots  + {a}_{2}^{2} + {a}_{1}^{2}$ ,

$\therefore \frac{{a}_{1}^{2} + {a}_{2}^{2} + {a}_{3}^{2} + \ldots  + {a}_{n}^{2}}{{a}_{n}} = {a}_{n + 1}$ ,

故答案为: $n + 1$ .

9、已知数列 $\left\{  {a}_{n}\right\}$ 满足:① ${a}_{1} = 0$ ，②对任意的 $n \in  {N}^{ * }$ 都有 ${a}_{n + 1} > {a}_{n}$ 成立.

函数 ${f}_{n}\left( x\right)  = \left| {\sin \frac{1}{n}\left( {x - {a}_{n}}\right) }\right| , x \in  \left\lbrack  {{a}_{n},{a}_{n + 1}}\right\rbrack$ 满足: 对于任意的实数 $m \in  \lbrack 0,1),{f}_{n}\left( x\right)  = m$ 总有两个不同的根, 则 $\left\{  {a}_{n}\right\}$ 的通项公式是___.

【难度】 $\star   \star   \star   \star$

【答案】 ${a}_{n} = \frac{n\left( {n - 1}\right) }{2}\pi$

【解析】解: $\because {a}_{1} = 0$ ,当 $n = 1$ 时, ${f}_{1}\left( x\right)  = \left| {\sin \left( {x - {a}_{1}}\right) }\right|  = \left| {\sin x}\right| , x \in  \left\lbrack  {0,{a}_{2}}\right\rbrack$ ,

又 $\because$ 对任意的 $m \in  \lbrack 0,1),{f}_{1}\left( x\right)  = m$ 总有两个不同的根, $\therefore {a}_{2} = \pi$ ,

$\therefore {f}_{1}\left( x\right)  = \sin x, x \in  \left\lbrack  {0,\pi }\right\rbrack  ,{a}_{2} = \pi$ ,

又 ${f}_{2}\left( x\right)  = \left| {\sin \frac{1}{2}\left( {x - {a}_{2}}\right) }\right|  = \left| {\sin \frac{1}{2}\left( {x - \pi }\right) }\right|  = \left| {\cos \frac{x}{2}}\right| , x \in  \left\lbrack  {\pi ,{a}_{3}}\right\rbrack$ ,

$\because$ 对任意的 $m \in  \lbrack 0,1)$ ， ${f}_{1}\left( x\right)  = m$ 总有两个不同的根， $\therefore {a}_{3} = {3\pi }$ ，

又 ${f}_{3}\left( x\right)  = \left| {\sin \frac{1}{3}\left( {x - {a}_{3}}\right) }\right|  = \left| {\sin \frac{1}{3}\left( {x - {3\pi }}\right) }\right|  = \left| {\sin \frac{1}{3}\pi }\right| , x \in  \left\lbrack  {{3\pi },{a}_{4}}\right\rbrack$ ,

$\because$ 对任意的 $b \in  \lbrack 0,1),{f}_{1}\left( x\right)  = m$ 总有两个不同的根, $\therefore {a}_{4} = {6\pi }$ ,

由此可得 ${a}_{n + 1} - {a}_{n} = {n\pi }$ ,

$\therefore {a}_{n} = {a}_{1} + \left( {{a}_{2} - {a}_{1}}\right)  + \ldots  + \left( {{a}_{n} - {a}_{n - 1}}\right)  = 0 + \pi  + \ldots  + \left( {n - 1}\right) \pi  = \frac{n\left( {n - 1}\right) }{2}\pi$ ,

故答案为: ${a}_{n} = \frac{n\left( {n - 1}\right) }{2}\pi$ ,

10、已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 2,{a}_{n + 1} = 3{a}_{n} + {2}^{n - 1}, n \in  {\mathbf{N}}^{ * }$ .

(1)求证:数列 $\left\{  {{a}_{n} + {2}^{n - 1}}\right\}$ 是等比数列，并求 $\left\{  {a}_{n}\right\}$ 的通项公式;

(2)设 ${b}_{n} = {\log }_{\sqrt{3}}\left( {{a}_{n} + {2}^{n - 1}}\right)  + 1$ ，若不等式 ${15}\left( {1 + \frac{1}{{b}_{1}}}\right) \left( {1 + \frac{1}{{b}_{2}}}\right) \cdots \left( {1 + \frac{1}{{b}_{n}}}\right)  \geq  k\sqrt{{10n} + {15}}$ 对于任意 $n \in  {\mathbf{N}}^{ * }$ 都成立,求正数 $k$ 的最大值.

【难度】 $\star   \star   \star   \star$

【答案】(1)证明见解析; ${a}_{n} = {3}^{n} - {2}^{n - 1}, n \in  {N}^{ * }$ ; (2) 正数 $k$ 的最大值为 4

【解析】(1) 证明: ${a}_{1} = 2,{a}_{n + 1} = 3{a}_{n} + {2}^{n - 1}, n \in  {N}^{ * }$ ,可得 ${a}_{n + 1} + {2}^{n} = 3\left( {{a}_{n} + {2}^{n - 1}}\right)$ ,

所以 $\left\{  {{a}_{n} + {2}^{n - 1}}\right\}$ 是以 3 为首项、 3 为公比的等比数列,所以 ${a}_{n} + {2}^{n - 1} = {3}^{n}$ ,

则 ${a}_{n} = {3}^{n} - {2}^{n - 1}, n \in  {N}^{ * }$ ;

(3) ${b}_{n} = {\log }_{\sqrt{3}}\left( {{3}^{n} - {2}^{n - 1} + {2}^{n - 1}}\right)  + 1 = {\log }_{\sqrt{3}}{3}^{n} + 1 = {2n} + 1$ ,

不等式 $\left( {1 + \frac{1}{{b}_{1}}}\right) \left( {1 + \frac{1}{{b}_{2}}}\right) \cdots \left( {1 + \frac{1}{{b}_{n}}}\right)  \geq  \frac{\sqrt{5}k}{15}\sqrt{{2n} + 3}$ ,即

$\frac{\sqrt{5}k}{15} \leq  \frac{\left( {1 + \frac{1}{{b}_{1}}}\right) \left( {1 + \frac{1}{{b}_{2}}}\right) \cdots \left( {1 + \frac{1}{{b}_{n}}}\right) }{\sqrt{{2n} + 3}} = \frac{4}{3} \cdot  \frac{6}{5} \cdot  \frac{8}{7}\cdots \frac{{2n} + 2}{{2n} + 1} \cdot  \frac{1}{\sqrt{{2n} + 3}},$

设 $f\left( n\right)  = \frac{4}{3} \cdot  \frac{6}{5} \cdot  \frac{8}{7}\cdots \frac{{2n} + 2}{{2n} + 1} \cdot  \frac{1}{\sqrt{{2n} + 3}}$ ,

$\frac{f\left( {n + 1}\right) }{f\left( n\right) } = \frac{\frac{4}{3} \cdot  \frac{6}{5} \cdot  \frac{8}{7}\cdots \frac{{2n} + 2}{{2n} + 1} \cdot  \frac{{2n} + 4}{{2n} + 3} \cdot  \frac{1}{\sqrt{{2n} + 5}}}{\frac{4}{3} \cdot  \frac{6}{5} \cdot  \frac{8}{7}\cdots \frac{{2n} + 2}{{2n} + 1} \cdot  \frac{1}{\sqrt{{2n} + 3}}}$

$= \frac{{2n} + 4}{{2n} + 3} \cdot  \frac{\sqrt{{2n} + 3}}{\sqrt{{2n} + 5}} = \frac{{2n} + 4}{\sqrt{\left( {{2n} + 3}\right) \left( {{2n} + 5}\right) }} = \frac{{2n} + 4}{\sqrt{4{n}^{2} + {16n} + {15}}}$

$> \frac{{2n} + 4}{\sqrt{4{n}^{2} + {16n} + {16}}} = \frac{{2n} + 4}{\sqrt{{\left( 2n + 4\right) }^{2}}} = 1$ ,

所以 $f\left( {n + 1}\right)  > f\left( n\right)$ ,即当 $n$ 增大时, $f\left( n\right)$ 也增大,

所以只需 $\frac{\sqrt{5}}{15}k \leq  f{\left( n\right) }_{\min }$ 即可. 因为 $f{\left( n\right) }_{\min } = f\left( 1\right)  = \frac{4}{3} \cdot  \frac{1}{\sqrt{5}} = \frac{4\sqrt{5}}{15}$ ,

所以, $\frac{\sqrt{5}}{15}k \leq  \frac{4\sqrt{5}}{15}$ 即 $k \leq  4$ ,所以正数 $k$ 的最大值为 4 .

## (二) 数列求和

## 知识梳理

求数列前 $\mathrm{n}$ 项和:

1、公式法求和

① 等差数列求和公式: ${S}_{n} = \frac{n\left( {{a}_{1} + {a}_{n}}\right) }{2} = n{a}_{1} + \frac{n\left( {n - 1}\right) }{2}d$

② 等比数列求和公式: ${S}_{n} = \left\{  \begin{array}{ll} \begin{matrix} {a}_{1} \\  \frac{{a}_{1}\left( {1 - {q}^{n}}\right) }{1 - q} = \frac{{a}_{1} - {a}_{n}q}{1 - q} \end{matrix} & \begin{matrix} \left( {q = 1}\right) \\  \left( {q \neq  1}\right)  \end{matrix} \end{array}\right.$

③ ${S}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}k = \frac{1}{2}n\left( {n + 1}\right) \;$ ④ ${S}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}{k}^{2} = \frac{1}{6}n\left( {n + 1}\right) \left( {{2n} + 1}\right) \;$ ⑤ ${S}_{n} = \mathop{\sum }\limits_{{k = 1}}^{n}{k}^{3} = {\left\lbrack  \frac{1}{2}n\left( n + 1\right) \right\rbrack  }^{2}$

公式法求和注意事项:(1)弄准求和项数 $n$ 的值；

(2)等比数列公比 $q$ 未知时，运用前 $n$ 项和公式要分类.

## 2、分组求和法

分组求和有两种情况, 一种是将数列适当拆开, 可分为几个等差、等比或常见的数列, 然后分别求和, 再将其合并即可; 另一种是将数列相邻的两项(或若干项)并成一项(或一组)得到一个新数列(容易求和).

## 3、裂项相消法

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

(2)在写出 “ ${S}_{n}$ ” 与 “ $q{S}_{n}$ ” 的表达式时应特别注意将两式 “错项对齐” 以便下一步准确写出 “ ${S}_{n} - q{S}_{n}$ ” 的表达式;

(3)在应用错位相减法求和时，若等比数列的公比为参数，应分公比等于 1 和不等于 1 两种情况求解.

## 例题精讲

【例 15】(1)已知各项均为正数的数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，且 ${a}_{1} = 1,{a}_{n + 1}\left( {{a}_{n + 1} - 1}\right)  = {a}_{n}\left( {{a}_{n} + 1}\right)$ . 若 $\left\lbrack  x\right\rbrack$ 表示不超过 $x$ 的最大整数, ${b}_{n} = \left\lbrack  \frac{{\left( n + 1\right) }^{2}}{2{S}_{n}}\right\rbrack$ ,则数列 $\left\{  {b}_{n}\right\}$ 的前 2021 项和 ${T}_{2021} =$ (   )

A. 1010 B. 1011 C. 2021 D. 2022

【难度】★★★★

【答案】 $D$

【解析】解: $\because {a}_{n + 1}\left( {{a}_{n + 1} - 1}\right)  = {a}_{n}\left( {{a}_{n} + 1}\right) ,\therefore {a}_{n + 1}^{2} - {a}_{n}^{2} = {a}_{n + 1} + {a}_{n}$ ,即 $\left( {{a}_{n + 1} - {a}_{n}}\right) \left( {{a}_{n + 1} + {a}_{n}}\right)  = {a}_{n + 1} + {a}_{n}$ , $\because {a}_{n} > 0,\therefore {a}_{n + 1} - {a}_{n} = 1$ (常数), $\because {a}_{1} = 1,\therefore$ 数列 $\left\{  {a}_{n}\right\}$ 是首项为 1 、公差为 1 的等差数列, $\therefore {a}_{n} = n$ , $\therefore {S}_{n} = \frac{n\left( {1 + n}\right) }{2},\therefore \frac{{\left( n + 1\right) }^{2}}{2{S}_{n}} = \frac{{\left( n + 1\right) }^{2}}{n\left( {1 + n}\right) } = \frac{n + 1}{n},\therefore {T}_{2021} = 2 + 1 + 1\cdots 1 = 2 + {2020} = {2022}$ .

故选: $D$

(2)“中国剩余定理”又称 “孙子定理”，讲的是关于整除的问题(如 7 被 3 除余 1:1 被 2 除余 1). 现有这样一个整除问题: 将 1 到 100 这 100 个正整数中能被 2 除余 1 且被 3 除余 1 的数按从小到大的顺序排成一列,构成数列 $\left\{  {a}_{n}\right\}$ ,则数列 $\left\{  {a}_{n}\right\}$ 各项的和为(   )

A. 736 B. 816 C. 833 D. 29800

【难度】★★★★

【答案】 $C$

【解析】解: “能被 2 除余 1 且被 3 除余 1 的数” 即 “被 6 除余 1 ”,

所有项为等差数列,通项为 “ ${a}_{n} = {6n} - 5$ ”,由题意知 ${6n} - 5 \leq  {100}$ ,得 $n \leq  \frac{35}{2}$ ,

$\therefore n \leq  {17},{a}_{17} = 6 \times  {17} - 5 = {97},{a}_{1} = 1,\therefore {S}_{17} = \frac{{17}\left( {{a}_{1} + {a}_{17}}\right) }{2} = \frac{{17}\left( {1 + {97}}\right) }{2} = {833}$ . 故选: $C$ .

【例 16】已知数列 $\left\{  {a}_{n}\right\}$ 和 $\left\{  {b}_{n}\right\}$ 满足 ${a}_{1} = 1,{b}_{1} = 0,4{a}_{n + 1} = 3{a}_{n} - {b}_{n} + 4,4{b}_{n + 1} = 3{b}_{n} - {a}_{n} - 4$ .

(1)证明: $\left\{  {{a}_{n} + {b}_{n}}\right\}$ 是等比数列， $\left\{  {{a}_{n} - {b}_{n}}\right\}$ 是等差数列；

(2)求 $\left\{  {a}_{n}\right\}$ 和 $\left\{  {b}_{n}\right\}$ 的通项公式；

(3)令 ${c}_{n} = \left\{  \begin{array}{ll} {a}_{n} & n\text{ 是奇数 } \\  {b}_{n} & n\text{ 是偶数 } \end{array}\right.$ ，求数列 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n}$ 的通项公式，并求数列 $\left\{  \frac{1}{{S}_{n}}\right\}$ 的最大值、最小值，并指出分别是第几项.

【难度】 $\bigstar \bigstar \bigstar$

【答案】见解析

【解析】解: (1) 证明: $\because {a}_{1} = 1,{b}_{1} = 0,\therefore {a}_{1} + {b}_{1} = {a}_{1} - {b}_{1} = 1$ . 又 $\because 4{a}_{n + 1} = 3{a}_{n} - {b}_{n} + 4$ ①, $4{b}_{n + 1} = 3{b}_{n} - {a}_{n} - 4$ ②，由①+②可得: $4\left( {{a}_{n + 1} + {b}_{n + 1}}\right)  = 2\left( {{a}_{n} + {b}_{n}}\right)$ ，即 $\frac{{a}_{n + 1} + {b}_{n + 1}}{{a}_{n} + {b}_{n}} = \frac{1}{2}$ ， $\therefore$ 数列 $\left\{  {{a}_{n} + {b}_{n}}\right\}$ 是首项为 1，公比为 $\frac{1}{2}$ 的等比数列; 由①-②可得: $4\left( {{a}_{n + 1} - {b}_{n + 1}}\right)  = 4\left( {{a}_{n} - {b}_{n}}\right)  + 8$ ,即 $\left( {{a}_{n + 1} - {b}_{n + 1}}\right)  - \left( {{a}_{n} - {b}_{n}}\right)  = 2$ , $\therefore$ 数列 $\left\{  {{a}_{n} - {b}_{n}}\right\}$ 是首项为 1 , 公差为 2 的等差数列.

(2)解:由(1)知: ${a}_{n} + {b}_{n} = {\left( \frac{1}{2}\right) }^{n - 1}$ ③， ${a}_{n} - {b}_{n} = 1 + 2\left( {n - 1}\right)  = {2n} - 1$ ④，由③ + ④整理得: ${a}_{n} = n - \frac{1}{2} + \frac{1}{{2}^{n}}$ ； 由③-④整理得: ${b}_{n} =  - n + \frac{1}{2} + \frac{1}{{2}^{n}}$ ，故 ${a}_{n} = n - \frac{1}{2} + \frac{1}{{2}^{n}}$ ， ${b}_{n} =  - n + \frac{1}{2} + \frac{1}{{2}^{n}}$ ；

(3)解:由(2)得 ${c}_{n} = \left\{  \begin{array}{l} n - \frac{1}{2} + \frac{1}{{2}^{n}}, n\text{ 为奇数 } \\   - n + \frac{1}{2} + \frac{1}{{2}^{n}}, n\text{ 为偶数 } \end{array}\right.$ ，即 ${c}_{n} = \frac{1}{{2}^{n}} + {\left( -1\right) }^{n - 1}\left( {n - \frac{1}{2}}\right)$ .

当 $n$ 为偶数时, ${S}_{n} = \frac{\frac{1}{2}\left\lbrack  {1 - {\left( \frac{1}{2}\right) }^{n}}\right\rbrack  }{1 - \frac{1}{2}} + \left\{  {\left\lbrack  {\left( {1 - \frac{1}{2}}\right)  - \left( {2 - \frac{1}{2}}\right) }\right\rbrack   + \left\lbrack  {\left( {3 - \frac{1}{2}}\right)  - \left( {4 - \frac{1}{2}}\right) }\right\rbrack   + \ldots  + \left\lbrack  {\left( {n - 1 - \frac{1}{2}}\right)  - \left( {n - \frac{1}{2}}\right) }\right\rbrack  }\right\}   = 1 - \frac{n}{2} - \frac{1}{{2}^{n}}$ ;

当 $n$ 为奇数时,

${S}_{n} = \frac{\frac{1}{2}\left\lbrack  {1 - {\left( \frac{1}{2}\right) }^{n}}\right\rbrack  }{1 - \frac{1}{2}} + \left\{  {\left\lbrack  {\left( {1 - \frac{1}{2}}\right)  - \left( {2 - \frac{1}{2}}\right) }\right\rbrack   + \left\lbrack  {\left( {3 - \frac{1}{2}}\right)  - \left( {4 - \frac{1}{2}}\right) }\right\rbrack   + \ldots  + \left\lbrack  {\left( {n - 2 - \frac{1}{2}}\right)  - \left( {n - 1 - \frac{1}{2}}\right) }\right\rbrack  }\right\}   + n - \frac{1}{2} = \frac{n}{2} + 1 - \frac{1}{{2}^{n}}$ ,

即 ${S}_{n} = 1 - {\left( \frac{1}{2}\right) }^{n} - \frac{n \cdot  {\left( -1\right) }^{n}}{2}$ .

易知: $\left\{  \frac{1}{{S}_{n}}\right\}$ 的最大值为 $\frac{1}{{S}_{1}} = 1$ ,为第一项; 最小值为 $\frac{1}{{S}_{2}} =  - 4$ ,为第二项.

【例 17】求证: ${C}_{n}^{0} + 3{C}_{n}^{1} + 5{C}_{n}^{2} + \cdots  + \left( {{2n} + 1}\right) {C}_{n}^{n} = \left( {n + 1}\right)  \cdot  {2}^{n}$ ;

【难度】 $\star   \star   \star$

【答案】见解析

【解析】令 $S = {C}_{n}^{0} + 3{C}_{n}^{1} + 5{C}_{n}^{2} + \cdots  + \left( {{2n} + 1}\right) {C}_{n}^{n}$①

$S = \left( {{2n} + 1}\right) {C}_{n}^{n} + \left( {{2n} - 1}\right) {C}_{n}^{n - 1} + \left( {{2n} - 3}\right) {C}_{n}^{n - 2} + \cdots  + {C}_{n}^{0}$

$= \left( {{2n} + 1}\right) {C}_{n}^{0} + \left( {{2n} - 1}\right) {C}_{n}^{1} + \left( {{2n} - 3}\right) {C}_{n}^{2} + \cdots  + {C}_{n}^{n}$②

①+②得 ${2S} = \left( {{2n} + 1}\right) {C}_{n}^{0} + \left( {{2n} + 1}\right) {C}_{n}^{1} + \left( {{2n} + 1}\right) {C}_{n}^{2} + \cdots  + \left( {{2n} + 1}\right) {C}_{n}^{n} = \left( {{2n} + 1}\right)  \cdot  {2}^{n}$

【例 18】数列 $\left\{  {b}_{n}\right\}$ 满足 ${b}_{n + 1} = \frac{{b}_{n}}{2} + \frac{1}{{2}^{n + 1}}$ ,若 ${b}_{1} = \frac{1}{2}$ ,则 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为( )

A. $1 - \frac{n + 2}{{2}^{n + 1}}$ B. $1 - \frac{n + 1}{{2}^{n + 1}}$ C. $2 - \frac{n + 2}{{2}^{n}}$ D. $2 - \frac{{3n} + 3}{{2}^{n + 1}}$

【难度】 $\star   \star   \star$

【答案】C

【解析】解: ${b}_{n + 1} = \frac{{b}_{n}}{2} + \frac{1}{{2}^{n + 1}} \Leftrightarrow  {2}^{n + 1}{b}_{n + 1} - {2}^{n}{b}_{n} = 1,{2}^{1}{b}_{1} = 1$ ,

可知数列 $\left\{  {{2}^{n}{b}_{n}}\right\}$ 是以 1 为首项 1 为公差的等差数列, $\therefore {2}^{n}{b}_{n} = 1 + \left( {n - 1}\right)  \times  1 = n$ , $\therefore {b}_{n} = \frac{n}{{2}^{n}}$ ,

设数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n} = \frac{1}{2} + \frac{2}{{2}^{2}} + \frac{3}{{2}^{3}} + \cdots  + \frac{n - 1}{{2}^{n - 1}} + \frac{n}{{2}^{n}}$ ①

① $\times  \frac{1}{2}$ 得 $\frac{1}{2}{S}_{n} = \frac{1}{{2}^{2}} + \frac{2}{{2}^{3}} + \frac{3}{{2}^{4}} + \cdots  + \frac{n - 1}{{2}^{n}} + \frac{n}{{2}^{n + 1}}$ ②

①-② $\frac{1}{2}{S}_{n} = \frac{1}{2} + \frac{1}{{2}^{2}} + \frac{1}{{2}^{3}} + \cdots  + \frac{1}{{2}^{n}} - \frac{n}{{2}^{n + 1}} = \frac{\frac{1}{2} - \frac{1}{{2}^{n + 1}}}{1 - \frac{1}{2}} - \frac{n}{{2}^{n + 1}} = 1 - \frac{n + 2}{{2}^{n + 1}}$ ， $\therefore {S}_{n} = 2 - \frac{n + 2}{{2}^{n}}$ .

故选: $C$ .

【例 19】已知数列 $\left\{  {a}_{n}\right\}$ : 满足 ${a}_{1} = 2,{a}_{n + 1} = {a}_{n}^{2} + 6{a}_{n} + 6\left( {n \in  {N}^{ * }}\right)$ .

(1)设 ${C}_{n} = {\log }_{5}\left( {{a}_{n} + 3}\right)$ ，求证是等比数列；

(2)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式

(3)设 ${b}_{n} = \frac{1}{{a}_{n} - 6} - \frac{1}{{a}_{n}^{2} + 6{a}_{n}}$ ，数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ，求证: $- \frac{5}{16} \leq  {T}_{n} <  - \frac{1}{4}$ .

【难度】 $\star   \star   \star   \star$

【答案】详见解析

【解析】(1) $\because {a}_{n + 1} = {a}_{n}{}^{2} + 6{a}_{n} + 6\therefore {a}_{n + 3} = {\left( {a}_{n} + 3\right) }^{2}$

$\therefore {\log }_{5}\left( {{a}_{n + 1} + 3}\right)  = 2{\log }_{5}\left( {{a}_{n} + 3}\right)$ ,即 ${C}_{n + 1} = 2{C}_{n}$ ,

$\therefore \left\{  {C}_{n}\right\}$ 是以 2 为公比的等比数列

(2)又 ${C}_{1} = {\log }_{5}5 = 1\therefore {C}_{n} = {2}^{n - 1}$ 即 ${\log }_{5}\left( {{a}_{n} + 3}\right)  = {2}^{n - 1}$ ,

$\therefore {a}_{n} + 3 = {5}^{{2}^{n - 1}}$ . 故而 ${a}_{n} = {5}^{{2}^{n - 1}} - 3.n \in  {N}^{ * }$

(3) $\because {b}_{n} = \frac{1}{{a}_{n} - 6} - \frac{1}{{a}_{n}^{2} + 6{a}_{n}} = \frac{1}{{a}_{n} - 6} - \frac{1}{{a}_{n + 1} - 6},\therefore {T}_{n} = \frac{1}{{a}_{1} - 6} - \frac{1}{{a}_{n + 1} - 6} =  - \frac{1}{4} - \frac{1}{{5}^{{2}^{n}} - 9}$ .

又 $0 < \frac{1}{{5}^{{2}^{n}} - 9} \leq  \frac{1}{{5}^{2} - 9} = \frac{1}{16},\therefore  - \frac{5}{16} \leq  {T}_{n} <  - \frac{1}{4}$ .

【例 20】已知等差数列 $\left\{  {a}_{n}\right\}$ 的公差为 2,前 $n$ 项和为 ${S}_{n}$ ,且 ${S}_{1},{S}_{2},{S}_{4}$ 成等比数列.

(I)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(II) 令 ${b}_{n} = {\left( -1\right) }^{n - 1}\frac{4n}{{a}_{n}{a}_{n + 1}}$ ,求数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和 ${T}_{n}$ .

【难度】 $\star   \star   \star   \star   \star$

【答案】见解析

【解析】(1) $\because {S}_{1} = {a}_{1},{S}_{2} = 2{a}_{1} + \frac{2 \times  1}{2} \times  2 = 2{a}_{1} + 2$ ,

${S}_{4} = 4{a}_{1} + \frac{4 \times  3}{2} \times  2 = 4{a}_{1} + {12}$ ,又 ${S}_{1},{S}_{2},{S}_{4}$ 成等比数列,

$\therefore {\left( 2{a}_{1} + 2\right) }^{2} = {a}_{1}\left( {4{a}_{1} + {12}}\right)$ .

解得 ${a}_{1} = 1,\therefore {a}_{n} = {2n} - 1$ .

(2) ${b}_{n} = {\left( -1\right) }^{n - 1}\frac{4n}{{a}_{n}{a}_{n + 1}} = {\left( -1\right) }^{n - 1}\frac{4n}{\left( {{2n} - 1}\right) \left( {{2n} + 1}\right) } = {\left( -1\right) }^{n - 1}\left( {\frac{1}{{2n} - 1} + \frac{1}{{2n} + 1}}\right)$

当 $n$ 为偶数时,

${T}_{n} = \left( {1 + \frac{1}{3}}\right) \left( {\frac{1}{3} + \frac{1}{5}}\right)  + \ldots  + \left( {\frac{1}{{2n} - 3} + \frac{1}{{2n} - 1}}\right) \left( {\frac{1}{{2n} - 1} + \frac{1}{{2n} + 1}}\right)  = 1 - \frac{1}{{2n} + 1} = \frac{2n}{{2n} + 1}.$

当 $n$ 为奇数时,

${T}_{n} = \left( {1 + \frac{1}{3}}\right)  - \left( {\frac{1}{3} + \frac{1}{5}}\right)  + \ldots  - \left( {\frac{1}{{2n} - 3} + \frac{1}{{2n} - 1}}\right)  + \left( {\frac{1}{{2n} - 1} + \frac{1}{{2n} + 1}}\right)  = 1 + \frac{1}{{2n} + 1} = \frac{{2n} + 2}{{2n} + 1}.$

$\therefore {T}_{n} = \left\{  {\begin{array}{ll} \frac{{2n} + 2}{{2n} + 1}, & n\text{ 为奇数, } \\  \frac{2n}{{2n} + 1}, & n\text{ 为偶数 } \end{array}\text{ 或 }{T}_{n} = \frac{{2n} + 1 + {\left( -1\right) }^{n - 1}}{{2n} + 1}}\right.$ .

## 巩固训练

1、记 ${a}_{m}$ 为数列 $\left\{  {3}^{n}\right\}$ 在区间 $(0, m\rbrack \left( {n \in  {N}^{ * }}\right)$ 中的项的个数，则数列 $\left\{  {a}_{m}\right\}$ 的前 100 项的和 ${S}_{100} =$ ___.

【难度】 $\star   \star   \star   \star$

【答案】284

【解析】解: 对于区间 $(0, m\rbrack , m \in  \left\{  {m \mid  m \in  N,1 \leq  m \leq  {100}}\right\}$ ,可知:

(1)当 $m = 1,2$ 时，区间内不含 ${3}^{n}$ 项，故 ${a}_{1} = {a}_{2} = 0$ ，共 2 项；

(2)当 $m = 3,4,5,\ldots {.8}$ 时，区间内含有 ${3}^{1}$ 一项，故 ${a}_{3} = {a}_{4} = {a}_{5} = \ldots \ldots {a}_{8} = 1$ ，共 6 项；

(3)当 $m = 9,{10},{11},\ldots {.26}$ 时，区间内含有 ${3}^{1},{3}^{2}$ 两项，故 ${a}_{9} = {a}_{10} = {a}_{11} = \ldots \ldots  = {a}_{26} = 2$ ，共 18 项；

(4)当 $m = {27},{28},{29},\ldots \ldots ,{80}$ 时，区间内含有 ${3}^{1},{3}^{2},{3}^{3}$ 三项，故 ${a}_{27} = {a}_{28} = {a}_{29} = \ldots \ldots  = {a}_{80} = 3$ ，共 54 项;

(5) 当 $m = {81},{82},{83},\ldots \ldots ,{100}$ 时,区间内含有 $3,{3}^{2},{3}^{3},{3}^{4}$ 四项,故 ${a}_{81} = {a}_{82} = {a}_{83} = \ldots \ldots  = {a}_{100} = 4$ , 共 20 项.

故 ${S}_{100} = 2 \times  0 + 6 \times  1 + {18} \times  2 + {54} \times  3 + {20} \times  4 = {284}$ .

故答案为:284.

2、已知等差数列 $\left\{  {a}_{n}\right\}$ 中 ${a}_{1} = d = 1$ ， ${b}_{n} = \tan {a}_{n} \cdot  \tan {a}_{n + 1}\left( {n \in  {N}^{ * }}\right)$ ，则数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n} =$ ___.

【难度】 $\star   \star   \star   \star$

【答案】 $\frac{\tan \left( {n + 1}\right) }{\tan 1} - 1 - n$

【解析】解: 由已知可得 ${a}_{n} = n$ ,则 ${b}_{n} = \tan n \cdot  \tan \left( {n + 1}\right)$ ,

由 $\tan 1 = \tan \left\lbrack  {\left( {n + 1}\right)  - n}\right\rbrack   = \frac{\tan \left( {n + 1}\right)  - \tan n}{1 + \tan \left( {n + 1}\right) \tan n}$ ,

可得 ${b}_{n} = \tan n \cdot  \tan \left( {n + 1}\right)  = \frac{1}{\tan 1}\left\lbrack  {\tan \left( {n + 1}\right)  - \tan n}\right\rbrack   - 1$ ,

所以 ${S}_{n} = {b}_{1} + {b}_{2} + \ldots  + {b}_{n} = \frac{1}{\tan 1}\left\lbrack  {\left( {\tan 2 - \tan 1}\right)  + \left( {\tan 3 - \tan 2}\right)  + \ldots  + \tan \left( {n + 1}\right)  - \tan n}\right\rbrack   - n \; = \frac{1}{\tan 1}\left\lbrack  {\tan \left( {n + 1}\right)  - \tan 1}\right\rbrack   - n = \frac{\tan \left( {n + 1}\right) }{\tan 1} - 1 - n$ .

故答案为: $\frac{\tan \left( {n + 1}\right) }{\tan 1} - 1 - n$ .

3. 已知 ${a}_{1} = 2$ ，点 $\left( {{a}_{n},{a}_{n + 1}}\right)$ 在函数 $f\left( x\right)  = {x}^{2} + {2x}$ 的图象上 $\left( {n \in  {N}^{ * }}\right)$ ， ${b}_{n} = \frac{1}{{a}_{n}} + \frac{1}{{a}_{n} + 2}$ ，则数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n} =$ ___.

【难度】★★★★

【答案】 $1 - \frac{2}{{3}^{{2}^{n}} - 1}$

【解析】解: 由已知可得: ${a}_{n + 1} = {a}_{n}^{2} + {2n},\therefore {a}_{n + 1} + 1 = {\left( {a}_{n} + 1\right) }^{2}$ ,

$\because {a}_{1} = 2,\therefore {a}_{n} + 1 > 1$ ,

两边去对数得: $\lg \left( {{a}_{n + 1} + 1}\right)  = 2\lg \left( {{a}_{n} + 1}\right)$ ,即 $\frac{\lg \left( {{a}_{n + 1} + 1}\right) }{\lg \left( {{a}_{n} + 1}\right) } = 2$ ,

$\therefore$ 数列 $\left\{  {{lg}\left( {{a}_{n} + 1}\right) }\right\}$ 是首项为 $\lg 3$ ,公比为 2 的等比数列,

$\therefore \lg \left( {{a}_{n} + 1}\right)  = \lg 3 \cdot  {2}^{n - 1},\therefore {a}_{n} = {3}^{{2}^{n - 1}} - 1$ ,又 ${a}_{n + 1} = {a}_{n}^{2} + 2{a}_{n}$ ,

$\therefore \frac{1}{{a}_{n + 1}} = \frac{1}{2}\left( {\frac{1}{{a}_{n}} - \frac{1}{{a}_{n} + 2}}\right) ,\therefore \frac{1}{{a}_{n} + 2} = \frac{1}{{a}_{n}} - \frac{2}{{a}_{n + 1}}$ ,又 ${b}_{n} = \frac{1}{{a}_{n}} + \frac{1}{{a}_{n} + 2}$ ,

$\therefore {b}_{n} = 2\left( {\frac{1}{{a}_{n}} - \frac{1}{{a}_{n + 1}}}\right) ,\therefore {S}_{n} = {b}_{1} + {b}_{2} + \ldots  + {b}_{n} = 2\left( {\frac{1}{{a}_{1}} - \frac{1}{{a}_{2}} + \frac{1}{{a}_{2}} - \frac{1}{{a}_{3}} + \ldots  + \frac{1}{{a}_{n}} - \frac{1}{{a}_{n + 1}}}\right)  = 2\left( {\frac{1}{{a}_{1}} - \frac{1}{{a}_{n + 1}}}\right)$ ,

$\because {a}_{n} = {3}^{{2}^{n - 1}} - 1,{a}_{1} = 2,{a}_{n + 1} = {3}^{{2}^{n}} - 1,\therefore {S}_{n} = 1 - \frac{2}{{3}^{{2}^{n}} - 1}$ ,

故答案为: $1 - \frac{2}{{3}^{{2}^{n}} - 1}$ .

4. $\frac{1}{0!{10}!} + \frac{1}{1!9!} + \frac{1}{2!8!} + \frac{1}{3!7!} + \frac{1}{4!6!} + \frac{1}{5!5!} + \frac{1}{6!4!} + \frac{1}{7!3!} + \frac{1}{8!2!} + \frac{1}{9!1!} + \frac{1}{{10}!0!} =$

【难度】

【答案】 $\frac{4}{14175}$

【解析】解: $\frac{1}{0!{10}!} + \frac{1}{1!9!} + \frac{1}{2!8!} + \frac{1}{3!7!} + \frac{1}{4!6!} + \frac{1}{5!5!} + \frac{1}{6!4!} + \frac{1}{7!3!} + \frac{1}{8!2!} + \frac{1}{9!1!} + \frac{1}{{10}!0!} \; = \frac{1}{{10}!}\left( {\frac{{10}!}{0!{10}!} + \frac{{10}!}{1!9!} + \frac{{10}!}{2!8!} + \frac{{10}!}{3!7!} + \frac{{10}!}{4!6!} + \frac{{10}!}{5!5!} + \frac{{10}!}{6!4!} + \frac{{10}!}{7!3!} + \frac{{10}!}{8!2!} + \frac{{10}!}{9!1!} + \frac{{10}!}{{10}!0!}}\right) \; = \frac{1}{{10}!}\left( {{C}_{10}^{0} + {C}_{10}^{1} + {C}_{10}^{2} + {C}_{10}^{3} + {C}_{10}^{4} + {C}_{10}^{5} + {C}_{10}^{6} + {C}_{10}^{7} + {C}_{10}^{8} + {C}_{10}^{9} + {C}_{10}^{10}}\right) \; = \frac{1}{{10}!}{\left( 1 + 1\right) }^{10} = \frac{{2}^{10}}{{10}!} = \frac{4}{14175}.$

故答案为: $\frac{4}{14175}$ .

5、已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = {24},{a}_{n + 1} = \frac{n + 3}{n}{a}_{n} + \left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right)$ .

(1)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)用适当的组合数形式表示 ${a}_{n}$ ，并求数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n}$ ；

(3)若 ${b}_{n} = \frac{{a}_{n} \cdot  {2}^{n + 1}}{{\left( n + 2\right) }^{2}\left( {n + 3}\right) }$ ，记数列 $\left\{  \frac{1}{{b}_{n}}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ，求 $\mathop{\lim }\limits_{{x \rightarrow  \infty }}{T}_{n}$ .

【难度】

【答案】见解析

【解析】解: (1) $\because {a}_{n + 1} = \frac{n + 3}{n}{a}_{n} + \left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right)$ , $\therefore \frac{{a}_{n + 1}}{\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right) } = \frac{{a}_{n}}{n\left( {n + 1}\right) \left( {n + 2}\right) } + 1$ ,即 $\frac{{a}_{n + 1}}{\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right) )} - \frac{{a}_{n}}{n\left( {n + 1}\right) \left( {n + 2}\right) } = 1$ , $\because {a}_{1} = {24},\therefore \frac{{a}_{1}}{1 \times  2 \times  3} = 4,\therefore \left\{  \frac{{a}_{n}}{n\left( {n + 1}\right) \left( {n + 2}\right) }\right\}$ 是首项为 4,公差为 1 的等差数列, $\therefore \frac{{a}_{n}}{n\left( {n + 1}\right) \left( {n + 2}\right) } = 4 + 1 \times  \left( {n - 1}\right)  = n + 3$ ,即 ${a}_{n} = n\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right)$ ,

$\therefore$ 数列 $\left\{  {a}_{n}\right\}$ 的通项公式是 ${a}_{n} = n\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right)$ .

(2) ${a}_{n} = n\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right)  = 4 \times  3 \times  2 \times  1 \times  \frac{n\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right) }{4 \times  3 \times  2 \times  1} = {24}{C}_{n + 3}^{4}$ ,

$\therefore {S}_{n} = {a}_{1} + {a}_{2} + {a}_{3} + \cdots  + {a}_{n} = {24}{C}_{4}^{4} + {24}{C}_{5}^{4} + {24}{C}_{6}^{4} + \cdots  + {24}{C}_{n + 3}^{4} = {24}\left( {{C}_{5}^{5} + {C}_{5}^{4} + {C}_{6}^{4} + \cdots  + {C}_{n + 3}^{4}}\right)$

$= {24}{C}_{n + 4}^{5} = {24} \times  \frac{\left( {n + 4}\right) \left( {n + 3}\right)  \times  \left( {n + 2}\right) \left( {n + 1}\right) n}{5 \times  4 \times  3 \times  2 \times  1} = \frac{\left( {n + 4}\right) \left( {n + 3}\right) \left( {n + 2}\right) \left( {n + 1}\right) n}{5}$ ,

$\therefore$ 数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 $\frac{n\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right) \left( {n + 4}\right) }{5}$ .

(3)由(1)知 ${a}_{n} = n\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right)$ ，

$\therefore {b}_{n} = \frac{{a}_{n} \cdot  {2}^{n + 1}}{{\left( n + 2\right) }^{2}\left( {n + 3}\right) } = \frac{n\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right)  \cdot  {2}^{n + 1}}{{\left( n + 2\right) }^{2}\left( {n + 3}\right) } = \frac{n\left( {n + 1}\right)  \cdot  {2}^{n + 1}}{\left( n + 2\right) }$ ,

$\therefore \frac{1}{{b}_{n}} = \frac{n + 2}{n\left( {n + 1}\right)  \cdot  {2}^{n + 1}} = \frac{1}{n \cdot  {2}^{n}} - \frac{1}{\left( {n + 1}\right)  \cdot  {2}^{n + 1}}$ ,

$\therefore {T}_{n} = \frac{1}{{b}_{1}} + \frac{1}{{b}_{2}} + \frac{1}{{b}_{3}} + \cdots  + \frac{1}{{b}_{n}} = \frac{1}{1 \cdot  {2}^{1}} - \frac{1}{2 \cdot  {2}^{2}} + \frac{1}{2 \cdot  {2}^{2}} - \frac{1}{3 \cdot  {2}^{3}} + \cdots  + \frac{1}{n \cdot  {2}^{n}} - \frac{1}{\left( {n + 1}\right)  \cdot  {2}^{n + 1}} = \frac{1}{2} - \frac{1}{\left( {n + 1}\right)  \cdot  {2}^{n + 1}}$ ,

$\therefore \mathop{\lim }\limits_{{n \rightarrow  \infty }}{T}_{n} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\left\lbrack  {\frac{1}{2} - \frac{1}{\left( {n + 1}\right)  \cdot  {2}^{n + 1}}}\right\rbrack   = \frac{1}{2}$ .

6、在数列 $\left\{  {a}_{n}\right\}$ 中,已知 ${a}_{1} = 2,{a}_{n + 1}{a}_{n} = 2{a}_{n} - {a}_{n + 1}\left( {n \in  {N}^{ * }}\right)$ .

(1)证明:数列 $\left\{  {\frac{1}{{a}_{n}} - 1}\right\}$ 为等比数列；

(2)记 ${b}_{n} = \frac{{a}_{n}{a}_{n + 1}}{{2}^{n}}$ ，数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，求使得 ${S}_{n} > {1.999}$ 的整数 $n$ 的最小值；

(3)是否存在正整数 $m\text{ 、 }n\text{ 、 }k$ ,且 $m < n < k$ ，使得 ${a}_{m}\text{ 、 }{a}_{n}\text{ 、 }{a}_{k}$ 成等差数列？若存在，求出 $m\text{ 、 }n\text{ 、 }k$ 的值; 若不存在, 请说明理由.

【难度】 $\star   \star   \star   \star   \star$

【答案】见解析

【解析】证明: (1) 数列 $\left\{  {a}_{n}\right\}$ 中,已知 ${a}_{1} = 2,{a}_{n + 1}{a}_{n} = 2{a}_{n} - {a}_{n + 1}\left( {n \in  {N}^{ * }}\right)$ .

所以 ${a}_{n + 1} = \frac{2{a}_{n}}{{a}_{n} + 1}$ ,整理得 $\frac{1}{{a}_{n + 1}} = \frac{1}{2} \times  \frac{1}{{a}_{n}} + \frac{1}{2}$ ,故 $\frac{1}{{a}_{n + 1}} - 1 = \frac{1}{2}\left( {\frac{1}{{a}_{n}} - 1}\right) ,\left( {\frac{1}{{a}_{1}} - 1 \neq  0}\right)$

所以数列 $\left\{  {\frac{1}{{a}_{n}} - 1}\right\}$ 为等比数列;

(2)由(1)得: $\frac{1}{{a}_{n}} - 1 =  - \frac{1}{2} \times  {\left( \frac{1}{2}\right) }^{n - 1} =  - {\left( \frac{1}{2}\right) }^{n}$ ，所以 ${a}_{n} = \frac{{2}^{n}}{{2}^{n} - 1}$ ，

所以 ${b}_{n} = \frac{{a}_{n}{a}_{n + 1}}{{2}^{n}} = \frac{{2}^{n + 1}}{\left( {{2}^{n} - 1}\right) \left( {{2}^{n + 1} - 1}\right) } = \frac{2}{{2}^{n} - 1} - \frac{2}{{2}^{n + 1} - 1}$ ,

故 ${S}_{n} = \left( {\frac{2}{2 - 1} - \frac{2}{{2}^{2} - 1}}\right)  + \left( {\frac{2}{{2}^{2} - 1} - \frac{2}{{2}^{3} - 1}}\right)  + \ldots  + \left( {\frac{2}{{2}^{n} - 1} - \frac{2}{{2}^{n + 1} - 1}}\right)  = 2 - \frac{2}{{2}^{n + 1} - 1}$ .

令 $2 - \frac{2}{{2}^{n + 1} - 1} > {1.999}$ ,则 ${2}^{n + 1} > {2001}$ ,解得 $n > {\log }_{2}{2001} - 1 \approx  {9.97}$ ,

所以 $n$ 的最小正值为 10 .

(3)假设存在正整数 $m\text{ 、 }n\text{ 、 }k$ 满足题意，则 $2{a}_{n} = {a}_{m} + {a}_{k}$ ，

即 $\frac{2 \cdot  {2}^{n}}{{2}^{n} - 1} = \frac{{2}^{m}}{{2}^{m} - 1} + \frac{{2}^{k}}{{2}^{k} - 1}$ ,整理得 ${2}^{n - m + 1}\left( {{2}^{m} - 1}\right) \left( {{2}^{k} - 1}\right)  = \left( {{2}^{n} - 1}\right) \left( {{2}^{k} - 1}\right)  + {2}^{k - m}\left( {{2}^{n} - 1}\right) \left( {{2}^{m} - 1}\right)$ ,

由于 $m < n < k$ ,得到 $k - m \geq  2, n - m + 1 \geq  2$ ,

所以 $\left( {{2}^{n} - 1}\right) \left( {{2}^{k} - 1}\right)$ 为奇数,而 ${2}^{n - m + 1}\left( {{2}^{m} - 1}\right) \left( {{2}^{k} - 1}\right)$ 和 ${2}^{k - m}\left( {{2}^{n} - 1}\right) \left( {{2}^{m} - 1}\right)$ 均为偶数,

故 (1) 式不能成立,即不存在正整数 $m\text{ 、 }n\text{ 、 }k$ 且 $m < n < k$ ,使得 ${a}_{m},{a}_{n},{a}_{k}$ 成等差数列.

## 实战演练

一、填空题

1、已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 3$ ，且 $n \in  {N}^{ * }$ 时， ${a}_{n + 1} = \frac{n}{n + 2}{a}_{n}$ ，求通项 ${a}_{n} =$ ___.

【难度】 $\star   \star   \star$

【答案】 $\therefore {a}_{n} = \frac{6}{n\left( {n + 1}\right) }$

【解析】解: $\because {a}_{n + 1} = \frac{n}{n + 2}{a}_{n},\therefore \frac{{a}_{n + 1}}{{a}_{n}} = \frac{n}{n + 2}$ ,

$\therefore \frac{{a}_{2}}{{a}_{1}} = \frac{1}{3},\frac{{a}_{3}}{{a}_{2}} = \frac{2}{4},\frac{{a}_{4}}{{a}_{3}} = \frac{3}{5},\ldots ,\frac{{a}_{n}}{{a}_{n - 1}} = \frac{n - 1}{n + 1}$

$\therefore \frac{{a}_{2}}{{a}_{1}} \times  \frac{{a}_{3}}{{a}_{2}} \times  \frac{{a}_{4}}{{a}_{3}} \times  \ldots  \times  \frac{{a}_{n}}{{a}_{n - 1}} = \frac{1}{3} \times  \frac{2}{4} \times  \ldots \frac{n - 1}{n + 1} = \frac{1 \times  2}{n\left( {n + 1}\right) }$

$\because {a}_{1} = 3$ ,

$\therefore {a}_{n} = \frac{6}{n\left( {n + 1}\right) }$ .

2、已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,3{a}_{n + 1}{a}_{n} = {a}_{n} - {a}_{n + 1}$ ,则通项 ${a}_{n} =$ ___.

【难度】 $\star   \star   \star$

【答案】 $\frac{1}{{3n} - 2}$

【解析】解: 数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,3{a}_{n + 1}{a}_{n} = {a}_{n} - {a}_{n + 1}$ ,

可得 $\frac{1}{{a}_{n + 1}} - \frac{1}{{a}_{n}} = 3$ ,可得数列 $\left\{  \frac{1}{{a}_{n}}\right\}$ 是等差数列,首项为 1,公差为 3,所以 $\frac{1}{{a}_{n}} = 1 + 3\left( {n - 1}\right)$ ,

所以 ${a}_{n} = \frac{1}{{3n} - 2}$ . 故答案为: $\frac{1}{{3n} - 2}$ .

3、设 ${S}_{n}$ 是数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和且 ${a}_{1} = 2,{a}_{n + 1} = {S}_{n} \cdot  {S}_{n + 1}$ ,则 ${S}_{n} =$ ___.

【难度】 $\star   \star   \star$

【答案】 $\frac{2}{3 - {2n}}$

【解析】解: 根据题意,数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{n + 1} = {S}_{n} \cdot  {S}_{n + 1}$ ,即 ${S}_{n + 1} - {S}_{n} = {S}_{n} \cdot  {S}_{n + 1}$ ,

变形可得: $\frac{1}{{s}_{n}} - \frac{1}{{s}_{n + 1}} = 1$ ,即 $\frac{1}{{s}_{n + 1}} - \frac{1}{{s}_{n}} =  - 1$ ,又由 ${a}_{1} = 2$ ,即 $\frac{1}{{s}_{1}} = \frac{1}{{a}_{1}} = \frac{1}{{a}_{1}}$ ;

故数列 $\left\{  \frac{1}{{S}_{n}}\right\}$ 是首项为 $\frac{1}{2}$ ,公差为 -1 的等差数列,则 $\frac{1}{{S}_{n}} = \frac{1}{2} + \left( {-1}\right) \left( {n - 1}\right)  =  - n + \frac{3}{2}$ ,

故 ${s}_{n} = \frac{2}{3 - {2n}}$ ; 故答案为: $\frac{2}{3 - {2n}}$ .

4、若数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1$ ， $n{a}_{n + 1} - \left( {n + 1}\right) {a}_{n} = 2$ ，则数列 $\left\{  {a}_{n}\right\}$ 的通项公式为___.

【难度】 $\star   \star   \star$

【答案】 ${a}_{n} = {3n} - 2$

【解析】解: 因为 $n{a}_{n + 1} - \left( {n + 1}\right) {a}_{n} = 2$ ,两边同时除以 $n\left( {n + 1}\right)$ ,

得 $\frac{{a}_{n + 1}}{n + 1} - \frac{{a}_{n}}{n} = \frac{2}{n\left( {n + 1}\right) } = 2\left( {\frac{1}{n} - \frac{1}{n + 1}}\right)$ ,所以 $\frac{{a}_{2}}{2} - \frac{{a}_{1}}{1} = 2\left( {1 - \frac{1}{2}}\right)$ ,

$\frac{{a}_{3}}{3} - \frac{{a}_{2}}{2} = 2\left( {\frac{1}{2} - \frac{1}{3}}\right) ,$

$\frac{{a}_{4}}{4} - \frac{{a}_{3}}{3} = 2\left( {\frac{1}{3} - \frac{1}{4}}\right)$

...

$\frac{{a}_{n}}{n} - \frac{{a}_{n - 1}}{n - 1} = 2\left( {\frac{1}{n - 1} - \frac{1}{n}}\right) ,$

所以 $\frac{{a}_{n}}{n} - {a}_{1} = 2\left( {1 - \frac{1}{2} + \frac{1}{2} - \frac{1}{3} + \frac{1}{3} - \frac{1}{4} + \ldots  + \frac{1}{n - 1} - \frac{1}{n}}\right)  = 2\left( {1 - \frac{1}{n}}\right)$ ,所以 $\frac{{a}_{n}}{n} = 2\left( {1 - \frac{1}{n}}\right)  + 1 = 3 - \frac{2}{n}$ ,

所以 ${a}_{n} = {3n} - 2$ . 故答案为: ${a}_{n} = {3n} - 2$ .

5、已知数列 $\left\{  {a}_{n}\right\}  ,\left\{  {b}_{n}\right\}$ 满足 ${a}_{1} = {b}_{1} = 1$ ，对任何正整数 $n$ 均有 ${a}_{n + 1} = {a}_{n} + {b}_{n} + \sqrt{{a}_{n}^{2} + {b}_{n}^{2}}$ ， ${b}_{n + 1} = {a}_{n} + {b}_{n} - \sqrt{{a}_{n}^{2} + {b}_{n}^{2}}$ ， 设 ${c}_{n} = {3}^{n}\left( {\frac{1}{{a}_{n}} + \frac{1}{{b}_{n}}}\right)$ ,则数列 $\left\{  {c}_{n}\right\}$ 的前 2020 项之和为___.

【难度】 $\star   \star   \star   \star$

【答案】 ${3}^{2021} - 3$

【解析】解: 依题意, ${a}_{n + 1} = {a}_{n} + {b}_{n} + \sqrt{{a}_{n}^{2} + {b}_{n}^{2}}$ ,①

${b}_{n + 1} = {a}_{n} + {b}_{n} - \sqrt{{a}_{n}^{2} + {b}_{n}^{2}}$ ,②

①+②，可得 ${a}_{n + 1} + {b}_{n + 1} = 2\left( {{a}_{n} + {b}_{n}}\right)$ ，

$\because {a}_{1} + {b}_{1} = 1 + 1 = 2,\therefore$ 数列 $\left\{  {{a}_{n} + {b}_{n}}\right\}$ 是以 2 为首项,2 为公比的等比数列,

$\therefore {a}_{n} + {b}_{n} = 2 \cdot  {2}^{n - 1} = {2}^{n}$ .

又①×②，可得

${a}_{n + 1} \cdot  {b}_{n + 1} = \left( {{a}_{n} + {b}_{n} + \sqrt{{a}_{n}^{2} + {b}_{n}^{2}}}\right)  \cdot  \left( {{a}_{n} + {b}_{n} - \sqrt{{a}_{n}^{2} + {b}_{n}^{2}}}\right)  = {\left( {a}_{n} + {b}_{n}\right) }^{2} - {\left( \sqrt{{a}_{n}^{2} + {b}_{n}^{2}}\right) }^{2} = 2{a}_{n} \cdot  {b}_{n}$ ,

$\because {a}_{1} \cdot  {b}_{1} = 1$ ， $\therefore$ 数列 $\left\{  {{a}_{n} \cdot  {b}_{n}}\right\}$ 是以 1 为首项，2 为公比的等比数列，

$\therefore {a}_{n} \cdot  {b}_{n} = 1 \cdot  {2}^{n - 1} = {2}^{n - 1} \cdot  \therefore {c}_{n} = {3}^{n}\left( {\frac{1}{{a}_{n}} + \frac{1}{{b}_{n}}}\right)  = {3}^{n} \cdot  \frac{{a}_{n} + {b}_{n}}{{a}_{n} \cdot  {b}_{n}} = {3}^{n} \cdot  \frac{{2}^{n}}{{2}^{n - 1}} = 2 \cdot  {3}^{n} = 6 \cdot  {3}^{n - 1}$ ,

$\therefore$ 数列 $\left\{  {c}_{n}\right\}$ 是以 6 为首项,3 为公比的等比数列,

设数列 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项之和为 ${S}_{n}$ ,则 ${S}_{2020} = \frac{6\left( {1 - {3}^{2020}}\right) }{1 - 3} = {3}^{2021} - 3$ .

故答案为: ${3}^{2021} - 3$ .

6、我们知道: $\frac{n + p}{n\left( {n + q}\right) } = \frac{p}{q} \cdot  \frac{1}{n} - \frac{p - q}{q} \cdot  \frac{1}{n + q}$ .

已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 1$ ， ${a}_{n} = 2{a}_{n - 1} + \frac{n + 2}{n\left( {n + 1}\right) }$ ( $n \geq  2$ ， $n \in  {N}^{ * }$ )，则数列 $\left\{  {a}_{n}\right\}$ 的通项公式 ${a}_{n} =$ ___.

【难度】 $\star   \star   \star   \star$

【答案】 $3 \cdot  {2}^{n - 2} - \frac{1}{n + 1}\left( {n \in  {N}^{ * }}\right)$

【解析】解: ${a}_{1} = 1,{a}_{n} = 2{a}_{n - 1} + \frac{n + 2}{n\left( {n + 1}\right) }\left( {n \geq  2, n \in  {N}^{ * }}\right)  = 2{a}_{n - 1} + \frac{n + 2}{n} - \frac{n + 2}{n + 1} = 2{a}_{n - 1} + \frac{2}{n} - \frac{1}{n + 1}$ ,

即为 ${a}_{n} + \frac{1}{n + 1} = 2\left( {{a}_{n - 1} + \frac{1}{n}}\right)$ ,设 ${b}_{n} = {a}_{n} + \frac{1}{n + 1}$ ,则 ${b}_{n} = 2{b}_{n - 1}$ ,则 ${b}_{n} = {b}_{1}{q}^{n - 1} = \left( {1 + \frac{1}{2}}\right)  \cdot  {2}^{n - 1}$ ,

可得 ${a}_{n} + \frac{1}{n + 1} = 3 \cdot  {2}^{n - 2}$ ,即有 ${a}_{n} = 3 \cdot  {2}^{n - 2} - \frac{1}{n + 1}\left( {n \in  {N}^{ * }}\right)$ .

故答案为: $3 \cdot  {2}^{n - 2} - \frac{1}{n + 1}\left( {n \in  {N}^{ * }}\right)$ .

## 二、选择题

7、已知数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 1$ ， ${a}_{n + 1} - {a}_{n} = \frac{1}{n\left( {n + 1}\right) }$ ，则 ${a}_{2020}$ 等于( )

A. $\frac{2019}{2020}$ B. $\frac{4039}{2020}$ C. $\frac{2020}{2021}$ D. $\frac{4041}{2021}$

【难度】 $\star   \star   \star$

【答案】 $B$

【解析】解: 数列 $\left\{  {a}_{n}\right\}$ 中, ${a}_{1} = 1,{a}_{n + 1} - {a}_{n} = \frac{1}{n\left( {n + 1}\right) } = \frac{1}{n} - \frac{1}{n + 1}$ ,

所以 ${a}_{n} - {a}_{n - 1} = \frac{1}{n - 1} - \frac{1}{n},{a}_{n - 1} - {a}_{n - 2} = \frac{1}{n - 2} - \frac{1}{n - 1},\ldots ,{a}_{2} - {a}_{1} = \frac{1}{1} - \frac{1}{2}$ ,

所以 ${a}_{n} - {a}_{1} = \frac{1}{n - 1} - \frac{1}{n} + \frac{1}{n - 2} - \frac{1}{n - 1} + \ldots  + 1 - \frac{1}{2} = 1 - \frac{1}{n}$ ,则: ${a}_{n} = 2 - \frac{1}{n}$ ,

所以 ${a}_{2020} = 2 - \frac{1}{2020} = \frac{4039}{2020}$ . 故选: $B$ .

8、在各项均为正数的数列 $\left\{  {a}_{n}\right\}$ 中, ${S}_{n}$ 是其前 $n$ 项和, $n{a}_{n + 1}^{2} = \left( {n + 1}\right) {a}_{n}^{2} + {a}_{n}{a}_{n + 1}$ 且 ${a}_{3} = \pi$ ,则 $\tan {S}_{4}$ 的值等于 ( )

A. $- \sqrt{3}$

B. $- \frac{\sqrt{3}}{3}$ C. $\frac{\sqrt{3}}{3}$ D. $\sqrt{3}$

【难度】 $\star   \star   \star$

【答案】 $D$

【解析】解: $n{a}_{n + 1}^{2} = \left( {n + 1}\right) {a}_{n}^{2} + {a}_{n}{a}_{n + 1}$ ,化为: $\left\lbrack  {n{a}_{n + 1} - \left( {n + 1}\right) {a}_{n}}\right\rbrack  \left( {{a}_{n + 1} + {a}_{n}}\right)  = 0$ ,

$\because$ 数列 $\left\{  {a}_{n}\right\}$ 中各项均为正数, $\therefore n{a}_{n + 1} - \left( {n + 1}\right) {a}_{n} = 0,\therefore \frac{{a}_{n + 1}}{n + 1} = \frac{{a}_{n}}{n} = \ldots \ldots  = \frac{{a}_{3}}{3} = \frac{\pi }{3}$ ,

解得 ${a}_{n} = \frac{n\pi }{3},\therefore {S}_{4} = \frac{\pi }{3} \times  \left( {1 + 2 + 3 + 4}\right)  = \frac{10\pi }{3},\therefore \tan {S}_{4} = \tan \frac{10\pi }{3} = \tan \frac{\pi }{3} = \sqrt{3}$ .

故选: $D$ .

9、已知正数数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{n + 1} \geq  2{a}_{n} + 1$ ，且 ${a}_{n} < {2}^{n + 1}$ 对 $n \in  {N}^{ * }$ 恒成立，则 ${a}_{1}$ 的范围为( )

A. $\left\lbrack  {1,3}\right\rbrack$ B. $\left( {1,3}\right)$ C. $(0,3\rbrack$ D. $\left( {0,4}\right)$

【难度】 $\star   \star   \star   \star$

【答案】 $C$

【解析】解: 正数数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{n + 1} \geq  2{a}_{n} + 1$ ,可得 $1 + {a}_{n + 1} \geq  2\left( {{a}_{n} + 1}\right)$ ,

设 ${b}_{n} = 1 + {a}_{n},\left( {{a}_{n} > 0,{b}_{n} > 1}\right)$ 即有 ${b}_{2} \geq  2{b}_{1},{b}_{3} \geq  2{b}_{2},\ldots ,{b}_{n} \geq  2{b}_{n - 1}$ ,

累乘可得 ${b}_{n} \geq  {b}_{1} \cdot  {2}^{n - 1}$ ,可得 $1 + {a}_{n} \geq  \left( {1 + {a}_{1}}\right)  \cdot  {2}^{n - 1}$ ,又 ${a}_{n} < {2}^{n + 1}$ 对 $n \in  N$ * 恒成立,

可得 $1 + {2}^{n + 1} > 1 + {a}_{n} \geq  \left( {1 + {a}_{1}}\right)  \cdot  {2}^{n - 1}$ ,即有 $1 + {2}^{n + 1} > \left( {1 + {a}_{1}}\right)  \cdot  {2}^{n - 1}$ ,可得 ${a}_{1} < 3 + \frac{1}{{2}^{n - 1}}$ 恒成立,

由 $3 + \frac{1}{{2}^{n - 1}} > 3$ ,可得 $0 < {a}_{1} \leq  3$ . 故选: $C$ .

10、已知“整数对”按如下规律排列:(1,1)，(1,2)，(2,1)，(1,3)，(2,2)，(3,1)，(1,4)，(2,3)，(3,2)，(4,1)，...，则第 68 个“整数对”为( )

A. $\left( {1,{12}}\right)$ B. $\left( {3,{10}}\right)$ C. $\left( {2,{11}}\right)$ D. $\left( {3,9}\right)$

【难度】 $\star   \star   \star   \star$

【答案】C

【解析】设“整数对”为 $\left( {m, n}\right) \left( {m, n \in  {N}^{ * }}\right)$ ,由已知可知点列的排列规律是 $m + n$ 的和从 2 开始,依次是 $3,4,\ldots$ ,其中 $m$ 依次增大.

当 $m + n = 2$ 时只有 1 个 $\left( {1,1}\right)$ ;

当 $m + n = 3$ 时有 2 个 $\left( {1,2}\right) ,\left( {2,1}\right)$ ;

当 $m + n = 4$ 时有 3 个 $\left( {1,3}\right) ,\left( {2,2}\right) ,\left( {3.1}\right) ;\ldots$ ;

当 $m + n = {12}$ 时有 11 个 $\left( {1.11}\right) ,\left( {2.10}\right) ,\ldots \left( {11.1}\right)$ ;

其上面共有 $1 + 2 + 3 + \cdots  + {11} = \frac{{11} \times  \left( {1 + {11}}\right) }{2} = {66}$ 个数对.

所以第 67 个“整数对”为(1.12)，第 68 个“整数对”为(2.11)，故选:C.

## 三、解答题

11、等差数列 $\left\{  {a}_{n}\right\}$ 的首项为 1,公差 $d \neq  0$ ,且 ${a}_{1}\text{ 、 }{a}_{2}\text{ 、 }{a}_{5}$ 成等比数列,数列 $\left\{  {b}_{n}\right\}$ 满足 ${b}_{1} = 1$ 且 $\frac{1}{{b}_{n + 1}} = \frac{1}{{b}_{n}} - \frac{1}{{2}^{n}}\left( {n \in  {N}^{ * }}\right) .$

(1)求 ${a}_{n}$ 、 ${b}_{n}$ ；

(2)若 ${c}_{n} = \frac{{a}_{n}}{{b}_{n}}$ ，数列 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ .

① 求 ${S}_{n}$ ；

② 求使 ${S}_{n} > \frac{35}{8}$ 的最小正整数 $n$ .

【难度】 $\star   \star   \star   \star$

【答案】(1) ${a}_{n} = {2n} - 1,{b}_{n} = {2}^{n - 1}\left( {n \in  {N}^{ * }}\right)$ ; (2) ① $6 - \frac{{2n} + 3}{{2}^{n - 1}}$ ; ②4.

【解析】(1) 由已知得: ${\left( {a}_{1} + d\right) }^{2} = {a}_{1}\left( {{a}_{1} + {4d}}\right)$ ,又 ${a}_{1} = 1, d \neq  0$ ,

$\Rightarrow  d = 2, \Rightarrow  {a}_{n} = {2n} - 1$ ,

又 $\frac{1}{{b}_{n}} - \frac{1}{{b}_{n + 1}} = \frac{1}{{2}^{n}}$ ,当 $n \geq  2$ 时, $\left( {\frac{1}{{b}_{1}} - \frac{1}{{b}_{2}}}\right)  + \left( {\frac{1}{{b}_{2}} - \frac{1}{{b}_{3}}}\right)  + \cdots  + \left( {\frac{1}{{b}_{n - 1}} - \frac{1}{{b}_{n}}}\right)$

$= \frac{1}{2} + \frac{1}{{2}^{2}} + \cdots  + \frac{1}{{2}^{n - 1}} = \frac{\frac{1}{2}\left( {1 - \frac{1}{{2}^{n - 1}}}\right) }{1 - \frac{1}{2}} = 1 - \frac{1}{{2}^{n}} = \frac{1}{{b}_{1}} - \frac{1}{{b}_{n}},$

$\therefore {b}_{n} = {2}^{n - 1}$ ,又 ${b}_{1} = 1$ 也适合公式,故 ${b}_{n} = {2}^{n - 1}\left( {n \in  {N}^{ * }}\right)$ .

(2)① ${c}_{n} = \frac{{a}_{n}}{{b}_{n}} = \frac{{2n} - 1}{{2}^{n - 1}}$ ，

$\left. \begin{array}{l} {S}_{n} = 1 + \frac{3}{2} + \frac{5}{{2}^{2}} + \cdots  + \frac{{2n} - 1}{{2}^{n - 1}} \\  \frac{1}{2}{S}_{n} = \frac{1}{2} + \frac{3}{{2}^{2}} + \cdots  + \frac{{2n} - 3}{{2}^{n - 1}} + \frac{{2n} - 1}{{2}^{n}} \end{array}\right\}$

$\Rightarrow  \frac{1}{2}{S}_{n} = 1 + 2\left( {\frac{1}{2} + \frac{1}{{2}^{2}} + \cdots  + \frac{1}{{2}^{n - 1}}}\right)  - \frac{{2n} - 1}{{2}^{n}}$

$\Rightarrow  {S}_{n} = 6 - \frac{{2n} + 3}{{2}^{n - 1}}$ .

②因为 ${c}_{n} > 0$ ，所以 ${S}_{n}$ 关于 $n$ 单调递增，

又 ${S}_{3} = \frac{15}{4} = \frac{30}{8} < \frac{35}{8},{S}_{4} = \frac{37}{8} > \frac{35}{8}$ ,

所以,使 ${S}_{n} > \frac{35}{8}$ 的最小正整数 $n = 4$ .

12、已知 $\overrightarrow{a} = \left( {{S}_{n},2}\right) ,\overrightarrow{b} = \left( {1,1 - {a}_{n}}\right)$ ,对任意 $n \in  {N}^{ * }$ ,有 $\overrightarrow{a} \bot  \overrightarrow{b}$ 成立.

(1)求 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)设 ${b}_{n + 1} = 2{b}_{n} - {2}^{n + 1},{b}_{1} = 8,{T}_{n}$ 是数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和，求正整数 $k$ ，使得对任意 $n \in  {N}^{ * },{T}_{k} \geq  {T}_{n}$ 恒成立;

(3)设 ${c}_{n} = \frac{{a}_{n + 1}}{\left( {1 + {a}_{n}}\right) \left( {1 + {a}_{n + 1}}\right) },{R}_{n}$ 是数列 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项和，若对任意 $n \in  {N}^{ * }$ 均有 ${R}_{n} < \lambda$ 恒成立，求 $\lambda$ 的最小值.

【难度】 $\star   \star   \star   \star$

【答案】见解析

【解析】解: (1) 由 $\overrightarrow{a} = \left( {{S}_{n},2}\right) ,\overrightarrow{b} = \left( {1,1 - {a}_{n}}\right)$ ,对任意 $n \in  {N}^{ * }$ ,有 $\overrightarrow{a} \bot  \overrightarrow{b}$ 成立,

得 $\overrightarrow{a} \cdot  \overrightarrow{b} = {S}_{n} + 2 - 2{a}_{n} = 0, n \geq  2$ 时, ${S}_{n - 1} + 2 - 2{a}_{n - 1} = 0$ ,

两式相减,得 ${a}_{n} - 2{a}_{n} + 2{a}_{n - 1} = 0$ ,故 ${a}_{n} = 2{a}_{n - 1}\left( {n \geq  2}\right)$ .

又 $n = 1$ 时, ${a}_{1} + 2 - 2{a}_{1} = 0,{a}_{1} = 2$ . 所以数列 $\left\{  {a}_{n}\right\}$ 是以 2 为首项,2 为公比的等比数列,

$\therefore$ 数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = {2}^{n}$ ;

(2) ${b}_{1} = 8,{b}_{n + 1} = 2{b}_{n} - {2}^{n + 1}$ ，即为 $\frac{{b}_{n + 1}}{{2}^{n + 1}} = \frac{{b}_{n}}{{2}^{n}} - 1$ ，可得 $\left\{  \frac{{b}_{n}}{{2}^{n}}\right\}$ 为首项为4，公差为 -1 的等差数列，

则 $\frac{{b}_{n}}{{2}^{n}} = 4 - \left( {n - 1}\right)  = 5 - n$ ,即有 ${b}_{n} = \left( {5 - n}\right)  \cdot  {2}^{n}$ ,

${T}_{n} = 4 \cdot  2 + 3 \cdot  4 + 2 \cdot  8 + \ldots  + \left( {5 - n}\right)  \cdot  {2}^{n},$

$2{T}_{n} = 4 \cdot  4 + 3 \cdot  8 + 2 \cdot  {16} + \ldots  + \left( {5 - n}\right)  \cdot  {2}^{n + 1},$

两式相减可得 $- {T}_{n} = 8 - 4 - 8 + \ldots  - {2}^{n} - \left( {5 - n}\right)  \cdot  {2}^{n + 1} = 8 - \frac{4\left( {1 - {2}^{n - 1}}\right) }{1 - 2} - \left( {5 - n}\right)  \cdot  {2}^{n + 1}$ ,

化简可得 ${T}_{n} =  - {12} + \left( {6 - n}\right)  \cdot  {2}^{n + 1}$ ,

由 $f\left( n\right)  = \left( {6 - n}\right)  \cdot  {2}^{n + 1}$ ,当 $1 \leq  n \leq  6$ 时, $f\left( n\right)  \geq  0, n \geq  7$ 时, $f\left( n\right)  < 0$ ,

可得 $f\left( 1\right)  = {20}, f\left( 2\right)  = {32}, f\left( 3\right)  = {48}, f\left( 4\right)  = {64}, f\left( 5\right)  = {64}, f\left( 6\right)  = 0$ ,则 $n = 4, f\left( n\right)$ 取得最大值 64,可得 ${T}_{n}$ 的最大值为 ${64} - {12} = {52}$ ,

则存在正整数 $k$ ,且为 4,使得对任意 $n \in  {N}^{ * },{T}_{k} \geq  {T}_{n}$ 恒成立;

(3) ${c}_{n} = \frac{{a}_{n + 1}}{\left( {1 + {a}_{n}}\right) \left( {1 + {a}_{n + 1}}\right) } = \frac{{2}^{n + 1}}{\left( {{2}^{n} + 1}\right) \left( {{2}^{n + 1} + 1}\right) } = 2\left( {\frac{1}{{2}^{n} + 1} - \frac{1}{{2}^{n + 1} + 1}}\right)$ ,

可得 ${R}_{n} = 2\left( {\frac{1}{3} - \frac{1}{{2}^{2} + 1} + \frac{1}{{2}^{2} + 1} - \frac{1}{{2}^{3} + 1} + \ldots  + \frac{1}{{2}^{n} + 1} - \frac{1}{{2}^{n + 1} + 1}}\right)  = 2\left( {\frac{1}{3} - \frac{1}{{2}^{n + 1} + 1}}\right)  < \frac{2}{3}$ ,

对任意 $n \in  {N}^{ * }$ 均有 ${R}_{n} < \lambda$ 恒成立,可得 $\lambda  \geq  \frac{2}{3}$ ,

即 $\lambda$ 的最小值为 $\frac{2}{3}$ .
