## 数列的函数性质

<table><tr><td>教学目标</td><td>1、熟悉等差等比数列的基本性质并能利用其解决实际问题; <br> 2、数列的单调性及数列的最值问题; <br> 3、了解等差等比数列前 $\mathrm{n}$ 项和的思想,对于等比数列前 $\mathrm{n}$ 项和问题注意分类讨论.</td></tr><tr><td>重点</td><td>1、数列的单调性与最值； <br> 2、等差等比数列的性质及其应用.</td></tr><tr><td>难 点</td><td>1、数列的单调性，周期性 <br> 2、利用周期进行有关计算.</td></tr></table>

## (一) 数列的单调性与最值

## 知识梳理

## 数列的单调性

数列单调性是数列最重要的性质之一, 也是解决数列综合问题的最重要的方法之一, 判断数列单调性的方法常用的有二种, 一种是利用数列对应的函数的单调性; 另一种是对数列的前后项作差 (或作商) 比较法判断；而数列单调性的应用更为重要。

## 1、判断数列单调性:

${a}_{n + 1} - {a}_{n} > 0 \Leftrightarrow$ 数列 $\left\{  {a}_{n}\right\}$ 是递增数列

${a}_{n + 1} - {a}_{n} = 0 \Leftrightarrow$ 数列 $\left\{  {a}_{n}\right\}$ 是常数列

${a}_{n + 1} - {a}_{n} < 0 \Leftrightarrow$ 数列 $\left\{  {a}_{n}\right\}$ 是递减数列

<table><tr><td></td><td>$\frac{{a}_{n + 1}}{{a}_{n}} > 1$</td><td>$\frac{{a}_{n + 1}}{{a}_{n}} < 1$</td><td>$\frac{{a}_{n + 1}}{{a}_{n}} = 1$</td></tr><tr><td>${a}_{n} > 0$</td><td>递增数列</td><td>递减数列</td><td>常数列</td></tr><tr><td>${a}_{n} < 0$</td><td>递减数列</td><td>递增数列</td><td>常数列</td></tr></table>

## 2、数列单调性的应用: 求数列最大项和最小项

方法一:利用判断函数增减性的方法，先判断数列的增减情况，再求数列的最大项或最小项。

方法二: 设 ${a}_{n}$ 是最大项,则有 $\left\{  \begin{array}{l} {a}_{n} \geq  {a}_{n - 1} \\  {a}_{n} \geq  {a}_{n + 1} \end{array}\right.$ 对任意的 $n \in  {N}^{ * }$ 且 $n \geq  2$ 均成立,解不等式组即可。 方法三:利用做差(或作商)，研究相邻项间的关系，进而求得数列的最大项或最小项。

## 例题精讲

【例 1】( 1 )已知等差数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ， ${a}_{6} + {a}_{8} = 6$ ， ${S}_{9} - {S}_{6} = 3$ ，则使 ${S}_{n}$ 取得最大值时 $n$ 的值为( )

A. 5 B. 6 C. 7 D. 8

【难度】★★★

【答案】D

【解析】由题意,根据等差数列的性质,可得 ${a}_{6} + {a}_{8} = 2{a}_{7} = 6$ ,即 ${a}_{7} = 3$

由 ${S}_{9} - {S}_{6} = {a}_{7} + {a}_{8} + {a}_{9} = 3{a}_{8} = 3$ ,即 ${a}_{8} = 1$ ,所以等差数列的公差为 $d = {a}_{8} - {a}_{7} =  - 2$ ,即数列 $\left\{  {a}_{n}\right\}$ 为递减数列。

又由 ${a}_{7} = {a}_{1} + {6d} = {a}_{1} - {12} = 3$ ，解得 ${a}_{1} = {15}$ ，

所以数列的通项公式为 ${a}_{n} = {a}_{1} + \left( {n - 1}\right) d = {15} + \left( {n - 1}\right)  \times  \left( {-2}\right)  = {17} - {2n}$ ,

令 ${a}_{n} = {17} - {2n} \geq  0$ ,解得 $n \leq  8 + \frac{1}{2}$ ,所以使得 ${S}_{n}$ 取得最大值时 $n$ 的值为 8,故选 $D$ .

(2)设 ${S}_{n}$ 是公差为 $d\left( {d \neq  0}\right)$ 的无穷等差数列 $\left\{  {a}_{n}\right\}$ 的前 $\mathrm{n}$ 项和，则下列命题错误的是:( )

A 若 $d < 0$ ,则数列 $\left\{  {S}_{n}\right\}$ 有最大项 B 若数列 $\left\{  {S}_{n}\right\}$ 有最大项,则 $d < 0$

C 若数列 $\left\{  {S}_{n}\right\}$ 是递增数列,则对任意的 $n \in  {N}^{ * }$ ,均有 ${S}_{n} > 0$

D 若对任意的 $n \in  {N}^{ * }$ ,均有 ${S}_{n} > 0$ ,则数列 $\left\{  {S}_{n}\right\}$ 是递增数列

【难度】 $\star   \star   \star$

【答案】C

【解析】C 反例: $- 1,0,1,2,3\ldots$ 。

(3)已知 ${S}_{n}$ 是等差数列 $\left\{  {a}_{n}\right\}  \left( {n \in  {N}^{ * }}\right)$ 的前 $\mathrm{n}$ 项和,且 ${S}_{5} < {S}_{6},{S}_{6} = {S}_{7} > {S}_{8}$ ,则下列结论错误的是 ( )

A. ${S}_{6}$ 和 ${S}_{7}$ 均为 ${S}_{n}$ 的最大值. B. ${a}_{7} = 0$ ;

C. 公差 $d < 0$ ； D. ${S}_{9} > {S}_{5}$ ;

【难度】★★★

【答案】D

【解析】等差数列求和公式是二次函数, 根据二次函数的对称性

【例 2】若数列 $\left\{  {a}_{n}\right\}$ 是等比数列,则“首项 ${a}_{1} > 0$ ，且公比 $q > 1$ ”是“数列 $\left\{  {a}_{n}\right\}$ 单调递增”的( )

A. 充要条件 B. 充分不必要条件

C. 必要不充分条件 D. 非充分非必要条件

【难度】 $\star   \star   \star$

【答案】B

【解析】数列 $\left\{  {a}_{n}\right\}$ 是等比数列,首项 ${a}_{1} > 0$ ,且公比 $q > 1$ ,所以数列 ${a}_{n} = {a}_{1}{q}^{n - 1} > 0$ ,且 ${a}_{n + 1} = {a}_{n}q > {a}_{n}$ , 所以得到数列 $\left\{  {a}_{n}\right\}$ 单调递增;

因为数列 $\left\{  {a}_{n}\right\}$ 单调递增,可以得到首项 ${a}_{1} > 0$ ,且公比 $q > 1$ ,也可以得到 ${a}_{1} < 0$ ,且公比 $0 < q < 1$ . 所以“首项 ${a}_{1} > 0$ ，且公比 $q > 1$ ”是“数列 $\left\{  {a}_{n}\right\}$ 单调递增”的充分不必要条件.

故选: B.

【例 3】已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{n + 1} = {a}_{n} + {2n}$ ，且 ${a}_{1} = {33}$ ，则 $\frac{{a}_{n}}{n}$ 的最小值为( )

A. 21 B. 10

C. $\frac{21}{2}$ D. $\frac{17}{2}$

【难度】 $\star   \star   \star$

【答案】C

【解析】 ${a}_{n} = \left( {{a}_{n} - {a}_{n - 1}}\right)  + \left( {{a}_{n - 1} - {a}_{n - 2}}\right)  + \ldots  + \left( {{a}_{2} - {a}_{1}}\right)  + {a}_{1}$

$= 2\left\lbrack  {1 + 2 + \ldots  + \left( {n - 1}\right) }\right\rbrack   + {33} = {33} + {n}^{2} - n$ ,所以 $\frac{{a}_{n}}{n} = \frac{33}{n} + n - 1$ ,设 $f\left( n\right)  = \frac{33}{n} + n - 1$ ,由对勾函数的性质可知, $f\left( n\right)$ 在 $\left( {0,\sqrt{33}}\right)$ 上单调递减,在 $\left( {\sqrt{33}, + \infty }\right)$ 上单调递减,又因为 $n \in  {\mathbf{N}}_{ + }$ ,所以当 $n = 5$ 或 6 时 $f\left( n\right)$ 可能取到最小值.,又因为 $\frac{{a}_{5}}{5} = \frac{53}{5},\frac{{a}_{6}}{6} = \frac{63}{6} = \frac{21}{2}$ ,所以 $\frac{{a}_{n}}{n}$ 的最小值为 $\frac{{a}_{6}}{6} = \frac{21}{2}$ ,故选 C.

【例 4】已知数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = {\left( \frac{4}{9}\right) }^{n - 1} - {\left( \frac{2}{3}\right) }^{n - 1}$ ,则数列 $\left\{  {a}_{n}\right\}$ (   )

A. 有最大项，没有最小项 B. 有最小项，没有最大项

C. 既有最大项又有最小项 D. 既没有最大项也没有最小项

【难度】 $\star   \star   \star$

【答案】C

【解析】换元法,注意新元的范围

【例 5】已知 ${a}_{n} = \frac{n - \sqrt{2018}}{n - \sqrt{2019}}\left( {n \in  {N}^{ * }}\right)$ ,则数列 $\left\{  {a}_{n}\right\}$ 的前 50 项中最小项和最大项分别是 ( )

A. ${a}_{1},{a}_{50}$ B. ${a}_{1},{a}_{44}$ C. ${a}_{45},{a}_{50}$ D. ${a}_{44},{a}_{45}$

【难度】 $\star   \star   \star$

【答案】D

【解析】解: ${a}_{n} = \frac{n - \sqrt{2018}}{n - \sqrt{2019}} = 1 + \frac{\sqrt{2019} - \sqrt{2018}}{n - \sqrt{2019}}$

$\because {44}^{2} = {1936},{45}^{2} = {2025}$ ,

$\therefore n \leq  {44}$ 时,数列 $\left\{  {a}_{n}\right\}$ 单调递增,且 ${a}_{n} > 0;n \geq  {45}$ 时,数列 $\left\{  {a}_{n}\right\}$ 单调递增,且 ${a}_{n} < 1$ .

$\therefore$ 在数列 $\left\{  {a}_{n}\right\}$ 的前 50 项中最小项和最大项分别是 ${a}_{44},{a}_{45}$ .

故选: $D$ .

【例 6】已知数列 $\left\{  {a}_{n}\right\}$ 为等差数列,若 $\frac{{a}_{5}}{{a}_{6}} <  - 1$ ,则数列 $\left\{  \left| {a}_{n}\right| \right\}$ 的最小项是第___项

【难度】 $\star   \star   \star$

【答案】 6

【解析】由 $\frac{{a}_{5}}{{a}_{6}} <  - 1$ 得,若 ${a}_{6} > 0$ ,则 ${a}_{5} <  - {a}_{6} < 0$ ,此时等差数列为递增数列, $\left| {a}_{5}\right|  > \left| {a}_{6}\right|$ ,此时 $\left\{  \left| {a}_{n}\right| \right\}$ 中第 6 项最小; 若 ${a}_{6} < 0$ ,则 ${a}_{5} >  - {a}_{6} > 0$ ,此时等差数列为递减数列, $\left| {a}_{5}\right|  > \left| {a}_{6}\right|$ ,仍然有 $\left\{  \left| {a}_{n}\right| \right\}$ 中第 6 项最小,故 $\left\{  \left| {a}_{n}\right| \right\}$ 中的最小项是第 6 项。

【例 7】数列 $\left\{  {\left( {n + 3}\right) {\left( \frac{8}{9}\right) }^{n}}\right\}$ 的最大项为第 $k$ 项,则 $k =$ (   )

A. 4 或 5 B. 5 C. 5 或 6 D. 6

【难度】 $\star   \star   \star$

【答案】C

【解析】解: ${a}_{n + 1} - {a}_{n} = \left( {n + 4}\right) {\left( \frac{8}{9}\right) }^{n + 1} - \left( {n + 3}\right)  \cdot  {\left( \frac{8}{9}\right) }^{n} = {\left( \frac{8}{9}\right) }^{n} \cdot  \frac{5 - n}{9},{a}_{5} = {a}_{6}$ .

可得: $n \leq  5$ 时,数列 $\left\{  {\left( {n + 3}\right) {\left( \frac{8}{9}\right) }^{n}}\right\}$ 单调递增; $n \geq  6$ 数列 $\left\{  {\left( {n + 3}\right) {\left( \frac{8}{9}\right) }^{n}}\right\}$ 单调递减.

$\therefore n = 5,6$ 时,此数列取得最大值,

故选: $C$ .

【例 8】在数列 $\left\{  {a}_{n}\right\}$ 中 ${a}_{1} = 0,{a}_{n} - {a}_{n - 1} + 5 = 2\left( {n + 2}\right) \left( {n \in  {N}^{ * }, n \geq  2}\right)$ ,若数列 $\left\{  {b}_{n}\right\}$ 满足

${b}_{n} = n\sqrt{{a}_{n + 1} + 1} \cdot  {\left( \frac{8}{11}\right) }^{n}$ ，则数列 $\left\{  {b}_{n}\right\}$ 的最大项为( )

A. 第 5 项 B. 第 6 项 C. 第 7 项 D. 第 8 项

【难度】 $\star   \star   \star$

【答案】B

【解析】数列 $\left\{  {a}_{n}\right\}$ 中, ${a}_{1} = 0,{a}_{n} - {a}_{n - 1} + 5 = 2\left( {n + 2}\right)$ ,得到: ${a}_{n} - {a}_{n - 1} = {2n} - 1$ ,

${a}_{n - 1} - {a}_{n - 2} = 2\left( {n - 1}\right)  - 1,$

...,

${a}_{2} - {a}_{1} = 2 \times  2 - 1,$

上边 $\left( {n - 1}\right)$ 个式子相加得: ${a}_{n} - {a}_{1} = 2\left( {2 + 3 + \ldots  + n}\right)  - \left( {n - 1}\right)$ ，解得: ${a}_{n} = {n}^{2} - 1$ .

当 $n = 1$ 时,首项符合通项. 故: ${a}_{n} = {n}^{2} - 1$ .

数列 $\left\{  {b}_{n}\right\}$ 满足 ${b}_{n} = n\sqrt{{a}_{n + 1} + 1}{\left( \frac{8}{11}\right) }^{n}$ ，则 ${b}_{n} = n\left( {n + 1}\right) {\left( \frac{8}{11}\right) }^{n - 1}$ ，

由于 $\left\{  \begin{array}{l} {b}_{n} \geq  {b}_{n - 1} \\  {b}_{n} \geq  {b}_{n + 1} \end{array}\right.$ ,故: $\left\{  \begin{array}{l} \left( {{n}^{2} + n}\right)  \cdot  {\left( \frac{8}{11}\right) }^{n - 1} \geq  \left( {{n}^{2} - n}\right)  \cdot  {\left( \frac{8}{11}\right) }^{n - 2} \\  \left( {{n}^{2} + n}\right)  \cdot  {\left( \frac{8}{11}\right) }^{n - 1} \geq  \left( {{n}^{2} + {3n} + 2}\right)  \cdot  {\left( \frac{8}{11}\right) }^{n}\;\text{ ,解得: }\frac{16}{3} \leq  n \leq  \frac{19}{3}\text{ , } \end{array}\right.$

由于 $n$ 是正整数,故 $n = 6$ . 故选 B.

【例 9】已知数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = {n}^{2} - {\lambda n}\left( {\lambda  \in  R}\right)$ ,且为单调递增数列,则实数 $\lambda$ 的取值范围是 ___.

【难度】 $\star   \star   \star$

【答案】 $\left( {-\infty ,3}\right)$

【解析】解: 根据题意,数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = {n}^{2} - {\lambda n}\left( {\lambda  \in  R}\right)$

若数列 $\left\{  {a}_{n}\right\}$ 是递增数列,必有 ${a}_{n + 1} - {a}_{n} = {\left( n + 1\right) }^{2} - \lambda \left( {n + 1}\right)  - \left( {{n}^{2} - {\lambda n}}\right)  = {2n} + 1 - \lambda  > 0$ 恒成立,

又由 $n \geq  2$ ,且 $n \in  Z$ ,则 ${2n} + 1 - \lambda  \geq  2 \times  1 + 1 - \lambda  = 3 - \lambda  > 0$ ,

必有 $\lambda  < 3$ ,

即实数 $\lambda$ 的取值范围是 $\left( {-\infty ,3}\right)$ .

故答案为: $\left( {-\infty ,3}\right)$

【例 10】已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 3,{a}_{n + 1} = \frac{3\left( {n + 1}\right) {a}_{n}}{n}\left( {n \in  {N}^{ * }}\right)$ ,若存在 $n \in  {N}^{ * }$ ,使得 ${a}_{n} - {3k} \cdot  {4}^{n} > 0$ 成立,则实数 $k$ 的取值范围是( )

A. $\left( {-\infty ,\frac{1}{4}}\right)$ B. $( - \infty ,0\rbrack$ C. $\left( {-\infty ,\frac{3}{8}}\right)$ D. $\left( {-\infty ,\frac{27}{64}}\right)$

【难度】 $\star   \star   \star$

【答案】D

【解析】 $\because {a}_{n + 1} = \frac{3\left( {n + 1}\right) {a}_{n}}{n}\left( {n \in  {N}^{ * }}\right) ,\therefore \frac{{a}_{n + 1}}{n + 1} = 3\frac{{a}_{n}}{n}$ ,记 ${b}_{n} = \frac{{a}_{n}}{n}$ ,则 $\left\{  {b}_{n}\right\}$ 是以 ${b}_{1} = 3, q = 3$ 的等比数列, $\therefore \; {b}_{n} = {3}^{n},\therefore {a}_{n} = n \cdot  {3}^{n},\because \exists n \in  {N}^{ * },{a}_{n} - {3k} \cdot  {4}^{n} > 0$ ,等价于 $\exists n \in  {N}^{ * },{3k} < n{\left( \frac{3}{4}\right) }^{n}$ ,即 ${3k} < {\left( n{\left( \frac{3}{4}\right) }^{n}\right) }_{\max }$ , 令 ${c}_{n} = n{\left( \frac{3}{4}\right) }^{n}$ ,则 ${c}_{n + 1} - {c}_{n} = \left( {n + 1}\right) {\left( \frac{3}{4}\right) }^{n + 1} - n{\left( \frac{3}{4}\right) }^{n} = {\left( \frac{3}{4}\right) }^{n} \cdot  \frac{3 - n}{4},\therefore n < 3$ 时, ${c}_{n + 1} > {c}_{n};n \geq  4$ 时, ${c}_{n + 1} < {c}_{n},\therefore {c}_{1} < {c}_{2} < {c}_{3} = {c}_{4} > {c}_{5} > {c}_{6}\cdots ,\therefore {\left( n{\left( \frac{3}{4}\right) }^{n}\right) }_{\max } = {c}_{3} = {c}_{4} = \frac{81}{64}$ . $\therefore k < \frac{27}{64},\therefore$ 实数 $k$ 的取值范围为 $\left( {-\infty ,\frac{27}{64}}\right)$ ,故选 D

【例 11】已知数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n}$ 满足, ${S}_{n} = 3{a}_{n} - 2$ . 数列 $\left\{  {n{a}_{n}}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ,则满足 ${T}_{n} > {100}$ 的最小的 $n$ 值为___.

【难度】 $\star   \star   \star$

【答案】7

【解析】根据题意,数列 $\left\{  {a}_{n}\right\}$ 满足 ${S}_{n} = 3{a}_{n} - 2$ ,①

当 $n \geq  2$ 时,有 ${S}_{n - 1} = 3{a}_{n - 1} - 2$ ,②,

①-②可得: ${a}_{n} = 3{a}_{n} - 3{a}_{n - 1}$ ，变形可得 $2{a}_{n} = 3{a}_{n - 1}$ ，

当 $n = 1$ 时，有 ${S}_{1} = {a}_{1} = 3{a}_{1} - 2$ ，解可得 ${a}_{1} = 1$ ，

则数列 $\left\{  {a}_{n}\right\}$ 是以 ${a}_{1} = 1$ 为首项,公比为 $\frac{3}{2}$ 的等比数列,则 ${a}_{n} = {\left( \frac{3}{2}\right) }^{n - 1}$ ,

数列 $\left\{  {n{a}_{n}}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ,则 ${T}_{n} = 1 + 2 \times  \frac{3}{2} + 3 \times  {\left( \frac{3}{2}\right) }^{2} + 4\ldots \ldots  + n \times  {\left( \frac{3}{2}\right) }^{n - 1}$ ,③

则有 $\frac{3}{2}{T}_{n} = \frac{3}{2} + 2 \times  {\left( \frac{3}{2}\right) }^{2} + 3 \times  {\left( \frac{3}{2}\right) }^{3} + \ldots \ldots  + n \times  {\left( \frac{3}{2}\right) }^{n}$ ,④

③ 一④可得: $- \frac{1}{2}{T}_{n} = 1 + \left( \frac{3}{2}\right)  + {\left( \frac{3}{2}\right) }^{2} + \ldots \ldots  \times  {\left( \frac{3}{2}\right) }^{n - 1} - n \times  {\left( \frac{3}{2}\right) }^{n} =  - 2\left( {1 - \frac{{3}^{n}}{{2}^{n}}}\right)  - n \times  {\left( \frac{3}{2}\right) }^{n}$ ,

变形可得: ${T}_{n} = 4 + \left( {{2n} - 4}\right)  \times  {\left( \frac{3}{2}\right) }^{n}$ ,

若 ${T}_{n} > {100}$ ,即 $4 + \left( {{2n} - 4}\right)  \times  {\left( \frac{3}{2}\right) }^{n} > {100}$ ,

分析可得: $n \geq  7$ ,故满足 ${T}_{n} > {100}$ 的最小的 $n$ 值为 7 ;

## 巩固训练

1、若数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = {2n} - 7$ ，则其前 $n$ 项和 ${S}_{n}$ 达到最小值时， $n =$ ___.

【难度】 $\star   \star$

【答案】 3

【解析】因为数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = {2n} - 7$ ,

令 ${a}_{n} \geq  0$ ,即 ${2n} - 7 \geq  0$ ,解得 $n \geq  \frac{7}{2}$ ,所以当 $1 \leq  n \leq  3, n \in  {N}^{ + }$ 时, ${a}_{n} < 0$ ,当 $n \geq  4, n \in  {N}^{ + }$ 时, ${a}_{n} > 0$ , 所以数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n}$ 达到最小值,此时 $n = 3$ .

2、已知数列 $\left\{  {a}_{n}\right\}$ 满足: ${a}_{1} > 0$ ， $3{a}_{n + 1} - {a}_{n} = 0$ ，则数列 $\left\{  {a}_{n}\right\}$ 是( )

A. 递增数列 B. 递减数列 C. 摆动数列 D. 不确定

【难度】★★★

【答案】B

【解析】因为 $3{a}_{n + 1} - {a}_{n} = 0$ ,所以 $\frac{{a}_{n + 1}}{{a}_{n}} = \frac{1}{3}$ ,所以数列 $\left\{  {a}_{n}\right\}$ 是等比数列所以 ${a}_{n} = {a}_{1} \times  {\left( \frac{1}{3}\right) }^{n - 1}$

又因为 ${a}_{1} > 0$ ,所以数列 $\left\{  {a}_{n}\right\}$ 是递减数列

3、已知函数 $f\left( x\right)$ 是定义在 $R$ 上的奇函数,且满足 $f\left( x\right)  =  - f\left( {x + 1}\right)$ ,数列 $\left\{  {a}_{n}\right\}$ 是首项为 1、公差为 1 的等差数列,则 $f\left( {a}_{1}\right)  + f\left( {a}_{2}\right)  + f\left( {a}_{3}\right)  + \cdots  + f\left( {a}_{51}\right)$ 的值为(   )

A. -1 B. 0 C. 1 D. 2

【难度】 $\star   \star   \star$

【答案】 $B$

【解析】解: $\because$ 函数 $f\left( x\right)$ 是定义在 $R$ 上的奇函数,

$\therefore f\left( x\right)  =  - f\left( {-x}\right)$ ,且 $f\left( 0\right)  = 0$ ,又 $\because f\left( x\right)  =  - f\left( {x + 1}\right)$ ,

$\therefore f\left( x\right)  =  - f\left( {x + 1}\right)  = f\left( {x + 2}\right)$ ,故周期为 2 .

令 $x = 0$ ,可得 $f\left( 0\right)  =  - f\left( 1\right)  = 0,\therefore f\left( 1\right)  = 0.\therefore f\left( 1\right)  = f\left( 2\right)  = f\left( 3\right)  = \cdots  = f\left( {51}\right)  = 0$ . $\because$ 数列 $\left\{  {a}_{n}\right\}$ 是首项为 1 、公差为 1 的等差数列, $\therefore {a}_{n} = n$ , $\therefore$ 则 $f\left( {a}_{1}\right)  + f\left( {a}_{2}\right)  + f\left( {a}_{3}\right)  + \cdots  + f\left( {a}_{51}\right)  = 0$ , 故选: $B$ .

4、已知数列 $\left\{  {a}_{n}\right\}$ 满足: ${a}_{n} = \left\{  {\begin{array}{l} \left( {3 - a}\right) n - 8, n \leq  6 \\  {a}^{n - 6}, n > 6 \end{array}\left( {n \in  {N}^{ * }}\right) }\right.$ ,且数列 $\left\{  {a}_{n}\right\}$ 是递增数列,则实数 $a$ 的取值范围是 ( )

A. $\left( {2,3}\right)$ B. $\left\lbrack  {2,3}\right)$ C. $\left( {\frac{10}{7},3}\right)$ D. $\left\lbrack  {2,3}\right\rbrack$

【难度】 $\star   \star   \star$

【答案】 $C$

【解析】解: 根据题意,数列 $\left\{  {a}_{n}\right\}$ 满足: ${a}_{n} = \left\{  {\begin{array}{l} \left( {3 - a}\right) n - 8, n \leq  6 \\  {a}^{n - 6}, n > 6 \end{array}\left( {n \in  {N}^{ * }}\right) }\right.$ ,且数列 $\left\{  {a}_{n}\right\}$ 是递增数列, 必有 $\left\{  \begin{array}{l} 3 - a > 0 \\  a > 1 \\  6\left( {3 - a}\right)  - 8 < {a}^{7 - 6} \end{array}\right.$ ,解可得 $\frac{10}{7} < a < 3$ ,即 $a$ 的取值范围为 $\left( {\frac{10}{7},3}\right)$ ,故选: $C$ .

5、已知 $F\left( x\right)  = f\left( {x + \frac{1}{2}}\right)  - 1$ 是 $R$ 上的奇函数, ${a}_{n} = f\left( 0\right)  + f\left( \frac{1}{n}\right)  + f\left( \frac{2}{n}\right)  + \ldots  + f\left( \frac{n - 1}{n}\right)  + f\left( 1\right) \left( {n \in  {N}^{ * }}\right)$ ,则数列 $\left\{  {a}_{n}\right\}$ 的通项公式为( )

A. ${a}_{n} = n - 1$ B. ${a}_{n} = n$ C. ${a}_{n} = n + 1$ D. ${a}_{n} = {n}^{2}$

【难度】 $\star   \star   \star$

【答案】 $C$

【解析】解: $F\left( x\right)  = f\left( {x + \frac{1}{2}}\right)  - 1$ 在 $R$ 上为奇函数,故 $F\left( {-x}\right)  =  - F\left( x\right)$ ,

代入得: $f\left( {\frac{1}{2} - x}\right)  + f\left( {\frac{1}{2} + x}\right)  = 2,\left( {x \in  R}\right)$ 当 $x = 0$ 时, $f\left( \frac{1}{2}\right)  = 1$ .

令 $t = \frac{1}{2} - x$ ,则 $\frac{1}{2} + x = 1 - t$ ,上式即为: $f\left( t\right)  + f\left( {1 - t}\right)  = 2$ .

当 $n$ 为偶数时:

${a}_{n} = f\left( 0\right)  + f\left( \frac{1}{n}\right)  + f\left( \frac{2}{n}\right)  + \ldots  + f\left( \frac{n - 1}{n}\right)  + f\left( 1\right) \left( {n \in  {N}^{ * }}\right) \; = \left\lbrack  {f\left( 0\right)  + f\left( 1\right) }\right\rbrack   + \left\lbrack  {f\left( \frac{1}{n}\right)  + f\left( \frac{n - 1}{n}\right) }\right\rbrack   + \ldots  + \left\lbrack  {f\left( \frac{\frac{1}{2}n - 1}{2}\right)  + f\left( \frac{\frac{1}{2}n + 1}{2}\right) }\right\rbrack   + f\left( \frac{1}{2}\right)  = 2 \times  \frac{n}{2} + 1 = n + 1$ .

当 $n$ 为奇数时:

${a}_{n} = f\left( 0\right)  + f\left( \frac{1}{n}\right)  + f\left( \frac{2}{n}\right)  + \ldots  + f\left( \frac{n - 1}{n}\right)  + f\left( 1\right) \;\left( {n \in  {N}^{ * }}\right)$

$= \left\lbrack  {f\left( 0\right)  + f\left( 1\right) }\right\rbrack   + \left\lbrack  {f\left( \frac{1}{n}\right)  + f\left( \frac{n - 1}{n}\right) }\right\rbrack   + \ldots  + \left\lbrack  {f\left( \frac{\frac{n - 1}{2}}{n}\right)  + f\left( \frac{\frac{n + 1}{2}}{n}\right) }\right\rbrack   = 2 \times  \frac{n + 1}{2} = n + 1.$

综上所述, ${a}_{n} = n + 1$ .

故选: $C$ .

## (二)数列的周期性

## 知识梳理

1、常见结论:

在数列 $\left\{  {a}_{n}\right\}$ 中,关于数列的周期性有以下常见结论;

1、若 ${a}_{n} = {a}_{n - k} + {a}_{n + k}\left( {n > k}\right)$ 恒成立,则 $T = {6k}$ 是 $\left\{  {a}_{n}\right\}$ 的一个周期;

2、若 ${a}_{n} \neq  0,{a}_{n} = {a}_{n - k} \cdot  {a}_{n + k}\left( {n > k}\right)$ 恒成立,则 $T = {6k}$ 是 $\left\{  {a}_{n}\right\}$ 的一个周期;

3、若 ${a}_{n + k} = \frac{{a}_{n} - 1}{{a}_{n} + 1}$ 恒成立,则 $T = {4k}$ 是 $\left\{  {a}_{n}\right\}$ 的一个周期;

4、若 ${a}_{n + p} = {a}_{p - n}$ 且 ${a}_{n + q} = {a}_{q - n}\left( {p > q > n, p, q \in  {N}^{ * }}\right)$ 恒成立,则 $T = 2\left( {p - q}\right)$ 是 $\left\{  {a}_{n}\right\}$ 的一个周期;

5、若 ${a}_{n + p} + {a}_{p - n} = m$ 且 ${a}_{n + q} + {a}_{q - n} = m\left( {p > q > n, p, q \in  {N}^{ * }}\right)$ 恒成立,则 $T = 2\left( {p - q}\right)$ 是 $\left\{  {a}_{n}\right\}$ 的一个周期;

6、若 ${a}_{n + p} = {a}_{p - n}$ 且 ${a}_{n + q} =  - {a}_{q - n}\left( {p > q > n, p, q \in  {N}^{ * }}\right)$ 恒成立,则 $T = 4\left( {p - q}\right)$ 是 $\left\{  {a}_{n}\right\}$ 的一个周期;

## 2、周期数列:

①某个数列与周期数列相乘，这样的数列求和，用 “并项法”

② ${\left( -1\right) }^{n}$ 是最常见的周期因子，此外 $\cos \frac{n\pi }{2}$ ， $\cos \frac{2n\pi }{3}$ ， ${\cos }^{2}\frac{n\pi }{3} - {\sin }^{2}\frac{n\pi }{3}$ 都是

③我们一般只 $\mathrm{n}$ 为周期整数倍的前 $\mathrm{n}$ 项和 ${S}_{n}$ ，其余的用 ${S}_{n} + {a}_{n + 1}$ 这样的方法计算

## 例题精讲

【例12】数列 $\left\{  {a}_{n}\right\}$ 满足满足 ${a}_{1} = 2,{a}_{n + 1} =  - \frac{1}{{a}_{n} + 1}$ ，则 ${a}_{2017}$ 的值为___.

【难度】 $\star   \star   \star$

【答案】 2

【解析】周期为3

【例 13】设等差数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和是 ${S}_{n}$ ,且 ${a}_{4} = {11},{S}_{5} = 4{a}_{3} + 8$ .

(1)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)若 ${b}_{n} = \left( {{a}_{n} + 1}\right) \cos {n\pi }$ ，记数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和是 ${T}_{n}$ ，求 ${T}_{2020}$ .

【难度】 $\star   \star   \star$

【答案】( 1 ) ${a}_{n} = {3n} - 1$ ；( 2 ) ${T}_{2020} = {3030}$ .

【解析】(1) 设等差数列 $\left\{  {a}_{n}\right\}$ 的公差为 $d$

所以 $\left\{  {\begin{array}{l} {a}_{4} = {11} \\  {S}_{5} = 4{a}_{3} + 8 \end{array} \Rightarrow  \left\{  \begin{array}{l} {a}_{1} + {3d} = {11} \\  5{a}_{1} + \frac{5 \times  {4d}}{2} = 4\left( {{a}_{1} + {2d}}\right)  + 8 \end{array}\right. }\right.$

解得 $\left\{  \begin{array}{l} {a}_{1} = 2 \\  d = 3 \end{array}\right.$ ,所以 ${a}_{n} = {3n} - 1$ ,

(2)由(1)可知 ${a}_{n} = {3n} - 1$ ，所以 ${b}_{n} = {3n}\cos {n\pi }$

所以当 $n$ 为奇数,则 ${b}_{n} =  - {3n}$ ; 当 $n$ 为偶数,则 ${b}_{n} = {3n}$

所以 ${T}_{2020} = {b}_{1} + {b}_{2} + \ldots  + {b}_{2020}$

所以 ${T}_{2020} = 3\left\lbrack  {\left( {-1 + 2}\right)  + \left( {-3 + 4}\right)  + \ldots  + \left( {-{2019} + {2020}}\right) }\right\rbrack$

所以 ${T}_{2020} = {3030}$

【例 14】对于数列 $\left\{  {a}_{n}\right\}$ ,若存在正整数 $T$ ,对于任意正整数 $n$ 都有 ${a}_{n + T} = {a}_{n}$ 成立,则称数列 $\left\{  {a}_{n}\right\}$ 是以 $T$ 为周期的周期数列. 设 ${b}_{1} = m\left( {0 < m < 1}\right)$ ,对任意正整数 $n$ 都有 ${b}_{n + 1} = \left\{  \begin{array}{l} {b}_{n} - 1\;\left( {{b}_{n} > 1}\right) , \\  \frac{1}{{b}_{n}}\;\left( {0 < {b}_{n} \leq  1}\right) , \end{array}\right.$ 若数列 $\left\{  {b}_{n}\right\}$ 是以 5 为周期的周期数列，则 $m$ 的值可以是___. (只要求填写满足条件的一个 $m$ 值即可)

【难度】 $\star   \star   \star$

【答案】 $\sqrt{5} - 2$ (或 $\frac{\sqrt{3} - 1}{2}$ ，或 $\sqrt{3} - 1$ ).

【解析】由题意可得,当 $0 < {b}_{n} \leq  1$ 时, ${b}_{n + 1} \geq  1$ ,所以要使 ${b}_{6} = {b}_{1} = m \in  \left( {0,1}\right)$ ,必有 ${b}_{5} > 1$ 。

且 $0 < {b}_{1} < 1$ ,所以 ${b}_{2} > 1$ ,所以情况有 3 种:

① $0 < {b}_{1} < 1,{b}_{2} > 1,{b}_{3} > 1,{b}_{4} > 1,{b}_{5} > 1$ ，则 ${b}_{6} = \frac{1}{m} - 4 = m$ ，解得 $m = \sqrt{5} - 2$

② $0 < {b}_{1} < 1,{b}_{2} > 1,{b}_{3} > 1,0 < {b}_{4} < 1,{b}_{5} > 1$ ，则 ${b}_{5} = \frac{1}{\frac{1}{m} - 2},{b}_{6} = \frac{1}{\frac{1}{m} - 2} - 1 = m$ ，解得 $m = \frac{\sqrt{3} - 1}{2}$

③ $0 < {b}_{1} < 1,{b}_{2} > 1,0 < {b}_{3} < 1,{b}_{4} > 1,{b}_{5} > 1$ ，则 ${b}_{4} = \frac{1}{\frac{1}{m} - 1},{b}_{6} = \frac{1}{\frac{1}{m} - 1} - 2 = m$ ，解得 $m = \sqrt{3} - 1$

## 巩固训练

1、已知无穷数列 $\left\{  {a}_{n}\right\}  ,{a}_{1} = 1,{a}_{2} = 2$ ,对任意 $n \in  {N}^{ * }$ ,有 ${a}_{n + 2} = {a}_{n}$ ,数列 $\left\{  {b}_{n}\right\}$ 满足 ${b}_{n + 1} - {b}_{n} = {a}_{n}\left( {n \in  {N}^{ * }}\right)$ , 若数列 $\left\{  \frac{{b}_{2n}}{n}\right\}$ 中的任意一项都在该数列中重复出现无数次，则满足要求的 ${b}_{1}$ 的值为___.

【难度】 $\star   \star   \star$

【答案】 2

【解析】解: ${a}_{1} = 1,{a}_{2} = 2$ ,对任意 $n \in  {N}^{ * }$ ,有 ${a}_{n + 2} = {a}_{n}$ ,

$\therefore {a}_{n} = \left\{  {\begin{array}{l} 1, n\text{ 为奇数 } \\  2, n\text{ 为偶数 } \end{array},\;\therefore {b}_{n + 1} - {b}_{n} = {a}_{n} = \left\{  \begin{array}{l} 1, n\text{ 为奇数 } \\  2, n\text{ 为偶数 } \end{array}\right. }\right.$ ,

${b}_{1} = {b}_{2},\;{b}_{2} = {b}_{1} + 1,\;{b}_{3} = {b}_{1} + 3,\;{b}_{4} = {b}_{1} + 4,\;{b}_{5} = {b}_{1} + 6,\;{b}_{6} = {b}_{1} + 7,\;\ldots ,$

$\therefore$ 数列 $\left\{  {b}_{2n}\right\}$ 是以 ${b}_{1} + 1$ 为首项,公差为 3 的等差数列,

$\therefore {b}_{2n} = {b}_{1} + {3n} - 2,\frac{{b}_{2n}}{n} = \frac{{b}_{1} + {3n} - 2}{n}$ ,

$\because$ 数列 $\left\{  \frac{{b}_{2n}}{n}\right\}$ 中的任意一项都在该数列中重复出现无数次, $\therefore \frac{{b}_{1} - 2}{n} + 3$ 应该为常数,

$\therefore {b}_{1} = 2$ ,故答案为: 2

2、数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,若 ${a}_{n} = 1 + n\cos \frac{n\pi }{2}\left( {n \in  {N}^{ * }}\right)$ ,则 ${S}_{2014} =$ ___.

【难度】 $\star   \star   \star$

【答案】 1006

【解析】: $\cos \frac{n\pi }{2} = 0, - 1,0,1\cdots$ ,故当 $n = {4k}$ 时,考虑连续的 4 项:

${a}_{n - 3} + {a}_{n - 2} + {a}_{n - 1} + {a}_{n} = 0 \times  \left( {n - 3}\right)  + \left( {-1}\right)  \times  \left( {n - 2}\right)  + 0 \times  \left( {n - 1}\right)  + 1 \times  n + 4 = 6$

当 $\mathbf{n}$ 是 4 的倍数时,连续 4 个并为 1 组,每组和为 6,其 $\frac{n}{4}$ 组, ${S}_{n} = \frac{3}{2}n$

${S}_{2014} = {S}_{2012} + {a}_{2013} + {a}_{2014} = \frac{3}{2} \times  {2012} + \left( {1 + 0 \times  {2013}}\right)  + \left( {1 + \left( {-1}\right)  \times  {2014}}\right)  = {1006}$

3、若数列 $\left\{  {a}_{n}\right\}$ 满足: 存在正整数 $T$ ,对于任意正整数 $n$ 都有 ${a}_{n + T} = {a}_{n}$ 成立,则称数列 $\left\{  {a}_{n}\right\}$ 为周期数列,周期为 $T$ . 已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = m\left( {m > 0}\right) ,{a}_{n + 1} = \left\{  \begin{array}{l} {a}_{n} - 1,{a}_{n} > 1 \\  \frac{1}{{a}_{n}},0 < {a}_{n} \leq  1 \end{array}\right.$ ,若 ${a}_{3} = 4$ ,则 $m$ 的所有可能取值为 ( )

A. $\left\{  {6,\frac{5}{4}}\right\}$ B. $\left\{  {6,\frac{5}{4},\frac{2}{5}}\right\}$ C. $\left\{  {6,\frac{5}{4},\frac{1}{5}}\right\}$ D. $\left\{  {6,\frac{1}{5}}\right\}$

【难度】 $\star   \star   \star$

【答案】 $C$

【解析】解: 数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = m\left( {m > 0}\right) ,{a}_{n + 1} = \left\{  \begin{array}{l} {a}_{n} - 1,{a}_{n} > 1 \\  \frac{1}{{a}_{n}},0 < {a}_{n} \leq  1 \end{array}\right.$ , ${a}_{3} = 4$ ,

① 若 $m > 2$ ,则 ${a}_{2} = m - 1 > 1,\therefore {a}_{3} = m - 2 = 4$ ,解得 $m = 6$ .

② 若 $m = 2$ ，则 ${a}_{2} = m - 1 = 1$ ， $\therefore {a}_{3} = \frac{1}{{a}_{2}} = 1 \neq  4$ ，舍去.

③ 若 $1 < m < 2$ ，则 ${a}_{2} = m - 1 \in  \left( {0,1}\right)$ ， $\therefore {a}_{3} = \frac{1}{m - 1} = 4$ ，解得 $m = \frac{5}{4}$ .

④若 $m = 1$ ，则 ${a}_{2} = \frac{1}{{a}_{1}} = 1$ ， $\therefore {a}_{3} = \frac{1}{{a}_{2}} \neq  4$ ，舍去.

⑤ 若 $0 < m < 1$ ，则 ${a}_{2} = \frac{1}{{a}_{1}} = \frac{1}{m} > 1$ ， $\therefore {a}_{3} = {a}_{2} - 1 = \frac{1}{m} - 1 = 4$ ，解得 $m = \frac{1}{5}$ .

综上可得: $m \in  \left\{  {6,\frac{5}{4},\frac{1}{5}}\right\}$ . 故选: $C$ .

4、数列 $\left\{  {a}_{n}\right\}$ 的通项公式 ${a}_{n} = n\cos \frac{n\pi }{2} + 1$ ，前 $n$ 项和为 ${S}_{n}$ ，则 ${S}_{2012} =$ ___.

【难度】 $\star   \star   \star$

【答案】3022

【解析】根据余弦的周期性

## 实战演练

一、填空题

1、数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,若 ${a}_{n + 1} = \frac{1}{1 - {a}_{n}}\left( {n \in  {N}^{ * }}\right) ,{a}_{1} = 2$ ,则 ${a}_{2022} =$ ___.

【难度】 $\star   \star   \star$

【答案】 $\frac{1}{2}$

【解析】解: $\because {a}_{n + 1} = \frac{1}{1 - {a}_{n}}\left( {n \in  {N}^{ * }}\right) ,{a}_{1} = 2\therefore {a}_{2} = \frac{1}{1 - 2} =  - 1,{a}_{3} = \frac{1}{1 - \left( {-1}\right) } = \frac{1}{2},{a}_{4} = \frac{1}{1 - \frac{1}{2}} = 2,\ldots$ , $\therefore {a}_{n + 3} = {a}_{n}$ ,则 ${a}_{2022} = {a}_{{673} \times  3 + 3} = {a}_{3} = \frac{1}{2}$ ,

故答案为: $\frac{1}{2}$ .

2、已知数列 $\left\{  {a}_{n}\right\}$ 的首项 ${a}_{1} = 1$ ，函数 $f\left( x\right)  = {x}^{3} + \left( {{a}_{n + 1} - {a}_{n} - \cos \frac{n\pi }{2}}\right) {x}^{2}$ 为奇函数，记 ${S}_{n}$ 为数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和， 则 ${S}_{2020}$ 的值为___.

【难度】★★★

【答案】 1010

【解析】解: 因为 $f\left( x\right)$ 是奇函数, $f\left( {-x}\right)  =  - f\left( x\right)$ ,

所以 ${a}_{n + 1} - \left( {{a}_{n} + \cos \frac{n\pi }{2}}\right)  = 0,{a}_{n + 1} = {a}_{n} + \cos \frac{n\pi }{2},{a}_{1} = 1$ ,

${a}_{2} = {a}_{1} + \cos \frac{\pi }{2} = 1,\;{a}_{3} = {a}_{2} + \cos \frac{2\pi }{2} = 0,\;{a}_{4} = {a}_{3} + \cos \frac{3\pi }{2} = 0,$

如此继续,得 ${a}_{n + 4} = {a}_{n}.{S}_{2020} = {505}\left( {{a}_{1} + {a}_{2} + {a}_{3} + {a}_{4}}\right)  = {505} \times  2 = {1010}$ . 故答案为: 1010 .

3、在等差数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{2} =  - {11}$ ， ${a}_{5} =  - 5$ ，记 ${T}_{n} = {a}_{1}{a}_{2}\ldots {a}_{n}\left( {n = 1,2,\ldots }\right)$ ，则数列 $\left\{  {T}_{n}\right\}$ 的最大项是第___项. 【难度】 $\star   \star   \star$

【答案】 6

【解析】解: 设等差数列 $\left\{  {a}_{n}\right\}$ 的公差为 $d$ ,由 ${a}_{2} =  - {11},{a}_{5} =  - 5$ ,可得 ${a}_{1} + d =  - {11},{a}_{1} + {4d} =  - 5$ , 解得 ${a}_{1} =  - {13}, d = 2$ ,则 ${a}_{n} =  - {13} + 2\left( {n - 1}\right)  = {2n} - {15}$ ,可得当 $1 \leq  n \leq  7$ 时, ${a}_{n} < 0.n \geq  8$ 时, ${a}_{n} > 0$ , 则当 $n = 2,4,6$ 时, ${T}_{n} = {a}_{1}{a}_{2}\ldots {a}_{n} > 0$ ,当 $n \geq  7$ 时, ${T}_{n} = {a}_{1}{a}_{2}\ldots {a}_{n} < 0$ ,则 $n = 6$ 时, ${T}_{n}$ 取得最大值.

## 故答案为:6.

4、已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,{a}_{n + 1} = \sin \left( {\frac{\pi }{2} \cdot  {a}_{n}}\right)  + 1$ ，则 ${a}_{6} =$ ___.

【难度】 $\star   \star   \star$

【答案】 2

【解析】解: 因为数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = 1,{a}_{n + 1} = \sin \left( {\frac{\pi }{2} \cdot  {a}_{n}}\right)  + 1$ ,所以 ${a}_{2} = \sin \left( {\frac{\pi }{2} \cdot  {a}_{1}}\right)  + 1 = \sin \frac{\pi }{2} + 1 = 1 + 1 = 2$ , ${a}_{3} = \sin \left( {\frac{\pi }{2} \cdot  {a}_{2}}\right)  + 1 = \sin \left( {\frac{\pi }{2} \times  2}\right)  + 1 = \sin \pi  + 1 = 1,\;{a}_{4} = \sin \left( {\frac{\pi }{2} \cdot  {a}_{3}}\right)  + 1 = \sin \frac{\pi }{2} + 1 = 1 + 1 = 2$ ,

由此可知: 数列 $\left\{  {a}_{n}\right\}$ 是以 2 为周期的数列,所以 ${a}_{6} = {a}_{4} = {a}_{2} = 2$ ,

故答案为: 2 .

5、已知函数 $f\left( x\right)  = {x}^{2} + \left( {a + 8}\right) x + {a}^{2} + a - {12}$ ，且 $f\left( {{a}^{2} - 4}\right)  = f\left( {{2a} - 8}\right)$ ，设等差数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ， 若 ${S}_{n} = f\left( n\right)$ ,则 $\frac{{S}_{n} - {4a}}{{a}_{n} - 1}$ 的最小值为___.

【难度】 $\star   \star   \star$

【答案】 $\frac{37}{8}$

【解析】解: 由题意可得 ${a}^{2} - 4 = {2a} - 8$ 或 ${a}^{2} - 4 + {2a} - 8 = 2 \times  \left( {-\frac{a + 8}{2}}\right)$ ,

解得 $a = 1$ 或 $a =  - 4$ ,当 $a =  - 1$ 时, $f\left( x\right)  = {x}^{2} + {7x} - {12}$ ,数列 $\left\{  {a}_{n}\right\}$ 不是等差数列;

当 $a =  - 4$ 时, $f\left( x\right)  = {x}^{2} + {4x},{S}_{n} = f\left( n\right)  = {n}^{2} + {4n}$ ,

$\therefore {a}_{1} = 5,\;{a}_{2} = 7,\;{a}_{n} = 5 + \left( {7 - 5}\right) \left( {n - 1}\right)  = {2n} + 3$ ,

$\therefore \frac{{S}_{n} - {4a}}{{a}_{n} - 1} = \frac{{n}^{2} + {4n} + {16}}{{2n} + 2} = \frac{1}{2} \cdot  \frac{{\left( n + 1\right) }^{2} + 2\left( {n + 1}\right)  + {13}}{n + 1} = \frac{1}{2} \cdot  \left\lbrack  {\left( {n + 1}\right)  + \frac{13}{n + 1} + 2}\right\rbrack   \geq  \frac{1}{2}\left( {2\sqrt{\left( {n + 1}\right)  \cdot  \frac{13}{n + 1}} + 2}\right)  = \sqrt{13} + 1$ ,

当且仅当 $n + 1 = \frac{13}{n + 1}$ 即 $n = \sqrt{13} - 1$ 时取等号, $\because n$ 为正数,故当 $n = 3$ 时原式取最小值 $\frac{37}{8}$ .

6、已知函数 $y = f\left( x\right)$ 为定义域 $R$ 上的奇函数,且在 $R$ 上是单调递增函数,函数 $g\left( x\right)  = f\left( {x - 3}\right)  + x$ ,数列 $\left\{  {a}_{n}\right\}$ 为等差数列,且公差不为 0,若 $g\left( {a}_{1}\right)  + g\left( {a}_{2}\right)  + \ldots  + g\left( {a}_{9}\right)  = {27}$ ,则 ${a}_{1} + {a}_{2} + \ldots  + {a}_{9} =$ ___.

【难度】 $\star   \star   \star$

【答案】 27

【解析】解: 因为函数 $f\left( x\right)$ 为定义域上的奇函数,则 $f\left( x\right)$ 关于 $\left( {0,0}\right)$ 对称.

设 $h\left( x\right)  = f\left( {x - 3}\right)  + x - 3$ ,所以 $h\left( x\right)$ 关于 $\left( {3,0}\right)$ 对称,则 $h\left( x\right)  + h\left( {6 - x}\right)  = 0$ .

数列的函数性质一教师版

由 $g\left( {a}_{1}\right)  + g\left( {a}_{2}\right)  + \ldots \ldots  + g\left( {a}_{9}\right)  = {27}$ 可得: $f\left( {{a}_{1} - 3}\right)  + {a}_{1} + f\left( {{a}_{2} - 3}\right)  + {a}_{2} + \ldots \ldots  + f\left( {{a}_{9} - 3}\right)  + {a}_{9} = {27}$ ,

所以 $f\left( {{a}_{1} - 3}\right)  + {a}_{1} - 3 + f\left( {{a}_{2} - 3}\right)  + {a}_{2} - 3 + \ldots \ldots  + f\left( {{a}_{9} - 3}\right)  + {a}_{9} - 3 = 0$ 即 $h\left( {a}_{1}\right)  + h\left( {a}_{2}\right)  + \ldots \ldots  + h\left( {a}_{9}\right)  = 0$

又数列 $\left\{  {a}_{n}\right\}$ 为等差数列,且 $h\left( x\right)$ 在 $R$ 上是单调递增函数,所以必有 $h\left( {a}_{1}\right)  + h\left( {a}_{9}\right)  = 0$ ,则有 ${a}_{1} - 3 + {a}_{9} - 3 = 0$ , 所以 $2{a}_{5} = {a}_{1} + {a}_{9} = 6$ ,即 ${a}_{5} = 3$

所以 ${a}_{1} + {a}_{2} + \ldots \ldots  + {a}_{9} = 9{a}_{5} = {27}$

故答案为: 27 .

## 二、选择题

7、设 ${S}_{n}$ 等差数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和,若 ${a}_{7} = 5,{S}_{5} =  - {55}$ ,则 $n{a}_{n}$ 的最小值为 ( )

A. -33 B. -30 C. -28 D. -19

【难度】 $\star   \star$

【答案】 $A$

【解析】解: 设等差数列 $\left\{  {a}_{n}\right\}$ 的公差为 $d,\because {a}_{7} = 5,{S}_{5} =  - {55}$ ,

$\therefore {a}_{1} + {6d} = 5,5{a}_{1} + \frac{5 \times  4}{2} =  - {55}$ ,联立解得: ${a}_{1} =  - {19}, d = 4$ .

$\therefore {a}_{n} =  - {19} + 4\left( {n - 1}\right)  = {4n} - {23}$ . 则 $n{a}_{n} = 4{n}^{2} - {23n}$ ,当 $n = \frac{23}{8}$ 时,函数 $y = 4{n}^{2} - {23n}$ 取得最小值,

因为 $n \in  N$ ,所以 $n = 3$ 时, $n{a}_{n}$ 取得最小值:-33. 故选: $A$ .

8、已知数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = \left\{  \begin{array}{l} \left( {3 - a}\right) n - 3, n \leq  7, n \in  {N}^{ * } \\  {a}^{n - 6}, n > 7, n \in  {N}^{ * } \end{array}\right.$ ，且 ${a}_{n} < {a}_{n + 1}, n \in  {N}^{ * }$ . 则实数 $a$ 的取值范围是( )

A. $\left( {\frac{9}{4},3}\right)$ B. $\left\lbrack  {\frac{9}{4},3}\right)$ C. $\left( {1,3}\right)$ D. $\left( {2,3}\right)$

【难度】 $\star   \star   \star$

【答案】 $D$

【解析】解: 由 ${a}_{n} < {a}_{n + 1}, n \in  {N}^{ * }$ ,可得数列 $\left\{  {a}_{n}\right\}$ 单调递增,

因此必有 $a > 1,\because {a}_{n} = \left\{  {\begin{array}{l} \left( {3 - a}\right) n - 3, n \leq  7, n \in  {N}^{ * } \\  {a}^{n - 6}, n > 7, n \in  {N}^{ * } \end{array},\therefore 3 - a > 0}\right.$ , ${a}_{7} = 7\left( {3 - a}\right)  - 3 < {a}_{8} = {a}^{2}$ ,

解得: $2 < a < 3$ ,则实数 $a$ 的取值范围是 $\left( {2,3}\right)$ ,故选: $D$ .

9、已知无穷等比数列 $\left\{  {a}_{n}\right\}$ 满足 $- {a}_{2} < {a}_{3} < {a}_{2}$ ，其前 $n$ 项和为 ${S}_{n}$ ，则()

A. 数列 $\left\{  {a}_{n}\right\}$ 为递增数列 B. 数列 $\left\{  {a}_{n}\right\}$ 为递减数列

C. 数列 $\left\{  {S}_{n}\right\}$ 有最小项 D. 数列 $\left\{  {S}_{n}\right\}$ 有最大项

【难度】 $\star   \star   \star$

【答案】 $C$

【解析】解: 设等比数列 $\left\{  {a}_{n}\right\}$ 公比为 $q\left( {q \neq  0}\right)$ ,由 $- {a}_{2} < {a}_{3} < {a}_{2}$ ,得 $- {a}_{2} < {a}_{2}q < {a}_{2}$ ,

当 ${a}_{2} > 0$ 时, $- 1 < q < 1$ ,此时 ${a}_{n} = {a}_{2} \cdot  {q}^{n - 2}$ ,

${a}_{n + 1} - {a}_{n} = {a}_{2} \cdot  {q}^{n - 2}\left( {q - 1}\right) ,\because {q}^{n - 2}$ 正负未知, $\therefore {a}_{n + 1} - {a}_{n}$ 正负不确定, $\therefore {AB}$ 错误;

${S}_{n} = \frac{{a}_{1}\left( {1 - {q}^{n}}\right) }{1 - q} = \frac{{a}_{2}\left( {1 - {q}^{n}}\right) }{\left( {1 - q}\right) q},$

当 $q \in  \left( {-1,0}\right)$ 时, $\frac{{a}_{2}}{\left( {1 - q}\right) q} < 0,1 - {q}^{n} \in  \left\lbrack  {1 - {q}^{2},1 - q}\right\rbrack$ ,此时 $\left\{  {S}_{n}\right\}$ 既有最大值,也有最小值,

当 $q \in  \left( {0,1}\right)$ 时, $\frac{{a}_{2}}{\left( {1 - q}\right) q} > 0,1 - {q}^{n} \in  \left\lbrack  {1 - q,1}\right)$ ,此时 $\left\{  {S}_{n}\right\}$ 只有最小值,没有最大值, $\therefore D$ 错误.

故选: $C$ .

10、已知数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = {n}^{2} - {11n} + \frac{a}{n}$ ， ${a}_{5}$ 是数列 $\left\{  {a}_{n}\right\}$ 的最小项，则实数 $a$ 的取值范围是( )

A. $\left\lbrack  {-{40}, - {25}}\right\rbrack$ B. $\left\lbrack  {-{40},0}\right\rbrack$ C. $\left\lbrack  {-{25},{25}}\right\rbrack$ D. $\left\lbrack  {-{25},0}\right\rbrack$

【难度】★★★

【答案】 $D$

【解答】解: 由条件有对任意的 $n \in  {N}^{ * }$ ,由 ${a}_{n} \geq  {a}_{5}$ 恒成立,即 ${n}^{2} - {11n} + \frac{a}{n} \geq  \frac{a}{5} - {30}$ ,整理得 $\left( {n - 5}\right) \left( {n - 6}\right)  \geq  \frac{a\left( {n - 5}\right) }{5n}.$

当 $n \leq  4$ 时,不等式化简为 $a \geq  {5n}\left( {n - 6}\right)$ 恒成立,所以 $a \geq   - {25}$ ;

当 $n \geq  6$ 时,不等式化简为 $a \leq  {5n}\left( {n - 6}\right)$ 恒成立,所以 $a \leq  0$ ;

综上: $- {25} \leq  a \leq  0$ .

故选: $D$ .

## 三、解答题

11、已知数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = \frac{{3n} - 2}{{3n} + 1}$ .

(1)求这个数列的第 10 项；

(2)在区间 $\left( {\frac{1}{3},\frac{2}{3}}\right)$ 内是否存在数列中的项? 若有，有几项? 若没有，说明理由.

【难度】 $\star   \star   \star$

【答案】见解析

【解析】解: (1) 根据题意,数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = \frac{{3n} - 2}{{3n} + 1}$ ,

则 ${a}_{10} = \frac{3 \times  {10} - 2}{3 \times  {10} + 1} = \frac{28}{31}$ ;

(2)根据题意， $\frac{1}{3} < \frac{{3n} - 2}{{3n} + 1} < \frac{2}{3}$ ，解可得: $\frac{7}{6} < n < \frac{8}{3}$ ，

又由 $n$ 为正整数,则 $n = 2$ ,

则在区间 $\left( {\frac{1}{3},\frac{2}{3}}\right)$ 内只存在数列的一项.

12、设数列 $\left\{  {a}_{n}\right\}$ 的首项 ${a}_{1}$ 为常数,且 ${a}_{n + 1} = {3}^{n} - 2{a}_{n},\left( {n \in  {N}^{ * }}\right)$

(1)证明: $\left\{  {{a}_{n} - \frac{{3}^{n}}{5}}\right\}$ 是等比数列;

(2)若 ${a}_{1} = \frac{3}{2}$ ， $\left\{  {a}_{n}\right\}$ 中是否存在连续三项成等差数列？若存在，写出这三项，若不存在说明理由.

(3)若 $\left\{  {a}_{n}\right\}$ 是递增数列，求 ${a}_{1}$ 的取值范围.

【难度】 $\star   \star   \star$

【答案】见解析

【解析】(1) 证明: $\because {a}_{n + 1} = {3}^{n} - 2{a}_{n},\left( {n \in  {N}^{ * }}\right) ,\therefore \frac{{a}_{n + 1} - \frac{1}{5} \times  {3}^{n + 1}}{{a}_{n} - \frac{1}{5} \times  {3}^{n}} = \frac{\frac{2}{5} \times  {3}^{n} - 2{a}_{n}}{{a}_{n} - \frac{1}{5} \times  {3}^{n}} =  - 2$ ,

$\therefore$ 数列 $\left\{  {{a}_{n} - \frac{{3}^{n}}{5}}\right\}$ 是等比数列.

(2)解: $\left\{  {{a}_{n} - \frac{{3}^{n}}{5}}\right\}$ 是公比为-2，首项为 ${a}_{1} - \frac{3}{5} = \frac{9}{10}$ 的等比数列.

通项公式为 ${a}_{n} = \frac{{3}^{n}}{5} + \left( {{a}_{1} - \frac{3}{5}}\right) {\left( -2\right) }^{n - 1} = \frac{{3}^{n}}{5} + \frac{9}{10} \times  {\left( -2\right) }^{n - 1}$ ,

若 $\left\{  {a}_{n}\right\}$ 中存在连续三项成等差数列,则必有 $2{a}_{n + 1} = {a}_{n} + {a}_{n + 2}$ ,

即 $2\left\lbrack  {\frac{{3}^{n + 1}}{5} + \frac{9}{10} \times  {\left( -2\right) }^{n}}\right\rbrack   = \frac{{3}^{n}}{5} + \frac{9}{10} \times  {\left( -2\right) }^{n - 1} + \frac{{3}^{n + 2}}{5} + \frac{9}{10} \times  {\left( -2\right) }^{n + 1}$ ,解得 $n = 4$ ,即 ${a}_{4},{a}_{5},{a}_{6}$ 成等差数列.

(3)解:如果 ${a}_{n + 1} > {a}_{n}$ 成立，

即 $\frac{{3}^{n + 1}}{5} + \left( {{a}_{1} - \frac{3}{5}}\right)  \times  {\left( -2\right) }^{n} > \frac{{3}^{n}}{5} + \left( {{a}_{1} - \frac{3}{5}}\right) {\left( -2\right) }^{n - 1}$ 对任意自然数均成立. 化简得 $\frac{4}{15} \times  {3}^{n} >  - \left( {{a}_{1} - \frac{3}{5}}\right)  \times  {\left( -2\right) }^{n}$ ,

当 $n$ 为偶数时 ${a}_{1} > \frac{3}{5} - \frac{4}{15} \times  {\left( \frac{3}{2}\right) }^{n},\because p\left( n\right)  = \frac{3}{5} - \frac{4}{15} \times  {\left( \frac{3}{2}\right) }^{n}$ 是递减数列, $\therefore p{\left( n\right) }_{\max } = p\left( 2\right)  = 0$ ,即 ${a}_{1} > 0$ ; 当 $n$ 为奇数时, ${a}_{1} < \frac{3}{5} + \frac{4}{15} \times  {\left( \frac{3}{2}\right) }^{n},\because q\left( n\right)  = \frac{3}{5} + \frac{4}{15} \times  {\left( \frac{3}{2}\right) }^{n}$ 是递增数列, $\therefore q{\left( n\right) }_{\min } = q\left( 1\right)  = 1$ ,即 ${a}_{1} < 1$ ; 故 ${a}_{1}$ 的取值范围为 $\left( {0,1}\right)$ .
