# HINA
Heterogeneous Integration for Natural Assessment

## 状态方程建立初步设计

### 状态量选取与单帧搜索

以./data/路径下的 Gauss 白噪声加载数据为例，基本可以使用的传感器数据包括$\varepsilon, u, a, F_{excitation}, F_{inner}$，分别为钢筋应变、纵向&横向的位移与加速度、外部激励、测点内力，目前初步拟使用以上物理量建立状态方程。

- 状态向量$$\vec{x} = [u, \ddot{u}, \varepsilon, p_{\varepsilon}]$$，其中$$u$$为位移，$\varepsilon$为钢筋应变，$p_{\varepsilon}$为应变的共轭变量，或者广义动量
- 对于线弹性范围内，状态转移方程可以为：$\dot{x} = Ax + Bf$，可以展开为
  \[
  \begin{bmatrix}
  \dot{u}\\
  \ddot{u}\\
  \dot{\varepsilon}\\
  \dot{p_{\varepsilon}}
  \end{bmatrix} =
  \begin{bmatrix}
  0 & 1 & 0 & 0\\
  -\frac{k}{m} & -\frac{c}{m} & 0 & 0\\
  0 & 0 & 0 & 1\\
  0 & 0 & 0 & -\frac{1}{\tau_{c}}
  \end{bmatrix}
  \begin{bmatrix}
  u\\
  \dot{u}\\
  \varepsilon\\
  p_{\varepsilon}
  \end{bmatrix} +
  \begin{bmatrix}
  0\\
  \frac{1}{m}\\
  0\\
  0\\
  \end{bmatrix} F(t)
  \]
- 广义动量定义为拉格朗日函数对广义速度的导数， 拉格朗日函数为\( L(u, \dot{u}, \epsilon_{\text{steel}}, p_{\epsilon}) \)，其中 \( u \) 是位移，\( \dot{u} \) 是位移的速度，\( \epsilon_{\text{steel}} \) 是应变，\( p_{\epsilon} \) 是应变的共轭变量。
-   根据哈密顿原理，系统的运动方程可以通过哈密顿函数的导数和拉格朗日函数的关系得到：

   \[
   \dot{u} = \frac{\partial H}{\partial p_u}, \quad \dot{p}_u = -\frac{\partial H}{\partial u}
   \]

   \[
   \dot{\epsilon}_{\text{steel}} = \frac{\partial H}{\partial p_{\epsilon}}, \quad \dot{p}_{\epsilon} = -\frac{\partial H}{\partial \epsilon_{\text{steel}}}
   \]
- 引入广义动量主要目的在于把位移的影响纳入状态转移方程，但是需要进一步严谨推导确定可行性
- 拟对应变进行归一化，避免方程奇异
- 目前只考虑**线弹性**场景，拟对塑形、非线性情况使用摄动法级数分解
- 单帧的搜索目标是动力学参数\(m\)、\(c\)与\(k\)，验证可以先使用Gauss白噪声进行验证，并通过搜索各阶\(\omega_{n}\)进一步确认有效性

### 时序记忆、投票与状态转移

预计待单帧/线弹性/白噪声激励测试完成后实现，数据结构已定义
