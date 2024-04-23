# 状态方程建立初步设计

### 状态量选取与单帧搜索

以./data/路径下的 Gauss 白噪声加载数据为例，基本可以使用的传感器数据包括$\varepsilon, u, a, F_{excitation}, F_{inner}$，分别为钢筋应变、纵向&横向的位移与加速度、外部激励、测点内力，目前初步拟使用以上物理量建立状态方程。

目前对于状态空间、状态方程，重新进行了定义与推导，并舍弃了广义冲量作为**状态向量**的成员（考虑到存在更简洁的定义方法，但仍可作为评估指标），重新推导的详细过程如下：

#### 状态空间建立推导

对于该系统，考虑分别选取位移\(u\)、应变\(\varepsilon\)为广义坐标，则状态向量\[\boldsymbol{x} = [u \ \dot{u} \ \varepsilon \ \dot{\varepsilon}]^{T}\]这里的目标就是构建出\(\boldsymbol{\dot{x}}\)关于\(\boldsymbol{x}\)的线性矩阵方程。首先对于广义坐标位移，有\[\dot{u} = \cfrac{du}{dt}\]而通过阻尼受迫振动系统的动力学控制方程\[m\ddot{u} + c\dot{u} + ku = Bf\]其中\(f=f(t)\).

仅考虑线弹性条件下的结构力学特征，可以认为对于位移和应变，二者应成立线性关系\[u = L\varepsilon\]其中\(L\)可以是零阶或二阶张量，但不论如何均为线性性表达.

对于另一个广义坐标应变，不难看出其广义速度为\[\dot{\varepsilon} = \cfrac{d\varepsilon}{dt}\]通过对位移-应变关系方程左右对时间微分，代入可得\[\hat{m}\ddot{\varepsilon} + \hat{c}\dot{u} + \hat{k}u = Bf\]其中\(\hat{m} = mL, \hat{c} = cL, \hat{k} = kL\).

此时对于线弹性范围内，状态转移方程可以为：$\dot{\boldsymbol{x}} = A\boldsymbol{x} + Bf$，可以展开为
  \[
  \begin{bmatrix}
  \dot{u}\\
  \ddot{u}\\
  \dot{\varepsilon}\\
  \ddot{\varepsilon}
  \end{bmatrix} =
  \begin{bmatrix}
  0 & 1 & 0 & 0\\
  -\frac{k}{m} & -\frac{c}{m} & 0 & 0\\
  0 & 0 & 0 & 1\\
  0 & 0 & -\frac{k}{mL} & -\frac{c}{mL}
  \end{bmatrix}
  \begin{bmatrix}
  u\\
  \dot{u}\\
  \varepsilon\\
  \dot{\varepsilon}
  \end{bmatrix} +
  \begin{bmatrix}
  0\\
  \frac{1}{m}\\
  0\\
  \frac{1}{mL}\\
  \end{bmatrix} f(t)
  \]
若使用阻尼比与固有频率表示，则系数矩阵\(A\)可以表示为\[A = 
  \begin{bmatrix}
  0 & 1 & 0 & 0\\
  -\omega_{0}^{2} & -2\zeta\omega_{0} & 0 & 0\\
  0 & 0 & 0 & 1\\
  0 & 0 & -\frac{\omega_{0}^{2}}{L} & -\frac{2\zeta\omega_{0}}{L}
  \end{bmatrix} \]
求解\(A\)的特征根，可得\[A_{1,2} = \cfrac{-\zeta\omega_{0}\pm\omega_{0}\sqrt{\zeta-L}}{L}\]\[A_{3,4} = \cfrac{-L\zeta\omega_0 \pm L\omega_0\sqrt{\zeta-1}}{L}\]
令\(A_1 = A_2\)，显然\[\zeta = L\]
令\(A_3 = A_4\)，显然\[\zeta = 1\]
令\(A_1 = A_3\)，可得\(\omega_0(L-1)(\zeta+\sqrt{\zeta-L})=0\)，可得\[L = 1\]
令\(A_1 = A_4\)，可得\(\omega_0(L-1)(\zeta-\sqrt{\zeta-L})=0\)，该方程另外解从\[\zeta-\sqrt{\zeta - L} = 0\]可以得出，为\[\zeta_{1,2} = \cfrac{1\pm \sqrt{1-4L}}{2}\]
考虑到\(L\)为位移与应变的映射矩阵，则应该有\(L<<1\)，因此通过简化，可知\(A\)不满秩的成立条件为\[\zeta \ne 1,0,L\]对于大部分情况而言该条件是成立的，**但是必须考虑不成立的情况**，处理方法也很简单：
- 对于timestamp != 0 时，当\(A_n\)不满秩时，可以使用前一帧的\(A_{n-1}\)进行计算，或者直接把该帧参数和上一帧取相同，并抛出一个warning，在log中记录执行了该操作的timestamp
- 对于timestamp == 0 时，当\(A\)不满秩，不开始，直到搜索出一个符合开始条件的timestamp，若存在该timestamp != total_timestamp.size() - 1，则抛出warning，否则抛出error

#### 方程离散化

以上推导了状态方程，但微分方程无法数值求解，需要写成差分形式，首先\[\boldsymbol{\dot{x}} = \cfrac{d\boldsymbol{x}}{dt}\]当\(dt\)写成时间步\(\Delta t\)时，有差分方程\[\Delta \boldsymbol{x} = A\Delta t\boldsymbol{x}+L\Delta tf\]
即\[\boldsymbol{x}(n+1) - \boldsymbol{x}(n) = A\Delta t\boldsymbol{x}(n)+L\Delta tf(n)\]整理可得\[\boldsymbol{x}(n+1) = (A\Delta t+\boldsymbol{I})\boldsymbol{x}(n)+L\Delta tf(n)\]
考虑到\(A\Delta t+\boldsymbol{I}\)形式上非常类似\(e^{A\Delta t}\)的Taylor级数的0阶、1阶级数的截断，故可取\[\hat{A} = e^{A\Delta t}\]同理可得\[\Delta t \boldsymbol{I} = A^{-1}(\hat{A} - \boldsymbol{I})\]
因此\[\hat{L} = L\Delta t = \Delta t \boldsymbol{I}L =  A^{-1}(\hat{A} - \boldsymbol{I})L\]最终得到状态转移方程为\[\boldsymbol{x}(n+1) = \hat{A}\boldsymbol{x}(n) + \hat{L} f(n)\]
**对于量级问题的处理**，需要对输入向量首先做缩放变换，可取\[\boldsymbol{\alpha} =  
  \begin{bmatrix}
  1 & 0 & 0 & 0\\
  0 & 1 & 0 & 0\\
  0 & 0 & \alpha & 0\\
  0 & 0 & 0 & \alpha
  \end{bmatrix} \]并使\[\boldsymbol{x}'= \alpha\boldsymbol{x}\]