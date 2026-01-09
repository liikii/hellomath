# <P, Q>
# 在 ∂P/∂y=0 的前提下，Q 随 x 的变化会导致 “同一水平线上不同位置的垂直分量差异”，这种差异会让局部微元产生 “剪切式旋转”
# 在 XY 平台绕原点做 刚体旋转（比如机械臂末端的旋转、转盘的转动）的情况下，外围（离原点越远）的线速度确实比内围快；但如果是非刚体旋转（比如流体的涡旋），则不一定。
import numpy as np
import matplotlib.pyplot as plt

# ---------------------- 1. 全局设置与网格生成 ----------------------
# 设置绘图样式，确保矢量箭头清晰
plt.rcParams['figure.figsize'] = (15, 12)  # 整体图尺寸
plt.rcParams['font.size'] = 10  # 全局字体大小

# 生成 x, y 网格（范围：-3 到 3，均匀取 15 个点）
x = np.linspace(-3, 3, 15)
y = np.linspace(-3, 3, 15)
X, Y = np.meshgrid(x, y)

# ---------------------- 2. 定义 5 种矢量场（满足对应偏导数条件） ----------------------
# 场景 1: ∂P/∂y=0，∂Q/∂x>0  | 选取 F=(1, x) （P=1，Q=x；∂P/∂y=0，∂Q/∂x=1>0）
P1 = np.ones_like(X)
Q1 = X

# 场景 2: ∂P/∂y=0，∂Q/∂x<0  | 选取 F=(1, -x)（P=1，Q=-x；∂P/∂y=0，∂Q/∂x=-1<0）
P2 = np.ones_like(X)
Q2 = -X

# 场景 3: ∂P/∂y>0，∂Q/∂x=0  | 选取 F=(y, 1) （P=y，Q=1；∂P/∂y=1>0，∂Q/∂x=0）
P3 = Y
Q3 = np.ones_like(X)

# 场景 4: ∂P/∂y<0，∂Q/∂x=0  | 选取 F=(-y, 1)（P=-y，Q=1；∂P/∂y=-1<0，∂Q/∂x=0）
P4 = -Y
Q4 = np.ones_like(X)

# 场景 5: ∂P/∂y=0，∂Q/∂x=0  | 选取 F=(1, 1) （P=1，Q=1；∂P/∂y=0，∂Q/∂x=0）
P5 = np.ones_like(X)
Q5 = np.ones_like(X)

# 整理所有矢量场数据和标题（便于循环绘图）
vector_fields = [
    (P1, Q1, r'$\partial P/\partial y=0$, $\partial Q/\partial x>0$ (F=(1, x))'),
    (P2, Q2, r'$\partial P/\partial y=0$, $\partial Q/\partial x<0$ (F=(1, -x))'),
    (P3, Q3, r'$\partial P/\partial y>0$, $\partial Q/\partial x=0$ (F=(y, 1))'),
    (P4, Q4, r'$\partial P/\partial y<0$, $\partial Q/\partial x=0$ (F=(-y, 1))'),
    (P5, Q5, r'$\partial P/\partial y=0$, $\partial Q/\partial x=0$ (F=(1, 1))')
]

# ---------------------- 3. 循环绘制 5 张子图 ----------------------
fig, axes = plt.subplots(3, 2)  # 创建 3x2 子图网格（适配 5 张图，最后一个子图隐藏）
axes = axes.flatten()  # 扁平化子图数组，便于索引

for idx, (P, Q, title) in enumerate(vector_fields):
    ax = axes[idx]

    # 绘制矢量场（quiver 函数：箭头矢量图）
    ax.quiver(X, Y, P, Q, color='royalblue', scale=30, width=0.005)

    # 设置子图标题和坐标轴标签（英文）
    ax.set_title(title, fontsize=11)
    ax.set_xlabel('X-axis', fontsize=9)
    ax.set_ylabel('Y-axis', fontsize=9)

    # 添加网格和坐标轴参考线（增强可读性）
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='black', linewidth=0.8, alpha=0.7)
    ax.axvline(x=0, color='black', linewidth=0.8, alpha=0.7)

    # 统一坐标轴范围（保证所有图视角一致）
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)

# 隐藏多余的第 6 个子图（3x2 网格的最后一个）
axes[5].set_visible(False)

# ---------------------- 4. 整体布局优化与显示 ----------------------
plt.tight_layout()  # 自动调整子图间距，避免重叠
plt.suptitle('Vector Fields with Different Partial Derivative Conditions', fontsize=14, y=1.02)  # 总标题
plt.show()
