## 第7章 概率初步 (续)

### 7.1 条件概率与相关公式

#### 7.1.1 条件概率

1. 条件概率: 在古典概率模型中,事件 $A$ 发生之后,随机现象的结果就剩下事件 $A$ 中的基本事件,所以事件 $A$ 变成了由这些基本事件所构成的新的样本空间. 这个样本空间仍然是等可能的，这时事件 $B$ 发生的概率称为事件 $B$ 基于条件 $A$ 的概率,或在事件 $A$ 发生的条件下,事件 $B$ 发生的概率, 或已知事件 $A$ 发生，事件 $B$ 发生的概率，记为 $P\left( {B \mid  A}\right)$ .

2. 这等于是在一个样本空间为 $A$ 的随机试验中,求事件 $A \cap  B$ 发生的概率,即 $P\left( {B \mid  A}\right)  = \frac{\left| A \cap  B\right| }{\left| A\right| }$ .

3. 条件概率公式: 在事件 $A$ 发生的条件下,事件 $B$ 发生的概率是 $P\left( {B \mid  A}\right)  = \frac{P\left( {A \cap  B}\right) }{P\left( A\right) }$ .

4. 概率的乘法公式: $P\left( {A \cap  B}\right)  = P\left( A\right) P\left( {B \mid  A}\right)$ .

#### 7.1.2 全概率公式

1. 全概率公式是指一个事件发生的概率是其在不同条件下发生概率的 加权平均 .

2. 设某个随机试验的结果可以分成 $n$ 种情况,即设样本空间 $\Omega$ 可分成 $n$ 个两两不同时发生(两两互斥)的事件 ${\Omega }_{1},{\Omega }_{2},\ldots ,{\Omega }_{n}$ ,即 $\Omega  = {\Omega }_{1} \cup  {\Omega }_{2} \cup  \cdots  \cup  {\Omega }_{n}$ ,且当 $i \neq  j$ 时有 ${\Omega }_{i} \cap  {\Omega }_{j} = \varnothing$ . 于是得到全概率公式: $P\left( A\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}P\left( {A \mid  {\Omega }_{i}}\right) P\left( {\Omega }_{i}\right) .$

*7.1.3 贝叶斯公式

由乘法公式得 $P\left( {A \mid  {\Omega }_{i}}\right) P\left( {\Omega }_{i}\right)  = P\left( {A \cap  {\Omega }_{i}}\right)  = P\left( A\right) P\left( {{\Omega }_{i} \mid  A}\right)$ ,因此 $P\left( {{\Omega }_{i} \mid  A}\right)  = \frac{P\left( {A \mid  {\Omega }_{i}}\right) P\left( {\Omega }_{i}\right) }{P\left( A\right) }$ ,再对分母应用全概率公式即推出贝叶斯公式: $P\left( {{\Omega }_{i} \mid  A}\right)  = \frac{P\left( {A \mid  {\Omega }_{i}}\right) P\left( {\Omega }_{i}\right) }{\mathop{\sum }\limits_{{k = 1}}^{n}P\left( {A \mid  {\Omega }_{k}}\right) P\left( {\Omega }_{k}\right) }$ .

### 7.2 随机变量的分布与特征

#### 7.2.1 随机变量与分布

1. 以样本空间作为 定义域 的 函数 $X$ 称为一个随机变量，即对样本空间 $\Omega$ 中任意给定的元素 $\omega$ ，都有唯一的实数 $X\left( \omega \right)$ 与之对应. 尽管随机变量的名字中用了“变量”这两个字，但实际上它是一个函数.

2. 随机变量所有可能的取值以及相应的概率，称为随机变量的 分布列.

3. 当随机变量取所有值的概率均相等时，称它是等可能分布或 均匀分布 的. 另外，只取两个值的随机变量称为伯努利型，其分布称为 伯努利 分布.

#### 7.2.2 期望

1. 定义: 如果随机变量 $X$ 的分布是 $\left( \begin{array}{llll} {x}_{1} & {x}_{2} & \ldots & {x}_{n} \\  {p}_{1} & {p}_{2} & \ldots & {p}_{n} \end{array}\right)$ 那么它的期望定义为如下的加权平均: $E\left\lbrack  X\right\rbrack   = \; {x}_{1}{p}_{1} + {x}_{2}{p}_{2} + \cdots  + {x}_{n}{p}_{n}$

2. 期望的线性性质:

①如果 $X$ 是一个随机变量， $a$ 是一个实数，那么 $E\left\lbrack  {aX}\right\rbrack   = {aE}\left\lbrack  X\right\rbrack$ .

②如果 $X, Y$ 是两个随机变量，那么 $E\left\lbrack  {X + Y}\right\rbrack   = E\left\lbrack  X\right\rbrack   + E\left\lbrack  Y\right\rbrack$ .

#### 7.2.3 方差

1. 对随机变量 $X$ 而言,用 $X$ 与其期望的偏差的平方的期望,即 $E\left\lbrack  {\left( X - E\left\lbrack  X\right\rbrack  \right) }^{2}\right\rbrack$ 来衡量随机变量 $X$ 的分散度,称为 $X$ 的方差,记为 $D\left\lbrack  X\right\rbrack  .D\left\lbrack  X\right\rbrack   = E\left\lbrack  {X}^{2}\right\rbrack   - {\left( E\left\lbrack  X\right\rbrack  \right) }^{2}$ .

2. 性质:

①如果 $X$ 是一个随机变量， $a$ 是一个实数，那么 $D\left\lbrack  {aX}\right\rbrack   = {a}^{2}D\left\lbrack  X\right\rbrack$ .

②如果 $X, Y$ 分别是两个独立的随机试验所对应的随机变量，那么 $D\left\lbrack  {X + Y}\right\rbrack   = D\left\lbrack  X\right\rbrack   + D\left\lbrack  Y\right\rbrack$ .

### 7.3 常用分布

#### 7.3.1 二项分布

1. 定义:独立地重复一个成功概率为 $p$ 的伯努利试验 $n$ 次，其成功次数的分布称为二项分布，亦称成功次数 $X$ 服从二项分布 $B\left( {n, p}\right)$ .

2. 成功次数为 $k$ 的概率为 $P\left( {X = k}\right)  = {}_{n}^{k}{p}^{k}{\left( 1 - p\right) }^{n - k}$ ,其中 $k = 0,1,2,\ldots , n$ .

3. 二项分布的期望 $E\left\lbrack  X\right\rbrack   = {np}$ ,方差 $D\left\lbrack  X\right\rbrack   = {np}\left( {1 - p}\right)$ .

#### 7.3.2 超几何分布

1. 定义: 从一个装有大小与质地相同的 $a$ 个白球, $b$ 个黑球的袋中随机且不放回地取 $n$ 个球,其中的白球数的分布称为超几何分布.

2. 且 $P\left( {X = k}\right)  = \frac{{\mathrm{C}}_{a}^{k}{\mathrm{C}}_{b}^{n - k}}{{\mathrm{C}}_{a + b}^{n}}$ ,其中 $k$ 的取值范围由以下条件决定: $k$ 不能超过 $n$ ,也不能超过 $a$ ; 同时, $n - k$ 不能超过 $b$ ,即成立 $k \leq  n, k \leq  a, n - k \leq  b$ .

3. *超几何分布的期望 $E\left\lbrack  X\right\rbrack   = \frac{na}{a + b}$ ,超几何分布的方差 $D\left\lbrack  X\right\rbrack   = n \cdot  \frac{a}{a + b} \cdot  \frac{b}{a + b} \cdot  \frac{a + b - n}{a + b - 1}$ .

#### 7.3.3 正态分布

1. 数学中的正态分布是指由下面的函数所表达的分布: ${\phi }_{\mu ,{\sigma }^{2}}\left( x\right)  = \frac{1}{\sqrt{{2\pi }{\sigma }^{2}}}{e}^{-\frac{{\left( x - \mu \right) }^{2}}{2{\sigma }^{2}}}, - \infty  < x <  + \infty$ ,其中有两个参数: $\left( 1\right) \mu$ 是该分布的数学 期望 (均值) ; (2) ${\sigma }^{2}$ 是该分布的 方差,且总是假设 $\sigma  > 0$ . 这个函数的图像如同钟形, 该函数在数学上称为 正态密度函数 ，也称为钟形曲线.

2. 定义: 设 $X$ 是一个取实数值的随机变量. 如果对任何给定的实数 $a$ 与 $b\left( {a < b}\right) , X$ 落在区间 $\left( {a, b}\right)$ 上的概率 $P\left( {a < X < b}\right)$ 等于三条直线 $y = 0, x = a, x = b$ 与正态密度函数图像 $y = {\phi }_{\mu ,{\sigma }^{2}}\left( x\right)$ 所围的区域面积, 那么 $X$ 服从正态分布,或更准确地说, $X$ 服从参数为 $\mu \text{ 、 }{\sigma }^{2}$ 的正态分布,记为 $X \sim  N\left( {\mu ,{\sigma }^{2}}\right)$ . 当 $\mu  = 0,{\sigma }^{2} = 1$ 时,相应的正态分布称为标准正态分布,记作 $X \sim  N\left( {0,1}\right)$ ,其密度函数 $\phi \left( x\right)  = \frac{1}{\sqrt{2\pi }}{e}^{-\frac{{x}^{2}}{2}}\;$ ,称为标准正态分布的密度函数,简记作 $y = \phi \left( x\right)$ .

3. 用 $\Phi \left( x\right)$ 表示标准正态分布的密度函数 $y = \phi \left( x\right)$ 从 $- \infty$ 到 $x$ 的累计面积,称为标准正态分布函数. 满足 $\Phi \left( {-x}\right)  = 1 - \Phi \left( x\right) .$

4. 如果 $X \sim  N\left( {\mu ,{\sigma }^{2}}\right)$ ,那么将 $X$ 平移再伸缩后将服从标准正态分布,即成立 $\frac{X - \mu }{\sigma } \sim  N\left( {0,1}\right)$ .

5. 当 $\sigma$ 变 小 时，最大值变大，钟形变“ 高瘦 ”，分布向中心 $x = \mu$ 处集中；反之，当 $\sigma$ 变 大 时， 最大值变小，钟形变“矮胖”，分布向 $x = \mu$ 的两边分散。
