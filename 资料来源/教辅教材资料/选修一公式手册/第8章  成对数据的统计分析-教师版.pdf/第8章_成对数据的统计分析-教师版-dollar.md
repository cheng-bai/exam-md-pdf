## 第8章 成对数据的统计分析

### 8.1 成对数据的相关分析

#### 8.1.1 成对数据间的关系

把来自 同一 对象的 两组 数据称为成对数据，研究成对数据相关性的方法称为 相关 分析.

#### 8.1.2 相关系数

1. 两组数据 ${x}_{i}$ 和 ${y}_{i}$ 的线性相关系数是度量两个变量 $x$ 与 $y$ 间 线性相关 程度的统计量,其计算公式为

$$
r = \frac{\mathop{\sum }\limits_{{i = 1}}^{n}\left( {{x}_{i} - \bar{x}}\right) \left( {{y}_{i} - \bar{y}}\right) }{\sqrt{\mathop{\sum }\limits_{{i = 1}}^{n}{\left( {x}_{i} - \bar{x}\right) }^{2}\mathop{\sum }\limits_{{i = 1}}^{n}{\left( {y}_{i} - \bar{y}\right) }^{2}}}.
$$

其中, $\bar{x} = \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i},\bar{y} = \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i}$ ,它们分别是这两组数据的算术平均数.

2. 可以证明,相关系数 $r$ 的值满足 $\left| r\right|  \leq  1,\left| r\right|$ 越接近 1 , 两个变量的线性相关程度越高; $\left| r\right|$ 越接近 0 ，两个变量的线性相关程度越低. $r > 0$ 时，当 $x$ 的值由小变大， $y$ 的值具有 由小变大 的变化趋势，称这种相关为正相关； $r < 0$ 时，当 $x$ 的值由小变大， $y$ 的值具有 由大变小 的变化趋势，称这种相关为 负 相关.

### 8.2 一元线性回归分析

#### 8.2.1 一元线性回归分析的基本思想

1. 一般地，设给定一组有线性相关关系的成对数据 $\left( {{x}_{1},{y}_{1}}\right) ,\left( {{x}_{2},{y}_{2}}\right) ,\ldots ,\left( {{x}_{n},{y}_{n}}\right)$ 和一个线性方程(或称线性模型 $y = {ax} + b$ ,记 ${\widehat{y}}_{i} = a{x}_{i} + b$ ,它是 ${x}_{i}$ 对应的理想值,但数据中的 ${y}_{i}$ 与 ${\widehat{y}}_{i}$ 不一定相同,称它们的差 ${y}_{i} - {\widehat{y}}_{i}$ 为在 ${x}_{i}$ 处的 离差 ,用离差的 平方和 $Q = \mathop{\sum }\limits_{{i = 1}}^{n}{\left( {y}_{i} - {\widehat{y}}_{i}\right) }^{2}$ 来刻画直线与点之间的拟合程度, $Q$ 称为 拟合误差 ,它是一个很好的描述数据与线性方程贴近度的指标.

2. 拟合误差最小时: $\left\{  \begin{array}{l} \widehat{a} = \frac{\mathop{\sum }\limits_{{i = 1}}^{n}\left( {{x}_{i} - \bar{x}}\right) \left( {{y}_{i} - \bar{y}}\right) }{\mathop{\sum }\limits_{{i = 1}}^{n}{\left( {x}_{i} - \bar{x}\right) }^{2}} = \frac{\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{y}_{i} - n\bar{x}\bar{y}}{\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}^{2} - n{\bar{x}}^{2}} \\  \widehat{b} = \bar{y} - \widehat{a}\bar{x} = \frac{\mathop{\sum }\limits_{{i = 1}}^{n}{y}_{i} - \widehat{a}\mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}}{n} \end{array}\right.$

3. 回归分析是基于 $Q$ 取最小值的假设，即基于所有离差的平方和取最小值的假设进行的. 这种回归分析的方法称为 最小二乘法

4. 我们把拟合误差取得最小值时得到的线性方程(线性模型)记为 $y = \widehat{a}x + \widehat{b}$ ，并称之为变量 $y$ 随 $x$ 波动的回归方程 或回归模型，其中自变量 $x$ 称为 解释变量，因变量 $y$ 称为 反应变量，回归方程定义的直线称为 回归直线 ，回归方程的系数(或称回归模型的参数) $\widehat{a}$ 与 $\widehat{b}$ 称为 回归系数 . 由一组有某种线性关系的成对数据求其回归方程的方法称为 回归分析.

## 8. $3 \times  2 \times  2$ 列联表

#### 8.3.1 $2 \times  2$ 列联表独立性检验

1. 变量的不同“值”表示研究对象所属的不同类别，这类变量称为 分类变量 .

2. 要检验两个随机变量是否有关，统计上一般先假设它们没有关系，即相互独立，再进行统计检验，这种假设称为 原假设，也称为零假设，习惯上用 ${H}_{0}$ 表示.

3. 两组分类变量的2×2列联表可以如下表表示:

<table><tr><td></td><td>A组</td><td>B组</td><td>总计</td></tr><tr><td>0</td><td>$a$</td><td>$b$</td><td>$a + b$</td></tr><tr><td>1</td><td>$c$</td><td>$d$</td><td>$c + d$</td></tr><tr><td>总计</td><td>$a + c$</td><td>$b + d$</td><td>$a + b + c + d$</td></tr></table>

4. 为了描述观察值与预期值之间的总体偏差,我们引入统计量 ${\chi }^{2} = \sum \frac{{\left( \text{ 观察值 } - \text{ 预期值 }\right) }^{2}}{\text{ 预期值 }}$ 形可得 ${\chi }^{2}$ 的一般计算公式: ${\chi }^{2} = \frac{n{\left( ad - bc\right) }^{2}}{\left( {a + b}\right) \left( {c + d}\right) \left( {a + c}\right) \left( {b + d}\right) }$ ,其中, $n = a + b + c + d$ .

5.2×2列联表独立性检验通常有如下步骤:

(1)提出原假设 ${H}_{0}$ :两个随机变量没有关系.

(2)确定显著性水平 $\alpha$ (因题而异)，本书中规定 $\alpha  = {0.05}$ ，也即 $P\left( {{\chi }^{2} \geq  {3.841}}\right)  \approx  {0.05}$ .

(3)计算统计量 ${\chi }^{2}$ 的值.

(4)统计决断:比较上述 ${\chi }^{2}$ 值与3.841的大小，若 ${\chi }^{2}$ 值 $\geq  {3.841}$ ，则 ${\chi }^{2}$ 的值超过了 $\alpha$ 所确定的界限，从而拒绝 ${H}_{0}$ ；若 ${\chi }^{2}$ 值 $< {3.841}$ ，则小概率事件没有发生，从而接受 ${H}_{0}$ . 最后根据上述推断作出结论.
