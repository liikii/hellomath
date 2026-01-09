import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置字体支持中文（可选）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 定义函数 f(x, y)
def f(x, y):
    return np.sin(x) + np.cos(y) + 2  # 确保 f >= 0

# 区域定义
a, b = 0, np.pi      # x ∈ [0, π]
c, d = 0, np.pi      # y ∈ [0, π]

# 网格划分（小矩形数量）
m, n = 6, 6          # m × n 个子矩形

# 计算步长
dx = (b - a) / m
dy = (d - c) / n

# 生成采样点（这里用每个子矩形的中心）
x_centers = a + dx/2 + np.arange(m) * dx   # shape: (m,)
y_centers = c + dy/2 + np.arange(n) * dy   # shape: (n,)

Xc, Yc = np.meshgrid(x_centers, y_centers, indexing='ij')  # (m, n)
Zc = f(Xc, Yc)  # 高度

# 创建图形
fig = plt.figure(figsize=(12, 5))

# ====== 子图 1：三维柱状图（黎曼和）======
ax1 = fig.add_subplot(121, projection='3d')

# 绘制每个柱体
for i in range(m):
    for j in range(n):
        x0 = a + i * dx
        y0 = c + j * dy
        height = Zc[i, j]
        # 使用 bar3d: (x, y, z, dx, dy, dz)
        ax1.bar3d(x0, y0, 0, dx, dy, height, shade=True, color='lightblue', edgecolor='k', alpha=0.8)

# 设置标签
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.set_title('Riemann Sum (3D Bars)')

# ====== 子图 2：真实曲面 + 柱体叠加（可选）======
ax2 = fig.add_subplot(122, projection='3d')

# 绘制光滑曲面（作为参考）
x_surf = np.linspace(a, b, 50)
y_surf = np.linspace(c, d, 50)
Xs, Ys = np.meshgrid(x_surf, y_surf)
Zs = f(Xs, Ys)
ax2.plot_surface(Xs, Ys, Zs, cmap='viridis', alpha=0.6, linewidth=0)

# 再叠加柱体（半透明）
for i in range(m):
    for j in range(n):
        x0 = a + i * dx
        y0 = c + j * dy
        height = Zc[i, j]
        ax2.bar3d(x0, y0, 0, dx, dy, height, color='red', alpha=0.5, edgecolor='k')

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_title('Surface + Riemann Sum')

plt.tight_layout()
plt.show()
