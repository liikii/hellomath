import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建数据网格
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)
Z = 4 - X**2 - 2*Y**2  # z = 4 - x² - 2y²

# 创建3D图形
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面（浅蓝色）
surf = ax.plot_surface(X, Y, Z, cmap='Blues', alpha=0.7, edgecolor='none')

# --- 图1：y = 1 平面与曲面相交 → C1 ---
# 固定 y = 1，z = 4 - x² - 2(1)² = 2 - x²
x1 = np.linspace(-2, 2, 100)
y1 = np.ones_like(x1)  # y = 1
z1 = 2 - x1**2

# 绘制曲线 C1（红色）
ax.plot(x1, y1, z1, 'r-', linewidth=2, label='C₁: y=1')

# 在点 (1,1,1) 处画切线（斜率 -2）
# 切线方向：dz/dx = -2x，在 x=1 时为 -2
# 参数方程：x = 1 + t, y = 1, z = 1 - 2t （t ∈ [-0.5, 0.5]）
t = np.linspace(-0.5, 0.5, 10)
x_tangent1 = 1 + t
y_tangent1 = np.ones_like(t)
z_tangent1 = 1 - 2*t

ax.plot(x_tangent1, y_tangent1, z_tangent1, 'r--', linewidth=2, label='Tangent to C₁ at (1,1,1)')

# --- 图2：x = 1 平面与曲面相交 → C2 ---
# 固定 x = 1，z = 4 - (1)² - 2y² = 3 - 2y²
y2 = np.linspace(-2, 2, 100)
x2 = np.ones_like(y2)  # x = 1
z2 = 3 - 2*y2**2

# 绘制曲线 C2（绿色）
ax.plot(x2, y2, z2, 'g-', linewidth=2, label='C₂: x=1')

# 在点 (1,1,1) 处画切线（斜率 -4）
# 切线方向：dz/dy = -4y，在 y=1 时为 -4
# 参数方程：x = 1, y = 1 + s, z = 1 - 4s
s = np.linspace(-0.5, 0.5, 10)
x_tangent2 = np.ones_like(s)
y_tangent2 = 1 + s
z_tangent2 = 1 - 4*s

ax.plot(x_tangent2, y_tangent2, z_tangent2, 'g--', linewidth=2, label='Tangent to C₂ at (1,1,1)')

# 标注点 (1,1,1)
ax.scatter(1, 1, 1, color='red', s=50, label='Point (1,1,1)')

# 设置标签和视角
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Graph of $z = 4 - x^2 - 2y^2$ with Cross-Section Curves and Tangents')

# 添加图例
ax.legend()

# 调整视角（更清晰地看到两个切线）
ax.view_init(elev=20, azim=45)

# 显示图形
plt.tight_layout()
plt.show()
