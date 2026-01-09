import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建图形
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')

# 参数范围
t = np.linspace(0, 4 * np.pi, 100)  # 调整到4π，让螺旋线绕两圈

# 螺旋线：r(t) = (cos t, sin t, t)
x = np.cos(t)
y = np.sin(t)
z = t

# 绘制螺旋线
ax.plot(x, y, z, 'm-', linewidth=2, label='Helix: $\\vec{r}(t) = \\langle \\cos t, \\sin t, t \\rangle$')

# 圆柱面（半径为1）
theta = np.linspace(0, 2*np.pi, 100)
z_cylinder = np.linspace(0, 4*np.pi, 100)  # 与螺旋线相同高度
theta_grid, z_grid = np.meshgrid(theta, z_cylinder)

# 圆柱侧面坐标
x_cylinder = np.cos(theta_grid)
y_cylinder = np.sin(theta_grid)

# 绘制圆柱侧面
ax.plot_surface(x_cylinder, y_cylinder, z_grid, alpha=0.3, color='skyblue', rstride=10, cstride=10)

# 标注关键点
ax.scatter([1], [0], [0], color='red', s=50, label='$ (1,0,0) $')
ax.scatter([0], [1], [np.pi/2], color='green', s=50, label='$ (0,1,\\frac{\\pi}{2}) $')

# 添加标签
ax.text(1.1, 0, 0, '(1,0,0)', fontsize=10, color='red')
ax.text(0, 1.1, np.pi/2, '(0,1,π/2)', fontsize=10, color='green')

# 设置坐标轴
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(0, 4*np.pi + 0.5)
ax.view_init(elev=20, azim=-60)  # 视角调整
ax.grid(True, alpha=0.3)
ax.legend()

plt.title('Vector Curve: Helix on a Cylinder')
plt.show()
