## 数列与不等式、函数、方程的综合

<table><tr><td>教学目标</td><td>1、数列的单调性及数列的最值问题在不等式中的运用； <br> 2、根据方程有解、恒成立问题，再结合数列不定方程中取整数解，需考虑奇数偶数，函数有界性讨论解的情况;</td></tr><tr><td>重点</td><td>1、数列的单调性与最值； <br> 2、数列中方程问题常见思路</td></tr><tr><td>难点</td><td>1、数列的单调性与最值; <br> 2、数列中方程问题常见思路</td></tr></table>

## (一) 数列与函数、不等式的综合运用

## 例题精讲

【例 1】设数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n},{a}_{n} + {S}_{n} = 3 - {\left( \frac{1}{2}\right) }^{n - 1}\left( {n \in  {N}^{ * }}\right)$ .

(1)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式;

(2)令 ${c}_{n} = \frac{{3n} - 1}{n + 1}{a}_{n}$ ，数列 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ，若对任意的正整数 $n$ ，恒有 $\frac{n - 2}{{2}^{n}}\lambda  < {T}_{n}$ ，求实数 $\lambda$ 的取值范围.

【难度】 $\star   \star   \star$

【答案】( 1 ) ${a}_{n} = \frac{n + 1}{{2}^{n}};\;\left( 2\right) \left( {-2,{26}}\right)$ .

【解析】(1)由已知, ${a}_{n} + {S}_{n} = 3 - {\left( \frac{1}{2}\right) }^{n - 1}\left( {n \in  {N}^{ * }}\right)$ ,

当 $n = 1$ 时, $2{a}_{1} = 2$ ,解得 ${a}_{1} = 1$ . 当 $n \geq  2$ 时, ${a}_{n - 1} + {S}_{n - 1} = 3 - {\left( \frac{1}{2}\right) }^{n - 2}$ .

两式相减,得 $2{a}_{n} - {a}_{n - 1} = {\left( \frac{1}{2}\right) }^{n - 1}$ .

两边同时乘以 ${2}^{n - 1}$ ，得 ${2}^{n}{a}_{n} - {2}^{n - 1}{a}_{n - 1} = 1$ ，

令 ${b}_{n} = {2}^{n}{a}_{n}$ ,则 ${b}_{n} - {b}_{n - 1} = 1\left( {n \geq  2}\right)$ ,

所以数列 $\left\{  {b}_{n}\right\}$ 是公差为 1 的等差数列,其首项为 ${b}_{1} = 2{a}_{1} = 2$ 所以 ${b}_{n} = 2 + \left( {n - 1}\right)  = n + 1$ ,即 $n + 1 = {2}^{n}{a}_{n}$ ,所以 ${a}_{n} = \frac{n + 1}{{2}^{n}}$ .

(2)由(1)知， ${a}_{n} = \frac{n + 1}{{2}^{n}}$ ，所以 ${c}_{n} = \frac{{3n} - 1}{{2}^{n}}$ .

则 ${T}_{n} = 2 \times  \frac{1}{2} + 5 \times  {\left( \frac{1}{2}\right) }^{2} + 8 \times  {\left( \frac{1}{2}\right) }^{3} + \ldots  + \left( {{3n} - 1}\right)  \times  {\left( \frac{1}{2}\right) }^{n}$ ，①

$\frac{1}{2}{T}_{n} = 2 \times  {\left( \frac{1}{2}\right) }^{2} + 5 \times  {\left( \frac{1}{2}\right) }^{3} + 8 \times  {\left( \frac{1}{2}\right) }^{4} + \ldots  + \left( {{3n} - 1}\right)  \times  {\left( \frac{1}{2}\right) }^{n + 1}$ ,②

①-②，得 $\frac{1}{2}{T}_{n} = 1 + 3 \times  {\left( \frac{1}{2}\right) }^{2} + 3 \times  {\left( \frac{1}{2}\right) }^{3} + \ldots  + 3 \times  {\left( \frac{1}{2}\right) }^{n} - \left( {{3n} - 1}\right)  \times  {\left( \frac{1}{2}\right) }^{n + 1}$ ,

即 $\frac{1}{2}{T}_{n} = 1 + 3 \times  \frac{\frac{1}{4}\left\lbrack  {1 - {\left( \frac{1}{2}\right) }^{n - 1}}\right\rbrack  }{1 - \frac{1}{2}} - \left( {{3n} - 1}\right)  \times  {\left( \frac{1}{2}\right) }^{n + 1},\frac{1}{2}{T}_{n} = \frac{5}{2} - \frac{{3n} + 5}{2} \times  {\left( \frac{1}{2}\right) }^{n}$ ,则 ${T}_{n} = 5 - \left( {{3n} + 5}\right)  \times  {\left( \frac{1}{2}\right) }^{n}$ .

由已知,对任意的正整数 $n$ ,恒有 $\frac{n - 2}{{2}^{n}}\lambda  < {T}_{n}$ .

当 $n = 1$ 时, $\frac{n - 2}{{2}^{n}}\lambda  < {T}_{n}$ 化为 $- \frac{1}{2}\lambda  < 1$ ,得 $\lambda  >  - 2$ . 当 $n = 2$ 时, $\frac{n - 2}{{2}^{n}}\lambda  < {T}_{n}$ 化为 $0 \times  \lambda  < \frac{9}{4}$ ,

此时, $\lambda$ 为任意实数不等式都成立.

当 $n \geq  3$ 时, $\frac{n - 2}{{2}^{n}}\lambda  < {T}_{n}$ 化为 $\lambda  < \frac{{2}^{n}}{n - 2}{T}_{n}$ ,即 $\lambda  < \frac{5 \times  {2}^{n} - {3n} - 5}{n - 2}$ .

令 $f\left( n\right)  = \frac{5 \times  {2}^{n} - {3n} - 5}{n - 2}\left( {n \geq  3, n \in  {\mathrm{N}}^{ * }}\right)$ ,则 $f\left( {n + 1}\right)  = \frac{5 \times  {2}^{n + 1} - 3\left( {n + 1}\right)  - 5}{n - 1} = \frac{{10} \times  {2}^{n} - {3n} - 8}{n - 1}$ ,

所以

$f\left( {n + 1}\right)  - f\left( n\right)  = \frac{{10} \times  {2}^{n} - {3n} - 8}{n - 1} - \frac{5 \times  {2}^{n} - {3n} - 5}{n - 2} = \frac{\left( {{10} \times  {2}^{n} - {3n} - 8}\right) \left( {n - 2}\right)  - \left( {5 \times  {2}^{n} - {3n} - 5}\right) \left( {n - 1}\right) }{\left( {n - 1}\right) \left( {n - 2}\right) } \; = \frac{\left( {{5n} - {15}}\right)  \times  {2}^{n} + {11}}{\left( {n - 1}\right) \left( {n - 2}\right) }$ .

当 $n \geq  3$ 时, $\frac{\left( {{5n} - {15}}\right)  \times  {2}^{n} + {11}}{\left( {n - 1}\right) \left( {n - 2}\right) } > 0$ ,则 $f\left( {n + 1}\right)  > f\left( n\right)$ ,所以 $f\left( n\right)  = \frac{5 \times  {2}^{n} - {3n} - 5}{n - 2}\left( {n \geq  3, n \in  {\mathrm{N}}^{ * }}\right)$ 单调递增,所以 $f\left( n\right)$ 的最小值为 $f\left( 3\right)  = {26}$ ,则 $\lambda  < {26}$ .

综上可知, $- 2 < \lambda  < {26}$ ,即 $\lambda$ 的取值范围是 $\left( {-2,{26}}\right)$ .

【例 2】已知各项均为正数的数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,且满足 ${a}_{1}^{3} + {a}_{2}^{3} + \cdots  + {a}_{n}^{3} = {\left( {a}_{1} + {a}_{2} + \cdots  + {a}_{n}\right) }^{2}$ , $n \in  {\mathrm{N}}^{ * }$ .

(1)求证: ${a}_{n}{}^{2} = 2{S}_{n} - {a}_{n}$ ；

(2)设 ${c}_{n} = \left( {{a}_{n} - \frac{1}{2}}\right)  \cdot  {2}^{n}$ ，其前 $n$ 项和为 ${T}_{n}$ ，求 ${T}_{n}$ ；

(3)在(2)的条件下，设 ${b}_{n} = \frac{{T}_{n} - 3}{{2}^{n}} + 2$ ，求使不等式 $\left( {1 + \frac{1}{{b}_{1}}}\right) \left( {1 + \frac{1}{{b}_{2}}}\right) \cdots \left( {1 + \frac{1}{{b}_{n}}}\right)  \geq  p\sqrt{{2n} + 1}$ 对一切 $n \geq  2$ 且 $n \in  {\mathbf{N}}^{ * }$ 均成立的最大整数 $p$ .

【难度】 $\star   \star   \star   \star$

【答案】( 1 )证明见解析；( 2 ) ${T}_{n} = \left( {{2n} - 3}\right)  \cdot  {2}^{n} + 3$ ；( 3 ) ${p}_{\max } = 1$ .

【解析】(1) ${a}_{1}^{3} + {a}_{2}^{3} + \cdots  + {a}_{n}^{3} = {\left( {a}_{1} + {a}_{2} + \cdots  + {a}_{n}\right) }^{2}\left( *\right)$ ,

${a}_{1}^{3} + {a}_{2}^{3} + \cdots  + {a}_{n - 1}^{3} = {\left( {a}_{1} + {a}_{2} + \cdots  + {a}_{n - 1}\right) }^{2}\left( {n \geq  2}\right) ,$

所以 ${a}_{n}^{3} = {\left( {a}_{1} + {a}_{2} + \cdots  + {a}_{n}\right) }^{2} - {\left( {a}_{1} + {a}_{2} + \cdots  + {a}_{n - 1}\right) }^{2} = {a}_{n}\left( {2{S}_{n} - {a}_{n}}\right)$

又 ${a}_{n} > 0$ ,所以 ${a}_{n}^{2} = 2{S}_{n} - {a}_{n}\left( {n \geq  2}\right)$ ,又因为由 $\left( *\right)$ 式可得 ${a}_{1} = 1$ 满足前式,所以 ${a}_{n}^{2} = 2{S}_{n} - {a}_{n}\left( {n \in  {\mathrm{N}}^{ * }}\right)$ .

(2)由(1)得 ${a}_{n - 1}^{2} = 2{S}_{n - 1} - {a}_{n - 1}\left( {n \geq  2}\right)$ ，所以 $\left( {{a}_{n} + {a}_{n - 1}}\right) \left( {{a}_{n} - {a}_{n - 1} - 1}\right)  = 0$ ，

又 ${a}_{n} > 0$ ,所以 ${a}_{n} + {a}_{n - 1} > 0$ ,所以 ${a}_{n} - {a}_{n - 1} = 1$ ,

所以 $\left\{  {a}_{n}\right\}$ 是以 1 为首项,1 为公差的等差数列. 所以 ${a}_{n} = 1 + \left( {n - 1}\right)  \cdot  1 = n$ ,所以 ${c}_{n} = \left( {n - \frac{1}{2}}\right)  \cdot  {2}^{n}$ ,

${T}_{n} = \frac{1}{2} \times  {2}^{1} + \frac{3}{2} \times  {2}^{2} + \frac{5}{2} \times  {2}^{3} + \cdots  + \left( {n - \frac{1}{2}}\right)  \times  {2}^{n}$ ①,

$2{T}_{n} = \frac{1}{2} \times  {2}^{2} + \frac{3}{2} \times  {2}^{3} + \cdots  + \left( {n - \frac{3}{2}}\right)  \times  {2}^{n} + \left( {n - \frac{1}{2}}\right)  \times  {2}^{n + 1}$ ②,

①-②得:

$- {T}_{n} = 1 + {2}^{2} + {2}^{3} + \cdots  + {2}^{n} - \left( {n - \frac{1}{2}}\right)  \cdot  {2}^{n + 1} = 2 + {2}^{2} + {2}^{3} + \cdots  + {2}^{n} - \left( {n - \frac{1}{2}}\right)  \cdot  {2}^{n + 1} - 1 \; = \frac{2\left( {1 - {2}^{n}}\right) }{1 - 2} - \left( {n - \frac{1}{2}}\right)  \cdot  {2}^{n + 1} - 1 = \left( {3 - {2n}}\right)  \cdot  {2}^{n} - 3$ ,所以 ${T}_{n} = \left( {{2n} - 3}\right)  \cdot  {2}^{n} + 3$ .

(3)由(2)得 ${b}_{n} = \frac{{T}_{n} - 3}{{2}^{n}} + 2 = \frac{\left( {{2n} - 3}\right)  \cdot  {2}^{n}}{{2}^{n}} + 2 = {2n} - 1$ ，

由题意得 $p \leq  \frac{1}{\sqrt{{2n} + 1}}\left( {1 + \frac{1}{{b}_{1}}}\right) \left( {1 + \frac{1}{{b}_{2}}}\right) \cdots \left( {1 + \frac{1}{{b}_{n}}}\right)$ 对 $n \geq  2, n \in  {\mathrm{N}}^{ * }$ 恒成立,

记 $F\left( n\right)  = \frac{1}{\sqrt{{2n} + 1}}\left( {1 + \frac{1}{{b}_{1}}}\right) \left( {1 + \frac{1}{{b}_{2}}}\right) \cdots \left( {1 + \frac{1}{{b}_{n}}}\right)$ ,

则 $\frac{F\left( {n + 1}\right) }{F\left( n\right) } = \frac{\frac{1}{\sqrt{{2n} + 3}}\left( {1 + \frac{1}{{b}_{1}}}\right) \left( {1 + \frac{1}{{b}_{2}}}\right) \cdots \left( {1 + \frac{1}{{b}_{n}}}\right) \left( {1 + \frac{1}{{b}_{n + 1}}}\right) }{\frac{1}{\sqrt{{2n} + 1}}\left( {1 + \frac{1}{{b}_{1}}}\right) \left( {1 + \frac{1}{{b}_{2}}}\right) \cdots \left( {1 + \frac{1}{{b}_{n}}}\right) } = \frac{{2n} + 2}{\sqrt{{2n} + 1}\sqrt{{2n} + 3}} = \sqrt{\frac{4{n}^{2} + {8n} + 4}{4{n}^{2} + {8n} + 3}} > 1$

$\because F\left( n\right)  > 0,\therefore F\left( {n + 1}\right)  > F\left( n\right)$ ,即 $F\left( n\right)$ 是随 $n$ 的增大而增大,

$F\left( n\right)$ 的最小值为 $F\left( 2\right)  = \frac{8}{15}\sqrt{5}$ ，所以 $p \leq  \frac{8}{15}\sqrt{5}$ ，

又 $p \in  Z$ ,所以 ${p}_{\max } = 1$ .

【例 3】已知正项数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,对任意 $n \in  {N}^{ * }$ ,点 $\left( {{a}_{n},{S}_{n}}\right)$ 都在函数 $f\left( x\right)  = {2x} - 2$ 的图象上.

(1)若 ${b}_{n} = \left( {{2n} - 1}\right) {a}_{n}$ ，求数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和 ${T}_{n}$ ；

(2)已知数列 $\left\{  {c}_{n}\right\}$ 满足 ${c}_{n} = \frac{1}{{a}_{n}} - \left( {\frac{1}{n} - \frac{1}{n + 1}}\right) \left( {n \in  {N}^{ * }}\right)$ ，若对任意 $n \in  {N}^{ * }$ ，存在 ${x}_{0} \in  \left\lbrack  {-\frac{1}{2},\frac{1}{2}}\right\rbrack$ ，使得 ${c}_{1} + {c}_{2} + \cdots  + {c}_{n} \leq  f\left( {x}_{0}\right)  - a$ 成立,求实数 $a$ 的取值范围.

【难度】 $\star   \star   \star   \star$

【答案】( 1 ) ${T}_{n} = 6 + \left( {{2n} - 3}\right)  \times  {2}^{n + 1};\;$ (2) $\left( {-\infty , - \frac{91}{80}}\right\rbrack$ .

【解析】解: (1) 由点 $\left( {{a}_{n},{S}_{n}}\right)$ 都在函数 $f\left( x\right)  = {2x} - 2$ 的图象上,可得 ${S}_{n} = 2{a}_{n} - 2$ ①，当 $n = 1$ 时，

${a}_{1} = {S}_{1} = 2{a}_{1} - 2$ ,解得 ${a}_{1} = 2$ ; 当 $n \geq  2$ 时,由 ${S}_{n} = 2{a}_{n} - 2$ 得, ${S}_{n - 1} = 2{a}_{n - 1} - 2$ ②,①-②,得 ${a}_{n} = {S}_{n} - {S}_{n - 1} = 2{a}_{n} - 2 - 2{a}_{n - 1} + 2$ ,即 ${a}_{n} = 2{a}_{n - 1}$ ,又 ${a}_{1} = 2 \neq  0$ ,所以数列 $\left\{  {a}_{n}\right\}$ 是首项为 2,公比为 2 的等比数列. 所以 ${a}_{n} = {2}^{n}, n \in  {N}^{ * }$ .

所以 ${b}_{n} = \left( {{2n} - 1}\right) {a}_{n} = \left( {{2n} - 1}\right) {2}^{n}$ ,则 ${T}_{n} = 1 \times  {2}^{1} + 3 \times  {2}^{2} + 5 \times  {2}^{3} + \cdots  + \left( {{2n} - 1}\right)  \times  {2}^{n}$ , $2{T}_{n} = 1 \times  {2}^{2} + 3 \times  {2}^{3} + \cdots  + \left( {{2n} - 3}\right)  \times  {2}^{n} + \left( {{2n} - 1}\right)  \times  {2}^{n + 1}$ ,两式相减可得 $- {T}_{n} = 2 + 2\left( {{2}^{2} + {2}^{3} + \cdots  + {2}^{n}}\right)  - \left( {{2n} - 1}\right)  \times  {2}^{n + 1} = 2 + 2 \times  \frac{4 \times  \left( {1 - {2}^{n - 1}}\right) }{1 - 2} - \left( {{2n} - 1}\right)  \times  {2}^{n + 1} = \left( {3 - {2n}}\right)  \times  {2}^{n + 1} - 6$ ,所以 ${T}_{n} = 6 + \left( {{2n} - 3}\right)  \times  {2}^{n + 1}$ .

(1)由(1)知 ${c}_{n} = \frac{1}{{2}^{n}} - \left( {\frac{1}{n} - \frac{1}{n + 1}}\right)$ ，设 $M$ 为数列 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项和，则 ${M}_{n} = \left( {\frac{1}{2} + \frac{1}{{2}^{2}} + \cdots  + \frac{1}{{2}^{n}}}\right)  - \left\lbrack  {\left( {1 - \frac{1}{2}}\right)  + \left( {\frac{1}{2} - \frac{1}{3}}\right)  + \cdots  + \left( {\frac{1}{n} - \frac{1}{n + 1}}\right) }\right\rbrack   = \frac{\frac{1}{2} \times  \left( {1 - \frac{1}{{2}^{n}}}\right) }{1 - \frac{1}{2}} - \left( {1 - \frac{1}{n + 1}}\right)  = \frac{1}{n + 1} - \frac{1}{{2}^{n}}$ ,因为 ${c}_{n} = \frac{1}{{2}^{n}} - \left( {\frac{1}{n} - \frac{1}{n + 1}}\right)  = \frac{1}{{2}^{n}} - \frac{1}{n\left( {n + 1}\right) }$ ,所以 ${c}_{1} = 0,{c}_{2} > 0,{c}_{3} > 0,{c}_{4} > 0$ ,当 $n \geq  5$ 时,令 ${d}_{n} = \frac{{2}^{n}}{n\left( {n + 1}\right) }$ , 则 ${d}_{n + 1} - {d}_{n} = \frac{{2}^{n + 1}}{\left( {n + 1}\right) \left( {n + 2}\right) } - \frac{{2}^{n}}{n\left( {n + 1}\right) } = \frac{{2}^{n}\left( {n - 2}\right) }{n\left( {n + 1}\right) \left( {n + 2}\right) } > 0$ ,所以 $\left\{  {d}_{n}\right\}$ 为递增数列. 又 ${d}_{5} = \frac{{2}^{5}}{5 \times  6} = \frac{16}{15} > 1$ ,所以 ${d}_{n} > 1$ ,所以 ${2}^{n} > n\left( {n + 1}\right)$ ,所以 ${c}_{n} < 0$ ,所以 ${M}_{n}$ 的最大值为 ${M}_{4} = \frac{1}{5} - \frac{1}{16} = \frac{11}{80}$ ,当 $x \in  \left\lbrack  {-\frac{1}{2},\frac{1}{2}}\right\rbrack$ 时, $f\left( x\right)  - a = {2x} - 2 - a$ 的最大值为 $- 1 - a$ ,因为对任意 $n \in  {N}^{ * }$ , 存在 ${x}_{0} \in  \left\lbrack  {-\frac{1}{2},\frac{1}{2}}\right\rbrack$ ,使得 ${c}_{1} + {c}_{2} + \cdots  + {c}_{n} \leq  f\left( {x}_{0}\right)  - a$ 成立,所以 $\frac{11}{80} \leq   - 1 - a$ ,解得 $a \leq   - \frac{91}{80}$ . 所以实数 $a$ 的取值范围是 $\left( {-\infty , - \frac{91}{80}}\right\rbrack$ .

【例 4】设等差数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n},{a}_{3} = 4,{a}_{4} = {S}_{3}$ . 数列 $\left\{  {b}_{n}\right\}$ 满足: 对每个 $n \in  {\mathbf{N}}^{ * },{S}_{n} + {b}_{n}$ , ${S}_{n + 1} + {b}_{n},{S}_{n + 2} + {b}_{n}$ 成等比数列.

(1)求数列 $\left\{  {a}_{n}\right\}  ,\left\{  {b}_{n}\right\}$ 的通项公式；

(2)记 ${c}_{n} = \sqrt{\frac{{a}_{n}}{2{b}_{n}}}, n \in  {\mathbf{N}}^{ * }$ ，证明: ${c}_{1} + {c}_{2} + {c}_{3} + \cdots  + {c}_{n} < 2\sqrt{n}, n \in  {\mathbf{N}}^{ * }$ .

【难度】 $\star   \star   \star   \star$

【答案】( 1 ) ${a}_{n} = {2n} - 2,{b}_{n} = {n}^{2} + n, n \in  {\mathbf{N}}^{ * }$ ；( 2 )证明见解析.

【解析】(1)设数列 $\left\{  {a}_{n}\right\}$ 的公差为 $d$ ，由题意得 $\left\{  \begin{matrix} {a}_{1} + {2d} = 4, \\  {a}_{1} + {3d} = 3{a}_{1} + {3d}, \end{matrix}\right.$ 解得 ${a}_{1} = 0, d = 2$ ，

$\therefore {a}_{n} = {2n} - 2, n \in  {N}^{ * }\therefore {S}_{n} = {n}^{2} - n, n \in  {N}^{ * }$ .

$\because$ 数列 $\left\{  {b}_{n}\right\}$ 满足: 对每个 $n \in  {\mathbf{N}}^{ * }$ , ${S}_{n} + {b}_{n},{S}_{n + 1} + {b}_{n},{S}_{n + 2} + {b}_{n}$ 成等比数列,

$\therefore {\left( {S}_{n + 1} + {b}_{n}\right) }^{2} = \left( {{S}_{n} + {b}_{n}}\right) \left( {{S}_{n + 2} + {b}_{n}}\right)$ ,解得 ${b}_{n} = \frac{1}{d}\left( {{S}_{n + 1}{}^{2} - {S}_{n}{S}_{n + 2}}\right)$ ,即 ${b}_{n} = {n}^{2} + n, n \in  {\mathbf{N}}^{ * }$ .

(2)证明: ${c}_{n} = \sqrt{\frac{{a}_{n}}{2{b}_{n}}} = \sqrt{\frac{{2n} - 2}{{2n}\left( {n + 1}\right) }} = \sqrt{\frac{n - 1}{n\left( {n + 1}\right) }}$ ， $n \in  {\mathbf{N}}^{ * }$ ，

用数学归纳法证明:

① 当 $n = 1$ 时， ${c}_{1} = 0 < 2$ ，不等式成立；

② 假设当 $n = k\left( {k \in  {N}^{ * }}\right)$ 时不等式成立，即 ${c}_{1} + {c}_{2} + {c}_{3} + \cdots  + {c}_{k} < 2\sqrt{k}$ ，

则当 $n = k + 1$ 时， ${c}_{1} + {c}_{2} + {c}_{3} + \cdots  + {c}_{k} + {c}_{k + 1} < 2\sqrt{k} + \sqrt{\frac{k}{\left( {k + 1}\right) \left( {k + 2}\right) }} < 2\sqrt{k} + \sqrt{\frac{1}{k + 1}} < 2\sqrt{k} + \frac{2}{\sqrt{k + 1} + \sqrt{k}} =$

$2\sqrt{k} + 2\left( {\sqrt{k + 1} - \sqrt{k}}\right)  = 2\sqrt{k + 1}$ ; 即 $n = k + 1$ 时,不等式也成立.

由①②得 ${c}_{1} + {c}_{2} + {c}_{3} + \cdots  + {c}_{n} < 2\sqrt{n}, n \in  {\mathbf{N}}^{ * }$ .

【例 5】已知数列 $\left\{  {a}_{n}\right\}$ 与 $\left\{  {b}_{n}\right\}$ 满足 ${a}_{n + 1} - {a}_{n} = \lambda \left( {{b}_{n + 1} - {b}_{n}}\right)$ ( $\lambda$ 为非零常数), $n \in  {\mathbf{N}}^{ * }$ .

(1)若 $\left\{  {b}_{n}\right\}$ 是等差数列，求证:数列 $\left\{  {a}_{n}\right\}$ 也是等差数列；

(2)若 ${a}_{1} = 2,\lambda  = 3,{b}_{n} = \sin \frac{n\pi }{2}$ ，求数列 $\left\{  {a}_{n}\right\}$ 的前 2021 项和；

(3)设 ${a}_{1} = {b}_{1} = \lambda ,{b}_{2} = \frac{\lambda }{2},{b}_{n} = \frac{{b}_{n - 1} + {b}_{n - 2}}{2}\left( {n \geq  3, n \in  {\mathbf{N}}^{ * }}\right)$ ，若对 $\left\{  {a}_{n}\right\}$ 中的任意两项 ${a}_{i}$ ， ${a}_{j}\left( {i, j \in  {\mathbf{N}}^{ * }, i \neq  j}\right) ,\left| {{a}_{i} - {a}_{j}}\right|  < 2$ 都成立,求实数 $\lambda$ 的取值范围.

【难度】 $\star   \star   \star   \star$

【答案】(1)证明见解析；(2)-2018；(3) $\left( {-2,0}\right)  \cup  \left( {0,2}\right)$ .

【解析】(1)设 $\left\{  {b}_{n}\right\}$ 的公差为 $d$ ,则 ${a}_{n + 1} - {a}_{n} = \lambda \left( {{b}_{n + 1} - {b}_{n}}\right)  = {\lambda d}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ ，故数列 $\left\{  {a}_{n}\right\}$ 是等差数列；

(2)由 ${b}_{n} = \sin \frac{n\pi }{2}$ ，可知 $\left\{  {b}_{n}\right\}$ 是周期为 4 的数列，即 ${b}_{n + 4} = {b}_{n}$ ；

由 ${a}_{n + 4} - {a}_{n} = \left( {{a}_{n + 4} - {a}_{n + 3}}\right)  + \left( {{a}_{n + 3} - {a}_{n + 2}}\right)  + \left( {{a}_{n + 2} - {a}_{n + 1}}\right)  + \left( {{a}_{n + 1} - {a}_{n}}\right)$

$= \lambda \left( {{b}_{n + 4} - {b}_{n + 3}}\right)  + \lambda \left( {{b}_{n + 3} - {b}_{n + 2}}\right)  + \lambda \left( {{b}_{n + 2} - {b}_{n + 1}}\right)  + \lambda \left( {{b}_{n + 1} - {b}_{n}}\right)$

$= \lambda \left( {{b}_{n + 4} - {b}_{n}}\right)  = 0$ ,即 $\left\{  {a}_{n}\right\}$ 也是周期为 4 的数列.

又由 ${a}_{1} = 2,{b}_{n} = \sin \frac{n\pi }{2},{a}_{n + 1} - {a}_{n} = 3\left( {{b}_{n + 1} - {b}_{n}}\right)$ 可求:

${a}_{2} =  - 1,{a}_{3} =  - 4,{a}_{4} =  - 1,{S}_{4} = {a}_{1} + {a}_{2} + {a}_{3} + {a}_{4} =  - 4$ ,

所以 ${S}_{2021} = {a}_{1} + \left( {{a}_{2} + {a}_{3} + {a}_{4} + {a}_{5}}\right)  + \cdots  + \left( {{a}_{2018} + {a}_{2019} + {a}_{2020} + {a}_{2021}}\right)  = {a}_{1} + {505}{S}_{4} =  - {2018}$ .

(3)由 ${b}_{n} = \frac{{b}_{n - 1} + {b}_{n - 2}}{2}\left( {n \geq  3, n \in  {\mathbf{N}}^{ * }}\right)$ 得 ${b}_{n + 1} - {b}_{n} =  - \frac{1}{2}\left( {{b}_{n} - {b}_{n - 1}}\right) \left( {n \geq  2, n \in  {\mathbf{N}}^{ * }}\right)$ ，

即 $\left\{  {{b}_{n + 1} - {b}_{n}}\right\}$ 是以 ${b}_{2} - {b}_{1} =  - \frac{\lambda }{2}$ 为首项, $- \frac{1}{2}$ 为公比的等比数列,则 ${b}_{n + 1} - {b}_{n} =  - \frac{\lambda }{2} \cdot  {\left( -\frac{1}{2}\right) }^{n - 1} = \lambda  \cdot  {\left( -\frac{1}{2}\right) }^{n}$

所以 ${b}_{n} = \left( {{b}_{n} - {b}_{n - 1}}\right)  + \left( {{b}_{n - 1} - {b}_{n - 2}}\right)  + \cdots  + \left( {{b}_{2} - {b}_{1}}\right)  + {b}_{1} = \lambda  \cdot  {\left( -\frac{1}{2}\right) }^{n - 1} + \lambda  \cdot  {\left( -\frac{1}{2}\right) }^{n - 2} + \cdots  + \lambda  \cdot  \left( {-\frac{1}{2}}\right)  + \lambda$

$= \lambda  \cdot  \frac{1 \cdot  \left\lbrack  {1 - {\left( -\frac{1}{2}\right) }^{n}}\right\rbrack  }{1 - \left( {-\frac{1}{2}}\right) } = \frac{2\lambda }{3} + \frac{\lambda }{3}{\left( -\frac{1}{2}\right) }^{n - 1}$ .

则 ${a}_{n} = \lambda {b}_{n} + {a}_{1} - \lambda {b}_{1} = \frac{{\lambda }^{2}}{3}{\left( -\frac{1}{2}\right) }^{n - 1} + \lambda  - \frac{{\lambda }^{2}}{3}$ .

当 $n$ 为奇数时, ${a}_{n} = \frac{{\lambda }^{2}}{3}{\left( \frac{1}{2}\right) }^{n - 1} + \lambda  - \frac{{\lambda }^{2}}{3}$ 单调递减,且 $\lambda  - \frac{{\lambda }^{2}}{3} < {a}_{n} \leq  \lambda$ ;

当 $n$ 为偶数时, ${a}_{n} =  - \frac{{\lambda }^{2}}{3}{\left( \frac{1}{2}\right) }^{n - 1} + \lambda  - \frac{{\lambda }^{2}}{3}$ 单调递增,且 $\lambda  - \frac{{\lambda }^{2}}{2} \leq  {a}_{n} < \lambda  - \frac{{\lambda }^{2}}{3}$ ;

因为 $\lambda  \neq  0$ ,故 $\lambda  - \frac{{\lambda }^{2}}{2} < \lambda  - \frac{{\lambda }^{2}}{3} < \lambda$ ,

所以 $\left\{  {a}_{n}\right\}$ 的最大值为 ${a}_{1} = \lambda$ ,最小值为 ${a}_{2} = \lambda  - \frac{{\lambda }^{2}}{2}$ ,

因为对 $\left\{  {a}_{n}\right\}$ 中的任意两项 ${a}_{i},{a}_{j}\left( {i, j \in  {\mathbf{N}}^{ * }}\right) ,\left| {{a}_{i} - {a}_{j}}\right|  < 2$ 都成立,所以 ${a}_{1} - {a}_{2} < 2$ ,解得 $\lambda  \in  \left( {-2,0}\right)  \cup  \left( {0,2}\right)$

综上, $\lambda$ 的取值范围是 $\left( {-2,0}\right)  \cup  \left( {0,2}\right)$ .

【例 6】若存在常数 $m \in  \mathbf{R}$ ,使得对于任意 $n \in  {\mathbf{N}}^{ * }$ ,都有 ${a}_{n + 1} \geq  m{a}_{n}$ ,则称数列 $\left\{  {a}_{n}\right\}$ 为 $Z\left( m\right)$ 数列.

(1)已知数列 $\left\{  {a}_{n}\right\}$ 是公差为 2 的等差数列,其前 $n$ 项和为 ${S}_{n}$ ，若 ${S}_{n}$ 为 $Z\left( 1\right)$ 数列，求 ${a}_{1}$ 的取值范围；

(2)已知数列 $\left\{  {b}_{n}\right\}$ 的各项均为正数，记 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为 ${R}_{n}$ ，数列 $\left\{  {b}_{n}^{2}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ，且 $3{T}_{n} = {R}_{n}^{2} + 4{R}_{n}$ ， $n \in  {\mathbf{N}}^{ * }$ ,若数列 $\left\{  {c}_{n}\right\}$ 满足 ${c}_{n} = {b}_{n} + \frac{1}{{b}_{n}}$ ,且 $\left\{  {c}_{n}\right\}$ 为 $Z\left( m\right)$ 数列,求 $m$ 的最大值;

(3)已知正项数列 $\left\{  {d}_{n}\right\}$ 满足: ${d}_{n} \leq  {d}_{n + 1}\left( {n \in  {\mathbf{N}}^{ * }}\right)$ ，且数列 $\left\{  {{d}_{{2k} - 1}{d}_{{2k} + 1}}\right\}$ 为 $Z\left( r\right)$ 数列，数列 $\left\{  \frac{1}{{d}_{2k}{d}_{{2k} + 2}}\right\}$ 为 $Z\left( s\right)$ 数列,若 $\frac{{d}_{2}}{{d}_{1}} = {rs}$ ,求证: 数列 $\left\{  {d}_{n}\right\}$ 中必存在无穷多项可以组成等比数列.

【难度】 $\star   \star   \star   \star$

【答案】( 1 ) $\left\lbrack  {-2, + \infty }\right)$ ；( 2 ) ${m}_{\max } = \frac{17}{10}$ ；( 3 )证明见解析.

【解析】(1) 由题意可得 ${S}_{n + 1} \geq  {S}_{n}$ ,即 ${a}_{n + 1} = {a}_{1} + {2n} \geq  0,\therefore {a}_{1} \geq   - {2n}$ 对任意的 $n \in  {\mathbf{N}}^{ * }$ 恒成立,所以, ${a}_{1} \geq   - 2$ ;

(2)当 $n = 1$ 时，由题意可得 $3{T}_{1} = {R}_{1}^{2} + 4{R}_{1}$ ，即 $3{b}_{1}^{2} = {b}_{1}^{2} + 4{b}_{1}$ ，可得 ${b}_{1}^{2} - 2{b}_{1} = 0$ ，

$\because {b}_{1} > 0$ ,解得 ${b}_{1} = 2$ ;

当 $n = 2$ 时, $3{T}_{2} = {R}_{2}^{2} + 4{R}_{2}$ ,可得 $3\left( {4 + {b}_{2}^{2}}\right)  = {\left( 2 + {b}_{2}\right) }^{2} + 4\left( {2 + {b}_{2}}\right)$ ,可得 ${b}_{2}^{2} - 4{b}_{2} = 0$ ,

$\because {b}_{2} > 0$ ,解得 ${b}_{2} = 4$ ;

当 $n \geq  2$ 时,由 $3{T}_{n} = {R}_{n}^{2} + 4{R}_{n}$ 可得 $3{T}_{n - 1} = {R}_{n - 1}^{2} + 4{R}_{n - 1}$ ,

上述两式作差得 $3{b}_{n}^{2} = {R}_{n}^{2} - {R}_{n - 1}^{2} + 4{b}_{n} = \left( {{R}_{n} - {R}_{n - 1}}\right) \left( {{R}_{n} + {R}_{n - 1}}\right)  + 4{b}_{n} = {b}_{n}\left( {{R}_{n} + {R}_{n - 1}}\right)  + 4{b}_{n}$ ,

所以, $3{b}_{n} = {R}_{n} + {R}_{n - 1} + 4$ ,可得 $3{b}_{n + 1} = {R}_{n + 1} + {R}_{n} + 4$ ,

上述两式相减得 $3{b}_{n + 1} - 3{b}_{n} = {b}_{n + 1} + {b}_{n}$ ,可得 $\frac{{b}_{n + 1}}{{b}_{n}} = 2$ 且 $\frac{{b}_{2}}{{b}_{1}} = 2$ ,

所以，数列 $\left\{  {b}_{n}\right\}$ 是首项为 2，公比也为 2 的等比数列，所以， ${b}_{n} = {2}^{n}$ ，则 ${c}_{n} = {b}_{n} + \frac{1}{{b}_{n}} = {2}^{n} + \frac{1}{{2}^{n}}$ ，

由 ${c}_{n + 1} \geq  m{c}_{n}$ ,可得 ${2}^{n + 1} + \frac{1}{{2}^{n + 1}} \geq  m\left( {{2}^{n} + \frac{1}{{2}^{n}}}\right)$ ,所以, $m \leq  \frac{{2}^{n + 1} + \frac{1}{{2}^{n + 1}}}{{2}^{n} + \frac{1}{{2}^{n}}}$ ,

而 $\frac{{2}^{n + 1} + \frac{1}{{2}^{n + 1}}}{{2}^{n} + \frac{1}{{2}^{n}}} = \frac{{2}^{{2n} + 2} + 1}{{2}^{{2n} + 1} + 2} = \frac{2\left( {{2}^{{2n} + 1} + 2}\right)  - 3}{{2}^{{2n} + 1} + 2} = 2 - \frac{3}{{2}^{{2n} + 1} + 2} \geq  2 - \frac{3}{{2}^{3} + 2} = \frac{17}{10},\therefore m \leq  \frac{17}{10}$ ,

因此，实数 $m$ 的最大值为 $\frac{17}{10}$ ；

(3)因为数列 $\left\{  {{d}_{{2k} - 1}{d}_{{2k} + 1}}\right\}$ 为 $Z\left( r\right)$ 数列，则 $r{d}_{{2k} - 1}{d}_{{2k} + 1} \leq  {d}_{{2k} + 1}{d}_{{2k} + 3}$ ，可得 $r{d}_{{2k} - 1} \leq  {d}_{{2k} + 3}$ ， 另一方面,数列 $\left\{  \frac{1}{{d}_{2k}{d}_{{2k} + 2}}\right\}$ 为 $Z\left( s\right)$ 数列,则 $\frac{s}{{d}_{2k}{d}_{{2k} + 2}} \leq  \frac{1}{{d}_{{2k} + 2}{d}_{{2k} + 4}}$ ,可得 $s{d}_{{2k} + 4} \leq  {d}_{2k}$ , $\because \frac{{d}_{2}}{{d}_{1}} = {rs}$ ,且 $r{d}_{1} \leq  {d}_{5},{d}_{5} \leq  {d}_{6}, s{d}_{6} \leq  {d}_{2} = {d}_{1}{rs} \leq  s{d}_{5}$ ,

可得 ${d}_{5} = {d}_{6}$ 且中间每个等号都需取等,即 $s{d}_{6} = {d}_{2} = {d}_{1}{rs} = s{d}_{5}$ ,

$\because \frac{{d}_{2}}{{d}_{1}} = {rs},{d}_{1} \leq  {d}_{2},\therefore {rs} \geq  1$ ,

又 $\because r{d}_{5} \leq  {d}_{9}, s{d}_{10} \leq  {d}_{6},\therefore {rs}{d}_{10} \leq  r{d}_{5} = r{d}_{6} \leq  {d}_{9} \leq  {d}_{10}$ ,可得 ${rs} \leq  1,\therefore {rs} = 1$ ,

所以, ${d}_{10} \leq  r{d}_{5} = r{d}_{6} \leq  {d}_{9} \leq  {d}_{10}$ ,则 ${d}_{9} = {d}_{10}$ 且中间每个等号都需取等.

以此类推,可得出 $\left\{  \begin{array}{l} {d}_{{4k} + 1} = {d}_{{4k} + 2} \\  {d}_{{4k} + 1} = r{d}_{{4k} - 3} \\  {d}_{{4k} + 2} = r{d}_{{4k} - 2} \end{array}\right.$ . 因此,数列 $\left\{  {d}_{n}\right\}$ 中必存在无穷多项可以组成等比数列.

## 巩固训练

1、已知数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,点 $\left( {n,{S}_{n}}\right) \left( {n \in  {\mathbf{N}}^{ * }}\right.$ ) 在函数 $y = \frac{1}{2}{x}^{2} + \frac{1}{2}x$ 的图象上.

(1)求 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)若数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ，且 ${b}_{n} = \frac{1}{{a}_{n}{}^{2} + {2n}}$ ，求 ${T}_{n}$ 的取值范围；

(3)设 ${c}_{n} = {4}^{n} + {\left( -1\right) }^{n - 1} \cdot  \lambda  \cdot  {2}^{{a}_{n + 1}}$ ( $\lambda$ 为非零整数， $n \in  {\mathbf{N}}^{ * }$ )，是否存在确定的 $\lambda$ 值，使得对任意 $n \in  {\mathbf{N}}^{ * }$ ， 有 ${c}_{n + 1} > {c}_{n}$ 恒成立. 若存在,请求出 $\lambda$ 的值; 若不存在,请说明理由.

【答案】(1) ${a}_{n} = n\left( {n \in  {\mathbf{N}}^{ * }}\right) ;\;\left( 2\right) \frac{1}{3} \leq  {T}_{n} < \frac{3}{4}$ ;

【解析】解: (1) $\because$ 点 $\left( {n,{S}_{n}}\right)$ 在函数 $f\left( x\right)  = \frac{1}{2}{x}^{2} + \frac{1}{2}x$ 的图象上, $\because {S}_{n} = \frac{1}{2}{n}^{2} + \frac{1}{2}n$ . ①

当 $n \geq  2$ 时, ${S}_{n - 1} = \frac{1}{2}{\left( n - 1\right) }^{2} + \frac{1}{2}\left( {n - 1}\right)$ ,②

①-②得 ${a}_{n} = n$ . 当 $n = 1$ 时， ${a}_{1} = {S}_{1} = 1$ ，符合上式 $\therefore {a}_{n} = n\left( {n \in  {\mathbf{N}}^{ * }}\right)$ .

(2)由(1)得 ${b}_{n} = \frac{1}{{a}_{n}{}^{2} + {2n}} = \frac{1}{{n}^{2} + {2n}} = \frac{1}{n\left( {n + 2}\right) } = \frac{1}{2}\left( {\frac{1}{n} - \frac{1}{n + 2}}\right)$ ,

$\therefore {T}_{n} = \frac{1}{{b}_{1}} + \frac{1}{{b}_{2}} + \cdots  + \frac{1}{{b}_{n}} = \frac{1}{2}\left( {1 - \frac{1}{3} + \frac{1}{2} + \frac{1}{4} + \cdots  + \frac{1}{n} - \frac{1}{n + 2}}\right)  = \frac{3}{4} - \frac{1}{2}\left( {\frac{1}{n + 1} + \frac{1}{n + 2}}\right)$ .

$\because n \in  {\mathbf{N}}^{ * },\therefore \frac{1}{2}\left( {\frac{1}{n + 1} + \frac{1}{n + 2} > 0}\right) ,\therefore {T}_{n} = \frac{3}{4} - \frac{1}{2}\left( {\frac{1}{n + 1} + \frac{1}{n + 2}}\right)  < \frac{3}{4}$ ,

$\therefore {T}_{n + 1} - {T}_{n} = \frac{1}{\left( {n + 1}\right) \left( {n + 3}\right) } > 0,\therefore$ 数列 $\left\{  {T}_{n}\right\}$ 单调递增, $\therefore \left\{  {T}_{n}\right\}$ 中的最小项为 ${T}_{1} = \frac{1}{3}$ .

$\therefore {T}_{n} \geq  \frac{1}{3},\therefore \frac{1}{3} \leq  {T}_{n} < \frac{3}{4}$ .

(3) $\because {a}_{n} = n,\therefore {c}_{n} = {4}^{n} + {\left( -1\right) }^{n - 1} \cdot  \lambda  \cdot  {2}^{n + 1}$ ,

假设存在确定的 $\lambda$ 值,使得对任意 $n \in  {\mathbf{N}}^{ * }$ ,都有 ${c}_{n + 1} > {c}_{n}$ 恒成立,即 ${c}_{n + 1} - {c}_{n} > 0$ ,

对任意 $n \in  {\mathbf{N}}^{ * }$ 恒成立,即 ${4}^{n + 1} - {4}^{n} + {\left( -1\right) }^{n} \cdot  \lambda  \cdot  {2}^{n + 2} - {\left( -1\right) }^{n - 1} \cdot  \lambda  \cdot  {2}^{n + 1} > 0$ ,

对任意 $n \in  {\mathbf{N}}^{ * }$ 恒成立,即: ${\left( -1\right) }^{n - 1} \cdot  \lambda  < {2}^{n - 1}$ ,对任意 $n \in  {\mathbf{N}}^{ * }$ 恒成立.

①当 $n$ 为奇数时，即 $\lambda  < {2}^{n - 1}$ 恒成立，当且仅当 $n = 1$ 时， ${2}^{n - 1}$ 有最小值为 1， $\therefore \lambda  < 1$ ，

② 当 $n$ 为偶数时，即 $\lambda  >  - {2}^{n - 1}$ 恒成立，当且仅当 $n = 2$ 时， $- {2}^{n - 1}$ 有最大值 -2， $\therefore \lambda  >  - 2$ ，

即 $- 2 < \lambda  < 1$ ,又 $\lambda$ 为非零整数,则 $\lambda  =  - 1$ .

综上所述: 存在 $\lambda  =  - 1$ ,使得对任意 $n \in  {\mathbf{N}}^{ * }$ ,都有 ${c}_{n + 1} > {c}_{n}$ .

2、已知数列 $\left\{  {a}_{n}\right\}  \left\{  {b}_{n}\right\}$ 的各项为正,且 ${a}_{3} = {18}{b}_{1},\left\{  {b}_{n}\right\}$ 是公比为 $\frac{1}{3}$ 的等比数列. 再从:

①数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 ${S}_{n}$ 满足 $4{S}_{n} = {a}_{n}{}^{2} + 2{a}_{n}$ :

②数列 $\left\{  {a}_{n}\right\}$ 是公差不为 0 的等差数列,且 ${a}_{1} + {a}_{2} + {a}_{3} = {12},{a}_{1},{a}_{2},{a}_{4}$ ,成等比数列.

这两个条件中任选一个, 解答下列问题.

(1)求数列 $\left\{  {a}_{n}\right\}  ,\left\{  {b}_{n}\right\}$ 的通项公式；

(2)令 ${c}_{n} = \left( {{a}_{n} + {b}_{n}}\right) \cos {n\pi }$ ，设 $\left\{  {c}_{n}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ 若 ${\left( -1\right) }^{n} \times  \left( {\lambda  + n}\right)  > {T}_{n}$ 对 $n \in  {N}^{ * }$ 恒成立，求实数 $\lambda$ 的取值范围.

【答案】( 1 ) ${a}_{n} = {2n}$ ； ${b}_{n} = \frac{1}{{3}^{n}}$ ；( 2 ) $\left( {-\frac{2}{9},\frac{5}{4}}\right\rbrack$ .

【解析】(1)若选①， $n = 1$ 时， $4{S}_{1} = {a}_{1}^{2} + 2{a}_{1}$ ， $\therefore {a}_{1} = 2$ ，

$n \geq  2$ 时, $4{S}_{n} = {a}_{n}^{2} + 2{a}_{n},4{S}_{n - 1} = {a}_{n - 1}^{2} + 2{a}_{n - 1}$ ,两式相减得: $\left( {{a}_{n} + {a}_{n - 1}}\right) \left( {{a}_{n} - {a}_{n - 1} - 2}\right)  = 0$ ,

$\therefore {a}_{n} + {a}_{n - 1} = 0$ (舍) 或 ${a}_{n} - {a}_{n - 1} - 2 = 0$ ,

即数列 $\left\{  {a}_{n}\right\}$ 是首项为 2,公差为 2 的等差数列, $\therefore {a}_{n} = {2n}$ ;

若选②，因为 ${a}_{1} + {a}_{2} + {a}_{3} = 3{a}_{1} + {3d} = {12}$ ， $\therefore {a}_{1} + d = 4$ ，又 ${a}_{2}^{2} = {a}_{1}{a}_{4}$ ，

$\therefore {\left( {a}_{1} + d\right) }^{2} = {a}_{1}\left( {{a}_{1} + {3d}}\right)$ ,得 $d = {a}_{1}$ 或 0 (舍去), $\therefore d = {a}_{1} = 2,\therefore {a}_{n} = {2n}$ ,

$\because {a}_{3} = 6,\therefore {b}_{1} = \frac{1}{18}{a}_{3} = \frac{1}{3}$ ,又 $\left\{  {b}_{n}\right\}$ 的公比为 $\frac{1}{3},\therefore {b}_{n} = \frac{1}{{3}^{n}}$ .

(2)由(1)得 ${c}_{n} = \left( {{a}_{n} + {b}_{n}}\right)  \cdot  {\left( -1\right) }^{n} = \left( {{2n} + \frac{1}{{3}^{n}}}\right)  \cdot  {\left( -1\right) }^{n}$

当 $n$ 为偶数时, $\because {c}_{n - 1} + {c}_{n} =  - \left\lbrack  {\frac{1}{{3}^{n - 1}} + 2\left( {n - 1}\right) }\right\rbrack   + \left( {\frac{1}{{3}^{n}} + {2n}}\right)  =  - 2 \cdot  \frac{1}{{3}^{n}} + 2$

$\therefore {T}_{n} = \left( {{c}_{1} + {c}_{2}}\right)  + \left( {{c}_{3} + {c}_{4}}\right)  + \cdots  + \left( {{c}_{n - 1} + {c}_{n}}\right)$

$= \left( {-2 \cdot  \frac{1}{{3}^{2}} + 2}\right)  + \left( {-2 \cdot  \frac{1}{{3}^{4}} + 2}\right)  + \cdots  + \left( {-2 \cdot  \frac{1}{{3}^{n}} + 2}\right)  =  - 2 \times  \frac{\frac{1}{9}\left\lbrack  {1 - {\left( \frac{1}{9}\right) }^{\frac{n}{2}}}\right\rbrack  }{1 - \frac{1}{9}} + 2 \times  \frac{n}{2} = \frac{1}{4}\left( {\frac{1}{{3}^{n}} - 1}\right)  + n$

当 $n$ 为奇数时, ${T}_{n} = {T}_{n + 1} - {c}_{n + 1} = \frac{1}{4}\left( {\frac{1}{{3}^{n + 1}} - 1}\right)  + \left( {n + 1}\right)  - \left\lbrack  {\frac{1}{{3}^{n + 1}} + 2\left( {n + 1}\right) }\right\rbrack   =  - \frac{1}{4}\left( {\frac{1}{{3}^{n}} + 5}\right)  - n$

$\therefore {T}_{n} = \left\{  \begin{array}{l} \frac{1}{4}\left( {\frac{1}{{3}^{n}} - 1}\right)  + n, n = {2k} \\   - \frac{1}{4}\left( {\frac{1}{{3}^{n}} + 5}\right)  - n, n = {2k} - 1 \end{array}\right. \left( {k \in  {\mathrm{N}}^{ * }}\right)$ ,

$\because {\left( -1\right) }^{n} \cdot  \left( {\lambda  + n}\right)  > {T}_{n}$ 对 $n \in  {N}^{ * }$ 恒成立,

当 $n$ 为偶数时, $\lambda  + n > \frac{1}{4}\left( {\frac{1}{{3}^{n}} - 1}\right)  + n$ 恒成立,即 $\lambda  > \frac{1}{4}\left( {\frac{1}{{3}^{n}} - 1}\right)$ 恒成立,

因为 $n$ 为偶数时, $y = \frac{1}{4}\left( {\frac{1}{{3}^{n}} - 1}\right)$ 单调递减,所以 $\lambda  > {\left\lbrack  \frac{1}{4}\left( \frac{1}{{3}^{n}} - 1\right) \right\rbrack  }_{\max } = \frac{1}{4}\left( {\frac{1}{{3}^{2}} - 1}\right)  =  - \frac{2}{9}$ ,

当 $n$ 为奇数时, $- \left( {\lambda  + n}\right)  >  - \frac{1}{4}\left( {\frac{1}{{3}^{n}} + 5}\right)  - n$ 恒成立,即 $\lambda  < \frac{1}{4}\left( {\frac{1}{{3}^{n}} + 5}\right)$ 恒成立,

因为 $n$ 为奇数时, $y = \frac{1}{4}\left( {\frac{1}{{3}^{n}} + 5}\right)$ 单调递减,且 $\frac{1}{4}\left( {\frac{1}{{3}^{n}} + 5}\right)  > \frac{5}{4}$ ,所以 $\lambda  \leq  \frac{5}{4}$ .

综上,实数 $\lambda$ 的取值范围为 $\left( {-\frac{2}{9},\frac{5}{4}}\right\rbrack$ .

3、已知数列 $\left\{  {a}_{n}\right\}  \left( {n \in  {N}^{ * }}\right)$ 的 ${a}_{2} = 2$ ,前 $n$ 项和为 ${S}_{n}$ ,且 ${S}_{n} = \frac{n}{2}{a}_{n}$ 对于任意的 $n \in  {N}^{ * }$ 恒成立.

(1)求 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)记 ${b}_{n} = {a}_{n} + \lambda \left( {2 - n}\right)$ ，且前 $m$ 项和为 ${T}_{m}$ ，不等式 $\left| {{T}_{m} - {2m}}\right|  < m + 1$ 有且仅有两个不同的正整数解， 求 $\lambda$ 的取值范围.

【答案】( 1 ) ${a}_{n} = {2n} - 2$ ；( 2 ) $- 1 < \lambda  \leq   - \frac{1}{2}$ 或 $\frac{9}{2} \leq  \lambda  < 5$ .

【解析】(1)由已知 ${S}_{1} = {a}_{1} = \frac{1}{2}{a}_{1},{a}_{1} = 0$ ,

因为 ${S}_{n} = \frac{n}{2}{a}_{n},\therefore n \geq  2$ 时, ${S}_{n - 1} = \frac{n - 1}{2}{a}_{n - 1}$ ,两式相减得 ${a}_{n} = {S}_{n} - {S}_{n - 1} = \frac{n}{2}{a}_{n} - \frac{n - 1}{2}{a}_{n - 1}$ ,

$\left( {n - 2}\right) {a}_{n} = \left( {n - 1}\right) {a}_{n - 1},$

$\therefore$ 当 $n \geq  3$ 时, $\frac{{a}_{n}}{{a}_{n - 1}} = \frac{n - 1}{n - 2},\therefore {a}_{n} = {a}_{2} \times  \frac{{a}_{3}}{{a}_{2}} \times  \frac{{a}_{4}}{{a}_{3}} \times  \cdots  \times  \frac{{a}_{n}}{{a}_{n - 1}} = 2 \times  \frac{2}{1} \times  \frac{3}{2} \times  \cdots  \times  \frac{n - 1}{n - 2} = 2\left( {n - 1}\right) , n = 1,2$ 也适合,

所以 ${a}_{n} = 2\left( {n - 1}\right) , n \in  {N}^{ * }$ ;

(2)由(1) ${b}_{n} = 2\left( {n - 1}\right)  + \lambda \left( {2 - n}\right)  = \left( {2 - \lambda }\right) n + {2\lambda } - 2$ ，

${T}_{m} = \left( {2 - \lambda }\right)  \times  \frac{m\left( {m + 1}\right) }{2} + {2m}\left( {\lambda  - 1}\right) ,$

$\left| {{T}_{m} - {2m}}\right|  = \left| {\left( {2 - \lambda }\right)  \times  \frac{m\left( {m + 1}\right) }{2} + {2m}\left( {\lambda  - 2}\right) }\right|  = \left| {\frac{2 - \lambda }{2} \times  \left( {{m}^{2} - {3m}}\right) }\right| ,$

不等式 $\left| {{T}_{m} - {2m}}\right|  < m + 1$ 为 $\left| {\frac{2 - \lambda }{2} \times  \left( {{m}^{2} - {3m}}\right) }\right|  < m + 1, m = 3$ 时,不等式恒成立,

在 $m > 3$ 时, $\left| \frac{\lambda  - 2}{2}\right|  < \frac{m + 1}{{m}^{2} - {3m}}$ ,记 $f\left( m\right)  = \frac{m + 1}{{m}^{2} - {3m}}$ ,

$f\left( {m + 1}\right)  - f\left( m\right)  = \frac{m + 2}{{\left( m + 1\right) }^{2} - 3\left( {m + 1}\right) } - \frac{m + 1}{{m}^{2} - {3m}} =  - \frac{{m}^{2} + {3m} - 2}{\left( {{m}^{2} - m - 2}\right) \left( {{m}^{2} - {3m}}\right) } < 0$ ,

$\therefore$ 在 $m > 3$ 时,数列 $\{ f\left( m\right) \}$ 递减, $f\left( 4\right)  = \frac{5}{4}$ ,不等式为 $\left| \frac{\lambda  - 2}{2}\right|  < \frac{5}{4}$ ①,

$m = 2$ 时,不等式为 $\left| \frac{\lambda  - 2}{2}\right|  < \frac{3}{2}$ ②, $m = 1$ 时,不等式为 $\left| \frac{\lambda  - 2}{2}\right|  < 1$ ③,

因此只要不等式②成立，不等式①不成立即可. 不等式①不成立时， $m \geq  5$ ，不等式都不成立，

$\therefore \frac{5}{4} \leq  \left| \frac{\lambda  - 2}{2}\right|  < \frac{3}{2}$ ,解得 $- 1 < \lambda  \leq   - \frac{1}{2}$ 或 $\frac{9}{2} \leq  \lambda  < 5$ .

4、已知函数 $f\left( x\right)  = {x}^{2} + {bx} + c\left( {b, c \in  \mathbf{R}}\right)$ ,且 $f\left( x\right)  < 0$ 的解集为 $\{ x \mid   - 3 < x < 1\}$ ; 数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,对任意 $n \in  {\mathrm{N}}^{ * }$ ,满足 ${S}_{n} = f\left( n\right)  + 3 - n$ .

(1)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)已知数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为 ${T}_{n}$ ，满足 ${T}_{n} = 2{b}_{n} - \frac{1}{2}, n \in  {\mathrm{N}}^{ * }$ ，求数列 $\left\{  {{a}_{n} \cdot  {b}_{n}}\right\}$ 的前 $n$ 项和 ${A}_{n}$ ；

(3)已知不等式 ${\left( \frac{11}{10}\right) }^{\frac{{a}_{n}}{2} - {18}}\left\lbrack  {f\left( x\right)  + {2x} + {403}}\right\rbrack   > n\left( {\frac{{a}_{n}}{2} + 6}\right)$ 对 $n \in  {\mathrm{N}}^{ * }$ 恒成立，求实数 $x$ 的取值范围.

(3) $\left( {-\infty , - 8}\right)  \cup  \left( {4, + \infty }\right)$ .

【解析】(1) 函数 $f\left( x\right)  = {x}^{2} + {bx} + c\left( {b, c \in  \mathbf{R}}\right)$ ,且 $f\left( x\right)  < 0$ 的解集为 $\{ x \mid   - 3 < x < 1\}$

可知 $x =  - 3, x = 1$ 是方程 ${x}^{2} + {bx} + c = 0$ 的两根,

则 $\left\{  \begin{matrix}  - 3 + 1 =  - b \\   - 3 \times  1 = c \end{matrix}\right.$ ,解得 $\left\{  \begin{array}{l} b = 2 \\  c =  - 3 \end{array}\right.$ ; 所以 $f\left( x\right)  = {x}^{2} + {2x} - 3$

由 ${S}_{n} = f\left( n\right)  + 3 - n$ ,代入可得 ${S}_{n} = {n}^{2} + n$

当 $n = 1$ 时, ${S}_{1} = {a}_{1} = 2$ ; 当 $n \geq  2$ 时, ${a}_{n} = {S}_{n} - {S}_{n - 1} = {2n}$ ,检验 $n = 1$ 时符合.

综上所述, ${a}_{n} = {2n}, n \in  {N}^{ * }$

(2)由 ${T}_{n} = 2{b}_{n} - \frac{1}{2}$ ，则 ${T}_{n - 1} = 2{b}_{n - 1} - \frac{1}{2},\left( {n \geq  2}\right)$ ，

由 ${T}_{n} - {T}_{n - 1} = 2{b}_{n} - 2{b}_{n - 1}$ ,则 ${b}_{n} = 2{b}_{n} - 2{b}_{n - 1}$ ,所以 ${b}_{n} = 2{b}_{n - 1}\left( {n \geq  2}\right)$

当 $n = 1$ 时, ${T}_{1} = 2{b}_{1} - \frac{1}{2}$ ; 则 ${b}_{1} = 2{b}_{1} - \frac{1}{2}$ ,解得 ${b}_{1} = \frac{1}{2}$

则 $\left\{  {b}_{n}\right\}$ 是以 $\frac{1}{2}$ 为首项,2 为公比的等比数列,则 ${b}_{n} = \frac{1}{2} \times  {2}^{n - 1}$ ,

由 ${a}_{n} \cdot  {b}_{n} = {2n} \times  \frac{1}{2} \times  {2}^{n - 1} = n \cdot  {2}^{n - 1}$ 则 ${A}_{n} = 1 \times  {2}^{0} + 2 \times  {2}^{1} + 3 \times  {2}^{2} + \cdots  + n \cdot  {2}^{n - 1}$ ①

$2{A}_{n} = 1 \times  {2}^{1} + 2 \times  {2}^{2} + 3 \times  {2}^{3} + \cdots  + n \cdot  {2}^{n}$ ② 由①-②可得

$- {A}_{n} = {2}^{0} + {2}^{1} + {2}^{2}\cdots  + {2}^{n - 1} - n \cdot  {2}^{n} = \frac{1 \times  \left( {1 - {2}^{n}}\right) }{1 - 2} - n \cdot  {2}^{n} = \left( {1 - n}\right) {2}^{n} - 1$

则 ${A}_{n} = \left( {n - 1}\right) {2}^{n} + 1, n \in  {\mathrm{N}}^{ * }$

(3)因为 ${a}_{n} = {2n}$ ，所以 ${\left( \frac{11}{10}\right) }^{\frac{{a}_{n}}{2} - {18}}\left\lbrack  {f\left( x\right)  + {2x} + {403}}\right\rbrack   > n\left( {\frac{{a}_{n}}{2} + 6}\right)$ 等价于: ${x}^{2} + {4x} + {400} > {c}_{n}$ ，

其中 ${c}_{n} = {\left( \frac{10}{11}\right) }^{n - {18}}\left( {n + 6}\right) n$ ,

而 ${c}_{n + 1} - {c}_{n} = {\left( \frac{10}{11}\right) }^{n - {17}}\left( {n + 1}\right) \left( {n + 7}\right)  - {\left( \frac{10}{11}\right) }^{n - {18}}n\left( {n + 6}\right)  = {\left( \frac{10}{11}\right) }^{n - {18}}\frac{-{n}^{2} + {14n} + {70}}{11}$ ,

当 $n \in  \left\lbrack  {1.17}\right\rbrack$ 时 ${c}_{n + 1} - {c}_{n} > 0 \Rightarrow  {c}_{n + 1} > {c}_{n}$ ,则 ${c}_{1} < {c}_{2} < \cdots  < {c}_{18}$

当 $n \in  \left( {{18}, + \infty }\right)$ 时, ${c}_{n + 1} - {c}_{n} < 0 \Rightarrow  {c}_{n + 1} < {c}_{n}$ ,综上所述, ${c}_{n}$ 的最大值为 ${c}_{18}$

由不等式 ${\left( \frac{11}{10}\right) }^{\frac{{a}_{n}}{2} - {18}}\left\lbrack  {f\left( x\right)  + {2x} + {403}}\right\rbrack   > n\left( {\frac{{a}_{n}}{2} + 6}\right)$ 对 $n \in  {\mathrm{N}}^{ * }$ 恒成立得

则 ${x}^{2} + {4x} + {400} > {c}_{18}$ ; 即 ${x}^{2} + {4x} - {32} > 0$

解不等式可得 $x > 4$ 或 $x <  - 8$ ,所以实数 $x$ 的取值范围 $\left( {-\infty , - 8}\right)  \cup  \left( {4, + \infty }\right)$

5、对于无穷数列 $\left\{  {a}_{n}\right\}$ 的某一项 ${a}_{k}$ ,若存在 $m \in  {N}^{ * }$ ,有 ${a}_{k} < {a}_{k + m}\left( {k \in  {\mathbf{N}}^{ * }}\right)$ 成立,则称 ${a}_{k}$ 具有性质 $P\left( m\right)$ .

(1)设 ${a}_{n} = \left| {n - 3}\right| \left( {n \in  {N}^{ * }}\right)$ ，若对任意的 $k \in  {\mathbf{N}}^{ * }$ ， ${a}_{k}$ 都具有性质 $P\left( m\right)$ ，求 $m$ 的最小值；

(2)设等差数列 $\left\{  {a}_{n}\right\}$ 的首项 ${a}_{1} =  - 2$ ，公差为 $d$ ，前 $n$ 项和为 ${S}_{n}\left( {n \in  {N}^{ * }}\right)$ ，若对任意的 $k \in  {\mathbf{N}}^{ * }$ 数列 $\left\{  {S}_{n}\right\}$ 中的项 ${S}_{k}$ 都具有性质 $P\left( 7\right)$ ,求实数 $d$ 的取值范围;

(3)设数列 $\left\{  {a}_{n}\right\}$ 的首项 ${a}_{1} = 2$ ，当 $n \geq  2\left( {n \in  {\mathbf{N}}^{ * }}\right)$ 时，存在 $i\left( {1 \leq  i \leq  n - 1, i \in  {\mathbf{N}}^{ * }}\right)$ 满足 ${a}_{n} = 2{a}_{i}$ ，且此数列中恰有一项 ${a}_{t}\left( {2 \leq  t \leq  {99}, t \in  {\mathbf{N}}^{ * }}\right)$ 不具有性质 $P\left( 1\right)$ ,求此数列的前100项和的最大值和最小值以及取得最值时对应的 $t$ 的值.

【答案】(1) $5;\left( 2\right) \left( {\frac{1}{2}, + \infty }\right) ;\left( 3\right) t = {99}$ 时,最大值为 $3 \times  {2}^{99} - 2;t = {50}$ 或 $t = {51}$ 时,最小值为 $6 \cdot  {2}^{50} - 6$ .

【解析】(1)经计算知: ${a}_{1} < {a}_{6} < {a}_{7} < \cdots$ ,此时 $m \geq  5;{a}_{2} < {a}_{5} < {a}_{6} < \cdots$ ,此时 $m \geq  3$ ;

当 $k \geq  3$ 时, ${a}_{k} < {a}_{k + 1} < {a}_{k + 2} < \cdots$ ,此时 $m \geq  1$ .

综上可知, $m \geq  5$ ,即对任意的 $k \in  {\mathbf{N}}^{ * },{a}_{k}$ 都具有性质 $P\left( m\right)$ 时, $m$ 的最小值为 5 ;

(2)由已知可得, ${S}_{n} =  - {2n} + \frac{n\left( {n - 1}\right) }{2}d$ ,若对任意的 $k \in  {\mathbf{N}}^{ * }$ ,数列 $\left\{  {S}_{n}\right\}$ 中的 ${S}_{k}$ 都具有性质 $P\left( 7\right)$ ,则 ${S}_{k} < {S}_{k + 7}$ 对任意的 $k \in  {\mathbf{N}}^{ * }$ 恒成立,

即 $- {2k} + \frac{k\left( {k - 1}\right) }{2}d <  - 2\left( {k + 7}\right)  + \frac{\left( {k + 7}\right) \left( {k + 7 - 1}\right) }{2}d$ ,整理得: $d > \frac{2}{k + 3}$ .

因为 $k \geq  1$ ,则 $\frac{2}{k + 3} \leq  \frac{1}{2}$ ,所以 $d > \frac{1}{2}$ . 因此,实数 $d$ 的取值范围是 $\left( {\frac{1}{2}, + \infty }\right)$ ;

(3)对于 $2 \leq  t \leq  {99}, t \in  {\mathbf{N}}^{ * }$ ,

因为 ${a}_{1}\text{ 、 }{a}_{2}\text{ 、 }\cdots \text{ 、 }{a}_{t - 1}$ 都具有性质 $P\left( 1\right)$ ,所以 ${a}_{1} < {a}_{2} < \cdots  < {a}_{t - 1} < {a}_{t}$ ,

而当 $n \geq  2\left( {n \in  {\mathbf{N}}^{ * }}\right)$ 时,存在 $i\left( {1 \leq  i \leq  n - 1, i \in  {\mathbf{N}}^{ * }}\right)$ 满足 ${a}_{n} = 2{a}_{i}$ ,

所以 ${a}_{1}\text{ 、 }{a}_{2}\text{ 、 }\cdots \text{ 、 }{a}_{t}$ 依次为: $2\text{ 、 }{2}^{2}\text{ 、 }{2}^{3}\text{ 、 }\cdots \text{ 、 }{2}^{t}$ ,

由已知 ${a}_{t}$ 不具有性质 $P\left( 1\right)$ ,故 ${a}_{t + 1}$ 的可能值为 ${2}^{2}\text{ 、 }{2}^{3}\text{ 、 }\cdots \text{ 、 }{2}^{t}$ ,

又因为 ${a}_{t + 1}\text{ 、 }{a}_{t + 2}\text{ 、 }\cdots \text{ 、 }{a}_{100}$ 都具有性质 $P\left( 1\right)$ ,所以 ${a}_{t + 1} < {a}_{t + 2} < \cdots  < {a}_{100}$ ,

欲使此数列的前 100 项和最大, ${a}_{t + 1}\text{ 、 }{a}_{t + 2}\text{ 、 }\cdots \text{ 、 }{a}_{100}$ 依次为: ${2}^{t}\text{ 、 }{2}^{t + 1}\text{ 、 }\cdots \text{ 、 }{2}^{99}$ ,

欲使此数列的前 100 项和最小, ${a}_{t + 1}\text{ 、 }{a}_{t + 2}\text{ 、 }\cdots \text{ 、 }{a}_{100}$ 依次为: ${2}^{2}\text{ 、 }{2}^{3}\text{ 、 }\cdots \text{ 、 }{2}^{{101} - t}$ ,

下面分别计算前 100 项和:

$\left( {{a}_{1} + {a}_{2} + \cdots  + {a}_{t}}\right)  + \left( {{a}_{t + 1} + {a}_{t + 2} + \cdots  + {a}_{100}}\right)  = \left( {2 + {2}^{2} + {2}^{3} + \cdots  + {2}^{t}}\right)  + \left( {{2}^{t} + {2}^{t + 1} + \cdots  + {2}^{99}}\right)  = {2}^{t} + {2}^{100} - 2$ ,

当 $t = {99}$ 时,此数列的前 100 项和最大,最大值为 ${2}^{99} + {2}^{100} - 2 = 3 \times  {2}^{99} - 2$ ;

$\left( {{a}_{1} + {a}_{2} + \cdots  + {a}_{t}}\right)  + \left( {{a}_{t + 1} + {a}_{t + 2} + \cdots  + {a}_{100}}\right)  = \left( {2 + {2}^{2} + {2}^{3} + \cdots  + {2}^{t}}\right)  + \left( {{2}^{2} + {2}^{3} + \cdots  + {2}^{{101} - t}}\right)$

$= 2\left( {{2}^{t} + \frac{{2}^{101}}{{2}^{t}}}\right)  - 6 \geq  4\sqrt{{2}^{t} \cdot  \frac{{2}^{101}}{{2}^{t}}} - 6 = {2}^{52}\sqrt{2} - 6$ .

当且仅当 ${2}^{t} = \frac{{2}^{101}}{{2}^{t}}$ 时,即 $t = \frac{101}{2}$ 时等号成立,但 $t = \frac{101}{2} \notin  {\mathbf{N}}^{ * }$ ,

这时取 $t = {50}$ 或 $t = {51}$ 时,此数列的前 100 项和最小,最小值为 $2\left( {{2}^{50} + {2}^{51}}\right)  - 6 = 6 \cdot  {2}^{50} - 6$ .

(二)数列中不定方程问题(方程有解与恒成立问题)

## 例题精讲

【例 7】已知数列 $\left\{  {a}_{n}\right\}$ 的各项均为正整数,对于 $n = 1,2,3,\ldots$ ,有 ${a}_{n + 1} = \left\{  \begin{array}{ll} 3{a}_{n} + 5, & {a}_{n}\text{ 为奇数 } \\  \frac{{a}_{n}}{{2}^{k}}, & {a}_{n}\text{ 为偶数 } \end{array}\right.$ ,其中 $k$ 为使 ${a}_{n + 1}$ 为奇数的正整数；若存在 $m \in  {N}^{ * }$ ，当 $n > m$ 且 ${a}_{n}$ 为奇数时， ${a}_{n}$ 恒为常数 $p$ ，则 $p$ 的值为___；

【难度】 $\star   \star   \star$

【答案】 $p = 1$ 或 5

【解析】令 ${a}_{n} = p$ ,则 ${a}_{n + 1} = {3p} + 5,{a}_{n + 2} = \frac{{3p} + 5}{{2}^{k}} = p$ ,所以 $p = \frac{5}{{2}^{k} - 3}$ ,因为 $p$ 是奇数,所以 ${2}^{k} - 3 = 5$ 或 1，则 $k = 3$ 或 2，符合题意，于是 $p = 1$ 或 5，

【例 8】已知等差数列 $\left\{  {a}_{n}\right\}$ 的公差 $d > 0$ . 设 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n},{a}_{1} = 1,{S}_{2} \cdot  {S}_{3} = {36}$ .

(1)求 $d$ 及 ${S}_{n}$ ；

(2)求 $m$ ， $k\left( {m\text{ ， }k \in  {\mathrm{N}}^{ * }}\right)$ 的值，使得 ${a}_{m} + {a}_{m + 1} + {a}_{m + 2} + \ldots  + {a}_{m + k} = {65}$ .

【难度】 $\star   \star   \star$

【答案】( 1 ) $d = 2,{S}_{n} = {n}^{2}$ ; ( 2 )当 $m = 5, k = 4$ 时， ${a}_{m} + {a}_{m + 1} + \ldots  + {a}_{m + k} = {65}$ .

【解析】(1) $\because {S}_{2} \cdot  {S}_{3} = {36},{a}_{1} = 1,\therefore \left( {2{a}_{1} + d}\right)  \cdot  \left( {3{a}_{1} + {3d}}\right)  = {36}$ ,即 ${d}^{2} + {3d} - {10} = 0$ ,

$\therefore d = 2$ 或 $d =  - 5.\;\because d > 0,\therefore d = 2$ ,

$\therefore \left\{  {a}_{n}\right\}$ 为 1 为首项,2 为公差的等差数列, $\therefore {S}_{n} = n + \frac{n\left( {n - 1}\right) }{2} \times  2 = {n}^{2}$ .

(2) $\because {a}_{m} + {a}_{m + 1} + \ldots  + {a}_{m + k} = {65},\therefore {S}_{m + k} - {S}_{m - 1} = {65}$ .

由 $\left( 1\right)$ 得 ${\left( m + k\right) }^{2} - {\left( m - 1\right) }^{2} = {65}$ ,即 ${2mk} + {k}^{2} + {2m} - 1 = {65},\;{2m}\left( {k + 1}\right)  + {k}^{2} - 1 = {65}$ ,

即 $\left( {k + 1}\right) \left( {{2m} + k - 1}\right)  = {65} = 5 \times  {13}$ ,

$\because k\text{ 、 }m \in  {\mathrm{N}}^{ + },\therefore {2m} + k - 1 > k + 1,\therefore \left\{  {\begin{array}{l} k + 1 = 5 \\  {2m} + k - 1 = {13} \end{array}\text{ 解之得 }m = 5, k = 4}\right.$ .

$\therefore$ 当 $m = 5, k = 4$ 时, ${a}_{m} + {a}_{m + 1} + \ldots  + {a}_{m + k} = {65}$ .

【例 9】已知数列 $\left\{  {a}_{n}\right\}$ 的奇数项是首项为 1 的等差数列,偶数项是首项为 2 的等比数列. 数列 $\left\{  {a}_{n}\right\}$ 前 $n$ 项和为 ${S}_{n}$ ,且满足 ${S}_{3} = {a}_{4},{a}_{3} + {a}_{5} = 2 + {a}_{4}$

(1)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)在数列 $\left\{  {a}_{n}\right\}$ 中，是否存在连续的三项 ${a}_{m},{a}_{m + 1},{a}_{m + 2}$ ，按原来的顺序成等差数列？若存在，求出所有满足条件的正整数 $m$ 的值; 若不存在,说明理由.

【难度】 $\star   \star   \star   \star$

【答案】(1) ${a}_{n} = \left\{  {\begin{array}{l} n,\;n = {2k} - 1 \\  2 \cdot  {3}^{\frac{n}{2} - 1}, n = {2k} \end{array}, k \in  {N}^{ * };\left( 2\right) }\right.$ 在数列 $\left\{  {a}_{n}\right\}$ 中,仅存在连续的三项 ${a}_{1},{a}_{2},{a}_{3}$ ,按原来的顺序成等差数列,此时正整数 $m$ 的值为 1 .

【解析】(1) 设等差数列的公差为 $d$ ,等比数列的公比为 $q$ ,则 ${a}_{1} = 1,{a}_{2} = 2,{a}_{3} = 1 + d,{a}_{4} = {2q},{a}_{5} = 1 + {2d}$ , $\because {S}_{3} = {a}_{4},\therefore 1 + 2\left( {1 + d}\right)  = {2q}$ ,即 $4 + d = {2q}$ ,

又 ${a}_{3} + {a}_{5} = 2 + {a}_{4},\left( {1 + d}\right) \left( {1 + {2d}}\right)  = 2 + {2q}$ ,即 ${3d} = {2q}$ ,解得 $d = 2, q = 3$ ,

$\therefore$ 对于 $k \in  {N}^{ * }$ ,有 ${a}_{{2k} - 1} = 1 + \left( {k - 1}\right)  \cdot  2 = {2k} - 1,{a}_{2k} = 2 \cdot  {3}^{k - 1}$ ,故 ${a}_{n} = \left\{  {\begin{array}{l} n,\;n = {2k} - 1 \\  2 \cdot  {3}^{\frac{n}{2} - 1}, n = {2k} \end{array}, k \in  {N}^{ * }}\right.$ .

(2)在数列 $\left\{  {a}_{n}\right\}$ 中，仅存在连续的三项 ${a}_{1},{a}_{2},{a}_{3}$ ，按原来的顺序成等差数列，此时正整数 $m$ 的值为 1，下面说明理由.

若 ${a}_{m} = {a}_{2k}$ ,则由 ${a}_{m} + {a}_{m + 2} = 2{a}_{m + 1}$ ,得 $2 \cdot  {3}^{k - 1} + 2 \cdot  {3}^{k} = 2\left( {{2k} + 1}\right)$ ,

化简得 $4 \cdot  {3}^{k - 1} = {2k} + 1$ ,此式左边为偶数,右边为奇数,不可能成立.

若 ${a}_{m} = {a}_{{2k} - 1}$ ,则由 ${a}_{m} + {a}_{m + 2} = 2{a}_{m + 1}$ ,得 $\left( {{2k} - 1}\right)  + \left( {{2k} + 1}\right)  = 2 \cdot  2 \cdot  {3}^{k - 1}$ ,化简得 $k = {3}^{k - 1}$ .

令 ${T}_{k} = \frac{k}{{3}^{k - 1}},\left( {k \in  {N}^{ * }}\right)$ ,则 ${T}_{k + 1} - {T}_{k} = \frac{k + 1}{{3}^{k}} - \frac{k}{{3}^{k - 1}} = \frac{1 - {2k}}{{3}^{k}} < 0$ .

因此, $1 = {T}_{1} > {T}_{2} > {T}_{3} > \cdots$ ,故只有 ${T}_{1} = 1$ ,此时 $k = 1, m = 2 \times  1 - 1 = 1$ .

综上,在数列 $\left\{  {a}_{n}\right\}$ 中,仅存在连续的三项 ${a}_{1},{a}_{2},{a}_{3}$ ,按原来的顺序成等差数列,此时正整数 $m$ 的值为 1

【例 10】已知数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ ,满足 $4{S}_{n} = \left( {{2n} + 1}\right) {a}_{n} + \lambda \left( {\lambda  \neq  0}\right)$ .

(1)求证:数列 $\left\{  {a}_{n}\right\}$ 等差数列；

(2)当 $\lambda  = 1$ 时，记 ${b}_{n} = {10}^{\frac{{a}_{n} + 1}{{2}^{2} \cdot  {3}^{n}}}$ ，是否存在正整数 $p\text{ 、 }q\left( {1 < p < q}\right)$ ，使得 ${b}_{1}\text{ 、 }{b}_{p}\text{ 、 }{b}_{q}$ 成等比数列? 若存在,求出所有满足条件的数对 $\left( {p, q}\right)$ ; 若不存在,请说明理由;

(3)若数列 ${a}_{{k}_{1}}\text{ 、 }{a}_{{k}_{2}}\text{ 、 }{a}_{{k}_{3}}\text{ 、 }\cdots \text{ 、 }{a}_{{k}_{n}}\text{ 、 }\cdots \left( {{k}_{1} = 1}\right)$ 是公比为3的等比数列，求最小正整数 $m$ ，使得当 $n \geq  m$ 时, ${k}_{n} > \frac{{n}^{3}}{2}$ .

【难度】 $\star   \star   \star   \star$

【答案】( 1 )证明见解析；( 2 )存在，有且只有一个为 $\left( {2,3}\right)$ ；(3)6.

【解析】(1)由题意得 $\left\{  \begin{array}{l} 4{S}_{n + 1} = \left( {{2n} + 3}\right) {a}_{n + 1} + \lambda \\  4{S}_{n} = \left( {{2n} + 1}\right) {a}_{n} + \lambda  \end{array}\right.$ ,两式相减得 $\left( {{2n} - 1}\right) {a}_{n + 1} = \left( {{2n} + 1}\right) {a}_{n}\left( {n \geq  2}\right)$ ,

则有 $\left( {{2n} - 3}\right) {a}_{n} = \left( {{2n} - 1}\right) {a}_{n - 1}\left( {n \geq  2}\right)$ ,所以 $\left( {{4n} - 2}\right) {a}_{n} = \left( {{2n} - 1}\right) {a}_{n - 1} + \left( {{2n} - 1}\right) {a}_{n + 1}\left( {n \geq  2}\right)$ .

因为 ${2n} - 1 > 0$ ,所以 ${a}_{n - 1} + {a}_{n + 1} = 2{a}_{n}\left( {n \geq  2}\right)$ ,故数列 $\left\{  {a}_{n}\right\}$ 为等差数列;

(2)因为 $\lambda  = 1$ ， $\therefore 4{S}_{n} = \left( {{2n} + 1}\right) {a}_{n} + 1$ ，

所以 $4{S}_{1} = 3{a}_{1} + 1$ ,解得 ${a}_{1} = 1;4{S}_{2} = 5{a}_{2} + 1$ ,即 $4 + 4{a}_{2} = 5{a}_{2} + 1$ ,解得 ${a}_{2} = 3$ .

所以数列 $\left\{  {a}_{n}\right\}$ 的公差为 2,所以 ${a}_{n} = {2n} - 1$ ,故 ${b}_{n} = {10}^{\frac{n}{{3}^{n}}}$ .

假设存在正整数 $p\text{ 、 }q\left( {1 < p < q}\right)$ ,使得 ${b}_{1},{b}_{p},{b}_{q}$ 成等比数列,则 ${\left( {10}^{\frac{p}{{3}^{p}}}\right) }^{2} = {10}^{\frac{1}{3}} \cdot  {10}^{\frac{q}{{3}^{q}}}$ ,

于是 $\frac{2p}{{3}^{p}} = \frac{1}{3} + \frac{q}{{3}^{q}}\;\left( *\right)$ ,所以 $q = {3}^{q}\left( {\frac{2p}{{3}^{p}} - \frac{1}{3}}\right)$ .

当 $p = 2$ 时, $q = {3}^{q} \cdot  \frac{1}{9} = {3}^{q - 2}$ ,则 $q = 3$ ,所以 $\left\{  \begin{array}{l} p = 2 \\  q = 3 \end{array}\right.$ 是方程 (*) 的一组解;

当 $p \geq  3$ 且 $p \in  {N}^{ * }$ 时,因为 $\frac{2\left( {p + 1}\right) }{{3}^{p + 1}} - \frac{2p}{{3}^{p}} = \frac{2 - {4p}}{{3}^{p + 1}} < 0$ ,所以,数列 $\left\{  \frac{2p}{{3}^{p}}\right\}$ 在 $\left\{  {p \mid  p \geq  3, p \in  {N}^{ * }}\right\}$ 上单调递减,

所以 $\frac{2p}{{3}^{p}} - \frac{1}{3} \leq  \frac{2 \times  3}{{3}^{3}} - \frac{1}{3} < 0$ ,此时方程 $\left( *\right)$ 无正整数解.

综上,满足题设的数对 $\left( {p, q}\right)$ 有且只有一个,为 $\left( {2,3}\right)$ ;

(3)由题意得 $\left\{  \begin{array}{l} 4{S}_{1} = 3{a}_{1} + \lambda \\  4{S}_{2} = 5{a}_{2} + \lambda  \end{array}\right.$ ，解得 $\left\{  \begin{array}{l} {a}_{1} = \lambda \\  {a}_{2} = {3\lambda } \end{array}\right.$ ，

故数列 $\left\{  {a}_{n}\right\}$ 的公差 $d = {a}_{2} - {a}_{1} = {2\lambda }$ ,所以 ${a}_{n} = {a}_{1} + \left( {n - 1}\right) d = \left( {{2n} - 1}\right) \lambda$ ,

故 ${a}_{{k}_{1}} = {a}_{1} = \lambda$ ,所以 ${a}_{{k}_{n}} = {a}_{{k}_{1}} \cdot  {3}^{n - 1} = {3}^{n - 1}\lambda$ .

又因为 ${a}_{{k}_{n}} = \left( {2{k}_{n} - 1}\right) \lambda$ ,所以 $2{k}_{n} - 1 = {3}^{n - 1}$ ,即 ${k}_{n} = \frac{{3}^{n - 1} + 1}{2}$ .

记 ${c}_{n} = {k}_{n} - \frac{{n}^{3}}{2} = \frac{{3}^{n - 1} - {n}^{3} + 1}{2} = \frac{{3}^{n}}{6}\left( {1 - \frac{{n}^{3}}{{3}^{n - 1}}}\right)  + \frac{1}{2}$ ,

则 ${c}_{1} > 0,{c}_{2} < 0,{c}_{3} < 0,{c}_{4} < 0,{c}_{5} < 0,{c}_{6} = \frac{1}{2}\left( {{243} - {216} + 1}\right)  > 0$ ,

猜想: 当 $n \geq  6$ 时, ${c}_{n} > 0$ . 验证如下: 记 ${P}_{n} = 1 - \frac{{n}^{3}}{{3}^{n - 1}}\left( {n \geq  6}\right)$ ,

则 ${P}_{n + 1} - {P}_{n} = \frac{{n}^{3}}{{3}^{n - 1}} - \frac{{\left( n + 1\right) }^{3}}{{3}^{n}} = \frac{1}{{3}^{n}}\left( {2{n}^{3} - 3{n}^{2} - {3n} - 1}\right)  = \frac{1}{{3}^{n}}\left\lbrack  {\left( {2{n}^{3} - 5{n}^{2}}\right)  + \left( {2{n}^{2} - {3n} - 2}\right)  + 1}\right\rbrack$

$= \frac{1}{{3}^{n}}\left\lbrack  {\left( {{2n} - 5}\right) {n}^{2} + \left( {n - 2}\right) \left( {{2n} + 1}\right)  + 1}\right\rbrack   > 0,$

所以数列 $\left\{  {P}_{n}\right\}$ 单调递增,故 ${P}_{n} \geq  {P}_{6} = 1 - \frac{216}{243} > 0$ ,所以 ${c}_{n} > 0$ ,故最小正整数 $m$ 的值为 6 .

【例 11】对于数列 $\left\{  {x}_{n}\right\}$ ,若存在 $m \in  {N}^{ * }$ ,使得 ${x}_{{2m} - k} = {x}_{k}$ 对任意 $1 \leq  k \leq  {2m} - 1\left( {k \in  {N}^{ * }}\right)$ 都成立,则称数列 $\left\{  {x}_{n}\right\}$ 为 “ $m$ - 折叠数列”.

(1)若 ${a}_{n} = \left| {{25n} - {200}}\right| \left( {n \in  {N}^{ * }}\right)$ ， ${b}_{n} = {n}^{2} - {2019n} - 1\left( {n \in  {N}^{ * }}\right)$ ，判断数列 $\left\{  {a}_{n}\right\}$ 、 $\left\{  {b}_{n}\right\}$ 是否是 “ $m -$ 折叠数列”,如果是,指出 $m$ 的值; 如果不是,请说明理由;

(2)若 ${x}_{n} = {q}^{n}\left( {n \in  {N}^{ * }}\right)$ ，求所有的实数 $q$ ，使得数列 $\left\{  {x}_{n}\right\}$ 是 3-折叠数列；

(3)给定常数 $p \in  {N}^{ * }$ ，是否存在数列 $\left\{  {x}_{n}\right\}$ ，使得对所有 $m \in  {N}^{ * }$ ， $\left\{  {x}_{n}\right\}$ 都是 ${pm} -$ 折叠数列，且 $\left\{  {x}_{n}\right\}$ 的各项中恰有 $p + 1$ 个不同的值,证明你的结论.

【难度】 $\star   \star   \star   \star$

【答案】( 1 ) $\left\{  {a}_{n}\right\}$ 是 “ $m$ -折叠数列”， $m = 8$ ； $\left\{  {b}_{n}\right\}$ 不是 “ $m$ -折叠数列”；( 2 ) $q = 0$ 或 $q = 1$ 或 $q =  - 1$ ； (3)存在，证明见解析.

【解析】(1) $\exists m \in  {N}^{ * }$ ,使得 ${x}_{{2m} - k} = {x}_{k}$ 对任意 $1 \leq  k \leq  {2m} - 1\left( {k \in  {N}^{ * }}\right)$ 都成立,知: $\left\{  {x}_{n}\right\}$ 在 $1 \leq  n \leq  {2m} - 1$ 内关于 $n = m$ 对称即可,

1、 ${a}_{n} = \left\{  {\begin{array}{ll} {200} - {25n}, & 1 \leq  n < 8 \\  {25n} - {200}, & n \geq  8 \end{array},\left( {n \in  {N}^{ * }}\right) }\right.$ 有 $\left\{  {a}_{n}\right\}$ 在 $1 \leq  n \leq  2 \times  8 - 1 = {15}$ 内关于 $n = 8$ 对称,故 $m = 8$ ,即是“8 - 折叠数列”;

2、 ${b}_{n} = {n}^{2} - {2019n} - 1,\left( {n \in  {N}^{ * }}\right)$ 有 $\left\{  {b}_{n}\right\}$ 在 $1 \leq  n \leq  {2018}$ 内关于 $n = \frac{2019}{2}$ 对称, $m = \frac{2019}{2} \notin  {N}^{ * }$ ,即不是 “ $m$ -折叠数列”;

(2)由(1)知: 若 ${x}_{n} = {q}^{n}\left( {n \in  {N}^{ * }}\right)$ 是 3-折叠数列,有:

$\left\{  {\begin{array}{l} q = {q}^{5} \\  {q}^{2} = {q}^{4} \end{array}\text{ 解之得: }q =  - 1\text{ 或 }q = 0}\right.$ 或 $q = 1$ ,

(3)给定 $p \in  {N}^{ * }$ ， $\left\{  {x}_{n}\right\}$ 都是 ${pm} -$ 折叠数列，即 $\left\{  {x}_{n}\right\}$ 有多条对称轴，其中关于 $n = {pm}$ 对称，设 ${x}_{n} = \cos \frac{\pi x}{p}$ ， 即 $\frac{\pi x}{p} = {m\pi }$ 有对称轴为 $x = {pm}, m \in  {N}^{ * }$ 且周期为 ${2p}$ ,

$\therefore$ 在周期 $(1,{2p}\rbrack$ 内,有对称轴 $x = p : (1,{2p}\rbrack$ 与 $\left\lbrack  {p,{2p}}\right\rbrack$ 上值的个数相同,

而 $\left\lbrack  {p,{2p}}\right\rbrack$ 上 ${x}_{n} = \cos \frac{\pi x}{p}$ 单调递增,则 $\left\{  {x}_{n}\right\}$ 的各项中有 $p + 1$ 个不同的值,

$\therefore$ 给定常数 $p \in  {N}^{ * }$ 存在数列 $\left\{  {x}_{n}\right\}$ ,使得对所有 $m \in  {N}^{ * },\left\{  {x}_{n}\right\}$ 都是 ${pm} -$ 折叠数列且 $\left\{  {x}_{n}\right\}$ 的各项中恰有 $p + 1$ 个不同的值.

巩固训练

1、已知数列 $\left\{  {a}_{n}\right\}$ 的奇数项是首项为 1 的等差数列,偶数项是首项为 2 的等比数列,数列 $\left\{  {a}_{n}\right\}$ 前 $n$ 项和为 ${S}_{n}$ ,且满足 ${S}_{3} = {a}_{4},{a}_{5} = {a}_{2} + {a}_{3}$ .

(1)求数列 $\left\{  {a}_{n}\right\}$ 的通项公式；

(2)若 ${a}_{m}{a}_{m + 1} = {a}_{m + 2}$ ，求正整数 $m$ 的值；

(3)是否存在正整数 $m$ ，使得 $\frac{{S}_{2m}}{{S}_{{2m} - 1}}$ 恰好为数列 $\left\{  {a}_{n}\right\}$ 中的一项？若存在，求出所有满足条件的 $m$ 值，若不存在, 说明理由.

【答案】( 1 ) ${a}_{n} = \left\{  {\begin{array}{l} n\left( {n\text{ 为奇数 }}\right) \\  2 \cdot  {3}^{\frac{n}{2} - 1}\left( {n\text{ 为偶数 }}\right)  \end{array};\left( 2\right) m = 2;\left( 3\right) m = 1}\right.$ 或 $m = 2$ .

【解析】(1) 设 ${a}_{1},{a}_{3},{a}_{5},\ldots ,{a}_{{2k} - 1},\cdots$ 的公差为 $d.{a}_{2},{a}_{4},{a}_{6},\ldots ,{a}_{2k},\cdots$ 的公比为 $q$ ,

则 ${a}_{4} = {a}_{2} \cdot  q = {2q},{a}_{3} = {a}_{1} + d = 1 + d,{a}_{5} = 1 + {2d}$ ,

由 $\left\{  {\begin{array}{l} {S}_{3} = {a}_{4} \\  {a}_{5} = {a}_{2} + {a}_{3} \end{array} \Rightarrow  \left\{  {\begin{array}{l} 4 + d = {2q} \\  1 + {2d} = 2 + 1 + d \end{array}, \Rightarrow  \left\{  {\begin{array}{l} {2q} = 4 + d \\  d = 2 \end{array} \Rightarrow  \left\{  \begin{array}{l} d = 2 \\  q = 3 \end{array}\right. }\right. }\right. }\right.$

故 ${a}_{2k} = {a}_{2}{q}^{k - 1} = 2 \cdot  {3}^{k - 1},{a}_{{2k} - 1} = {a}_{1} + \left( {k - 1}\right) d = {2k} - 1$ ,故 ${a}_{n} = \left\{  \begin{array}{l} n\left( {n\text{ 为奇数 }}\right) \\  2 \cdot  {3}^{\frac{n}{2} - 1}\left( {n\text{ 为偶数 }}\right)  \end{array}\right.$ ;

(2)由 ${a}_{m}{a}_{m + 1} = {a}_{m + 2}$ ，

若 $m = {2k}\left( {k \in  {N}^{ * }}\right)$ ,则 ${a}_{2k}{a}_{{2k} + 1} = {a}_{{2k} + 2}$ ,即 ${2k} + 1 = 3 \Rightarrow  k = 1$ ,即 $m = 2$ ,

若 $m = {2k} - 1\left( {k \in  {N}^{ * }}\right)$ ,即 ${a}_{{2k} - 1}{a}_{2k} = {a}_{{2k} + 1}$ ,即 $\left( {{2k} - 1}\right)  \cdot  2 \cdot  {3}^{k - 1} = {2k} + 1$ ,所以 $2 \cdot  {3}^{k - 1} = 1 + \frac{2}{{2k} - 1}$ , $\because 2 \cdot  {3}^{k - 1}$ 为正整数,所以 $\frac{2}{{2k} - 1}$ 为正整数,即 ${2k} - 1 = 1$ ,即 $k = 1$ ,此时式为 $2 \cdot  {3}^{0} = 3$ 不合题意, 综上, $m = 2$ .

(3)若 $\frac{{S}_{2m}}{{S}_{{2m} - 1}}$ 为 $\left\{  {a}_{n}\right\}$ 中的一项，则 $\frac{{S}_{2m}}{{S}_{{2m} - 1}}$ 为正整数，

又 ${S}_{{2m} - 1} = \left( {{a}_{1} + {a}_{3} + \ldots  + {a}_{{2m} - 1}}\right)  + \left( {{a}_{2} + {a}_{4} + \ldots  + {a}_{{2m} - 2}}\right)  = \frac{m\left( {1 + {2m} - 1}\right) }{2} + \frac{2\left( {{3}^{m - 1} - 1}\right) }{3 - 1} = {3}^{m - 1} + {m}^{2} - 1$ , $\therefore \frac{{S}_{2m}}{{S}_{{2m} - 1}} = \frac{{S}_{{2m} - 1} + {a}_{2m}}{{S}_{{2m} - 1}} = 1 + \frac{2 \cdot  {3}^{m - 1}}{{3}^{m - 1} + {m}^{2} - 1} = 1 + \frac{2 \cdot  \left( {{3}^{m - 1} + {m}^{2} - 1}\right)  - 2{m}^{2} + 2}{{3}^{m - 1} + {m}^{2} - 1} = 3 - \frac{2\left( {{m}^{2} - 1}\right) }{{3}^{m - 1} + {m}^{2} - 1} \leq  3$ , 故若 $\frac{{S}_{2m}}{{S}_{{2m} - 1}}$ 为 $\left\{  {a}_{n}\right\}$ 中的某一项只能为 ${a}_{1},{a}_{2},{a}_{3}$ ,

① 若 $3 - \frac{2\left( {{m}^{2} - 1}\right) }{{3}^{m - 1} + {m}^{2} - 1} = 1 \Rightarrow$ 无解;

② 若 $3 - \frac{2\left( {{m}^{2} - 1}\right) }{{3}^{m - 1} + {m}^{2} - 1} = 2 \Rightarrow  {3}^{m - 1} + 1 - {m}^{2} = 0$ ，显然 $m = 1$ 与题意不符， $m = 2$ 与题意相符，

当 $m \geq  3$ 时,即 $f\left( m\right)  = {3}^{m - 1} + 1 - {m}^{2}$ ,利用作差法可得 $f\left( m\right)$ 在 $\lbrack 3, + \infty )$ 为增函数

故 $f\left( m\right)  > f\left( 3\right)  = 1 > 0$ ,故当 $m \geq  3$ 时方程 ${3}^{m - 1} + 1 - {m}^{2} = 0$ 无解,即 $m = 2$ 是方程唯一解

③ 若 $3 - \frac{2\left( {{m}^{2} - 1}\right) }{{3}^{m - 1} + {m}^{2} - 1} = 3 \Rightarrow  {m}^{2} = 1$ ，即 $m = 1$ ，综上所述， $m = 1$ 或 $m = 2$ .

2、已知数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项的和为 ${S}_{n}$ ，记 ${b}_{n} = \frac{{S}_{n + 1}}{n}$ . 设数列 $\left\{  {a}_{n}\right\}$ 是公比为 $q\left( {q > 2}\right)$ 的等比数列,若存在 $r$ , $t\left( {r, t \in  {N}^{ * }, r < t}\right)$ 使得 $\frac{{b}_{t}}{{b}_{r}} = \frac{t + 2}{r + 2}$ ,求 $q$ 的值.

【答案】 $q = \frac{5 + \sqrt{85}}{6}$

【解析】因为 $\frac{{b}_{t}}{{b}_{r}} = \frac{\frac{{a}_{1}\left( {1 - {q}^{t + 1}}\right) }{t\left( {1 - q}\right) }}{\frac{{a}_{1}\left( {1 - {q}^{r + 1}}\right) }{r\left( {1 - q}\right) }} = \frac{t + 2}{r + 2}$ ,所以 $\frac{{q}^{t + 1} - 1}{t\left( {t + 2}\right) } = \frac{{q}^{r + 1} - 1}{r\left( {r + 2}\right) }$ .

设 $f\left( n\right)  = \frac{{q}^{n + 1} - 1}{n\left( {n + 2}\right) }, n \geq  2, n \in  {N}^{ * }$ .

则 $f\left( {n + 1}\right)  - f\left( n\right)  = \frac{{q}^{n + 2} - 1}{\left( {n + 1}\right) \left( {n + 3}\right) } - \frac{{q}^{n + 1} - 1}{n\left( {n + 2}\right) } = \frac{{q}^{n + 1}\left\lbrack  {\left( {q - 1}\right) {n}^{2} + 2\left( {q - 2}\right) n - 3}\right\rbrack   + {2n} + 3}{n\left( {n + 1}\right) \left( {n + 2}\right) \left( {n + 3}\right) }$ ,

因为 $q > 2, n \geq  2$ ,所以 $\left( {q - 1}\right) {n}^{2} + 2\left( {q - 2}\right) n - 3 > {n}^{2} - 3 \geq  1 > 0$ ,

所以 $f\left( {n + 1}\right)  - f\left( n\right)  > 0$ ,即 $f\left( {n + 1}\right)  > f\left( n\right)$ ,即 $f\left( n\right)$ 单调递增.

所以当 $r \geq  2$ 时, $t > r \geq  2$ ,

则 $f\left( t\right)  > f\left( r\right)$ ,即 $\frac{{q}^{t + 1} - 1}{t\left( {t + 2}\right) } > \frac{{q}^{r + 1} - 1}{r\left( {r + 2}\right) }$ ,这与 $\frac{{q}^{t + 1} - 1}{t\left( {t + 2}\right) } = \frac{{q}^{r + 1} - 1}{r\left( {r + 2}\right) }$ 互相矛盾.

所以 $r = 1$ ,即 $\frac{{q}^{t + 1} - 1}{t\left( {t + 2}\right) } = \frac{{q}^{2} - 1}{3}$ .

若 $t \geq  3$ ,则 $f\left( t\right)  \geq  f\left( 3\right)  = \frac{{q}^{4} - 1}{15} = \frac{{q}^{2} - 1}{3} \cdot  \frac{{q}^{2} + 1}{5} > \frac{{q}^{2} - 1}{3}$ ,

即 $\frac{{q}^{t + 1} - 1}{t\left( {t + 2}\right) } > \frac{{q}^{2} - 1}{3}$ ,与 $\frac{{q}^{t + 1} - 1}{t\left( {t + 2}\right) } = \frac{{q}^{2} - 1}{3}$ 相矛盾.

于是 $t = 2$ ,所以 $\frac{{q}^{3} - 1}{8} = \frac{{q}^{2} - 1}{3}$ ,即 $3{q}^{2} - {5q} - 5 = 0$ . 又 $q > 2$ ,所以 $q = \frac{5 + \sqrt{85}}{6}$ .

3、无穷数列 $\left\{  {a}_{n}\right\}$ 满足: 只要 ${a}_{p} = {a}_{q}\left( {p, q \in  {\mathbf{N}}^{ * }}\right)$ ,必有 ${a}_{p + 1} = {a}_{q + 1}$ ,则称 $\left\{  {a}_{n}\right\}$ 为 “和谐递进数列”. 若 $\left\{  {a}_{n}\right\}$ 为“和谐递进数列”, ${S}_{n}$ 为其前 $n$ 项和,且 ${a}_{1} = 1,{a}_{2} = 2,{a}_{4} = 1,{a}_{6} + {a}_{8} = 6$ ,则 ${S}_{2021} =$ ___.

【答案】 4714

【解析】由题知 ${a}_{1} = {a}_{4} = 1,{a}_{2} = 2$ ,所以 ${a}_{5} = {a}_{2} = 2$ ,

同理 ${a}_{3} = {a}_{6},{a}_{7} = {a}_{4} = 1,{a}_{8} = {a}_{5} = 2$ ,因为 ${a}_{6} + {a}_{8} = 6$ ,所以 ${a}_{3} = {a}_{6} = 4$ ,

故数列 $\left\{  {a}_{n}\right\}$ 是以 3 为周期的数列, ${S}_{2021} = {S}_{{673} \times  3 + 2} = \left( {1 + 2 + 4}\right)  \times  {673} + \left( {1 + 2}\right)  = {4714}$ ,故答案为: 4714.

4、数列 $\left\{  {a}_{n}\right\}$ 与 $\left\{  {b}_{n}\right\}$ 满足 ${a}_{1} = a,{b}_{n} = {a}_{n + 1} - {a}_{n},{S}_{n}$ 是数列 $\left\{  {a}_{n}\right\}$ 的前 $n$ 项和 $\left( {n \in  {\mathrm{N}}^{ * }}\right)$ .

(1)设数列 $\left\{  {b}_{n}\right\}$ 是首项和公比都为 $- \frac{1}{3}$ 的等比数列,且数列 $\left\{  {a}_{n}\right\}$ 也是等比数列,求 $a$ 的值；

(2)设 $a = 4$ ， ${b}_{n} = 2.{c}_{n} = \frac{{S}_{n} + {2\lambda }}{{2}^{n}}$ ( $n \in  {\mathbf{N}}^{ * }$ ， $\lambda  \geq   - 2$ )，若存在整数 $k$ ， $l$ ，且 $k > l > 1$ ，使得 ${c}_{k} = {c}_{l}$ 成立,求 $\lambda$ 的所有可能值.

【答案】( 1 ) $\frac{1}{4};$ ( 2 )-1 或 -2 .

【解析】解: (1) 数列 $\left\{  {b}_{n}\right\}$ 是首项和公比都为 $- \frac{1}{3}$ 的等比数列,所以 ${b}_{n} = {\left( -\frac{1}{3}\right) }^{n}$ .

数列 $\left\{  {a}_{n}\right\}$ 与 $\left\{  {b}_{n}\right\}$ 满足 ${a}_{1} = a,{b}_{n} = {a}_{n + 1} - {a}_{n}$ ,所以 ${a}_{n + 1} - {a}_{n} = {\left( -\frac{1}{3}\right) }^{n}$ .

所以 ${a}_{2} = a - \frac{1}{3},{a}_{3} = {a}_{2} + \frac{1}{9} = a - \frac{2}{9}$ ,

由于数列 $\left\{  {a}_{n}\right\}$ 也是等比数列,所以 ${a}_{2}{}^{2} = {a}_{1} \cdot  {a}_{3}$ ,整理得 ${\left( a - \frac{1}{3}\right) }^{2} = a\left( {a - \frac{2}{9}}\right)$ ,解得 $a = \frac{1}{4}$ .

(2)由于 $a = 4,{b}_{n} = 2$ 所以 ${a}_{n + 1} - {a}_{n} = 2$ ,整理得: ${a}_{n} = {2n} + 2$ . 故 ${S}_{n} = {4n} + 2 \times  \frac{n\left( {n - 1}\right) }{2} = {n}^{2} + {3n}$ . 所以 ${c}_{n} = \frac{{S}_{n} + {2\lambda }}{{2}^{n}} = \frac{{n}^{2} + {3n} + {2\lambda }}{{2}^{n}}$ ,假设存在整数 $k, l$ ,且 $k > l > 1$ ,使得 ${c}_{k} = {c}_{l}$ 成立,故 $\frac{{k}^{2} + {3k} + {2\lambda }}{{2}^{k}} = \frac{{l}^{2} + {3l} + {2\lambda }}{{2}^{l}}$ ,当 $\left\{  \begin{array}{l} k = 3 \\  l = 2 \\  \lambda  =  - 1 \end{array}\right.$ 或 $\left\{  \begin{matrix} k = 4 \\  l = 2 \\  \lambda  =  - 2 \end{matrix}\right.$ 时,满足条件.

5、已知数列 $\left\{  {a}_{n}\right\}$ 是一个公差大于零的等差数列,且 ${a}_{3}{a}_{6} = {55},{a}_{2} + {a}_{7} = {16}$ ,数列 $\left\{  {b}_{n}\right\}$ 的前 $n$ 项和为 ${S}_{n}$ , 且 ${S}_{n} = 2{b}_{n} - 2$ .

(1)求数列 $\left\{  {a}_{n}\right\}$ ， $\left\{  {b}_{n}\right\}$ 的通项公式；

(2)求数列 $\left\{  \frac{{a}_{n}}{{b}_{n}}\right\}$ 的前 $n$ 项和 ${T}_{n}$ ；

(3)设 ${c}_{n} = {b}_{n} + {4n} - 3$ ，是否存在正整数 $\mathrm{i}$ ， $j\left( {2 < i < j}\right)$ ，使 ${c}_{2}$ ， ${c}_{i}$ ， ${c}_{j}$ 成等差数列，若存在，求出所有的正整数 $\mathrm{i}, j$ ,若不存在,请说明理由.

【答案】( 1 ) ${a}_{n} = {2n} - 1$ ， ${b}_{n} = {2}^{n}$ ；( 2 ) ${T}_{n} = 3 - \frac{{2n} + 3}{{2}^{n}}$ ；( 3 )存在， $i = 4$ ， $j = 5$ .

【解析】(1)依题意，设等差数列 $\left\{  {a}_{n}\right\}$ 的公差为 $d\left( {d > 0}\right)$ ，则有 $\left\{  \begin{array}{l} \left( {{a}_{1} + {2d}}\right) \left( {{a}_{1} + {5d}}\right)  = {55}, \\  2{a}_{1} + {7d} = {16}, \end{array}\right.$ .

将②代入①得 $\left( {{16} - {3d}}\right) \left( {{16} + {3d}}\right)  = {220}$ ，即 ${d}^{2} = 4$ ， $\because d > 0$ ， $\therefore d = 2$ ， ${a}_{1} = 1.\therefore {a}_{n} = {2n} - 1$ .

当 $n = 1$ 时， ${S}_{1} = 2{b}_{1} - 2$ ， ${b}_{1} = 2 \neq  0$ ，

当 $n \geq  2$ 时， ${b}_{n} = {S}_{n} - {S}_{n - 1} = \left( {2{b}_{n} - 2}\right)  - \left( {2{b}_{n - 1} - 2}\right)  = 2{b}_{n} - 2{b}_{n - 1}$ ， $\therefore \frac{{b}_{n}}{{b}_{n - 1}} = 2 \neq  0$ ，

$\therefore$ 数列 $\left\{  {b}_{n}\right\}$ 是以 2 为首项,2 为公比的等比数列, ${b}_{n} = {2}^{n}$ .

(2) $\because \frac{{a}_{n}}{{b}_{n}} = \frac{{2n} - 1}{{2}^{n}},\;{T}_{n} = \frac{1}{2} + \frac{3}{{2}^{2}} + \ldots  + \frac{{2n} - 1}{{2}^{n}}$ ①， $\frac{1}{2}{T}_{n} = \frac{1}{{2}^{2}} + \frac{3}{{2}^{3}} + \ldots  + \frac{{2n} - 3}{{2}^{n}} + \frac{{2n} - 1}{{2}^{n + 1}}$ ②，

①-②，得 $\frac{1}{2}{T}_{n} = \frac{1}{2} + \frac{2}{{2}^{2}} + \frac{2}{{2}^{3}} + \ldots  + \frac{2}{{2}^{n}} - \frac{{2n} - 1}{{2}^{n - 1}} = \frac{1}{2} + \frac{1}{2} + \frac{1}{{2}^{2}} + \ldots  + \frac{1}{{2}^{n - 1}} - \frac{{2n} - 1}{{2}^{n + 1}}$ ,

$= \frac{1}{2} + \frac{\frac{1}{2}\left( {1 - \frac{1}{{2}^{n - 1}}}\right) }{1 - \frac{1}{2}} - \frac{{2n} - 1}{{2}^{n + 1}} = \frac{3}{2} - \frac{{2n} + 3}{{2}^{n + 1}},\therefore {T}_{n} = 3 - \frac{{2n} + 3}{{2}^{n}}$ .

(3)假设存在正整数 $\mathrm{i}, j\left( {2 < i < j}\right)$ ，使 ${c}_{2},{c}_{i},{c}_{j}$ ，成等差数列.

$\because {c}_{n} = {2}^{n} + {4n} - 3,\therefore 2\left( {{2}^{i} + {4i} - 3}\right)  = 9 + \left( {{2}^{j} + {4j} - 3}\right) ,\therefore {2}^{i - 1} + {2i} = {2}^{j - 2} + j + 3$ 且 $2 < i < j$ ,

当 $j = i + 1$ 时, ${2}^{i - 1} + {2i} = {2}^{i - 1} + i + 4$ ,解得 $i = 4, j = 5$ ;

当 $j \geq  i + 2$ 时, $\left( {{2}^{j - 2} + j + 3}\right)  - \left( {{2}^{i - 1} + {2i}}\right)  \geq  \left( {{2}^{i} + i + 5}\right)  - \left( {{2}^{i - 1} + {2i}}\right)  = {2}^{i - 1} - i + 5$ ,

令 $f\left( n\right)  = {2}^{n - 1} - n + 5\left( {n \geq  3}\right)$ ,

则 $f\left( {n + 1}\right)  - f\left( n\right)  = {2}^{n - 1} - 1 > 0,\therefore$ 当 $n \geq  3$ 时, $f\left( n\right)$ 单调递增, $\therefore f\left( n\right)  \geq  f\left( 3\right)  = 6 > 0$ ,

$\therefore {2}^{i - 1} + {2i} < {2}^{j - 2} + j + 3$ ,即 ${2}^{i - 1} + {2i} = {2}^{j - 2} + j + 3$ 无解,

综上: 存在正整数 $i = 4, j = 5$ ,使 ${c}_{2},{c}_{i},{c}_{j}$ 成等差数列.
