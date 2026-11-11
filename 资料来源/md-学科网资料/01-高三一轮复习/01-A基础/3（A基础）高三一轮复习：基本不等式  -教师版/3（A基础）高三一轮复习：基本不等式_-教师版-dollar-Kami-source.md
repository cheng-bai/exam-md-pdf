基本不等式

<table><tr><td>教学目标</td><td>1、会用基本不等式比较大小和不等式的证明; <br> 2、会用基本不等式求最值或研究值域; <br> 3、利用基本不等式解决恒成立问题； <br> 4、利用基本不等式解决实际问题.</td></tr><tr><td>重点</td><td>1、注意基本不等式求最值(取等号)成立的条件； <br> 2、在学习过程中注意转化与化归思想、分类讨论思想的应用.</td></tr><tr><td>难点</td><td>利用基本不等式解决恒成立问题</td></tr></table>

\vspace{14pt}

## (一)利用基本不等式求最值

\vspace{14pt}

## 知识梳理

\vspace{14pt}

## 1、基本不等式的形式

1. 基本不等式 1:

如果 $a, b \in  \mathrm{R}$ ,那么 ${a}^{2} + {b}^{2} \geq  {2ab}$ (当且仅当 $a = b$ 时取等号“=”).

2. 基本不等式 2:

如果 $a, b$ 是正数，那么 $\frac{a + b}{2} \geq  \sqrt{ab}$ (当且仅当 $a = b$ 时取等号“=”).

\begin{kaminotebox}[要点注释]
${a}^{2} + {b}^{2} \geq  {2ab}$ 和 $\frac{a + b}{2} \geq  \sqrt{ab}$ 两者的异同:

(1)成立的条件是不同的:前者只要求 $a, b$ 都是实数，而后者要求 $a, b$ 都是正数；

(2)取等号 “=” 的条件在形式上是相同的，都是 “当且仅当 $a = b$ 时取等号”.

(3) ${a}^{2} + {b}^{2} \geq  {2ab}$ 可以变形为: ${ab} \leq  \frac{{a}^{2} + {b}^{2}}{2},\frac{a + b}{2} \geq  \sqrt{ab}$ 可以变形为: ${ab} \leq  {\left( \frac{a + b}{2}\right) }^{2}$ .
\end{kaminotebox}

\noindent 3. 如图， ${AB}$ 是圆的直径，点 $C$ 是 ${AB}$ 上的一点， ${AC} = a,{BC} = b$ ，过点 $C$ 作 ${DC} \bot  {AB}$ 交圆于点 $\mathrm{D}$ ， 连接 ${AD}\text{ 、 }{BD}$ .

易证 ${Rt\Delta ACD} \sim  {Rt\Delta DCB}$ ,那么 $C{D}^{2} = {CA} \cdot  {CB}$ ,即 ${CD} = \sqrt{ab}$ .

这个圆的半径为 $\frac{a + b}{2}$ ,它大于或等于 ${CD}$ ,即 $\frac{a + b}{2} \geq  \sqrt{ab}$ ,其中当且仅当点 $C$ 与圆心重合,即 $a = b$ 时, 等号成立.

\begin{center}
\includegraphics[width=0.58\linewidth,keepaspectratio]{images/0_541_1706_317_281_0.jpg}
\end{center}

\begin{kaminotebox}[知识补充]
1. 在数学中,我们称 $\frac{a + b}{2}$ 为 $a, b$ 的算术平均数,称 $\sqrt{ab}$ 为 $a, b$ 的几何平均数. 因此基本不等式可叙述为:两个正数的算术平均数不小于它们的几何平均数.

2. 如果把 $\frac{a + b}{2}$ 看作是正数 $a, b$ 的等差中项, $\sqrt{ab}$ 看作是正数 $a, b$ 的等比中项,那么基本不等式可以叙述为: 两个正数的等差中项不小于它们的等比中项.
\end{kaminotebox}

\begin{kaminotebox}[知识拓展]
当 $0 < a \leq  b$ 时, $a \leq  \frac{2}{\frac{1}{a} + \frac{1}{b}} \leq  \sqrt{ab} \leq  \frac{a + b}{2} \leq  \sqrt{\frac{{a}^{2} + {b}^{2}}{2}} \leq  b$

推广: ${a}_{1},{a}_{2},{a}_{3},\cdots ,{a}_{n}$ 是 $n$ 个正数,则 $\frac{{a}_{1} + {a}_{2} + \cdots  + {a}_{n}}{n}$ 称为这 $n$ 个正数的算术平均数, $\sqrt[n]{{a}_{1} \cdot  {a}_{2}\cdots  \cdot  {a}_{n}}$ 称为这 $n$ 个正数的几何平均数,它们的关系是: $\frac{{a}_{1} + {a}_{2} + \cdots  + {a}_{n}}{n} \geq  \sqrt[n]{{a}_{1} \cdot  {a}_{2}\cdots  \cdot  {a}_{n}}$ ,当且仅当 ${a}_{1} = {a}_{2} = \cdots  = {a}_{n}$ 时等号成立.
\end{kaminotebox}

\clearpage

\vspace{14pt}

## 2、利用基本不等式证明不等式

利用基本不等式证明不等式是综合法证明不等式的一种情况，综合法是指从已证不等式和问题的已知条件出发, 借助不等式的性质和有关定理, 经过逐步的逻辑推理, 最后转化为所求问题, 其特征是以“已知” 看“可知”，逐步推向“未知”.

\vspace{14pt}

## 3、利用基本不等式求最值问题

(1)“积定和最小”: $a + b \geq  2\sqrt{ab} \Leftrightarrow$ 如果积 ${ab}$ 是定值 $\mathrm{P}$ ，那么当 $a = b$ 时，和 $a + b$ 有最小值 $2\sqrt{P}$ ；

(2)“和定积最大”: ${ab} \leq  {\left( \frac{a + b}{2}\right) }^{2} \Leftrightarrow$ 如果和 $a + b$ 是定值 $\mathrm{S}$ ，那么当 $a = b$ 时，积 ${ab}$ 有最大值 $\frac{1}{4}{S}^{2}$ .

\begin{kaminotebox}[要点注释]
基本不等式求最值需注意的问题:

\noindent (1)各数(或式)均为正；

\noindent (2)和或积为定值;

\noindent (3)等号能否成立，即“一正、二定、三相等”这三个条件缺一不可.

若无明显 “定值”，则用配凑的方法，使和为定值或积为定值.

当多次使用基本不等式时, 一定要注意每次是否能保证等号成立, 并且要注意取等号的条件的一致性, 否则就会出错, 因此在利用基本不等式处理问题时, 列出等号成立的条件不仅是解题的必要步骤, 而且也是检验转换是否有误的一种方法.
\end{kaminotebox}

\vspace{14pt}

## 例题精讲

【例 1】(1)下列函数中最小值为 4 的是( )

A. $y = x + \frac{4}{x}$ B. $y = {3}^{x} + 4 \cdot  {3}^{-x}$

C. $y = \sin x + \frac{4}{\sin x}\left( {0 < x < \pi }\right)$ D. $y = \lg x + 4{\log }_{x}{10}$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star$}}

\begin{kamianswerbox}
B
\end{kamianswerbox}


\begin{kamisolutionbox}
对于 $\mathrm{A}$ ,当 $x < 0$ 时, $y = x + \frac{4}{x} < 0$ ,故 $\mathrm{A}$ 错误;

对于 $\mathrm{B}, y = {3}^{x} + \frac{4}{{3}^{x}} \geq  2\sqrt{{3}^{x} \cdot  \frac{4}{{3}^{x}}} = 4$ ,当且仅当 ${3}^{x} = \frac{4}{{3}^{x}}$ ,即 $x = {\log }_{3}2$ 时,取等号,故 $\mathrm{B}$ 正确;

对于 $\mathrm{C}$ ,虽然 $x \in  \left( {0,\pi }\right) ,\sin x > 0$ ,但运用基本不等式后,等号成立的条件是 $\sin x = \frac{4}{\sin x}$ ,即 $\sin x = 2$ , 显然不可能，故 C 错误；

对于 $\mathrm{D}$ ，由于没有给出 $x$ 的范围，所以 $\lg x$ 的正负不确定，不满足最小值为 4，故 $\mathrm{D}$ 错误. 故选: $\mathrm{B}$ .
\end{kamisolutionbox}

(2)下列不等式恒成立的是( )

A. ${a}^{2} + {b}^{2} \leq  {2ab}$ B. ${a}^{2} + {b}^{2} \geq   - {2ab}$ C. $a + b \geq   - 2\sqrt{\left| ab\right| }$ D. $a + b \leq  2\sqrt{\left| ab\right| }$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
$B$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 对于 $A$ ,由 ${\left( a - b\right) }^{2} \geq  0$ ,知 ${a}^{2} + {b}^{2} \geq  {2ab}$ ,即 $A$ 错误;

对于 $B$ ,由 ${\left( a + b\right) }^{2} \geq  0$ ,知 ${a}^{2} + {b}^{2} \geq   - {2ab}$ ,即 $B$ 正确;

对于 $C$ ,当 $a = 0, b =  - 1$ 时, $a + b =  - 1, - 2\sqrt{\left| ab\right| } = 0$ ,此时 $a + b <  - 2\sqrt{\left| ab\right| }$ ,即 $C$ 错误;

对于 $D$ ,当 $a = 0, b = 1$ 时, $a + b = 1,2\sqrt{\left| ab\right| } = 0$ ,此时 $a + b >  - 2\sqrt{\left| ab\right| }$ ,即 $D$ 错误,故选: $B$ .
\end{kamisolutionbox}

【例 2】(1) 设 $a, b \in  \left( {0, + \infty }\right)$ ，若 ${2a} + b = 1$ ，则 ${ab}$ 的最大值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star$}}

\begin{kamianswerbox}
$\frac{1}{8}$ .
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $\because a > 0, b > 0,\therefore 1 = {2a} + b \geq  2\sqrt{2ab}$ ,

化为 ${ab} \leq  \frac{1}{8}$ ,当且仅当 $b = {2a} = \frac{1}{2}$ 时取等号. 则 ${ab}$ 的最大值为 $\frac{1}{8}$ . 故答案为: $\frac{1}{8}$ .
\end{kamisolutionbox}

(2)设 $x, y \in  {R}^{ + }$ ，若 ${4x} + \frac{1}{y} = 1$ . 则 $\frac{x}{y}$ 的最大值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
$\frac{1}{16}$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $\because {4x} + \frac{1}{y} = 1, x, y \in  {R}^{ + },\therefore 4{x}^{2} + \frac{x}{y} = x$ ,即 $\frac{x}{y} =  - 4{x}^{2} + x =  - 4{\left( x - \frac{1}{8}\right) }^{2} + \frac{1}{16} \leq  \frac{1}{16}$ ,

当且仅当 “ $x = \frac{1}{8}, y = 2$ ” 时取等号,故答案为: $\frac{1}{16}$ .
\end{kamisolutionbox}

【例 3】(1) 已知 $x > 1$ ，则不等式 $x + \frac{2}{x - 1} \geq  2\sqrt{2} + 1$ 等号成立时， $x =$ ___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
$1 + \sqrt{2}$ .
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $x > 1$ ,则 $x + \frac{2}{x - 1} = x - 1 + \frac{2}{x - 1} + 1 \geq  2\sqrt{2} + 1$ ,当且仅当 $x - 1 = \frac{2}{x - 1}$ ,即 $x = 1 + \sqrt{2}$ 时等号成立, 故答案为: $1 + \sqrt{2}$ .
\end{kamisolutionbox}

( 2 )若 $x > 4$ ，则函数 $y =  - x + \frac{1}{4 - x}$ 有(   )

A. 最大值-6 B. 最小值6 C. 最大值-2 D. 最小值-2

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
$A$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $y =  - x + \frac{1}{4 - x} = 4 - x + \frac{1}{4 - x} - 4 =  - \left\lbrack  {\left( {x - 4}\right)  + \frac{1}{x - 4}}\right\rbrack   - 4 \leq   - 2\sqrt{\left( {x - 4}\right)  \times  \frac{1}{x - 4}} - 4 =  - 6$ , 即函数有最大值-6,故选: $A$ .
\end{kamisolutionbox}

(3)已知正实数 $x$ 、 $y$ 满足 ${x}^{2} + {y}^{2} = 4$ ，则 $x\sqrt{1 + {y}^{2}}$ 的最大值为( )

A. 2

B. $\frac{5}{2}$ C. 3

D. $\frac{9}{4}$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star\star$}}

\begin{kamianswerbox}
B
\end{kamianswerbox}


\begin{kamisolutionbox}
$x\sqrt{1 + {y}^{2}} = \sqrt{{x}^{2}\left( {1 + {y}^{2}}\right) } \leq  \frac{{x}^{2} + 1 + {y}^{2}}{2} = \frac{5}{2}$ ,当且仅当 ${x}^{2} = 1 + {y}^{2}$ ,即 $x = \frac{\sqrt{10}}{2}, y = \frac{\sqrt{6}}{2}$ 时,等号成立. $\therefore$ 所求最大值为 $\frac{5}{2}$ . 故选: B.
\end{kamisolutionbox}

【例 4】(1) 已知 $x, y > 0$ 且 $x + {2y} = 1$ ，则 $\frac{1}{x} + \frac{1}{y}$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
$3 + 2\sqrt{2}$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 由已知: $\frac{1}{x} + \frac{1}{y} = \left( {\frac{1}{x} + \frac{1}{y}}\right) \left( {x + {2y}}\right)  = 1 + \frac{2y}{x} + \frac{x}{y} + 2 \geq  3 + 2\sqrt{2}$ ,

当且仅当 $\frac{2y}{x} = \frac{x}{y}$ 时等号成立,则 $\frac{1}{x} + \frac{1}{y}$ 的最小值为 $3 + 2\sqrt{2}$ ,故答案为: $3 + 2\sqrt{2}$ .
\end{kamisolutionbox}

(2)已知正数 $m$ ， $n$ 满足 $m\left( {n - 1}\right)  = {8n}$ ，则 $m + {2n}$ 的最小值是( ).

A. 18 B. 16 C. 8 D. 10

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：未标注}}

\begin{kamianswerbox}
A
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $\because$ 正数 $m, n$ 满足 $m\left( {n - 1}\right)  = {8n},\therefore \frac{8}{m} + \frac{1}{n} = 1$ .

$\therefore m + {2n} = \left( {m + {2n}}\right) \left( {\frac{8}{m} + \frac{1}{n}}\right)  = {10} + \frac{16n}{m} + \frac{m}{n} \geq  {10} + 2\sqrt{\frac{16n}{m} \cdot  \frac{m}{n}} = {18}$ ,

当且仅当 $\frac{16n}{m} = \frac{m}{n}$ ,即 $m = {12}, n = 3$ 时取等号, $\therefore m + {2n}$ 的最小值为 18 . 故选: $A$ .
\end{kamisolutionbox}

(3)已知 $x > 0, y > 0$ ，且 $\frac{1}{x + 1} + \frac{1}{y} = \frac{1}{2}$ ，则 $x + y$ 的最小值为( )

A. 3 B. 5 C. 7 D. 9

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$C$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $\because x > 0, y > 0$ ,且 $\frac{1}{x + 1} + \frac{1}{y} = \frac{1}{2}$ ,

$\therefore x + 1 + y = 2\left( {\frac{1}{x + 1} + \frac{1}{y}}\right) \left( {x + 1 + y}\right)  = 2\left( {1 + 1 + \frac{y}{x + 1} + \frac{x + 1}{y}}\right)  \geq  2\left( {2 + 2\sqrt{\frac{y}{x + 1} \cdot  \frac{x + 1}{y}}}\right)  = 8$ ,当且仅当 $\frac{y}{x + 1} = \frac{x + 1}{y}$ ,即 $x = 3, y = 4$ 时取等号, $\therefore x + y \geq  7$ ,故 $x + y$ 的最小值为 7,故选: $C$ .
\end{kamisolutionbox}

(4) 已知 $a$ 、 $b$ 均为正实数，且 $a + \frac{2}{b} = 3$ ，则 $\frac{2}{a} + b$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$\frac{8}{3}$ .
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 因为 $a\text{ 、 }b$ 均为正实数,且 $a + \frac{2}{b} = 3$ ,则

$\frac{2}{a} + b = \frac{1}{3}\left( {\frac{2}{a} + b}\right) \left( {a + \frac{2}{b}}\right)  = \frac{1}{3}\left( {4 + \frac{4}{ab} + {ab}}\right)  \geq  \frac{1}{3}\left( {4 + 2\sqrt{\frac{4}{ab} \cdot  {ab}}}\right)  = \frac{8}{3},$

当且仅当 ${ab} = \frac{4}{ab}$ 且 $a + \frac{2}{b} = 3$ ，即 $a = \frac{3}{2}$ ， $b = \frac{4}{3}$ 时取等号，所以 $\frac{2}{a} + b$ 的最小值 $\frac{8}{3}$ . 故答案为: $\frac{8}{3}$ .
\end{kamisolutionbox}

(5) 若 $a, b$ 均为非负实数，且 $a + b = 1$ ，则 $\frac{1}{a + {2b}} + \frac{4}{{2a} + b}$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
3
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 设 $a + {2b} = m,{2a} + b = n$ ,则 $m + n = 3$ ,

原式变形为: $\frac{1}{m} + \frac{4}{n} = \frac{1}{3}\left( {m + n}\right) \left( {\frac{1}{m} + \frac{4}{n}}\right)  = \frac{1}{3}\left\lbrack  {5 + \frac{n}{m} + \frac{4m}{n}}\right\rbrack   \geq  \frac{1}{3}\left( {5 + 2\sqrt{\frac{n}{m} \cdot  \frac{4m}{n}}}\right)  = 3$ ;

当且仅当 $\frac{n}{m} = \frac{4m}{n}$ 时等号成立; 故答案为: 3 .
\end{kamisolutionbox}

【例 5】( 1 )已知 $x, y$ 为正实数，则 $\frac{2y}{x} + \frac{9x}{{2x} + y}$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$6\sqrt{2} - 4$ .
\end{kamianswerbox}


\begin{kamisolutionbox}
方法一: 令 ${2x} + y = t\left( {t > 0}\right)$ ,则 $y = t - {2x},\therefore \frac{2y}{x} + \frac{9x}{{2x} + y} = \frac{{2t} - {4x}}{x} + \frac{9x}{t} = \frac{2t}{x} + \frac{9x}{t} - 4 \geq  6\sqrt{2} - 4$ , 当且仅当 $\frac{2t}{x} = \frac{9x}{t}$ ,即 $t = \frac{3\sqrt{2}}{2}x$ 时等号成立.

方法二: 令 $\frac{y}{x} = t > 0$ ,则

$\frac{2y}{x} + \frac{9x}{{2x} + y} = {2t} + \frac{9}{2 + t} = 2\left( {t + 2}\right)  + \frac{9}{2 + t} - 4 \geq  2\sqrt{2\left( {t + 2}\right)  \cdot  \frac{9}{2 + t}} - 4 = 6\sqrt{2} - 4$ ,

当且仅当 $2\left( {t + 2}\right)  = \frac{9}{2 + t}$ ,即 $\frac{y}{x} = t = \frac{3\sqrt{2}}{2} - 2$ 时,等号成立,

故答案为: $6\sqrt{2} - 4$ .
\end{kamisolutionbox}

(2)若直线 $l : \frac{2x}{{2b} + a} + \frac{y}{a + b} = 1$ 经过第一象限内的点 $P\left( {\frac{1}{a},\frac{1}{b}}\right)$ ，则 ${ab}$ 的最大值为( )

A. $\frac{7}{6}$ B. $4 - 2\sqrt{2}$ C. $5 - 2\sqrt{3}$ D. $6 - 3\sqrt{2}$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$B$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 直线 $l : \frac{2x}{{2b} + a} + \frac{y}{a + b} = 1$ 经过第一象限内的点 $P\left( {\frac{1}{a},\frac{1}{b}}\right)$ ,

则 $a, b > 0,\frac{2}{a\left( {{2b} + a}\right) } + \frac{1}{b\left( {a + b}\right) } = 1.\therefore {ab} = {ab}\left( {\frac{2}{a\left( {{2b} + a}\right) } + \frac{1}{b\left( {a + b}\right) }}\right)  = \frac{2b}{a + {2b}} + \frac{a}{a + b}$ .

令 $a + {2b} = m, a + b = n,\left( {m, n > 0}\right)$ ,则 $a = {2n} - m, b = m - n$ ,

代入上式得 $\therefore {ab} = \frac{2b}{a + {2b}} + \frac{a}{a + b} = \frac{2\left( {m - n}\right) }{m} + \frac{{2n} - m}{n} = 4 - \left( {\frac{2n}{m} + \frac{m}{n}}\right)  \leq  4 - 2\sqrt{2}$ .

当且仅当 $\frac{2n}{m} = \frac{m}{n}$ ,即 $m = \sqrt{2}n$ 时等号成立。故答案选 B.

另解: 由 $a, b > 0,\frac{2}{a\left( {{2b} + a}\right) } + \frac{1}{b\left( {a + b}\right) } = 1$ ,化为: $\frac{1}{ab} + \frac{1}{{a}^{2} + {3ab} + 2{b}^{2}} = 1$ ,

$\because {a}^{2} + 2{b}^{2} \geq  2\sqrt{2}{ab},\therefore 1 \leq  \frac{1}{ab} + \frac{1}{{3ab} + 2\sqrt{2}{ab}},\therefore {ab} \leq  1 + \frac{1}{3 + 2\sqrt{2}} = 4 - 2\sqrt{2}$ ,

当且仅当 $a = \sqrt{2}b = \sqrt{2}$ 时取等号. 故选: $B$ .
\end{kamisolutionbox}

(3)设 $a > b > c$ 且 $\frac{1}{a - b} + \frac{1}{b - c} \geq  \frac{m}{a - c}$ 恒成立，则 $m$ 的取值范围是___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star\star\star$}}

\begin{kamianswerbox}
$( - \infty ,4\rbrack$
\end{kamianswerbox}


\begin{kamisolutionbox}
因为 $\mathrm{a} > \mathrm{b} > \mathrm{c}$ ,所以 $\mathrm{a} - \mathrm{b} > 0,\mathrm{\;b} - \mathrm{c} > 0,\mathrm{\;a} - \mathrm{c} > 0$ .

又 $\left( {a - c}\right) \left( {\frac{1}{a - b} + \frac{1}{b - c}}\right)  = \left\lbrack  {\left( {a - b}\right)  + \left( {b - c}\right) }\right\rbrack  \left( {\frac{1}{a - b} + \frac{1}{b - c}}\right)  = 2 + \frac{b - c}{a - b} + \frac{a - b}{b - c} \geq  4$ ,

当且仅当 $\frac{b - c}{a - b} = \frac{a - b}{b - c}$ ,即 $2\mathrm{\;b} = a + c$ 时等号成立. 所以 $\mathrm{m} \leq  4$ .
\end{kamisolutionbox}

【例6】(1) 已知 $x, y \in  {\mathbb{R}}^{ + },{xy} = x + y + 1$ ,分别求 ${xy}, x + y$ 的最小值.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
见解析
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 由 $x, y \in  {\mathbb{R}}^{ + },{xy} = x + y + 1 \geq  2\sqrt{xy} + 1 \Leftrightarrow  {\left( \sqrt{xy}\right) }^{2} - 2\sqrt{xy} - 1 \geq  0$ ,

由 $\sqrt{xy} > 0$ ,解得 $\sqrt{xy} \geq  \sqrt{2} + 1 \Leftrightarrow  {xy} \geq  3 + 2\sqrt{2}$ ,等号成立 $\Leftrightarrow  x = y = \sqrt{2} + 1$ .

另一方面,由 ${xy} \leq  {\left( \frac{x + y}{2}\right) }^{2},{xy} = x + y + 1 \leq  \frac{1}{4}{\left( x + y\right) }^{2} \Leftrightarrow  {\left( x + y\right) }^{2} - 4\left( {x + y}\right)  - 4 \geq  0$ ,

由 $x + y > 0$ ，解得 $x + y \geq  2 + 2\sqrt{2}$ ，等号成立 $\Leftrightarrow  x = y = \sqrt{2} + 1$ ，

综上所述， ${\left( x + y\right) }_{\min } = 2 + 2\sqrt{2}$ ， ${\left( xy\right) }_{\min } = 3 + 2\sqrt{2}$ .
\end{kamisolutionbox}

(2)已知 $a > 0$ ， $b > 0$ ，且 $\frac{2}{a} + \frac{3}{b} = \sqrt{ab}$ ，则 ${ab}$ 的最小值是___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$2\sqrt{6}$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $a > 0, b > 0,\therefore \sqrt{ab} = \frac{2}{a} + \frac{3}{b} \geq  \frac{2\sqrt{6}}{\sqrt{ab}}$ ,即 $\sqrt{ab} \geq  \frac{2\sqrt{6}}{\sqrt{ab}}$ ,

$\therefore {ab} \geq  2\sqrt{6}$ ，当且仅当 $\frac{2}{a} = \frac{3}{b}$ 时取等号， $\therefore {ab}$ 的最小值是 $2\sqrt{6}$ . 故答案为: $2\sqrt{6}$ .
\end{kamisolutionbox}

(3)若实数 $x, y$ 满足 ${x}^{2}{y}^{2} + {x}^{2} + {y}^{2} = 8$ ，则 ${x}^{2} + {y}^{2}$ 的取值范围为( )

A. $\left\lbrack  {4,8}\right\rbrack$ B. $\left\lbrack  {8, + \infty }\right)$ C. $\left\lbrack  {2,8}\right\rbrack$ D. $\left\lbrack  {2,4}\right\rbrack$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$A$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $\because {x}^{2}{y}^{2} + {x}^{2} + {y}^{2} = 8,\therefore 8 = {x}^{2}{y}^{2} + {x}^{2} + {y}^{2} \leq  {\left( \frac{{x}^{2} + {y}^{2}}{2}\right) }^{2} + {x}^{2} + {y}^{2}$ ,

$\therefore {\left( {x}^{2} + {y}^{2}\right) }^{2} + 4\left( {{x}^{2} + {y}^{2}}\right)  - {32} \geq  0,\therefore {x}^{2} + {y}^{2} \geq  4$ ,或 ${x}^{2} + {y}^{2} \leq   - 8$ (舍),

$\because {x}^{2}{y}^{2} \geq  0,\therefore {x}^{2}{y}^{2} + {x}^{2} + {y}^{2} = 8 \geq  {x}^{2} + {y}^{2},\therefore 4 \leq  {x}^{2} + {y}^{2} \leq  8,\therefore {x}^{2} + {y}^{2}$ 的取值范围为 $\left\lbrack  {4,8}\right\rbrack$ . 故选: $A$ .
\end{kamisolutionbox}

【例 7】已知 $a > 0, b > 0$ ,当 ${\left( a + 4b\right) }^{2} + \frac{1}{ab}$ 取到最小值时, $b =$ ___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star   \star$}}

\begin{kamianswerbox}
$\frac{1}{4}$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $\because a > 0, b > 0;\therefore a + {4b} \geq  4\sqrt{ab}$ ,当 $a = {4b}$ 时取 “ $=$ ”; $\therefore {\left( a + 4b\right) }^{2} \geq  {16ab}$ ;

$\therefore {\left( a + 4b\right) }^{2} + \frac{1}{ab} \geq  {16ab} + \frac{1}{ab} = 4\left\lbrack  {a\left( {4b}\right) }\right\rbrack   + \frac{4}{a\left( {4b}\right) } \geq  8$ ,当 $a\left( {4b}\right)  = \frac{1}{a\left( {4b}\right) }$ ,即 ${a}^{2} = \frac{1}{{a}^{2}}, a = 1$ 时取 “ $=$ ”; 此时 $b = \frac{1}{4}$ . 故答案为: $\frac{1}{4}$ .
\end{kamisolutionbox}

\vspace{14pt}

## 巩固训练

1、已知关于 $x$ 的不等式 ${x}^{2} - {4ax} + 3{a}^{2} < 0\left( {a < 0}\right)$ 的解集为 $\left\{  {x \mid  {x}_{1} < x < {x}_{2}}\right\}$ ,若函数 $y = {x}_{1} + \frac{a}{{x}_{1}{x}_{2}}$ ,则下列说法正确的是( )

A. 函数有最小值 2

B. 函数有最小值 $\frac{2\sqrt{3}}{3}$

C. 函数有最大值-2

D. 函数有最大值 $- \frac{2\sqrt{3}}{3}$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
C
\end{kamianswerbox}


\begin{kamisolutionbox}
由题得, $\left( {x - a}\right) \left( {x - {3a}}\right)  < 0\left( {a < 0}\right)$ 的解集为 $\left\{  {x \mid  {x}_{1} < x < {x}_{2}}\right\}$ ,则 ${x}_{1} = {3a},{x}_{2} = a$ ,函数 $y = {x}_{1} + \frac{a}{{x}_{1}{x}_{2}} = {3a} + \frac{a}{{3a} \cdot  a}$ ,又 $a < 0$ ,则 $3\left( {-a}\right)  + \frac{1}{3\left( {-a}\right) } \geq  2\sqrt{3\left( {-a}\right)  \cdot  \frac{1}{3\left( {-a}\right) }} = 2$ ,故 $y = {3a} + \frac{1}{3a} \leq   - 2$ , 当且仅当 ${3a} = \frac{1}{3a}$ ，即 $a =  - \frac{1}{3}$ 时，取得等号，函数有最大值 -2 . 故选: $C$
\end{kamisolutionbox}

2、函数 $f\left( x\right)  = {2x} + \frac{1}{x} - 1$ 在区间 $\left( {-\infty ,0}\right)$ 上 ( ).

A. 有最大值, 无最小值 B. 有最小值, 无最大值

C. 既有最大值，又有最小值 D. 既无最大值, 又无最小值

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
A
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 因为函数 $f\left( x\right)  = {2x} + \frac{1}{x} - 1, x < 0$ ;

$\therefore f\left( x\right)  = {2x} + \frac{1}{x} - 1 =  - \left\lbrack  {\left( {-{2x}}\right)  + \frac{1}{-x}}\right\rbrack   - 1 \leq   - 2\sqrt{\left( {-{2x}}\right)  \cdot  \frac{1}{-x}} - 1 =  - 2\sqrt{2} - 1$ ; 当且仅当 $- {2x} = \frac{1}{-x}$ 即 $x =  - \frac{\sqrt{2}}{2}$ 时等号成立;

$\therefore$ 函数 $f\left( x\right)  = {2x} + \frac{1}{x} - 1$ 在区间 $\left( {-\infty ,0}\right)$ 上有最大值: $- 2\sqrt{2} - 1$ ,无最小值.

故选: A.
\end{kamisolutionbox}

3、已知 $\ln m + \ln n = \ln 2$ ，则 $\frac{{m}^{2} + 2}{m} + \frac{{n}^{2} + 2}{n}$ 的最小值是( )

A. $\sqrt{2}$ B. 4 C. $4\sqrt{2}$ D. $2\sqrt{2}$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
C
\end{kamianswerbox}


\begin{kamisolutionbox}
因为 $\ln m + \ln n = \ln 2$ ,所以 ${mn} = 2, m > 0, n > 0$ ,

所以 $\frac{{m}^{2} + 2}{m} + \frac{{n}^{2} + 2}{n} = \frac{{m}^{2} + {mn}}{m} + \frac{{n}^{2} + {mn}}{n} = 2\left( {m + n}\right)  \geq  2 \times  2\sqrt{mn} = 4\sqrt{2}$ ,当且仅当 $m = n = \sqrt{2}$ 时,取得等号.

故选: C
\end{kamisolutionbox}

4、已知 $a, b \in  \mathbf{R}$ ，且 $a - {2b} + 8 = 0$ ，则 ${2}^{a} + \frac{1}{{4}^{b}}$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star$}}

\begin{kamianswerbox}
$\frac{1}{8}$
\end{kamianswerbox}


\begin{kamisolutionbox}
: $a - {2b} + 8 = 0$ ,则 ${2}^{a} + \frac{1}{{4}^{b}} \geq  2\sqrt{{2}^{a} \cdot  \frac{1}{{4}^{b}}} = 2\sqrt{{2}^{a - {2b}}} = 2\sqrt{{2}^{-8}} = \frac{1}{8}$ .

当且仅当 $a =  - {2b}$ 即 $b = 2, a =  - 4$ 时取等号,故答案为: $\frac{1}{8}$ .
\end{kamisolutionbox}

5、已知正数 $x$ 、 $y$ 满足: ${2x} + y - {xy} = 0$ ，则 $x + {2y}$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
9
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $\because$ 正数 $x\text{ 、 }y$ 满足: ${2x} + y - {xy} = 0,\therefore \frac{2}{y} + \frac{1}{x} = 1$ .

则 $x + {2y} = \left( {x + {2y}}\right) \left( {\frac{2}{y} + \frac{1}{x}}\right)  = 5 + \frac{2x}{y} + \frac{2y}{x} \geq  5 + 2 \times  2\sqrt{\frac{x}{y} \cdot  \frac{y}{x}} = 9$ ,当且仅当 $x = y = 3$ 时取等号.

因此 $x + {2y}$ 的最小值为 9 . 故答案为: 9 .
\end{kamisolutionbox}

6、已知实数 $a, b$ 满足 $a, b \in  {R}^{ + }$ ，且 $a + {3b} = 1$ ，则 $\frac{1}{a + b} + \frac{9}{2\left( {a + {4b}}\right) }$ 的最小值为( )

A. $\frac{17}{3}$ B. $\frac{17}{4}$ C. $\frac{16}{3}$ D. $\frac{19}{4}$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
C
\end{kamianswerbox}


\begin{kamisolutionbox}
因为 $a + {3b} = 1$ ,所以 ${3a} + {9b} = 3$ ,即 $\left( {a + b}\right)  + \left( {{2a} + {8b}}\right)  = 3$ , $\therefore \frac{1}{a + b} + \frac{9}{2\left( {a + {4b}}\right) } = \left\lbrack  {\left( {a + b}\right)  + \left( {{2a} + {8b}}\right) }\right\rbrack  \left( {\frac{1}{a + b} + \frac{9}{2\left( {a + {4b}}\right) }}\right)  \times  \frac{1}{3} \; = \left\lbrack  {{10} + \frac{{2a} + {8b}}{a + b} + \frac{9\left( {a + b}\right) }{2\left( {a + {4b}}\right) }}\right\rbrack   \times  \frac{1}{3} \geq  \frac{1}{3} \times  \left( {{10} + 2\sqrt{9}}\right)  = \frac{16}{3}$ ,

当且仅当 ${2a} + {8b} = 3\left( {a + b}\right)$ 即 $a = \frac{5}{8}, b = \frac{1}{8}$ 时取等号. 故选: C.
\end{kamisolutionbox}

7、若正实数 $x\text{ 、 }y$ 满足 $x + y = 1$ ,则 $\frac{{x}^{2}}{x + 2} + \frac{{y}^{2}}{y + 4}$ 的最小值是 ( )

A. $\frac{1}{6}$ B. $\frac{1}{7}$ C. $\frac{1}{8}$ D. $\frac{1}{4}$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star   \star$}}

\begin{kamianswerbox}
$B$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 设 $x + 2 = s, y + 4 = t$ ,则 $s + t = x + y + 6 = 7$ ,即 $s + t = 7$ ,且 $x + y = 1$ .

则 $\frac{{x}^{2}}{x + 2} + \frac{{y}^{2}}{y + 4} = \frac{{\left( s - 2\right) }^{2}}{s} + \frac{{\left( t - 4\right) }^{2}}{t} = \frac{{s}^{2} - {4s} + 4}{s} + \frac{{t}^{2} - {8t} + {16}}{t} = s + \frac{4}{s} - 4 + t + \frac{16}{t} - 8$

$= s + \frac{4}{s} + t + \frac{16}{t} - {12} = s + t + \frac{4}{s} + \frac{16}{t} - {12} = 7 + \frac{4}{s} + \frac{16}{t} - {12} = \frac{4}{s} + \frac{16}{t} - 5$

$= \frac{s + t}{7} \cdot  \left( {\frac{4}{s} + \frac{16}{t}}\right)  - 5 = \frac{1}{7}\left( {4 + \frac{16s}{t} + \frac{4t}{s} + {16}}\right)  - 5 = \frac{1}{7}\left( {\frac{16s}{t} + \frac{4t}{s}}\right)  - \frac{15}{7} \geq  \frac{1}{7} \cdot  2\sqrt{\frac{16s}{t} \cdot  \frac{4t}{s}} - \frac{15}{7} = \frac{1}{7}$ ,

当且仅当 $\frac{16s}{t} = \frac{4t}{s}$ 时,即 $s = \frac{7}{3}, t = \frac{14}{3}$ 时,等号成立,故选: $B$ .
\end{kamisolutionbox}

8、已知 $x > 0$ ， $y > 0$ ，若不等式 $\left( {{2x} + y}\right) \left( {\frac{m}{x} + \frac{2}{y}}\right)  \geq  {18}$ 恒成立，则正数 $m$ 的最小值是( )

A. 2 B. 4 C. 6 D. 8

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star\star$}}

\begin{kamianswerbox}
B
\end{kamianswerbox}


\begin{kamisolutionbox}
$\left( {{2x} + y}\right) \left( {\frac{m}{x} + \frac{2}{y}}\right)  = {2m} + 2 + \frac{4x}{y} + \frac{my}{x} \geq  {2m} + 2 + 4\sqrt{m}$ ,

因为不等式 $\left( {{2x} + y}\right) \left( {\frac{m}{x} + \frac{2}{y}}\right)  \geq  {18}$ 恒成立,所以 ${2m} + 2 + 4\sqrt{m} \geq  {18}$ ,即 $\left( {\sqrt{m} + 4}\right) \left( {\sqrt{m} - 2}\right)  \geq  0$ , 解得 $\sqrt{m} \geq  2$ ,所以 $m \geq  4$ . 故选:B.
\end{kamisolutionbox}

9、若两个正实数 $x$ ， $y$ 满足 $\frac{1}{x} + \frac{4}{y} = 1$ ，且不等式 $x + \frac{y}{4} < {m}^{2} - {3m}$ 有解，则实数 $m$ 的取值范围是___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$\left( {-\infty , - 1}\right)  \cup  \left( {4, + \infty }\right)$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 正实数 $x, y$ 满足 $\frac{1}{x} + \frac{4}{y} = 1$ ,则 $x + \frac{y}{4} = \left( {\frac{1}{x} + \frac{4}{y}}\right) \left( {x + \frac{y}{4}}\right)  = 2 + \frac{4x}{y} + \frac{y}{4x} \geq  2 + 2\sqrt{\frac{4x}{y} \cdot  \frac{y}{4x}} = 4$ ,

当且仅当 $y = {4x} = 8$ ， $x + \frac{y}{4}$ 取得最小值4. 由 $x + \frac{y}{4} < {m}^{2} - {3m}$ 有解，可得 ${m}^{2} - {3m} > 4$ ，解得 $m > 4$ 或 $m <  - 1$ . 故答案为: $\left( {-\infty , - 1}\right)  \cup  \left( {4, + \infty }\right)$ .
\end{kamisolutionbox}

10、设 $x > 0$ ，则 $x\sqrt{1 - 4{x}^{2}}$ 的最大值为___

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$\frac{1}{4}$
\end{kamianswerbox}


\begin{kamisolutionbox}
由 $1 - 4{x}^{2} \geq  0$ 得 $- \frac{1}{2} \leq  x \leq  \frac{1}{2}$ ; 又 $x > 0$ ,所以 $0 < x \leq  \frac{1}{2}$

再由 $x\sqrt{1 - 4{x}^{2}} = \frac{1}{2} \cdot  {2x} \cdot  \sqrt{1 - 4{x}^{2}} \leq  \frac{1}{2} \cdot  \frac{4{x}^{2} + 1 - 4{x}^{2}}{2} = \frac{1}{4}$ ,

当且仅当 ${2x} = \sqrt{1 - 4{x}^{2}}$ ，即 $x = \frac{\sqrt{2}}{4} \in  \left( {0,\frac{1}{2}}\right\rbrack$ 时，等号成立. 所以 ${x\sqrt{1 - 4{x}^{2}}}$ 的最大值为 $\frac{1}{4}$ . 故答案为: $\frac{1}{4}$
\end{kamisolutionbox}

11、已知 $m, n \in  {R}^{ + }, m \neq  n, x, y \in  \left( {0, + \infty }\right)$ ,则有 $\frac{{m}^{2}}{x} + \frac{{n}^{2}}{y} \geq  \frac{{\left( m + n\right) }^{2}}{x + y}$ ,且当 $\frac{m}{x} = \frac{n}{y}$ 时等号成立,利用此结论,可求函数 $f\left( x\right)  = \frac{4}{3x} + \frac{3}{1 - x}, x \in  \left( {0,1}\right)$ 的最小值为___

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$\frac{25}{3}$
\end{kamianswerbox}


\begin{kamisolutionbox}
由题意可知, $f\left( x\right)  = \frac{\frac{4}{3}}{x} + \frac{3}{1 - x} = \frac{{\left( \frac{2\sqrt{3}}{3}\right) }^{2}}{x} + \frac{{\left( \sqrt{3}\right) }^{2}}{1 - x} \geq  \frac{{\left( \frac{2\sqrt{3}}{3} + \sqrt{3}\right) }^{2}}{1} = \frac{25}{3}$ ,

当且仅当 $\frac{\frac{2\sqrt{3}}{3}}{x} = \frac{\sqrt{3}}{1 - x}$ ，即 $\mathrm{x} = \frac{2}{5}$ 时，等号成立，所以其最小值为 $\frac{25}{3}$
\end{kamisolutionbox}

12、某种商品计划提价，现有四种方案:方案(1)先提价 $m\%$ ，再提价 $n\%$ ；方案(2)先提价 $n\%$ ，再提价 $m\%$ ; 方案 (3) 分两次提价,每次提价 $\left( \frac{m + n}{2}\right) \%$ ; 方案 (4) 一次性提价 $\left( {m + n}\right) \%$ . 已知 $m > n > 0$ , 那么四种提价方案中，提价最多的是___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：未标注}}

\begin{kamianswerbox}
(3)
\end{kamianswerbox}


\begin{kamisolutionbox}
依题意,设单价为 1 ,那么

方案 (1) 提价后的价格是 $\left( {1 + m\% }\right) \left( {1 + n\% }\right)  = 1 + \left( {m + n}\right) \%  + m\%  \cdot  n\%$ ;

方案(2)提价后的价格是 $\left( {1 + n\% }\right) \left( {1 + m\% }\right)  = 1 + \left( {m + n}\right) \%  + m\%  \cdot  n\%$ ;

方案 (3) 提价后的价格是 ${\left\lbrack  1 + \left( \frac{m + n}{2}\right) \% \right\rbrack  }^{2} = 1 + \left( {m + n}\right) \%  + {\left\lbrack  \left( \frac{m + n}{2}\right) \% \right\rbrack  }^{2}$ ;

方案(4)提价后的价格是 $1 + \left( {m + n}\right) \%$ ，所以只要比较 $m\%  \cdot  n\%$ 与 ${\left\lbrack  \left( \frac{m + n}{2}\right) \% \right\rbrack  }^{2}$ 的大小即可.

$\because {\left\lbrack  \left( \frac{m + n}{2}\right) \% \right\rbrack  }^{2} - m\%  \cdot  n\%  = {\left\lbrack  \left( \frac{m - n}{2}\right) \% \right\rbrack  }^{2} \geq  0$ ,所以 ${\left\lbrack  \left( \frac{m + n}{2}\right) \% \right\rbrack  }^{2} \geq  m\%  \cdot  n\%$ ;

又 $\because m > n > 0,\therefore {\left\lbrack  \left( \frac{m + n}{2}\right) \% \right\rbrack  }^{2} > m\%  \cdot  n\%$ ,即 ${\left\lbrack  1 + \left( \frac{m + n}{2}\right) \% \right\rbrack  }^{2} > \left( {1 + n\% }\right) \left( {1 + m\% }\right)$ ,

因此，方案(3)提价最多. 故答案为:(3)
\end{kamisolutionbox}

\vspace{14pt}

## (二)基本不等式的应用

\vspace{14pt}

## 知识梳理

在应用基本不等式解决实际问题时，要注意以下四点:

(1)设变量时一般把要求最值的变量定为函数；

(2)建立相应的函数关系式，确定函数的定义域；

(3)在定义域内，求出函数的最值；

(4)回到实际问题中去，写出实际问题的答案.

\vspace{14pt}

## 例题精讲

【例 8】(1)设 $a > 0, b > 0,\sqrt{3}$ 是 ${3}^{a}$ 与 ${3}^{b}$ 的等比中项，则 $\frac{1}{a} + \frac{2}{b}$ 的最小值是( )

A. $4\sqrt{2}$ B. $3 + 2\sqrt{2}$ C. 4 D. 3

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
B
\end{kamianswerbox}


\begin{kamisolutionbox}
$\because \sqrt{3}$ 是 ${3}^{a}$ 与 ${3}^{b}$ 的等比中项, $\therefore {3}^{a + b} = 3, a + b = 1$ ,

$\therefore \frac{1}{a} + \frac{2}{b} = \left( {\frac{1}{a} + \frac{2}{b}}\right) \left( {a + b}\right)  = 3 + \frac{b}{a} + \frac{2a}{b} \geq  3 + 2\sqrt{2}$ ,当且仅当 $\frac{b}{a} = \frac{2a}{b}$ 时,等号成立,即 $\frac{1}{a} + \frac{2}{b}$ 的最小值是 $3 + 2\sqrt{2}$ . 故选 B.
\end{kamisolutionbox}

(2)在各项均为正数的等比数列 $\left\{  {a}_{n}\right\}$ 中， ${a}_{6} = 3$ ，则 ${a}_{4} + {a}_{8} =$ ( )

A. 有最小值 6 B. 有最大值 6 C. 有最大值 9 D. 有最小值 3

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star\star$}}

\begin{kamianswerbox}
A
\end{kamianswerbox}


\begin{kamisolutionbox}
设等比数列 $\left\{  {a}_{n}\right\}$ 的公比为 $q\left( {q > 0}\right)$

$\because {a}_{6} = 3\;\therefore {a}_{4} = \frac{{a}_{6}}{{q}^{2}} = \frac{3}{{q}^{2}},{a}_{8} = {a}_{6}{q}^{2} = 3{q}^{2}$

$\therefore {a}_{4} + {a}_{8} = \frac{3}{{q}^{2}} + 3{q}^{2} \geq  2\sqrt{\frac{3}{{q}^{2}} \cdot  3{q}^{2}} = 6$ 当且仅当 $\frac{3}{{q}^{2}} = 3{q}^{2}$ 即 $q = 1$ 时上式等号成立

本题正确选项: $A$
\end{kamisolutionbox}

【例 9】( 1 )已知椭圆 $\frac{{x}^{2}}{25} + \frac{{y}^{2}}{{m}^{2}} = 1\left( {m > 0}\right)$ 与双曲线 $\frac{{x}^{2}}{7} - \frac{{y}^{2}}{{n}^{2}} = 1\left( {n > 0}\right)$ 有相同的焦点,则 $m + n$ 的最大值是( )

A. 3 B. $3\sqrt{2}$ C. 6 D. 9

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star\star$}}

\begin{kamianswerbox}
C
\end{kamianswerbox}


\begin{kamisolutionbox}
由题意可知: ${m}^{2} < {25}$ ,则 $0 < m < 5$ ,

由标准方程可知焦点坐标分别为: $\left( {\pm \sqrt{{25} - {m}^{2}},0}\right) ,\left( {\pm \sqrt{7 + {n}^{2}},0}\right)$ ,

由题意可知: ${25} - {m}^{2} = 7 + {n}^{2}$ ,据此有: ${m}^{2} + {n}^{2} = {18}$ ,

而 $m + n \leq  2\sqrt{\frac{{m}^{2} + {n}^{2}}{2}} = 6$ ,当且仅当 $m = n = 3$ 时等号取到,

综上可得: $m + n$ 的最大值是 6 . 故选:C
\end{kamisolutionbox}

(2)函数 $y = {\log }_{a}\left( {x + 3}\right)  - 1\left( {a > 0\text{ 且 }a \neq  1}\right)$ 的图像恒过定点 $\mathrm{A}$ ，若 $\mathrm{A}$ 在直线 ${mx} + {ny} + 1 = 0$ ，其中 $m, n$ 均大于 0,则 $\frac{1}{m} + \frac{2}{n}$ 的最小值___

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
8
\end{kamianswerbox}


\begin{kamisolutionbox}
由已知可得定点 $\mathrm{A}\left( {-2, - 1}\right)$ ,代入直线方程可得 ${2m} + n = 1$ ,从而

$\frac{1}{m} + \frac{2}{n} = \left( {\frac{1}{m} + \frac{2}{n}}\right) \left( {{2m} + n}\right)  = \frac{n}{m} + \frac{4m}{n} + 4 \geq  2\sqrt{\frac{n}{m}\frac{4m}{n}} + 4 = 8.$
\end{kamisolutionbox}

【例 10】某工厂生产某种产品的年固定成本为 200 万元,每生产 $x$ 千件,需另投入成本为 $C\left( x\right)$ ,当年产量不足 80 千件时, $C\left( x\right)  = \frac{1}{3}{x}^{2} + {10x}$ (万元). 当年产量不小于 80 千件时, $C\left( x\right)  = {51x} + \frac{10000}{x} - {1450}$ (万元). 每件商品售价为 0.05 万元. 通过市场分析, 该厂生产的商品能全部售完.

(1)写出年利润 $L\left( x\right)$ (万元)关于年产量 $x$ (千件)的函数解析式；

(2)当年产量为多少千件时，该厂在这一商品的生产中所获利润最大？

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
(1) $L\left( x\right)  = \left\{  \begin{array}{l}  - \frac{1}{3}{x}^{2} + {40x} - {200},0 < x < {80} \\  {1250} - \left( {x + \frac{10000}{x}}\right) , x \geq  {80} \end{array}\right.$ (2) 100 千件
\end{kamianswerbox}


\begin{kamisolutionbox}
解 (1) 因为每件商品售价为 0.05 万元,则 $x$ 千件商品销售额为 ${0.05} \times  {1000x}$ 万元,依题意得:

当 $0 < x < {80}$ 时, $L\left( x\right)  = \left( {{0.05} \times  {1000x}}\right)  - \left( {\frac{1}{3}{x}^{2} + {10x}}\right)  - {200} =  - \frac{1}{3}{x}^{2} + {40x} - {200}$ .

当 $x \geq  {80}$ 时, $L\left( x\right)  = \left( {{0.05} \times  {1000x}}\right)  - \left( {{51x} + \frac{10000}{x} - {1450}}\right)  - {200} = {1250} - \left( {x + \frac{10000}{x}}\right)$

所以 $L\left( x\right)  = \left\{  \begin{array}{l}  - \frac{1}{3}{x}^{2} + {40x} - {200},0 < x < {80} \\  {1250} - \left( {x + \frac{10000}{x}}\right) , x \geq  {80} \end{array}\right.$

(2)当 $0 < x < {80}$ 时， $L\left( x\right)  =  - \frac{1}{3}{\left( x - {60}\right) }^{2} + {1000}$ . 此时，当 $x = {60}$ 时， $L\left( x\right)$ 取得最大值 $L\left( {60}\right)  = {1000}$ 万元.

当 $x \geq  {80}$ 时, $L\left( x\right)  = {1250} - \left( {x + \frac{10000}{x}}\right)  \leq  {1250} - 2 \cdot  \sqrt{x \cdot  \frac{10000}{x}} = {1250} - {200} = {1050}$ .

此时 $x = \frac{10000}{x}$ ,即 $x = {100}$ 时, $L\left( x\right)$ 取得最大值 1050 万元. 由于 ${1000} < {1050}$ ,

答: 当年产量为 100 千件时, 该厂在这一商品生产中所获利润最大, 最大利润为 1050 万元
\end{kamisolutionbox}

【例11】如图,要设计一张矩形广告牌,该广告牌含有大小相等的左右两个矩形栏目(即图中阴影部分)， 这两栏的面积之和为 ${45}{m}^{2}$ ，四周空白的宽度为 ${0.5m}$ ，两栏之间的中缝空白的宽度为 ${0.25m}$ ，设广告牌的高为 ${xm}$ .

(1)求广告牌的面积关于 $x$ 的函数 $S\left( x\right)$ ；

(2)求广告牌的面积的最小值.

\begin{center}
\includegraphics[width=0.58\linewidth,keepaspectratio]{images/12_140_195_241_313_0.jpg}
\end{center}

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：未标注}}

\begin{kamianswerbox}
见解析
\end{kamianswerbox}


\begin{kamisolutionbox}
解: (1) 依题意广告牌的高为 ${tm}$ ,则 $\left( {x - 1}\right) \left( {t - {1.25}}\right)  = {45}$ ,

所以 $t = {1.25} + \frac{45}{x - 1}$ ,且 $x > 1$ ,所以广告牌的面积 $s\left( x\right)  = {tx} = x\left( {{1.25} + \frac{45}{x - 1}}\right) \left( {x > 1}\right)$ .

(2)由(1)知 $s\left( x\right)  = {tx} = x\left( {{1.25} + \frac{45}{x - 1}}\right)$

$= {1.25}\left( {x - 1}\right)  + \frac{45}{x - 1} + {46.25} \geq  2\sqrt{{1.25}\left( {x - 1}\right)  \cdot  \frac{45}{x - 1}} + {46.25} = {61.25}$ ,

当且仅当 ${1.25}\left( {x - 1}\right)  = \frac{45}{x - 1}$ ,即 $x = 7$ 号成立. 所以 $s{\left( x\right) }_{\min } = s\left( 7\right)  = {61.25}$ ,广告牌的面积的最小值为 61.25 .
\end{kamisolutionbox}

【例12】证明: 如果 $a > 0, b > 0$ ,那么 $\frac{a}{\sqrt{b}} + \frac{b}{\sqrt{a}} \geq  \sqrt{a} + \sqrt{b}$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
见解析
\end{kamianswerbox}


\begin{kamisolutionbox}
(1) 证明: $\frac{a}{\sqrt{b}} + \frac{b}{\sqrt{a}} + \sqrt{a} + \sqrt{b} = \frac{a}{\sqrt{b}} + \sqrt{b} + \frac{b}{\sqrt{a}} + \sqrt{a} \geq  2\sqrt{a} + 2\sqrt{b}$ ,当且仅当 $a = b$ 时等号成立, $\therefore \frac{a}{\sqrt{b}} + \frac{b}{\sqrt{a}} \geq  \sqrt{a} + \sqrt{b}$ .
\end{kamisolutionbox}

\vspace{14pt}

## 巩固训练

1、若点 $A\left( {-2, - 1}\right)$ 在直线 ${mx} + {ny} + 1 = 0$ 上，其中 ${mn} > 0$ ，则 $\frac{1}{m} + \frac{2}{n}$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star$}}

\begin{kamianswerbox}
8
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $\because$ 点 $A\left( {-2, - 1}\right)$ 在直线 ${mx} + {ny} + 1 = 0$ 上, $\therefore  - {2m} - n + 1 = 0$ ,即 ${2m} + n = 1$ , $\because \frac{1}{m} + \frac{2}{n} = \left( {\frac{1}{m} + \frac{2}{n}}\right) \left( {{2m} + n}\right)  = 4 + \frac{n}{m} + \frac{4m}{n} \geq  4 + 2\sqrt{\frac{n}{m} \cdot  \frac{4m}{n}} = 8$ ,当且仅当 $\frac{n}{m} = \frac{4m}{n}$ ,即 $n = {2m}$ 时取等号, $\therefore \frac{1}{m} + \frac{2}{n}$ 的最小值为 8,

故答案为:8
\end{kamisolutionbox}

2、某湖泊的水位 $h$ (单位: 米) 随时间 $t$ (单位: 小时) 的变化规律如下: $h = m \cdot  {2}^{t} + {2}^{1 - t}\left( {m > 0, t \geq  0}\right)$ , 若该湖泊的水位总不低于 2 米,则 $m$ 的取值范围是( )

A. $\lbrack 2, + \infty )$ B. $\lbrack 1, + \infty )$ C. $\left\lbrack  {\frac{1}{2}, + \infty }\right)$ D. $\left\lbrack  {-\frac{1}{4}, + \infty }\right)$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star\star$}}

\begin{kamianswerbox}
C
\end{kamianswerbox}


\begin{kamisolutionbox}
由题意 $h = m \cdot  {2}^{t} + {2}^{1 - t} \geq  2$ 恒成立, $m \geq  \frac{2}{{2}^{t}} - \frac{{2}^{1 - t}}{{2}^{t}}$ ,设 $x = \frac{1}{{2}^{t}}$ ,由 $t \geq  0$ 得 $0 < x \leq  1$ , $m \geq  {2x} - 2{x}^{2} =  - 2{\left( x - \frac{1}{2}\right) }^{2} + \frac{1}{2},0 < x \leq  1$ 时, $- 2{\left( x - \frac{1}{2}\right) }^{2} + \frac{1}{2}$ 的最大值为 $\frac{1}{2},\therefore m \geq  \frac{1}{2}$ . 故选: C.
\end{kamisolutionbox}

3、已知 $a > 0$ ， $\overrightarrow{a} = \left( {\frac{1}{2},{a}^{2} + 1}\right)$ ， $\overrightarrow{b} = \left( {{2a},\frac{1}{a}}\right)$ ，则 $\overrightarrow{a} \cdot  \overrightarrow{b}$ 的最小值是___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$2\sqrt{2}$
\end{kamianswerbox}


\begin{kamisolutionbox}
$\because \overrightarrow{a} = \left( {\frac{1}{2},{a}^{2} + 1}\right) ,\overrightarrow{b} = \left( {{2a},\frac{1}{a}}\right) ,\therefore \overrightarrow{a} \cdot  \overrightarrow{b} = \frac{1}{2} \times  \left( {2a}\right)  + \left( {{a}^{2} + 1}\right)  \times  \frac{1}{a} = {2a} + \frac{1}{a}$ ,

$\because a > 0,\therefore {2a} + \frac{1}{a} \geq  2\sqrt{\left( {2a}\right)  \cdot  \frac{1}{a}} = 2\sqrt{2}$ ,当且仅当 ${2a} = \frac{1}{a}$ ,即 $a = \frac{\sqrt{2}}{2}$ 时取等号,

$\therefore \overrightarrow{a} \cdot  \overrightarrow{b}$ 的最小值为 $2\sqrt{2}$

故答案为: $2\sqrt{2}$
\end{kamisolutionbox}

4、首届世界低碳经济大会近日召开，本届大会的主题为“节能减排，绿色生态”某单位在国家科研部门的支持下，进行技术攻关，采用了新工艺，把二氧化碳转化为一种可利用的化工产品. 已知该单位每月的处理量最少为 200 吨,最多为 500 吨,月处理成本 $y$ (元)与月处理量 $x$ (吨)之间的函数关系可近似地表示为 $y = \frac{1}{2}{x}^{2} - {200x} + {80000}$ ,且每处理一吨二氧化碳得到可利用的化工产品价值为 100 元.

(1)该单位每月处理量为多少吨时，才能使每吨的平均处理成本最低？

(2)该单位每月能否获利？如果获利，求出最大利润；如果不获利，则需要国家至少补贴多少元才能使该单位不亏损?

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
(1)400 吨；(2)每月不能获利，需要国家至少补贴35000 元才能不亏损
\end{kamianswerbox}


\begin{kamisolutionbox}
(1) 当每月处理量为 $x$ 吨时, $x \in  \left\lbrack  {{200},{500}}\right\rbrack$ ,每吨的平均处理成本为

$\frac{y}{x} = \frac{x}{2} - {200} + \frac{80000}{x} \geq  2\sqrt{40000} - {200} = {200}$ ,当且仅当 $\frac{x}{2} = \frac{80000}{x}$ ,即 $x = {400}$ 时等号成立,

所以每月处理量为 400 吨时, 每吨的平均处理成本最低.

(2)设该单位每月获利为 $S$ 元，则

$S = {100x} - y =  - \frac{1}{2}{x}^{2} + {300x} - {80000} =  - \frac{1}{2}{\left( x - {300}\right) }^{2} - {35000}, x \in  \left\lbrack  {{200},{500}}\right\rbrack$ ,

当 $x = {300}$ 时, ${S}_{\max } =  - {35000}$ ,

所以该单位每月不能获利, 需要国家至少补贴 35000 元才能不亏损.
\end{kamisolutionbox}

5、求证: ${a}^{2} + {b}^{2} + {c}^{2} \geq  {ab} + {bc} + {ca}$ .

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star$}}

\begin{kamianswerbox}
见解析
\end{kamianswerbox}


\begin{kamisolutionbox}
证明: ${a}^{2} + {b}^{2} + {c}^{2} = \frac{1}{2}\left( {{a}^{2} + {b}^{2} + {c}^{2} + {a}^{2} + {b}^{2} + {c}^{2}}\right)  \geq  \frac{1}{2}\left( {{2ab} + {2ca} + {2bc}}\right)  = {ab} + {bc} + {ca}$ . $\therefore {a}^{2} + {b}^{2} + {c}^{2} \geq  {ab} + {bc} + {ca}$ .
\end{kamisolutionbox}

\vspace{14pt}

## 实战演练

一、填空题

1、若 $x{y}^{2} = 1$ ，则 ${4x} + {y}^{2}$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
4
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 因为 $x{y}^{2} = 1,{y}^{2} \geq  0$ ,所以 $x > 0,{y}^{2} > 0$ ,则 ${4x} + {y}^{2} \geq  2\sqrt{{4x}{y}^{2}} = 4$ ,

当且仅当 ${4x} = {y}^{2}$ ,即 $x = \frac{1}{2},{y}^{2} = 2$ 时,等号成立,所以 ${4x} + {y}^{2}$ 的最小值为 4 .

故答案为:4.
\end{kamisolutionbox}

2、已知正实数 $x, y$ 满足 ${xy} = 1$ ，则 $\left( {\frac{x}{y} + y}\right) \left( {\frac{y}{x} + x}\right)$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star$}}

\begin{kamianswerbox}
4
\end{kamianswerbox}


\begin{kamisolutionbox}
$\left( {\frac{x}{y} + y}\right) \left( {\frac{y}{x} + x}\right)  = 1 + \frac{{x}^{2}}{y} + \frac{{y}^{2}}{x} + {xy} = 2 + \frac{{x}^{3} + {y}^{3}}{xy} = 2 + {x}^{3} + {y}^{3} \geq  2 + 2\sqrt{{x}^{3}{y}^{3}} = 4$ .

当且仅当 $x = y = 1$ 时等号成立.

据此可知: $\left( {\frac{x}{y} + y}\right) \left( {\frac{y}{x} + x}\right)$ 的最小值为 4 .
\end{kamisolutionbox}

3、已知 $a\text{ 、 }b \in  R$ ，且 $a\text{ 、 }{3b}$ 的等差中项为1，则 ${3}^{a} + {27}^{b}$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
6
\end{kamianswerbox}


\begin{kamisolutionbox}
由于 $a\text{ 、 }{3b}$ 的等差中项为 1,则 $a + {3b} = 2$ ,

由基本不等式得 ${3}^{a} + {27}^{b} = {3}^{a} + {3}^{3b} \geq  2\sqrt{{3}^{a} \cdot  {3}^{3b}} = 2\sqrt{{3}^{a + {3b}}} = 2\sqrt{{3}^{2}} = 6$ ,

当且仅当 $a = 1, b = \frac{1}{3}$ 时,等号成立,因此, ${3}^{a} + {27}^{b}$ 的最小值为 6 .

故答案为: 6 .
\end{kamisolutionbox}

4、已知正实数 $a, b$ 满足 $a + b = 4$ ，则 $\frac{1}{a + 1} + \frac{1}{b + 3}$ 的最小值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$\frac{1}{2}$
\end{kamianswerbox}


\begin{kamisolutionbox}
解: $\because$ 正实数 $a, b$ 满足 $a + b = 4,\therefore a + 1 > 1, b + 3 > 3, a + 1 + b + 3 = 8$ ,

$\therefore \frac{1}{a + 1} + \frac{1}{b + 3} = \frac{1}{8}\left( {\frac{1}{a + 1} + \frac{1}{b + 3}}\right) \left\lbrack  {\left( {a + 1}\right)  + \left( {b + 3}\right) }\right\rbrack   = \frac{1}{8}\left( {\frac{a + 1}{b + 3} + \frac{b + 3}{a + 1} + 2}\right)$

$\geq  \frac{1}{8}\left( {2\sqrt{\frac{a + 1}{b + 3} \times  \frac{b + 3}{a + 1}} + 2}\right)  = \frac{1}{2}$ . 当且仅当 $\frac{a + 1}{b + 3} = \frac{b + 3}{a + 1}$ 时,取等号,

$\therefore \frac{1}{a + 1} + \frac{1}{b + 3}$ 的最小值为 $\frac{1}{2}$ .

故答案为: $\frac{1}{2}$ .
\end{kamisolutionbox}

5、直角三角形的周长等于 2，则这个直角三角形面积的最大值为___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
3-2√2
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 直角三角形的两直角边为 $a\text{ 、 }b$ ,斜边为 $c$ ,面积为 $s$ ,周长 $L = 2$ ,

由于 $a + b + \sqrt{{a}^{2} + {b}^{2}} = L \geq  2\sqrt{ab} + \sqrt{2ab}$ . (当且仅当 $a = b$ 时取等号)

$\therefore \sqrt{ab} \leq  \frac{L}{2 + \sqrt{2}}.\therefore S = \frac{1}{2}{ab} \leq  \frac{1}{2}{\left( \frac{L}{2 + \sqrt{2}}\right) }^{2} = \frac{1}{2} \cdot  {\left\lbrack  \frac{\left( {2 - \sqrt{2}}\right) L}{2}\right\rbrack  }^{2} = \frac{3 - 2\sqrt{2}}{4}{L}^{2} = 3 - 2\sqrt{2}$ .

故答案为: $3 - 2\sqrt{2}$ .
\end{kamisolutionbox}

6、若正实数 $x, y$ 满足 $x + {2y} = {2xy}$ ,且不等式 $\left( {x + {2y} - a}\right) {xy} + 1 \geq  0$ 恒成立,则实数 $a$ 的取值范围是___.

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
$a \leq  2\sqrt{2}$ .
\end{kamianswerbox}


\begin{kamisolutionbox}
解: 因为正实数 $x, y$ 满足 $x + {2y} = {2xy}$ 且不等式 $\left( {x + {2y} - a}\right) {xy} + 1 \geq  0$ 恒成立,所以 $\left( {{2xy} - a}\right) {xy} + 1 \geq  0$ 恒成立,即 $a \leq  {2xy} + \frac{1}{xy}$ 恒成立,则 $a \leq  {\left( 2xy + \frac{1}{xy}\right) }_{\min }$ ,因为 ${2xy} + \frac{1}{xy} \geq  2\sqrt{2}$ ,

当且仅当 ${2xy} = \frac{1}{xy}$ ,即 ${xy} = \frac{\sqrt{2}}{2}$ 时取等号,此时 ${2xy} + \frac{1}{xy}$ 取得最小值 $2\sqrt{2}$ ,故 $a \leq  2\sqrt{2}$ . 故答案为: $a \leq  2\sqrt{2}$ .
\end{kamisolutionbox}

\vspace{14pt}

## 二、选择题

7、有以下三个代数式:其中最小值为 2 的代数式个数为( )

\textcircled{1} $\sqrt{{x}^{2} + 4} + \frac{1}{\sqrt{{x}^{2} + 4}}$ ; \textcircled{2} $\frac{{a}^{2} + 1}{a}$ ；\textcircled{3} ${t}^{2} + \frac{1}{{t}^{2} + 1}$ ；\textcircled{4} $\frac{1}{a} + \frac{1}{b}\left( {a, b \in  {R}^{ + }}\right.$ 且 $\left. {a + {4b} = 1}\right)$

A. 0 B. 1 C. 2 D. 3

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star$}}

\begin{kamianswerbox}
A
\end{kamianswerbox}


\begin{kamisolutionbox}
解: \textcircled{1}因为 $t = \sqrt{4 + {x}^{2}} \geq  2$ ,所以 $\sqrt{{x}^{2} + 4} + \frac{1}{\sqrt{{x}^{2} + 4}} = t + \frac{1}{t}$ 在 $\lbrack 2, + \infty )$ 上单调递增,

所以 $t = 2$ 时取得最小值 $\frac{5}{2}$ ; \textcircled{2} 当 $a < 0$ 时, $\frac{{a}^{2} + 1}{a} = a + \frac{1}{a}$ 没有最小值;

\textcircled{3}因为 $1 + {t}^{2} \geq  1$ ，所以当 $1 + {t}^{2} = 1$ 时， ${t}^{2} + \frac{1}{{t}^{2} + 1} = 1 + {t}^{2} + \frac{1}{{t}^{2} + 1} - 1$ 取得最小值 1，

\textcircled{4} $a, b \in  {R}^{ + }$ 且 $a + {4b} = 1$ ，则 $\frac{1}{a} + \frac{1}{b} = \frac{a + {4b}}{a} + \frac{a + {4b}}{b} = 5 + \frac{4b}{a} + \frac{a}{b} \geq  5 + 4 = 9$ 即最小值为 9 .

故选: $A$ .
\end{kamisolutionbox}

8、已知 $x \geq  \frac{5}{2}$ ，则 $\mathrm{f}\left( x\right)  = \frac{{x}^{2} - {4x} + 5}{{2x} - 4}$ 有( )

A. 最小值 1 B. 最大值 $\frac{5}{4}$

C. 最小值 $\frac{5}{4}$ D. 最大值 1

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star$}}

\begin{kamianswerbox}
A
\end{kamianswerbox}


\begin{kamisolutionbox}
$f\left( x\right)  = \frac{{x}^{2} - {4x} + 5}{{2x} - 4} = \frac{1}{2} \times  \frac{{\left( x - 2\right) }^{2} + 1}{x - 2} = \frac{1}{2}\left\lbrack  {\left( {x - 2}\right)  + \frac{1}{x - 2}}\right\rbrack   \geq  \frac{1}{2} \times  2\sqrt{1} = 1$ ,

当且仅当 $x - 2 = \frac{1}{x - 2}$ 即 $x = 3$ 时等号成立。
\end{kamisolutionbox}

9、已知点 $A\left( {3,1}\right)$ 在直线 $y = {mx} + n\left( {m > 0, n > 0}\right)$ 的图象上，则 $\frac{1}{m} + \frac{3}{n}$ 的最小值为( )

A. 8 B. 9 C. 12 D. 18

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star\star\star$}}

\begin{kamianswerbox}
C
\end{kamianswerbox}


\begin{kamisolutionbox}
依题意得, ${3m} + n = 1$ ,且 $m > 0, n > 0$ ,

$\frac{1}{m} + \frac{3}{n} = \left( {\frac{1}{m} + \frac{3}{n}}\right) \left( {{3m} + n}\right)  = 3 + 3 + \frac{n}{m} + \frac{9m}{n} \geq  6 + 2\sqrt{\frac{n}{m} \cdot  \frac{9m}{n}} = {12}$ ,

当且仅当 $\frac{n}{m} = \frac{9m}{n}$ ,即 $n = {3m}$ 时取等号,因此, $\frac{1}{m} + \frac{3}{n}$ 的最小值为 12 .

故选: C.
\end{kamisolutionbox}

10、 $n$ 是正数，若对于任意大于 2018 的实数 $x$ ，总有 ${n}^{2}x + \frac{x}{x - {2018}} > {2019}{n}^{2}$ 成立，则实数 $n$ 的取值范围为( )

A. $n > \sqrt{2019} - \sqrt{2018}$ B. $0 < n < \sqrt{2019} - \sqrt{2018}$

C. $n > \sqrt{2019} + \sqrt{2018}$ D. $0 < n < \sqrt{2019} + \sqrt{2018}$

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
D
\end{kamianswerbox}


\begin{kamisolutionbox}
由 ${n}^{2}x + \frac{x}{x - {2018}} > {2019}{n}^{2}$ 整理得, ${n}^{2}\left( {x - {2018}}\right)  + \frac{2018}{x - {2018}} > {n}^{2} - 1$ ,

要使上式成立,只需 ${\left\lbrack  {n}^{2}\left( x - {2018}\right)  + \frac{2018}{x - {2018}}\right\rbrack  }_{\text{ min }} = {2n}\sqrt{2018} > {n}^{2} - 1$ ,即 ${\left( n - \sqrt{2018}\right) }^{2} < {2019}$ ,

$\therefore 0 < n < \sqrt{2019} + \sqrt{2018}$ .

故选: D.
\end{kamisolutionbox}

\vspace{14pt}

## 三、解答题

11、《上海市生活垃圾管理条例》于 2019 年 7 月 1 日正式实施，某小区全面实施垃圾分类处理，已知该小区每月垃圾分类处理量不超过 300 吨,每月垃圾分类处理成本 $y$ (元)与每月分类处理量 $x$ (吨)之间的函数关系式可近似表示为 $y = {x}^{2} - {200x} + {40000}$ ,而分类处理一吨垃圾小区也可以获得 300 元的收益.

(1)该小区每月分类处理多少吨垃圾，才能使得每吨垃圾分类处理的平均成本最低；

(2)要保证该小区每月的垃圾分类处理不亏损，每月的垃圾分类处理量应控制在什么范围？

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
(1)200吨；(2) $\left\lbrack  {{100},{300}}\right\rbrack$ .
\end{kamianswerbox}


\begin{kamisolutionbox}
解: (1) 由题意可知, 每吨垃圾分类处理的平均成本为月处理成本除以月处理量,

即 $\frac{y}{x} = x + \frac{40000}{x} - {200}, x \in  (0,{300}\rbrack$ ,

又 $x + \frac{40000}{x} \geq  2\sqrt{x \cdot  \frac{40000}{x}} = {400}$ ,当且仅当 $x = \frac{40000}{x}$ ,即 $x = {200}$ 时取等号,

故 $x = {200}$ 时,才能使得每吨垃圾分类处理的平均成本最低;

(2)设该小区每月获利为 $S$ 元，则该小区每月获利为月分类处理垃圾的利润减去月处理成本，

$S = {300x} - y = {300x} - \left( {{x}^{2} - {200x} + {40000}}\right)  =  - {x}^{2} + {500x} - {40000}$ ,

令 $- {x}^{2} + {500x} - {40000} \geq  0$ ,解得 ${100} \leq  x \leq  {400}$ ,又 $0 < x \leq  {300}$ ,即 ${100} \leq  x \leq  {300}$ ,

故要保证该小区每月的垃圾分类处理不亏损,每月的垃圾分类处理量应控制在 $\left\lbrack  {{100},{300}}\right\rbrack$ .
\end{kamisolutionbox}

12、如图，长方形 ${ABCD}$ 表示一张 $6 \times  {12}$ (单位:分米)的工艺木板，其四周有边框(图中阴影部分)，中间为薄板. 木板上一瑕疵(记为点 $P$ )到外边框 ${AB}$ ， ${AD}$ 的距离分别为 1 分米，2 分米. 现欲经过点 $P$ 锯掉一块三角形废料 ${MAN}$ ,其中 $M, N$ 分别在 ${AB},{AD}$ 上. 设 ${AM},{AN}$ 的长分别为 $m$ 分米, $n$ 分米.

(1)为使锯掉一块三角形废料 ${MAN}$ 的面积最小，试确定 $m, n$ 的值；

(2)求剩下木板 ${MBCDN}$ 的外边框长度 $({MB},{BC},{CD},{DN}$ 的长度之和)的最大值.

\begin{center}
\includegraphics[width=0.58\linewidth,keepaspectratio]{images/17_144_683_603_308_0.jpg}
\end{center}

\noindent\textcolor{KamiNoteFrame}{\textbf{难度：$\star   \star   \star$}}

\begin{kamianswerbox}
见解析
\end{kamianswerbox}


\begin{kamisolutionbox}
解: (1) 过点 $P$ 分别作 ${AB},{AD}$ 的垂线，垂足分别为 $E, F$ ，则 $\triangle PNF \sim \triangle MPE$ ，

从而 $\frac{PF}{EM} = \frac{NF}{PE},\therefore \frac{2}{m - 2} = \frac{n - 1}{1}$ ,即 $\frac{2}{m} + \frac{1}{n} = 1$ .

欲使锯掉的三角形废料 ${MAN}$ 的面积 $S = \frac{1}{2}{mn}$ 最小.

由 $1 = \frac{2}{m} + \frac{1}{n} \geq  2\sqrt{\frac{2}{m} \cdot  \frac{1}{n}}$ 得, ${mn} \geq  8$ (当且仅当 $\frac{2}{m} = \frac{1}{n}$ ,即 $m = 4, n = 2$ 时,

“ $=$ ”成立)，此时 ${S}_{\min } = 4$ (平方分米).

(2)欲使剩下木板的外边框长度最大，即 $m + n$ 最小.

由(1)知， $m + n = \left( {m + n}\right) \left( {\frac{2}{m} + \frac{1}{n}}\right)  = 3 + \frac{2n}{m} + \frac{m}{n} \geq  3 + 2\sqrt{\frac{2n}{m} \cdot  \frac{m}{n}} = 3 + 2\sqrt{2}$ ，

(当且仅当 $\frac{2n}{m} = \frac{m}{n}$ 即 $m = 2 + \sqrt{2} = \sqrt{2}n$ 时,“=”成立)，

答: 此时剩下木板的外边框长度的最大值为 ${33} - 2\sqrt{2}$ 分米.
\end{kamisolutionbox}
