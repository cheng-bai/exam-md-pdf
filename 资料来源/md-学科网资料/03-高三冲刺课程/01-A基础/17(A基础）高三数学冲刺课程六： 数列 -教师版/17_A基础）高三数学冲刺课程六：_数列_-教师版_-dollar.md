数列

<table><tr><td>教学目标</td><td>掌握高考数列题型</td></tr><tr><td>重点</td><td>1、等差等比数列概念、通项公式与求和公式、及常用性质; <br> 2、求数列通项与求数列和问题、求数列极限; <br> 3、数列的性质及数列与其他章节知识点的综合运用； <br> 4、数列新定义问题.</td></tr><tr><td>难 点</td><td>1、数列的性质及数列与其他章节知识点的综合运用； <br> 2、数列新定义问题.</td></tr></table>

## (一) 等差数列与等比数列

知识梳理

等差数列的通项公式: ${a}_{n} = {a}_{1} + \left( {n - 1}\right) d$ .

等差数列的前 $n$ 项和: ${S}_{n} = \frac{n\left( {{a}_{1} + {a}_{n}}\right) }{2}$ 或 ${S}_{n} = n{a}_{1} + \frac{n\left( {n - 1}\right) }{2}d$

等比数列的通项公式: ${a}_{n} = {a}_{1}{q}^{n - 1}$

等比数列的前 $n$ 项和: ${S}_{n} = \left\{  \begin{array}{ll} n{a}_{1} & q = 1 \\  \frac{{a}_{1}\left( {1 - {q}^{n}}\right) }{1 - q} & q \neq  1 \end{array}\right.$

## 例题精讲

【例 1】( 1 )设 ${S}_{n}$ 为等差数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和，且 $2 + {a}_{5} = {a}_{6} + {a}_{3}$ ，则 ${S}_{7} =$ ( )

A. 28 B. 14

C. 7 D. 2

【难度】 $\star   \star$

【答案】B

【解析】由等差数列的性质知 ${a}_{4} + {a}_{5} = {a}_{6} + {a}_{3}$ ,结合 $2 + {a}_{5} = {a}_{6} + {a}_{3}$ ,得 ${a}_{4} = 2$ , 所以 ${S}_{7} = \frac{7\left( {{a}_{1} + {a}_{7}}\right) }{2} = 7{a}_{4} = {14}$ . 故选 B.

(2)设等差数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，公差 $d > 0$ 且 ${a}_{1}^{2} = {a}_{7}^{2}$ ，则 ${S}_{n}$ 取得最小值时， $n$ 的值为___.

【难度】 $\bigstar \bigstar \bigstar$

【答案】3 或 4

【解析】解: 因为 ${a}_{1}^{2} = {a}_{7}^{2}$ ,所以 $\left( {{a}_{1} + {a}_{7}}\right) \left( {{a}_{1} - {a}_{7}}\right)  = 0$ ,因为 $d > 0$ ,所以 ${a}_{1} - {a}_{7} \neq  0$ ,所以 ${a}_{1} + {a}_{7} = 0$ , 所以 $2{a}_{4} = 0$ 即 ${a}_{4} = 0$ ,因为 $d > 0$ ,所以 $\left\{  {a}_{n}\right\}$ 是递增数列,所以 ${a}_{1} < {a}_{2} < {a}_{3} < {a}_{4} = 0 < {a}_{5} < {a}_{6} < \cdots$ ,显然前 3 项和或前 4 项和最小. 故答案为: 3 或 4

【例 2】( 1 )已知等比数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，且 ${a}_{n + 1} + \lambda  = 3{S}_{n},{a}_{3} = {12}$ ，则实数 $\lambda$ 的值为___.

【难度】 $\star   \star$

【答案】 $- \frac{3}{4}$

【解析】当 $n \geq  2$ 时, $\left\{  \begin{array}{l} {a}_{n + 1} + \lambda  = 3{S}_{n} \\  {a}_{n} + \lambda  = 3{S}_{n - 1} \end{array}\right.$ ,两式相减得 ${a}_{n + 1} - {a}_{n} = 3\left( {{S}_{n} - {S}_{n - 1}}\right)  = 3{a}_{n}$ ,

即 ${a}_{n + 1} = 4{a}_{n}$ ,并且数列 $\left\{  {a}_{n}\right\}$ 是等比数列,所以 $q = 4$ ,

$\because {a}_{3} = {12},\therefore {a}_{2} = 3,{a}_{1} = \frac{3}{4}$ ,

当 $n = 2$ 时， ${a}_{3} + \lambda  = 3{S}_{2} = 3\left( {{a}_{1} + {a}_{2}}\right)$ ，解得 $\lambda  =  - \frac{3}{4}$ . 故答案为: $- \frac{3}{4}$

(2)在数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{1} = 3$ ， ${a}_{m + n} = {a}_{m} + {a}_{n}\left( {m, n \in  {\mathbf{N}}^{ * }}\right)$ ，若 ${a}_{1} + {a}_{2} + {a}_{3} + \cdots  + {a}_{k} = {135}$ ，则 $k =$ ( )

A. 10 B. 9 C. 8 D. 7

【难度】 $\star   \star   \star$

【答案】B

【解析】令 $m = 1$ ,由 ${a}_{m + n} = {a}_{m} + {a}_{n}$ 可得 ${a}_{n + 1} = {a}_{1} + {a}_{n}$ ,所以 ${a}_{n + 1} - {a}_{n} = 3$ ,

所以 $\left\{  {a}_{n}\right\}$ 是首项为 ${a}_{1} = 3$ ,公差为 3 的等差数列, ${a}_{n} = 3 + 3\left( {n - 1}\right)  = {3n}$ ,

所以 ${a}_{1} + {a}_{2} + {a}_{3} + \cdots  + {a}_{k} = \frac{k\left( {{a}_{1} + {a}_{k}}\right) }{2} = \frac{k\left( {3 + {3k}}\right) }{2} = {135}$ ,整理可得: ${k}^{2} + k - {90} = 0$ ,

解得: $k = 9$ 或 $k =  - {10}$ (舍)；故选:B.

【例 3】设等比数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ . 若 $- {S}_{1}\text{ 、 }{S}_{2}\text{ 、 }{a}_{3}$ 成等差数列,则数列 $\left\{  {a}_{n}\right\}$ 的公比为___.

【难度】 $\star   \star$

【答案】3 或 -1

【解析】设等比数列 $\left\{  {a}_{n}\right\}$ 的公比为 $q$ ,

因为等比数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ， $- {S}_{1}$ 、 ${S}_{2}$ 、 ${a}_{3}$ 成等差数列，所以 $2{S}_{2} =  - {S}_{1} + {a}_{3}$ ，则 $2\left( {{a}_{1} + {a}_{2}}\right)  =  - {a}_{1} + {a}_{3}$ ， 因此 $3{a}_{1} + 2{a}_{2} = {a}_{3}$ ,所以 ${q}^{2} - {2q} - 3 = 0$ ,解得 $q = 3$ 或 $q =  - 1$ . 故答案为: 3 或 -1 .

【例 4】已知数列 $\left\{  {a}_{n}\right\}$ 是公差为 $d$ 的等差数列,设 ${c}_{n} = {2}^{{a}_{1}} + {2}^{{a}_{2}} + {2}^{{a}_{3}} + \cdots  + {2}^{{a}_{n}}$ ,若存在常数 $m$ ,使得数列 $\left\{  {{c}_{n} + m}\right\}$ 为等比数列,则 $m$ 的值为___.

【难度】 $\star   \star   \star$

【答案】 $\frac{{2}^{{a}_{1}}}{{2}^{d} - 1}$

【解析】

当 $d = 0$ 时, ${c}_{n} = {2}^{{a}_{1}} + {2}^{{a}_{2}} + {2}^{{a}_{3}} + \cdots  + {2}^{{a}_{n}} = n \cdot  {2}^{{a}_{1}}$ . 若存在常数 $m$ ,使得数列 $\left\{  {{c}_{n} + m}\right\}$ 为等比数列,则 ${\left( {c}_{n} + m\right) }^{2} = \left( {{c}_{n - 1} + m}\right) \left( {{c}_{n + 1} + m}\right) \left( {n \geq  2}\right)$ ,记 ${2}^{a} = t$ ,则有 ${\left( nt + m\right) }^{2} = \left\lbrack  {\left( {n - 1}\right) t + m}\right\rbrack  \left\lbrack  {\left( {n + 1}\right) t + m}\right\rbrack$ ,化简得 ${t}^{2} = 0$ ,这与 ${2}^{{a}_{1}} > 0$ 矛盾,故此时不存在常数 $m$ ,使得数列 $\left\{  {{c}_{n} + m}\right\}$ 为等比数列.

当 $d \neq  0$ 时,

${c}_{n} = {2}^{{a}_{1}} + {2}^{{a}_{2}} + {2}^{{a}_{3}} + \cdots  + {2}^{{a}_{n}} = {2}^{{a}_{1}}\left\lbrack  {1 + {2}^{d} + {2}^{2d} + \cdots  + {2}^{\left( {n - 1}\right) d}}\right\rbrack   = {2}^{{a}_{1}} \cdot  1 \cdot  \frac{{\left( {2}^{d}\right) }^{n} - 1}{{2}^{d} - 1} = b \cdot  {2}^{dn} - b$ (其中 $b = \frac{{2}^{{a}_{1}}}{{2}^{d} - 1}$ ). 因为数列 $\left\{  {{c}_{n} + m}\right\}$ 为等比数列,对任意 $n \in  {\mathbf{N}}^{ * }$ ,恒有 $\frac{{c}_{n + 1} + m}{{c}_{n} + m} = C\left( {C\text{ 为常数且 }C \neq  0}\right)$ ,即 $\frac{b \cdot  {2}^{d\left( {n + 1}\right) } - b + m}{b \cdot  {2}^{dn} - b + m} = C$ ,所以 $b \cdot  {2}^{{dn} + d} + m - b = {Cb} \cdot  {2}^{dn} + C\left( {m - b}\right)$ ,

所以 $b \cdot  {2}^{dn}\left( {{2}^{d} - C}\right)  + \left( {m - b}\right) \left( {1 - C}\right)  = 0$ 对任意正整数 $n$ 恒成立,所以 $\left\{  \begin{array}{l} {2}^{d} - C = 0, \\  \left( {m - b}\right) \left( {1 - C}\right)  = 0, \end{array}\right.$ 解得 $\left\{  \begin{array}{l} m = b, \\  C = {2}^{d}, \end{array}\right.$ 或 $\left\{  \begin{array}{l} C = {2}^{d} \\  C = 1 \end{array}\right.$ (舍),所以数列 $\left\{  {{c}_{n} + m}\right\}$ 为等比数列时, $m = \frac{{2}^{{a}_{1}}}{{2}^{d} - 1}$ . 故答案为: $\frac{{2}^{{a}_{1}}}{{2}^{d} - 1}$

## 巩固训练

1、已知等差数列 $\left\{  {a}_{n}\right\}$ 的首项为 4，公差为 2，前 $\mathrm{n}$ 项和为 ${S}_{n}$ . 若 ${S}_{k} - {a}_{k + 5} = {44}\left( {k \in  {N}^{ * }}\right)$ ，则 $k$ 的值为___. 【答案】7

【解析】

${S}_{k} = {k}^{2} + {3k},{a}_{k + 5} = 4 + \left( {k + 5 - 1}\right)  \cdot  2 = {2k} + {12}$ ,则 ${k}^{2} + k - {56} = 0$ ，解得 $k = 7$ 或 $k =  - 8$ (舍去)，所以 $k = 7$ ；

2、已知数列 $\left\{  {a}_{n}\right\}$ 为递增等比数列, ${a}_{1},{a}_{2}$ 是关于 $x$ 的方程 ${x}^{2} - {3x} + 2 = 0$ 的两个实数根,则其前 5 项和 ${S}_{5} =$ ___.

【答案】31

【解析】由 ${x}^{2} - {3x} + 2 = 0$ ,解得 $x = 1$ ,或 $x = 2$ ,

$\because$ 数列 $\left\{  {a}_{n}\right\}$ 为递增等比数列, ${a}_{1},{a}_{2}$ 是关于 $x$ 的方程 ${x}^{2} - {3x} + 2 = 0$ 的两个实数根,

$\therefore {a}_{1} = 1,{a}_{2} = 2,\therefore$ 公比 $q = 2.\therefore$ 其前 5 项和 ${S}_{5} = \frac{{2}^{5} - 1}{2 - 1} = {31}$ . 故答案为: 31 .

3、等差数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，公差为 $d\left( {d \neq  0}\right)$ ，首项为 ${a}_{1}$ ，若 $\left\{  \sqrt{{S}_{n}}\right\}$ 也是等差数列，则 $\frac{{a}_{1}}{d} = \ldots$ . 【答案】 $\frac{1}{2}$

【解析】依题意 ${S}_{n} = n{a}_{1} + \frac{n\left( {n - 1}\right) }{2}d$ ,由于 $\left\{  \sqrt{{S}_{n}}\right\}$ 是等差数列,所以 $\sqrt{{S}_{1}} + \sqrt{{S}_{3}} = 2\sqrt{{S}_{2}}$ ,

即 $\sqrt{{a}_{1}} + \sqrt{3{a}_{1} + {3d}} = 2\sqrt{2{a}_{1} + d}, d \neq  0$

两边平方并化简得 $2\sqrt{3{a}_{1}^{2} + 3{a}_{1}d} = 4{a}_{1} + d$ ,两边平方并化简得 $4{a}_{1}^{2} - 4{a}_{1}d + {d}^{2} = 0$ ,

即 ${\left( 2{a}_{1} - d\right) }^{2} = 0,2{a}_{1} - d = 0 \Rightarrow  \frac{{a}_{1}}{d} = \frac{1}{2}$ . 故答案为: $\frac{1}{2}$

4、已知等差数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}\left( {n \in  {N}^{ * }}\right)$ ,公差 $d \neq  0,{S}_{6} = {90},{a}_{7}$ 是 ${a}_{3}$ 与 ${a}_{9}$ 的等比中项,当 ${S}_{n} > 0$ 时, $n$ 的最大值为___.

【答案】20.

【解析】因为 ${a}_{7}$ 是 ${a}_{3}$ 与 ${a}_{9}$ 的等比中项,所以 ${a}_{7}^{2} = {a}_{3} \cdot  {a}_{9}$ ,

所以 ${\left( {a}_{1} + 6d\right) }^{2} = \left( {{a}_{1} + {2d}}\right) \left( {{a}_{1} + {8d}}\right)$ ,化简得 ${a}_{1}d + {10}{d}^{2} = 0$ ,

因为 $d \neq  0$ ,所以 ${a}_{1} =  - {10d}$ ,因为 ${S}_{6} = {90}$ ,所以 $6{a}_{1} + \frac{6 \times  5}{2}d = {90}$ ,即 ${a}_{1} + \frac{5}{2}d = {15}$ ,

将 ${a}_{1} =  - {10d}$ 代入得 $- {10d} + \frac{5}{2}d = {15}$ ,解得 $d =  - 2$ ,所以 ${a}_{1} = {20}$ ,

所以 ${S}_{n} = {20n} + \frac{n\left( {n - 1}\right) }{2} \times  \left( {-2}\right)  =  - {n}^{2} + {21n}$ ,

由 ${S}_{n} > 0$ 得 $- {n}^{2} + {21n} > 0$ ,即 ${n}^{2} - {21n} < 0$ ,解得 $0 < n < {21}$ ,所以正整数 $n$ 的最大值为 20 . 故答案为: 20

5、已知 $a\text{ 、 }b\text{ 、 }c$ 为实常数，数列 $\left\{  {x}_{n}\right\}$ 的通项 ${x}_{n} = a{n}^{2} + {bn} + c, n \in  {\mathbf{N}}^{ * }$ ，则“存在 $k \in  {\mathbf{N}}^{ * }$ ， 使得 ${x}_{{100} + k}\text{ 、 }{x}_{{200} + k}\text{ 、 }{x}_{{300} + k}$ 成等差数列”的一个必要条件是( )

A. $a \geq  0$ B. $b \leq  0$ C. $c = 0$ D. $a - {2b} + c = 0$

【答案】A

【解析】存在 $k \in  {N}^{ + }$ ,使得 ${x}_{{100} + k},{x}_{{200} + k},{x}_{{300} + k}$ 成等差数列,可得

$2\left\lbrack  {a{\left( {200} + k\right) }^{2} + b\left( {{200} + k}\right)  + c}\right\rbrack   = a{\left( {100} + k\right) }^{2} + b\left( {{100} + k}\right)  + c + a{\left( {300} + k\right) }^{2} + b\left( {{300} + k}\right)  + c$ ,

化简可得 $a = 0$ ,所以使得 ${x}_{{100} + k},{x}_{{200} + k},{x}_{{300} + k}$ 成等差数列的必要条件是 $a \geq  0$

## (二) 数列的通项+数列的和+数列的极限+数学归纳法

## 知识梳理

## 一、数列通项公式的常见求法

1、已知递推式

①累加 ②累乘 ③构造(待定系数、取对数、取倒数等)

2、 ${a}_{n}$ 与 ${S}_{n}$

① 直接法:消 ${S}_{n}$ ，直接得到关于 ${a}_{n}$ 的递推式

②间接法:消 ${a}_{n}$ ，先求 ${S}_{n}$ ，再利用 ${a}_{n} = \left\{  \begin{array}{ll} {S}_{1} & n = 1 \\  {S}_{n} - {S}_{n - 1} & n \geq  2 \end{array}\right.$

## 二、数列求和

1、等差、等比数列求和公式

2、倒序相加

3、错位相减

4、裂项相消

5、分组求和:①奇数项、偶数项分组；②摆动型，两项一组；③利用“周期”分组等等

## 三、几个常见的极限:

(1) $\mathop{\lim }\limits_{{n \rightarrow  \infty }}c = c$ (C为常数)； (2) $\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{1}{n} = 0$ ； (3) $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{q}^{n} = 0\;\left( {\left| q\right|  < 1}\right)$ ；

(4) $\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{a{n}^{k} + b}{c{n}^{k} + d} = \frac{a}{c}\left( {k \in  N, a\text{ 、 }b\text{ 、 }c\text{ 、 }d \in  R\text{ 且 }c \neq  0}\right)$ ;

(5) $\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{a}^{n} - {b}^{n}}{{a}^{n} + {b}^{n}} = \left\{  \begin{array}{l} 1,\left| a\right|  > \left| b\right| \\   - 1,\left| a\right|  < \left| b\right| \\  0, a = b \\  \text{ 不存在, }a =  - b \end{array}\right.$ .

## 四、无穷等比数列各项的和

把公比 $q$ 满足 $\left| q\right|  < 1$ 的无穷等比数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n} = \frac{{a}_{1}\left( {1 - {q}^{n}}\right) }{1 - q}$ ,当 $n \rightarrow  \infty$ 时的极限叫做无穷等比数列各项的和,并用符号 $S$ 表示,即 $S = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{n} = \frac{{a}_{1}}{1 - q}\left( {0 < \left| q\right|  < 1}\right)$ .

## 例题精讲

【例 5】( 1 )已知数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n},{a}_{1} = \frac{1}{2}$ ,对任意的 $n \in  {\mathbf{N}}^{ * }$ 都有 $n{a}_{n} = \left( {n + 2}\right) {a}_{n + 1}$ ,则 ${S}_{2021} =$ ( )

A. $\frac{2019}{2020}$ B. $\frac{2020}{2021}$ C. $\frac{2021}{2022}$ D. $\frac{1010}{1011}$

【难度】 $\star   \star   \star$

【答案】C

【解析】数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = \frac{1}{2}$ ,对任意的 $n \in  {\mathbf{N}}^{ * }$ 都有 $n{a}_{n} = \left( {n + 2}\right) {a}_{n + 1}$ ,

则有 $n\left( {n + 1}\right) {a}_{n} = \left( {n + 1}\right) \left( {n + 2}\right) {a}_{n + 1}$ ,可得数列 $\left\{  {n\left( {n + 1}\right) {a}_{n}}\right\}$ 为常数列,

有 $n\left( {n + 1}\right) {a}_{n} = 2{a}_{1}$ ,得 $n\left( {n + 1}\right) {a}_{n} = 1$ ,得 ${a}_{n} = \frac{1}{n\left( {n + 1}\right) }$ ,

又由 ${a}_{n} = \frac{1}{n\left( {n + 1}\right) } = \frac{1}{n} - \frac{1}{n + 1}$ ,所以 ${S}_{2021} = 1 - \frac{1}{2} + \frac{1}{2} - \frac{1}{3} + \cdots \frac{1}{2021} - \frac{1}{2022} = 1 - \frac{1}{2022} = \frac{2021}{2022}$ . 故选: $\mathrm{C}$

(2)数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = \frac{1}{3}$ ，且 ${a}_{n} - {a}_{n + 1} = \left( {{2n} + 3}\right) {a}_{n}{a}_{n + 1}$ ，则数列 $\left\{  {a}_{n}\right\}$ 的前 10 项和为___.

【难度】 $\star   \star   \star$

【答案】 $\frac{175}{264}$

【解析】已知数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{1} = \frac{1}{3}$ ,且 ${a}_{n} - {a}_{n + 1} = \left( {{2n} + 3}\right) {a}_{n}{a}_{n + 1},\therefore \frac{1}{{a}_{n + 1}} - \frac{1}{{a}_{n}} = \frac{{a}_{n} - {a}_{n + 1}}{{a}_{n}{a}_{n + 1}} = {2n} + 3$ , 所以,

$\frac{1}{{a}_{n}} = \frac{1}{{a}_{1}} + \left( {\frac{1}{{a}_{2}} - \frac{1}{{a}_{1}}}\right)  + \left( {\frac{1}{{a}_{3}} - \frac{1}{{a}_{2}}}\right)  + \cdots  + \left( {\frac{1}{{a}_{n}} - \frac{1}{{a}_{n - 1}}}\right)  = 3 + 5 + 7 + \cdots  + \left( {{2n} + 1}\right)  = \frac{n\left( {3 + {2n} + 1}\right) }{2} = n\left( {n + 2}\right) \; \therefore {a}_{n} = \frac{1}{n\left( {n + 2}\right) } = \frac{1}{2}\left( {\frac{1}{n} - \frac{1}{n + 2}}\right)$ ,

因此,数列 $\left\{  {a}_{n}\right\}$ 的前 10 项和为

${S}_{10} = \frac{1}{2}\left\lbrack  {\left( {1 - \frac{1}{3}}\right)  + \left( {\frac{1}{2} - \frac{1}{4}}\right)  + \left( {\frac{1}{3} - \frac{1}{5}}\right)  + \cdots  + \left( {\frac{1}{10} - \frac{1}{12}}\right) }\right\rbrack   = \frac{1}{2}\left( {1 + \frac{1}{2} - \frac{1}{11} - \frac{1}{12}}\right)  = \frac{175}{264}$ . 故答案为: $\frac{175}{264}$ .

【例 6】已知公比大于 1 的等比数列 $\left\{  {a}_{n}\right\}$ 满足 ${a}_{2} + {a}_{4} = {20},{a}_{3} = 8$ ,记 ${b}_{m}$ 为 $\left\{  {a}_{n}\right\}$ 在区间 $(0, m\rbrack \left( {m \in  {N}^{ * }}\right)$ 中的项的个数, $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,则 ${S}_{{2}^{n}} =$ ___.

【难度】 $\star   \star   \star$

【答案】 $\left( {n - 1}\right) {2}^{n} - {2}^{n + 1} - 2 + n$

【解析】设 $\left\{  {a}_{n}\right\}$ 的公比为 $q\left( {q > 1}\right)$ ,由 $\left\{  \begin{array}{l} {a}_{2} + {a}_{4} = {20} \\  {a}_{3} = 8 \end{array}\right.$ ,得 $\left\{  \begin{array}{l} {a}_{1} = 2 \\  q = 2 \end{array}\right.$ 或 $\left\{  \begin{array}{l} {a}_{1} = {32} \\  q = \frac{1}{2} \end{array}\right.$ (舍去)

所以 ${a}_{n} = {2}^{n},{2}^{1} = 2,{2}^{2} = 4,{2}^{3} = 8,{2}^{4} = {16},{2}^{5} = {32},{2}^{6} = {64}$

数列一教师版

在区间 $(0,1\rbrack$ 上, ${b}_{1} = 0$ ,

在区间上 $(0,2\rbrack ,(0,3\rbrack$ 上 ${b}_{2} = {b}_{3} = 1,2$ 个 1

在区间 $(0,4\rbrack ,(0,5\rbrack (0,6\rbrack ,(0,7\rbrack$ 上, ${b}_{4} = {b}_{5} = {b}_{6} = {b}_{7} = 2,{2}^{2}$ 个 2

在区间 $(0,8\rbrack ,(0,9\rbrack (0,{10}\rbrack ,(0,{11}\rbrack ,\ldots (0,{15}\rbrack$ 上, ${b}_{8} = {b}_{9} = {b}_{11}\ldots  = {b}_{15} = 3,{2}^{3}$ 个 3,

...

归纳得当 ${2}^{n} \leq  m < {2}^{n + 1}$ 时, ${b}_{m} = n$

所以 ${S}_{{2}^{n}} = 1 \times  2 + 2 \times  {2}^{2} + 3 \times  {2}^{3} + \cdots  + \left( {n - 1}\right) {2}^{n - 1} + n$

令 ${T}_{n} = 1 \times  2 + 2 \times  {2}^{2} + 3 \times  {2}^{3} + \cdots  + \left( {n - 1}\right) {2}^{n - 1}$

则 $2{T}_{n} = 1 \times  2 + 2 \times  {2}^{2} + 3 \times  {2}^{3} + \cdots  + \left( {n - 1}\right) {2}^{n - 1} + \left( {n - 1}\right) {2}^{n}$

两式相减,整理得 ${T}_{n} = \left( {n - 1}\right) {2}^{n} - {2}^{n + 1} - 2$

所以 ${S}_{{2}^{n}} = \left( {n - 1}\right) {2}^{n} - {2}^{n + 1} - 2 + n$ ; 故答案为: $\left( {n - 1}\right) {2}^{n} - {2}^{n + 1} - 2 + n$

【例 7】( 1 )已知 ${a}_{n} = \left\{  {\begin{array}{l} {2n} - 1, n < {2015} \\  {\left( -\frac{1}{2}\right) }^{n - 1}, n \geq  {2015} \end{array},{S}_{n}}\right.$ 是数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和( )

A. $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n}$ 和 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{n}$ 都存在 B. $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n}$ 和 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{n}$ 都不存在

C. $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n}$ 存在, $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{n}$ 不存在 D. $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n}$ 不存在, $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{n}$ 存在

【难度】 $\star   \star$

【答案】A

【解析】 ${a}_{n} = \left\{  {\begin{array}{l} {2n} - 1, n < {2015} \\  {\left( -\frac{1}{2}\right) }^{n - 1}, n \geq  {2015} \end{array},{S}_{n}}\right.$ 是数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和,可得 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{a}_{n} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\left( -\frac{1}{2}\right) }^{n - 1} = 0$ .

$\mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{n} = {S}_{2014} + \frac{-\frac{1}{2}}{1 + \frac{1}{2}} = {S}_{2014} - \frac{1}{3}$ ,是定值. 所以两个极限存在. 故选: $A$ (2)无穷等比数列 $\left\{  {a}_{n}\right\}  \left( {n \in  {N}^{ * }}\right)$ 的前 $n$ 项的和是 ${S}_{n}$ ，则下列首项 ${a}_{1}$ 中，使得 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{n} = \frac{1}{2}$ 的只可能是( )

A. $\frac{1}{2}$ B. $- \frac{1}{2}$ C. $\frac{1}{4}$ D. $- \frac{1}{4}$

【难度】 $\star   \star$

【答案】C

【解析】无穷等比数列, $\mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{n} = \frac{{a}_{1}}{1 - q},\therefore \frac{{a}_{1}}{1 - q} = \frac{1}{2}$ ,

$\therefore q = 1 - 2{a}_{1}.\because  - 1 < q < 1, q \neq  0.\therefore  - 1 < 1 - 2{a}_{1} < 1,1 - 2{a}_{1} \neq  0.\therefore 0 < {a}_{1} < 1,{a}_{1} \neq  \frac{1}{2}$ . 所以选 C.

(3)设数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n} = 2{n}^{2} + 1\left( {n \in  {N}^{ * }}\right)$ ，则 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{S}_{n}}{{a}_{n}^{2}} =$ ___.

【难度】 $\star   \star$

【答案】 $\frac{1}{8}$

【解析】因为 ${S}_{n} = 2{n}^{2} + 1\left( {n \in  {N}^{ * }}\right)$ ,故 ${a}_{n} = \left\{  \begin{array}{l} 3, n = 1 \\  {4n} - 2, n \geq  2 \end{array}\right.$ ,故

$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{S}_{n}}{{a}_{n}^{2}} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{2{n}^{2} + 1}{{\left( 4n - 2\right) }^{2}} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{2 + \frac{1}{{n}^{2}}}{{\left( 4 - \frac{2}{n}\right) }^{2}} = \frac{2}{16} = \frac{1}{8}$ . 故答案为: $\frac{1}{8}$ .

【例 8】用数学归纳法证明不等式 $\frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots  + \frac{1}{{2}^{n - 1}} > \frac{n}{2} - 1\left( {n \in  {N}^{ * }, n \geq  2}\right)$ 时,以下说法正确的是( )

A. 第一步应该验证当 $n = 1$ 时不等式成立

B. 从 “ $n = k$ 到 $n = k + 1$ ” 左边需要增加的代数式是 $\frac{1}{{2}^{k}}$

C. 从 “ $n = k$ 到 $n = k + 1$ ” 左边需要增加 ${2}^{k}$ 项

D. 从 “ $n = k$ 到 $n = k + 1$ ” 左边需要增加的代数式是 $\frac{1}{{2}^{k - 1} + 1} + \frac{1}{{2}^{k - 1} + 2} + \cdots  + \frac{1}{{2}^{k}}$

【难度】★★

【答案】D

【解析】第一步应该验证当 $n = 2$ 时不等式成立,所以 $A$ 不正确;

因为 $\frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots  + \frac{1}{{2}^{k}} - \left( {\frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots  + \frac{1}{{2}^{k - 1}}}\right)  = \frac{1}{{2}^{k - 1} + 1} + \frac{1}{{2}^{k - 1} + 2} + \cdots \frac{1}{{2}^{k}}$ ,

所以从 “ $n = k$ 到 $n = k + 1$ ” 左边需要增加的代数式是 $\frac{1}{{2}^{k - 1} + 1} + \frac{1}{{2}^{k - 1} + 2} + \cdots  + \frac{1}{{2}^{k}}$ ,所以 $B$ 不正确;

所以从 “ $n = k$ 到 $n = k + 1$ ” 左边需要增加 ${2}^{k - 1}$ 项,所以 $C$ 不正确. 故选:D.

【例 9】某公司自 2020 年起，每年投入的设备升级资金为 500 万元，预计自 2020 年起 (2020 年为第 1 年)， 因为设备升级,第 $n$ 年可新增的盈利 ${a}_{n} = \left\{  \begin{array}{l} {80}\left( {n - 1}\right) , n \leq  5 \\  {1000}\left( {1 - {0.6}^{n - 5}}\right) , n \geq  6 \end{array}\right.$ (单位: 万元),求:

(1)第几年起，当年新增盈利超过当年设备升级资金；

(2)第几年起，累计新增盈利总额超过累计设备升级资金总额.

【难度】 $\star   \star   \star$

【答案】(1)第 7 年；(2)第 12 年.

【解析】(1)当 $n \leq  5$ 时， ${a}_{n} = {80}\left( {n - 1}\right)  > {500}$ ，解得 $n > {7.25}$ ，即 $n \geq  8$ ，不成立，

当 $n \geq  6$ 时， ${a}_{n} = {1000}\left( {1 - {0.6}^{n - 5}}\right)  > {500}$ ，即 ${0.6}^{n - 5} < {0.5}$ ， ${0.6}^{n - 5}$ 随着 $n$ 的增大而减小，

当 $n = 6$ 时， ${0.6}^{6 - 5} = {0.6} < {0.5}$ 不成立，当 $n = 7$ 时， ${0.6}^{7 - 5} = {0.36} < {0.5}$ 成立，

故第 7 年起, 当年新增盈利超过当年设备升级资金;

( 2 )当 $n = 5$ 时，累计新增盈利总额

${S}_{5} = {a}_{1} + {a}_{2} + {a}_{3} + {a}_{4} + {a}_{5} = 0 + {80} + {160} + {240} + {320} = {800} < {500} \times  5$ ,

可得所求 $n$ 超过 5,

当 $n \geq  6$ 时, ${S}_{n} = {S}_{5} + {1000}\left( {n - 5}\right)  - \frac{{600}\left( {1 - {0.6}^{n - 5}}\right) }{1 - {0.6}} > {500n}$ ,

整理得 $n + 3 \times  {0.6}^{n - 5} > {11.4}$ ,由于 $3 \times  {0.6}^{n - 5}$ 随着 $n$ 的增大而减小

又当 $n = {11}$ 时， ${11} + 3 \times  {0.6}^{{11} - 5} < {11.4}$ ，故不成立，

当 $n = {12}$ 时, ${12} + 3 \times  {0.6}^{{12} - 5} > {11.4}$ ,故成立,

故从第 12 年起, 累计新增盈利总额超过累计设备升级资金总额.

巩固训练

1、 $\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{2a}{n}^{2} - {bn} + c}{{2n} - 3} =  - 2$ ，则 $a + b =$ ( )

A. -4 B. 4 C. 1 D. -1

【答案】B

【解析】当 $a \neq  0$ 时,极限不存在,所以 $a = 0$ ,

$\mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{{2a}{n}^{2} - {bn} + c}{{2n} - 3} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{-{bn} + c}{{2n} - 3} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{\frac{-{bn}}{n} + \frac{c}{n}}{\frac{2n}{n} - \frac{3}{n}} = \mathop{\lim }\limits_{{n \rightarrow  \infty }}\frac{-b + \frac{c}{n}}{2 - \frac{3}{n}} =  - \frac{b}{2} =  - 2$ ,

所以 $b = 4$ ,所以 $a + b = 0 + 4 = 4$ ,故选: B

2、无穷等比数列 $\left\{  {a}_{n}\right\}$ 中， $\mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {{a}_{1} + {a}_{2} + \cdots  + {a}_{n}}\right)  = \frac{1}{2}$ ，则首项 ${a}_{1}$ 的取值范围是( )

A. $\left( {0,1}\right)$ B. $\left( {0,\frac{1}{2}}\right)  \cup  \left( {\frac{1}{2},1}\right)$ C. $\left( {-1,1}\right)$ D. $\left( {-1,0}\right)  \cup  \left( {0,1}\right)$

【答案】B

【解析】由题意,无穷等比数列 $\left\{  {a}_{n}\right\}$ 中, $\mathop{\lim }\limits_{{n \rightarrow  \infty }}\left( {{a}_{1} + {a}_{2} + \cdots  + {a}_{n}}\right)  = \frac{1}{2}$ ,

可得 $\frac{{a}_{1}}{1 - q} = \frac{1}{2}$ ,且 $- 1 < q < 1$ 且 $q \neq  0$ ,所以 ${a}_{1} = \frac{1}{2}\left( {1 - q}\right)$ ,

因为 $- 1 < q < 1$ 且 $q \neq  0$ ,所以 $0 < {a}_{1} < 1$ 且 ${a}_{1} \neq  \frac{1}{2}$ .

即首项 ${a}_{1}$ 的取值范围是 $\left( {0,\frac{1}{2}}\right)  \cup  \left( {\frac{1}{2},1}\right)$ . 故选: B.

3、在 $n$ 行 $n$ 列矩阵 $\left( \begin{matrix} 1 & 2 & 3 & \cdots & n - 2 & n - 1 & n \\  2 & 3 & 4 & \cdots & n - 1 & n & 1 \\  3 & 4 & 5 & \cdots & n & 1 & 2 \\  \cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\  n & 1 & 2 & \cdots & n - 3 & n - 2 & n - 1 \end{matrix}\right)$ 中,若记位于第 $\mathbf{i}$ 行第 $\mathbf{j}$ 列的数为 ${a}_{ij}\left( {i, j = 1,2,\cdots , n}\right)$ ，则当 $n = {11}$ 时， ${a}_{11} + {a}_{22} + {a}_{33} + \cdots  + {a}_{1111} =$ ___.

【答案】66

【解析】由题,若记位于第 $\mathrm{i}$ 行第 $j$ 列的数为 ${a}_{ij}\left( {i, j = 1,2,\cdots , n}\right)$ ,当 $n = {11}$ 时,

${a}_{11} = 1,{a}_{22} = 2 + 1 = 3,{a}_{33} = 3 + 2 = 5,{a}_{44} = 4 + 3 = 7,{a}_{55} = 5 + 4 = 9$ ,

${a}_{66} = 6 + 5 = {11},{a}_{77} = 7 + 6 - {11} = 2,{a}_{88} = 8 + 7 - {11} = 4,{a}_{99} = 9 + 8 - {11} = 6$ ,

${a}_{1010} = {10} + 9 - {11} = 8,{a}_{1111} = {11} + {10} - {11} = {10},$

所以， ${a}_{11} + {a}_{22} + {a}_{33} + \cdots  + {a}_{1111} = 1 + 3 + 5 + 7 + 9 + {11} + 2 + 4 + 6 + 8 + {10} = {66}$ ，故答案为:66

4、数列 $\left\{  {a}_{n}\right\}$ 由 $k$ 个不同的数组成， ${S}_{n}$ 为 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和，若对任意 $n \in  {N}^{ * }$ ， ${S}_{n} \in  \{ 1,3\}$ ，则 $k$ 的最大值为___

【答案】 4

【解析】

$\because$ 对任意 $n \in  N * ,{S}_{n} \in  \{ 1,3\} ,\therefore {a}_{1} = {S}_{1} \in  \{ 1,3\} ,\therefore {a}_{1} = 1$ 或 ${a}_{1} = 3$ ,

当 $n \geq  2$ 时, ${a}_{n} = {S}_{n} - {S}_{n - 1},\therefore {a}_{n}$ 可能的值只有 $0,2, - 2$ ,三种情况,

故数列 $\left\{  {a}_{n}\right\}$ 最多有 $1,0,2, - 2$ ,或 $3,0,2, - 2$ 四个数字组成,故答案为 4 .

5、等比数列 $\left\{  {a}_{n}\right\}$ 的前 $\mathrm{n}$ 项和 ${S}_{n} = {3}^{n + 1} + a$ ( $\mathrm{a}$ 为常数)， ${b}_{n} = \frac{1}{{a}_{n}^{2}}$ ，则数列 $\left\{  {b}_{n}\right\}$ 的前 $\mathrm{n}$ 项和为___. 【答案】 $\frac{1}{32} \times  \left\lbrack  {1 - {\left( \frac{1}{9}\right) }^{n}}\right\rbrack$

【解析】因为 ${S}_{n} = {3}^{n + 1} + a = 3 \times  {3}^{n} + a$ ,所以根据等比数列前 $\mathbf{n}$ 项和特征得 $a =  - 3$ ,首项为 ${3}^{1 + 1} - 3 = 6$ , 公比为 3,因此 ${b}_{n} = \frac{1}{{a}_{n}^{2}} = \frac{1}{{\left( 6 \times  {3}^{n - 1}\right) }^{2}} = \frac{1}{36} \times  {\left( \frac{1}{9}\right) }^{n - 1}$ ,数列 $\left\{  {b}_{n}\right\}$ 的前 $\mathrm{n}$ 项和为 $\frac{1}{36} \times  \frac{1 - {\left( \frac{1}{9}\right) }^{n}}{1 - \frac{1}{9}} = \frac{1}{32} \times  \left\lbrack  {1 - {\left( \frac{1}{9}\right) }^{n}}\right\rbrack  .$

6、已知正项等比数列 $\left\{  {a}_{n}\right\}$ 的前 $\mathrm{n}$ 项和为 ${S}_{n}$ . 若 $7{S}_{6} = 3{S}_{9},{a}_{4} = 2$ ,则 $\left\{  {{a}_{{3n} - 2} + {\log }_{2}{a}_{n}}\right\}$ 的前 $\mathrm{n}$ 项和 ${T}_{n} =$ ___.

【答案】 ${2}^{n} + \frac{{n}^{2} - n}{6} - 1$

【解析】由已知得 $q \neq  1,\therefore 7\frac{{a}_{1}\left( {1 - {q}^{6}}\right) }{1 - q} = 3\frac{{a}_{1}\left( {1 - {q}^{9}}\right) }{1 - q}$ ,解得 ${q}^{3} = 2$ . 又因为 ${a}_{4} = 2$ ,所以 ${a}_{1} = 1$ . 所以 ${a}_{n} = {2}^{\frac{n - 1}{3}}$ . 所以 ${a}_{{3n} - 2} + {\log }_{2}{a}_{n} = {2}^{n - 1} + \frac{n - 1}{3}$ .

令 ${a}_{n} = {2}^{n - 1},{b}_{n} = \frac{n - 1}{3},{c}_{1} = {2}^{n - 1} + \frac{n - 1}{3}$

${T}_{n} = {c}_{1} + {c}_{2} + {c}_{3} + \cdots {c}_{n} = \left( {{a}_{1} + {a}_{2} + {a}_{3} + \cdots {a}_{n}}\right)  + \left( {{b}_{1} + {b}_{2} + {b}_{3} + \cdots {b}_{n}}\right)$

而 ${a}_{1} + {a}_{2} + {a}_{3} + \cdots {a}_{n} = \frac{1 \times  \left( {1 - {2}^{n}}\right) }{1 - 2} = {2}^{n} - 1,{b}_{1} + {b}_{2} + {b}_{3} + \cdots {b}_{n} = 0 \times  n + \frac{n\left( {n - 1}\right) }{2} \times  \frac{1}{3} = \frac{{n}^{2} - n}{6}$ ,

所以 ${T}_{n} = {2}^{n} + \frac{{n}^{2} - n}{6} - 1$ .

7、设数列 $\left\{  {a}_{n}\right\}$ 是以 2 为首项，1 为公差的等差数列， $\left\{  {b}_{n}\right\}$ 是以 1 为首项，2 为公比的等比数列，则 ${a}_{{b}_{1}} + {a}_{{b}_{2}} + {a}_{{b}_{3}} + \cdots  + {a}_{{b}_{10}} =$ ___.

【答案】1033

【解析】: 数列 $\left\{  {a}_{n}\right\}$ 是以 2 为首项,1 为公差的等差数列, $\therefore {a}_{n} = 2 + \left( {n - 1}\right)  \times  1 = n + 1$ ,

$\because \left\{  {b}_{n}\right\}$ 是以 1 为首项,2 为公比的等比数列, $\therefore {b}_{n} = 1 \times  {2}^{n - 1} = {2}^{n - 1},\therefore {a}_{{b}_{n}} = {2}^{n - 1} + 1$ ,

$\therefore {a}_{{b}_{1}} + {a}_{{b}_{2}} + {a}_{{b}_{3}} + \cdots  + {a}_{{b}_{10}} = \frac{1 - {2}^{10}}{1 - 2} + {10} = {1033}$ . 故答案为: 1033.

8、已知等差数列 $\left\{  {a}_{n}\right\}$ 满足 $\left( {{a}_{1} + {a}_{2}}\right)  + \left( {{a}_{2} + {a}_{3}}\right)  + \cdots  + \left( {{a}_{n} + {a}_{n + 1}}\right)  = {2n}\left( {n + 1}\right) \left( {n \in  {N}^{ * }}\right)$ .

(1)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式;

(2)求数列 $\left\{  \frac{{a}_{n}}{{2}^{n}}\right\}$ 的前 $n$ 项和 ${S}_{n}$ .

【答案】( 1 ) ${a}_{n} = {2n} - 1$ ；( 2 ) ${S}_{n} = 3 - \frac{{2n} + 3}{{2}^{n}}$ .

【解析】(1)设等差数列 $\left\{  {a}_{n}\right\}$ 的公差为 $d$ ，

由已知得 $\left\{  \begin{array}{l} {a}_{1} + {a}_{2} = 4 \\  \left( {{a}_{1} + {a}_{2}}\right)  + \left( {{a}_{2} + {a}_{3}}\right)  = {12} \end{array}\right.$ ,即 $\left\{  \begin{array}{l} {a}_{1} + {a}_{2} = 4 \\  {a}_{2} + {a}_{3} = 8 \end{array}\right.$ ,所以 $\left\{  \begin{array}{l} {a}_{1} + \left( {{a}_{1} + d}\right)  = 4 \\  \left( {{a}_{1} + d}\right)  + \left( {{a}_{1} + {2d}}\right)  = 8 \end{array}\right.$ ,

解得 $\left\{  \begin{array}{l} {a}_{1} = 1 \\  d = 2 \end{array}\right.$ ,所以 ${a}_{n} = {2n} - 1$ .

(2)由(1)得 $\frac{{a}_{n}}{{2}^{n}} = \frac{{2n} - 1}{{2}^{n}}$ ，所以 ${S}_{n} = \frac{1}{{2}^{1}} + \frac{3}{{2}^{2}} + \ldots  + \frac{{2n} - 3}{{2}^{n - 1}} + \frac{{2n} - 1}{{2}^{n}}$ ，①

$\frac{1}{2}{S}_{n} = \frac{1}{{2}^{2}} + \frac{3}{{2}^{3}} + \ldots \ldots  + \frac{{2n} - 3}{{2}^{n}} + \frac{{2n} - 1}{{2}^{n + 1}}$ ,②

①-② 得: $\frac{1}{2}{S}_{n} = \frac{1}{2} + 2 \times  \left( {\frac{1}{{2}^{2}} + \ldots  + \frac{1}{{2}^{n}}}\right)  - \frac{{2n} - 1}{{2}^{n + 1}} = \frac{3}{2} - \frac{{2n} + 3}{{2}^{n + 1}}$ ，所以 ${S}_{n} = 3 - \frac{{2n} + 3}{{2}^{n}}$ .

9、根据预测，疫情期间，某医院第 $n\left( {n \in  {\mathbf{N}}^{ * }}\right)$ 天口罩供应量和消耗量分别为 ${a}_{n}$ 和 ${b}_{n}$ (单位:个)，其中 ${a}_{n} = \left\{  {\begin{array}{l} 5{n}^{4} + {15},1 \leq  n \leq  3 \\   - {10n} + {470}, n \geq  4 \end{array},{b}_{n} = n + 5}\right.$ ,第 $n$ 天末的口罩保有量是前 $n$ 天的累计供应量与消耗量的差.

(1)求该医院第 4 天末的口罩保有量；

(2)已知该医院口罩仓库在第 $n$ 天末的口罩容纳量 ${S}_{n} =  - 4{\left( n - {46}\right) }^{2} + {8800}$ (单位:个). 设在某天末， 口罩保有量达到最大, 问该保有量是否超出了此时仓库的口罩容纳量?

【答案】(1) 935；(2)第42天末，口罩保有量达到最大超过了.

【解析】(1)第 4 天末的口罩保有量是前 4 天口罩供应量和消耗量之差,

将 $n = 1,2,3,4$ 代入 ${a}_{n}$ 和 ${b}_{n}$ 得第 4 天末的口罩保有量为:

$\left( {{a}_{1} + {a}_{2} + {a}_{3} + {a}_{4}}\right)  - \left( {{b}_{1} + {b}_{2} + {b}_{3} + {b}_{4}}\right)  = \left( {{20} + {95} + {420} + {430}}\right)  - \left( {6 + 7 + 8 + 9}\right)  = {935},$

所以该医院第 4 天末的口罩保有量为 935 ;

(2)当 ${a}_{n} > {b}_{n}$ 时，保有量始终增加.

即 $- {10n} + {470} \geq  n + 5$ ， $n$ 为正整数，解得 $n \leq  {42}$ ，

即第 42 天末的时候，保有量达到最大，

此时 $\left( {{a}_{1} + {a}_{2} + {a}_{3} + \cdots  + {a}_{42}}\right)  - \left( {{b}_{1} + {b}_{2} + {b}_{3} + \cdots  + {b}_{42}}\right)$

$= {965} + \frac{\left( {{420} + {50}}\right)  \times  {38}}{2} - \frac{\left( {6 + {47}}\right)  \times  {42}}{2} = {8782}$ ,

而容纳量为 ${S}_{42} =  - 4{\left( {42} - {46}\right) }^{2} + {8800} = {8736}$ ,

而 ${8782} > {8736}$ ,所以保有量超过了容纳量.

## (三)数列综合

数列一教师版

## 例题精讲

【例 10】已知数列 $\left\{  {a}_{n}\right\}$ 的奇数项是首项为 1,公差为 $d$ 的等差数列,偶数项是首项为 2,公比为 $q$ 的等比数列.数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,且满足 ${S}_{3} = {a}_{4},{a}_{3} + {a}_{5} = 2 + {a}_{4}$ .

(1)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)设实数 $M > 0$ ，若对于任意 $k \in  {N}^{ * }$ ，都有 $\frac{{S}_{{2k} - 1}}{{a}_{2k}} \in  (0, M\rbrack$ ，求 $M$ 的最小值.

【难度】 $\star   \star   \star$

【答案】( 1 ) ${a}_{n} = \left\{  \begin{array}{l} n, n\text{ 是奇数 } \\  2 \times  {3}^{\frac{n - 2}{2}}, n\text{ 是偶数 } \end{array}\right.$ ( 2 ) 1 .

【解析】(1)由题意可得 ${a}_{1} = 1,{a}_{2} = 2$ ,

因为 ${S}_{3} = {a}_{4},{a}_{3} + {a}_{5} = 2 + {a}_{4}$ ,

所以 $\left\{  \begin{array}{l} {a}_{1} + {a}_{2} + {a}_{3} = {a}_{4} \\  {a}_{3} + {a}_{5} = 2 + {a}_{4} \end{array}\right.$ ,即 $\left\{  \begin{array}{l} 1 + 2 + 1 + d = {2q} \\  1 + d + 1 + {2d} = 2 + {2q} \end{array}\right.$ 整理得: $\left\{  \begin{array}{l} 4 + d = {2q} \\  {3d} = {2q} \end{array}\right.$

解得: $\left\{  \begin{array}{l} d = 2 \\  q = 3 \end{array}\right.$ ,所以 ${a}_{n} = \left\{  \begin{array}{l} n, n\text{ 是奇数 } \\  2 \times  {3}^{\frac{n - 2}{2}}, n\text{ 是偶数 } \end{array}\right.$ ,

${S}_{{2k} - 1} = \left( {{a}_{1} + {a}_{3} + \cdots  + {a}_{{2k} - 1}}\right)  + \left( {{a}_{2} + {a}_{4} + \cdots  + {a}_{{2k} - 2}}\right)  = \left( {1 + 3 + 5 + \cdots  + {2k} - 1}\right)  + 2 \times  \left( {{3}^{0} + {3}^{1} + \cdots  + {3}^{k - 2}}\right)$

$= \frac{k\left( {1 + {2k} - 1}\right) }{2} + 2 \times  \frac{1 \times  \left( {1 - {3}^{k - 1}}\right) }{1 - 3} = {k}^{2} + {3}^{k - 1} - 1$ ,

${a}_{2k} = 2 \times  {3}^{\frac{{2k} - 2}{2}} = 2 \times  {3}^{k - 1}$ ,所以 $\frac{{S}_{{2k} - 1}}{{a}_{2k}} = \frac{{k}^{2} + {3}^{k - 1} - 1}{2 \times  {3}^{k - 1}} = \frac{{k}^{2} - 1}{2 \times  {3}^{k - 1}} + \frac{1}{2}$ ,

令 $f\left( k\right)  = \frac{{k}^{2} - 1}{2 \times  {3}^{k - 1}} + \frac{1}{2}$ ,则 $f\left( {k + 1}\right)  - f\left( k\right)  = \frac{{\left( k + 1\right) }^{2} - 1}{2 \times  {3}^{k}} - \frac{{k}^{2} - 1}{2 \times  {3}^{k - 1}} = \frac{-2{k}^{2} + {2k} + 3}{2 \times  {3}^{k}}$ ,

令 $g\left( k\right)  =  - 2{k}^{2} + {2k} + 3$ ,对称轴为 $k = \frac{1}{2}$ ,

所以 $g\left( k\right)  =  - 2{k}^{2} + {2k} + 3$ 随 $k$ 的增大而减小,

$g\left( 1\right)  = 3 > 0, g\left( 2\right)  =  - 2 \times  {2}^{2} + 2 \times  2 + 3 =  - 1 < 0$ ,所以 $f\left( 2\right)  > f\left( 1\right) , f\left( 2\right)  > f\left( 3\right)  > f\left( 4\right)  > \cdots ,$

所以 $k = 2$ 时, $f\left( k\right)  = \frac{{k}^{2} - 1}{2 \times  {3}^{k - 1}} + \frac{1}{2}$ 最大值为 $f\left( 2\right)  = \frac{{2}^{2} - 1}{2 \times  {3}^{1}} + \frac{1}{2} = 1$ ,所以 $M \geq  1$ ,所以 $M$ 的最小值为 1 .

【例 11】已知点列 ${A}_{n}\left( {{x}_{n},0}\right)$ 满足: $\overrightarrow{{A}_{0}{A}_{n}} \cdot  \overrightarrow{{A}_{1}{A}_{n + 1}} = a - 1, n$ 是自然数，且 ${x}_{0} =  - 1,{x}_{1} = 1, a > 1$ .

(1)若 ${x}_{n + 1} = f\left( {x}_{n}\right)$ ，求 $f\left( x\right)$ 的表达式；

(2)已知点 $B\left( {\sqrt{a},0}\right)$ ，记 ${a}_{n} = \left| {B{A}_{n}}\right|$ ，且数列 $\left\{  {a}_{n}\right\}$ 单调递减，求 $a$ 的取值范围；

(3)设(2)中的数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ，证明: ${S}_{n} < \frac{\sqrt{a} - 1}{2 - \sqrt{a}}$ .

【难度】 $\star   \star   \star$

【答案】( 1 ) $f\left( x\right)  = \frac{x + a}{x + 1}$ ；( 2 ) $a \in  (1,4\rbrack$ ；( 3 )证明见解析.

【解析】

(1) $\because {A}_{0}\left( {-1,0}\right) ,{A}_{1}\left( {1,0}\right) ,\therefore \overrightarrow{{A}_{0}{A}_{n}} \cdot  \overrightarrow{{A}_{1}{A}_{n + 1}} = \left( {{x}_{n} + 1}\right) \left( {{x}_{n + 1} - 1}\right)  = a - 1$ ，

$\therefore {x}_{n + 1} = f\left( {x}_{n}\right)  = \frac{a - 1}{{x}_{n} + 1} + 1 = \frac{{x}_{n} + a}{{x}_{n} + 1},\therefore f\left( x\right)  = \frac{x + a}{x + 1}$ .

(2) $\because \overrightarrow{B{A}_{n}} = \left( {{x}_{n} - \sqrt{a},0}\right) ,\therefore {a}_{n} = \left| {B{A}_{n}}\right|  = \left| {{x}_{n} - \sqrt{a}}\right|$ ,

$\because {a}_{n + 1} = \left| {{x}_{n + 1} - \sqrt{a}}\right|  = \left| {f\left( {x}_{n}\right)  - \sqrt{a}}\right|  = \left| {\frac{{x}_{n} + a}{{x}_{n} + 1} - \sqrt{a}}\right|$

$= \frac{\left( \sqrt{a} - 1\right) }{\left| {x}_{n} + 1\right| } \cdot  \left| {{x}_{n} - \sqrt{a}}\right|  < \left( {\sqrt{a} - 1}\right)  \cdot  \left| {{x}_{n} - \sqrt{a}}\right|  = \left( {\sqrt{a} - 1}\right) {a}_{n},$

要使 ${a}_{n + 1} < {a}_{n}$ 成立,只要 $0 < \sqrt{a} - 1 \leq  1$ ,即 $1 < a \leq  4.\therefore a$ 的取值范围为 $(1,4\rbrack$ .

(3) ${a}_{n + 1} = \left( {\sqrt{a} - 1}\right) \left| {{x}_{n} - \sqrt{a}}\right|  < {\left( \sqrt{a} - 1\right) }^{2}\left| {{x}_{n - 1} - \sqrt{a}}\right|  < \cdots$

$< {\left( \sqrt{a} - 1\right) }^{n}\left| {{x}_{1} - \sqrt{a}}\right|  = {\left( \sqrt{a} - 1\right) }^{n + 1},\therefore {a}_{n} < {\left( \sqrt{a} - 1\right) }^{n}$ ,

$\therefore {S}_{n} = {a}_{1} + {a}_{2} + \cdots  + {a}_{n} < \left( {\sqrt{a} - 1}\right)  + {\left( \sqrt{a} - 1\right) }^{2} + \cdots  + {\left( \sqrt{a} - 1\right) }^{n}$

$= \frac{\left( {\sqrt{a} - 1}\right)  \cdot  \left\lbrack  {1 - {\left( \sqrt{a} - 1\right) }^{n}}\right\rbrack  }{2 - \sqrt{a}}, \; \because 1 < a \leq  4,\therefore 0 < \sqrt{a} - 1 \leq  1,\therefore 0 < {\left( \sqrt{a} - 1\right) }^{n} \leq  1,\therefore {S}_{n} < \frac{\sqrt{a} - 1}{2 - \sqrt{a}}$ .

【例 12】若 $\left\{  {a}_{n}\right\}$ 是等差数列,公差 $d \in  (0,\pi \rbrack$ ,数列 $\left\{  {b}_{n}\right\}$ 满足: ${b}_{n} = \sin \left( {a}_{n}\right) , n \in  {\mathbf{N}}^{ * }$ ,

记 $S = \left\{  {x \mid  x = {b}_{n}, n \in  {\mathbf{N}}^{ * }}\right\}$ .

(1)设 ${a}_{1} = 0, d = \frac{2}{3}\pi$ ，求集合 $S$ ；

(2)设 ${a}_{1} = \frac{\pi }{2}$ ，试求 $d$ 的值，使得集合 $S$ 恰有两个元素；

【难度】 $\star   \star   \star$

【答案】( 1 ) $\left\{  {-\frac{\sqrt{3}}{2},0,\frac{\sqrt{3}}{2}}\right\}$ ；( 2 ) $d = \frac{2}{3}\pi$ 或 $d = \pi$ ；

【解析】解: (1) $\because$ 等差数列 $\left\{  {a}_{n}\right\}$ 的公差 $d \in  (0,\pi \rbrack$ ,数列 $\left\{  {b}_{n}\right\}$ 满足 ${b}_{n} = \sin \left( {a}_{n}\right)$ ,集合 $S = \left\{  {x \mid  x = {b}_{n}, n \in  {N}^{ * }}\right\}$ . $\therefore$ 当 ${a}_{1} = 0, d = \frac{2\pi }{3}$ , 集合 $S = \left\{  {-\frac{\sqrt{3}}{2},0,\frac{\sqrt{3}}{2}}\right\}$ .

(2) $\because {a}_{1} = \frac{\pi }{2}$ ，数列 $\left\{  {b}_{n}\right\}$ 满足 ${b}_{n} = \sin \left( {a}_{n}\right)$ ，集合 $S = \left\{  {x \mid  x = {b}_{n}, n \in  {N}^{ * }}\right\}$ 恰好有两个元素，如图:

根据三角函数线,①等差数列 $\left\{  {a}_{n}\right\}$ 的终边落在 $y$ 轴的正负半轴上时,集合 $S$ 恰好有两个元素,此时 $d = \pi$ , ② ${a}_{1}$ 终边落在 ${OA}$ 上，要使得集合 $S$ 恰好有两个元素，可以使 ${a}_{2},{a}_{3}$ 的终边关于 $y$ 轴对称，如图 ${OB},{OC}$ ， 此时 $d = \frac{2\pi }{3}$ ,

综上, $d = \frac{2}{3}\pi$ 或者 $d = \pi$ .

## 巩固训练

1、设 ${S}_{n}$ 为数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和，“ $\left\{  {a}_{n}\right\}$ 是递增数列” 是 “ $\left\{  {S}_{n}\right\}$ 是递增数列” 的( )

A. 充分非必要条件 B. 必要非充分条件

C. 充要条件 D. 既非充分又非必要条件

【答案】D

【解析】解: 数列 $- 3, - 2, - 1,0$ . ___是递增数列，但 $\left\{  {S}_{n}\right\}$ 不是递增数列,即充分性不成立, 数列 $1,1,1,\ldots \ldots$ ,满足 $\left\{  {S}_{n}\right\}$ 是递增数列,但数列 $1,1,1,\ldots \ldots$ ,不是递增数列,即必要性不成立, 则 “ $\left\{  {a}_{n}\right\}$ 是递增数列” 是 “ $\left\{  {S}_{n}\right\}$ 是递增数列” 的既不充分也不必要条件,故选: $D$ .

数列一教师版

2、已知数列 $\left\{  {a}_{n}\right\}$ 满足 $\frac{1}{3}{a}_{n} \leq  {a}_{n + 1} \leq  3{a}_{n}, n \in  {N}^{ * },{a}_{1} = 1$ .

(1)若 ${a}_{2} = 2,{a}_{3} = x,{a}_{4} = 9$ ，求 $x$ 的取值范围；

(2)若 $\left\{  {a}_{n}\right\}$ 是等比数列，且 ${a}_{m} = \frac{1}{1000}$ ，求正整数 $m$ 的最小值，以及 $m$ 取最小值时相应 $\left\{  {a}_{n}\right\}$ 的公比；

(3)若 ${a}_{1},{a}_{2},\ldots {a}_{100}$ 成等差数列，求数列 ${a}_{1},{a}_{2},\ldots {a}_{100}$ 的公差的取值范围.

【答案】(1) $3 \leq  x \leq  6$ ； (2) $m$ 的最小值是8，此时 $q = {\left( \frac{1}{1000}\right) }^{\frac{1}{7}} = {10}^{-\frac{3}{7}}$ . ; (3) $\left\lbrack  {-\frac{2}{199},2}\right\rbrack$

【解析】解; (1) 由题意可得: $\frac{1}{3}{a}_{2} \leq  {a}_{3} \leq  3{a}_{2},\therefore \frac{2}{3} \leq  x \leq  6$ ;

又 $\frac{1}{3}{a}_{3} \leq  {a}_{4} \leq  3{a}_{3},\therefore 3 \leq  x \leq  {27}$ . 综上可得: $3 \leq  x \leq  6$ .

(2)设公比为 $q$ ，由已知可得， ${a}_{n} = {q}^{n - 1}$ ，又 $\frac{1}{3}{a}_{1} \leq  {a}_{2} \leq  3{a}_{1}$ ，

$\therefore \frac{1}{3} \leq  q \leq  3$ . 因此 ${a}_{m} = {q}^{m - 1} = \frac{1}{1000},\therefore \frac{1}{3} \leq  q < 1$ ,

$\therefore m = 1 - {\log }_{q}{1000} = 1 - \frac{1}{{\log }_{1000}q} = 1 - \frac{3}{\lg q} \geq  1 - \frac{3}{\lg \frac{1}{3}} = 1 + \frac{3}{\lg 3} \approx  {7.29}$ .

$\therefore m$ 的最小值是 8,因此 ${q}^{7} = \frac{1}{1000},\therefore q = {\left( \frac{1}{1000}\right) }^{\frac{1}{7}} = {10}^{-\frac{3}{7}}$ .

(3)设公差为 $d$ ，由已知可得 $\frac{1 + \left( {n - 1}\right) d}{3} \leq  1 + {nd} \leq  3\left\lbrack  {1 + \left( {n - 1}\right) d}\right\rbrack$ ; 即 $\left\{  \begin{array}{l} \left( {{2n} + 1}\right) d \geq   - 2 \\  \left( {{2n} - 3}\right) d \geq   - 2 \end{array}\right.$ ， 令 $n = 1$ ，得 $- \frac{2}{3} \leq  d \leq  2$ .

当 $2 \leq  n \leq  {99}$ 时，不等式即 $d \geq  \frac{-2}{{2n} + 1}, d \geq  \frac{-2}{{2n} - 3}.\therefore d \geq  \frac{-2}{199}$ .

综上可得: 公差 $d$ 的取值范围是 $\left\lbrack  {-\frac{2}{199},2}\right\rbrack$ .

3、已知数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n} = \frac{{n}^{2}}{8}\pi  + \left( {t - \frac{\pi }{8}}\right) n, n \in  {N}^{ * }, t \in  R$

(1)若 $t = \frac{\pi }{4}$ ，求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)设 ${f}^{-1}\left( x\right)$ 为 $f\left( x\right)$ 的反函数，称 $\left\{  {{f}^{-1}\left( n\right) }\right\}$ 为 $\{ f\left( n\right) \}$ 的反数列. 求证:当 $t \geq  1$ 时， $\left\{  {{a}_{n} + \frac{1}{{a}_{n}}}\right\}$ 存在反数列;

(3)若 $t \neq  \frac{\left( {{2k} - 1}\right) \pi }{4}, k \in  Z$ ，求 $\tan {a}_{1}\tan {a}_{2} + \tan {a}_{2}\tan {a}_{3} + \cdots  + \tan {a}_{2019}\tan {a}_{2020} + \tan {a}_{2020}\tan {a}_{1}$ 的值.

【答案】( 1 ) ${a}_{n} = \frac{\pi }{4}n$ ；( 2 )证明见解析；( 3 -2020.

【解析】解: (1) 当 $t = \frac{\pi }{4}$ 时,当 $n \geq  2$ 时, ${a}_{n} = {S}_{n} - {S}_{n - 1} = \frac{\pi }{4}n + t - \frac{\pi }{4} = \frac{\pi }{4}n$ , 当 $n = 1$ 时, ${a}_{1} = {S}_{1} = \frac{\pi }{4}$ 也满足上式,所以,数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = \frac{\pi }{4}n$ .

(2)由(1)知 ${a}_{n} = \frac{\pi }{4}n + t - \frac{\pi }{4},{a}_{n} \geq  t \geq  1$ ， $\left( {{a}_{n + 1} + \frac{1}{{a}_{n + 1}}}\right)  - \left( {{a}_{n} + \frac{1}{{a}_{n}}}\right)  = \frac{\left( {{a}_{n + 1} - {a}_{n}}\right) \left( {{a}_{n}{a}_{n + 1} - 1}\right) }{{a}_{n}{a}_{n + 1}} > 0$ ,即 ${a}_{n + 1} + \frac{1}{{a}_{n + 1}} > {a}_{n} + \frac{1}{{a}_{n}},\left\{  {{a}_{n} + \frac{1}{{a}_{n}}}\right\}$ 递增, 所以 $\left\{  {{a}_{n} + \frac{1}{{a}_{n}}}\right\}$ 存在反数列.

(3)由 $\tan \left( {{a}_{n + 1} - {a}_{n}}\right)  = \frac{\tan {a}_{n + 1} - \tan {a}_{n}}{1 + \tan {a}_{n + 1}\tan {a}_{n}}$ ，且 ${a}_{n + 1} - {a}_{n} = \frac{\pi }{4},{a}_{1} - {a}_{2020} =  - \frac{2019\pi }{4}$

$\tan {a}_{n + 1}\tan {a}_{n} = \frac{\tan {a}_{n + 1} - \tan {a}_{n}}{\tan \left( {{a}_{n + 1} - {a}_{n}}\right) } - 1 = \tan {a}_{n + 1} - \tan {a}_{n} - 1$ ,

$\tan {a}_{1}\tan {a}_{2020} = \frac{\tan {a}_{1} - \tan {a}_{2020}}{\tan \left( {{a}_{1} - {a}_{2020}}\right) } - 1 = \tan {a}_{1} - \tan {a}_{2020} - 1$

所以, $\tan {a}_{1}\tan {a}_{2} + \tan {a}_{2}\tan {a}_{3} + \cdots  + \tan {a}_{2019}\tan {a}_{2020} + \tan {a}_{2020}\tan {a}_{1} =$

$\left( {\tan {a}_{2} - \tan {a}_{1} - 1}\right)  + \left( {\tan {a}_{3} - \tan {a}_{2} - 1}\right)  + \cdots  + \left( {\tan {a}_{2020} - \tan {a}_{2019} - 1}\right)  + \left( {\tan {a}_{1} - \tan {a}_{2020} - 1}\right)  =  - {2020}$ .

## (四)数列新定义

## 例题精讲

【例 13】给定无穷数列 $\left\{  {a}_{n}\right\}$ ,若无穷数列 $\left\{  {b}_{n}\right\}$ 满足: 对任意 $n \in  {N}^{ * }$ ,都有 $\left| {{b}_{n} - {a}_{n}}\right|  \leq  1$ ,则称 $\left\{  {b}_{n}\right\}$ 与 $\left\{  {a}_{n}\right\}$ “接近”.

(1)设 $\left\{  {a}_{n}\right\}$ 是首项为 1，公比为 $\frac{1}{2}$ 的等比数列， ${b}_{n} = {a}_{n + 1} + 1, n \in  {N}^{ * }$ ，判断数列 $\left\{  {b}_{n}\right\}$ 是否与 $\left\{  {a}_{n}\right\}$ 接近， 并说明理由;

(2)设数列 $\left\{  {a}_{n}\right\}$ 的前四项为: ${a}_{1} = 1,{a}_{2} = 2,{a}_{3} = 4,{a}_{4} = 8$ ， $\left\{  {b}_{n}\right\}$ 是一个与 $\left\{  {a}_{n}\right\}$ 接近的数列，记集合 $M = \left\{  {x \mid  x = {b}_{i}, i = 1,2,3,4}\right\}$ ,求 $M$ 中元素的个数 $m$ ;

【难度】 $\star   \star   \star$

【答案】(1)是；(2) $m = 3$ 或4；

【解析】(1) $\left| {{b}_{n} - {a}_{n}}\right|  = 1 - \frac{1}{{2}^{n}} \leq  1$ ，所以 $\left\{  {b}_{n}\right\}$ 与 $\left\{  {a}_{n}\right\}$ “接近”；

(2) ${b}_{1} \in  \left\lbrack  {0,2}\right\rbrack  ,{b}_{2} \in  \left\lbrack  {1,3}\right\rbrack  ,{b}_{3} \in  \left\lbrack  {3,5}\right\rbrack  ,{b}_{4} \in  \left\lbrack  {7,9}\right\rbrack  , M = \left\{  {x \mid  x = {b}_{i}, i = 1,2,3,4}\right\}$ 元素个数 $m = 3$ 或 4 ；

【例 14】对于数列 $\left\{  {a}_{n}\right\}$ 与 $\left\{  {b}_{n}\right\}$ ,若对数列 $\left\{  {c}_{n}\right\}$ 的每一项 ${c}_{k}$ ,均有 ${c}_{k} = {a}_{k}$ 或 ${c}_{k} = {b}_{k}$ ,则称数列 $\left\{  {c}_{n}\right\}$ 是 $\left\{  {a}_{n}\right\}$ 与 $\left\{  {b}_{n}\right\}$ 的一个 “并数列”;

(1)设数列 $\left\{  {a}_{n}\right\}$ 与 $\left\{  {b}_{n}\right\}$ 的前三项分别为 ${a}_{1} = 1,{a}_{2} = 3,{a}_{3} = 5,{b}_{1} = 1,{b}_{2} = 2,{b}_{3} = 3$ ，若数列 $\left\{  {c}_{n}\right\}$ 是 $\left\{  {a}_{n}\right\}$ 与 $\left\{  {b}_{n}\right\}$ 的一个 “并数列”,求所有可能的有序数组 $\left( {{c}_{1},{c}_{2},{c}_{3}}\right)$ ;

(2)已知数列 $\left\{  {a}_{n}\right\}$ 、 $\left\{  {c}_{n}\right\}$ 均为等差数列， $\left\{  {a}_{n}\right\}$ 的公差为1，首项为正整数 $t$ ， $\left\{  {c}_{n}\right\}$ 的前 10 项和为-30， 前 20 项和为 -260,若存在唯一的数列 $\left\{  {b}_{n}\right\}$ ,使得 $\left\{  {c}_{n}\right\}$ 是 $\left\{  {a}_{n}\right\}$ 与 $\left\{  {b}_{n}\right\}$ 的一个 “并数列”,求 $t$ 的值所构成的集合;

【难度】 $\star   \star   \star$

【答案】(1) $\left( {1,3,5}\right) ,\left( {1,3,3}\right) ,\left( {1,2,5}\right) ,\left( {1,2,3}\right)$ ; (2) $\left\{  {t \mid  t \neq  3, t \neq  6, t \in  {N}^{ * }}\right\}$ ;

【解析】解: (1) $\left( {1,2,3}\right) ,\left( {1,2,5}\right) ,\left( {1,3,3}\right) ,\left( {1,3,5}\right)$ ;

(2) ${a}_{n} = t + n - 1$

设 $\left\{  {c}_{n}\right\}$ 的前 10 项和为 ${T}_{n},{T}_{10} =  - {30},{T}_{20} =  - {260}$ ,得 $d =  - 2,{c}_{1} = 6$ ,所以 ${C}_{n} = 8 - {2n};{c}_{k} = {a}_{k}$ 或

${c}_{k} = {b}_{k}$ . 当 ${c}_{k} = {a}_{k}$ 时, $8 - {2k} = t + k - 1, t = 9 - {3k} \in  {N}^{ * }, k \in  {N}^{ * }$ ,

$\therefore k = 1, t = 6$ ; 或 $k = 2, t = 3$ ,所以 $k \geq  3.k \in  {N}^{ * }$ 时, ${c}_{k} = {b}_{k}$ ,

$\because$ 数列 $\left\{  {b}_{n}\right\}$ 唯一,所以只要 ${b}_{1},{b}_{2}$ 唯一确定即可.

显然, $t = 6$ ,或 $t = 3$ 时, ${b}_{1},{b}_{2}$ 不唯一,

$t \in  {N}^{ * }$ 且 $t \neq  3, t \neq  6$ ,

即 $\left\{  {t \mid  t \in  {N}^{ * }\text{ 且 }t \neq  3, t \neq  6}\right\}$

## 巩固训练

1、已知有序数列 $\left\{  {a}_{n}\right\}$ 的各项均不相等,将 $\left\{  {a}_{n}\right\}$ 的项从大到小重新排序后相应的项数构成新数列 $\left\{  {p}_{n}\right\}$ ,称 $\left\{  {p}_{n}\right\}$ 为 $\left\{  {a}_{n}\right\}$ 的“序数列”. 例如:数列 ${a}_{1},{a}_{2},{a}_{3}$ 满足 ${a}_{1} > {a}_{3} > {a}_{2}$ ，则其“序数列” $\left\{  {p}_{n}\right\}$ 为1,3,2.

(1)若数列 $\left\{  {a}_{n}\right\}$ 的通项公式为 ${a}_{n} = {\left( -2\right) }^{n}\left( {n = 1,2,3,4}\right)$ ，写出 $\left\{  {a}_{n}\right\}$ 的“序数列”；

(2)若项数不少于 5 项的有穷数列 $\left\{  {b}_{n}\right\}  ,\left\{  {c}_{n}\right\}$ 的通项公式分别为 ${b}_{n} = n \cdot  {\left( \frac{3}{5}\right) }^{n}$ ， ${c}_{n} =  - {n}^{2} + {tn}$ ，且 $\left\{  {b}_{n}\right\}$ “序数列”与 $\left\{  {c}_{n}\right\}$ 的“序数列”相同，求实数 $t$ 的取值范围；

(3)已知有序数列 $\left\{  {a}_{n}\right\}$ 的“序数列”为 $\left\{  {p}_{n}\right\}$ . 求证: “ $\left\{  {p}_{n}\right\}$ 为等差数列”的充要条件是 “ $\left\{  {a}_{n}\right\}$ 为单调数列”.

【答案】(1) $4,2,1,3;$ (2) $\left( {4,5}\right)$ ；(3)证明见解析.

【解析】(1)由 ${a}_{n} = {\left( -2\right) }^{n}\left( {n = 1,2,3,4}\right)$ ,可得 ${a}_{1} =  - 2,{a}_{2} = 4,{a}_{3} =  - 8,{a}_{4} = {16}$

${a}_{4} > {a}_{2} > {a}_{1} > {a}_{3},\left\{  {a}_{n}\right\}$ 的“序数列”为:4,2,1,3

(2)由题意得，因为 ${b}_{n} = n \cdot  {\left( \frac{3}{5}\right) }^{n}\left( {n \in  {N}^{ * }}\right)$ ，所以 ${b}_{n + 1} - {b}_{n} = \frac{3 - {2n}}{5} \cdot  {\left( \frac{3}{5}\right) }^{n}$

当 $n \geq  2$ 时, ${b}_{n + 1} - {b}_{n} < 0$ ,即 ${b}_{n + 1} < {b}_{n}$ ;

${b}_{1} = \frac{3}{5},{b}_{2} = \frac{18}{25},{b}_{3} = \frac{81}{125},{b}_{4} = \frac{324}{625}$

${b}_{2} > {b}_{3} > {b}_{1} > {b}_{4} > {b}_{5} > \ldots  > {b}_{n - 1} > {b}_{n}$

又因为 ${c}_{n} =  - {n}^{2} + {tn}\left( {n \in  {N}^{ * }}\right)$ ,且 $\left\{  {b}_{n}\right\}$ 的序数列与 $\left\{  {c}_{n}\right\}$ 的序数列相同

所以 ${c}_{2} > {c}_{3} > {c}_{1} > {c}_{4} > {c}_{5} > \ldots  > {c}_{n - 1} > {c}_{n}$

又因为 ${c}_{1} = t - 1,{c}_{2} = {2t} - 4,{c}_{3} = {3t} - 9$ ,所以 ${2t} - 4 > {3t} - 9 > t - 1$ ; 所以 $4 < t < 5$ 即 $t \in  \left( {4,5}\right)$

(3)充分条件:

因为有穷数列 $\left\{  {a}_{n}\right\}$ 的序数列 $\left\{  {P}_{n}\right\}$ 为等差数列,所以① $\left\{  {P}_{n}\right\}$ 为 1，2，3， $\cdots$ ， $n - 2$ ， $n - 1$ ， $n$ 所以有穷数列 $\left\{  {a}_{n}\right\}$ 为递减数列,

② $\left\{  {P}_{n}\right\}$ 为 $n, n - 1, n - 2,\cdots ,3,2,1$ ，所以有穷数列 $\left\{  {a}_{n}\right\}$ 为递增数列，

所以由①②，有穷数列 $\left\{  {a}_{n}\right\}$ 为单调数列

必要条件: 因为有穷数列 $\left\{  {a}_{n}\right\}$ 为单调数列,所以①有穷数列 $\left\{  {a}_{n}\right\}$ 为递减数列

则 $\left\{  {P}_{n}\right\}$ 为 $1,2,3,\cdots , n - 2, n - 1, n$ 的等差数列

② 有穷数列 $\left\{  {a}_{n}\right\}$ 为递增数列,则 $\left\{  {P}_{n}\right\}$ 为 $n, n - 1, n - 2,\cdots ,3,2,1$ 的等差数列

所以由①②，序数列 $\left\{  {P}_{n}\right\}$ 为等差数列

综上,有穷数列 $\left\{  {a}_{n}\right\}$ 的序数列 $\left\{  {P}_{n}\right\}$ 为等差数列的充要条件是有穷数列 $\left\{  {a}_{n}\right\}$ 为单调数列

数列一教师版

2、对于给定的区间 $\left\lbrack  {m, t}\right\rbrack$ 和非负数列 $A : {a}_{1},{a}_{2},\cdots ,{a}_{k}$ ,若存在 ${x}_{0},{x}_{1},\cdots ,{x}_{k}$ ,使 $\left| {{x}_{i} - {x}_{i - 1}}\right|  = {a}_{i}$ 成立,其中 ${x}_{i} \in  \left\lbrack  {m, t}\right\rbrack  ,\;i = 0,1,\cdots , k$ ,则称数列 $\mathrm{A}$ 可“嵌入”区间 $\left\lbrack  {m, t}\right\rbrack$ .

(1)分别指出下列数列是否可“嵌入”区间 $\left\lbrack  {0,2}\right\rbrack$ ；

① ${A}_{1} : 2,3$ ;

② ${A}_{2} : 1,0,1$ .

(2)已知数列 $\mathrm{A}$ 满足 ${a}_{n} = n\left( {n = 1,2,\cdots , k}\right)$ ，若数列 $\mathrm{A}$ 可“嵌入”区间 $\left\lbrack  {1,{m}_{0}}\right\rbrack  \left( {{m}_{0} \in  {N}^{ * }}\right)$ ，求数列 $\mathrm{A}$ 的项数 $k$ 的最大值;

(3)求证:任取数列 $A : {a}_{1},{a}_{2},\cdots ,{a}_{2021}$ 满足 ${a}_{i} \in  \left\lbrack  {0,1}\right\rbrack  \left( {i = 1,2,\cdots ,{2021}}\right)$ ，均可以“嵌入”区间 $\left\lbrack  {0,2}\right\rbrack$ .

【答案】( 1 ) ${A}_{1}$ 不能嵌入， ${A}_{2}$ 能嵌入. ( 2 ) ${m}_{0} - 1$ ；( 3 )证明见解析；

【解析】( 1 )由题意知: ${x}_{i} \in  \left\lbrack  {0,2}\right\rbrack$ ,对于 ${A}_{1}$ 显然不存在 $\left| {{x}_{i} - {x}_{i - 1}}\right|  = 3$ ,而对于 ${A}_{2}$ 由 $2 \geq  \left| {{x}_{i} - {x}_{i - 1}}\right|  \geq  0$ ,即存在 $\left| {{x}_{i} - {x}_{i - 1}}\right|  = 0$ 或 $1,\therefore {A}_{1}$ 不能嵌入 $\left\lbrack  {0,2}\right\rbrack$ ,而 ${A}_{2}$ 可以.

(2)由数列 $A$ 可“嵌入”区间 $\left\lbrack  {1,{m}_{0}}\right\rbrack  \left( {{m}_{0} \in  {N}^{ * }}\right)$ ，知: ${x}_{i} \in  \left\lbrack  {1,{m}_{0}}\right\rbrack$ ， ${a}_{n} = n\left( {n = 1,2,\cdots , k}\right)$ ， $\because {m}_{0} - 1 \geq  \left| {{x}_{i} - {x}_{i - 1}}\right|  \geq  0,\therefore$ 数列 $\mathrm{A}$ 的项数 $k$ 的最大值为 $k = {m}_{0} - 1$ .

(3) $\because {x}_{i} \in  \left\lbrack  {0,2}\right\rbrack$ 时，有 $2 \geq  \left| {{x}_{i} - {x}_{i - 1}}\right|  \geq  0$ ，而数列 A 满足 ${a}_{i} \in  \left\lbrack  {0,1}\right\rbrack  \left( {i = 1,2,\ldots ,{2021}}\right)$ ，

由 $\left\lbrack  {0,1}\right\rbrack   \subset  \left\lbrack  {0,2}\right\rbrack$ ,

$\therefore$ 对于任取数列 $A : {a}_{1},{a}_{2},\cdots ,{a}_{2021}$ 满足 ${a}_{i} \in  \left\lbrack  {0,1}\right\rbrack  \left( {i = 1,2,\cdots ,{2021}}\right)$ ,均可以“嵌入”区间 $\left\lbrack  {0,2}\right\rbrack$ .
