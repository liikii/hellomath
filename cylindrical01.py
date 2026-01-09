import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 创建3D绘图对象
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 定义点P的圆柱坐标 (r, θ, z)，这里示例取 r=2, θ=60°(π/3弧度), z=3
r = 2
theta = np.pi / 3  # 角度转换为弧度
z = 3

# 转换为直角坐标（用于绘图）
x = r * np.cos(theta)
y = r * np.sin(theta)

# ------------------- 绘制坐标轴 -------------------
ax.plot3D([0, 4], [0, 0], [0, 0], 'k-', lw=2, label='x-axis')
ax.plot3D([0, 0], [0, 4], [0, 0], 'k-', lw=2, label='y-axis')
ax.plot3D([0, 0], [0, 0], [0, 4], 'k-', lw=2, label='z-axis')

# ------------------- 绘制点 (r,θ,0) 和 P(r,θ,z) -------------------
# 点 (r,θ,0)（xy平面上的投影点）
ax.scatter3D(x, y, 0, color='black', s=80, label='$(r,\\theta,0)$')
# 点 P(r,θ,z)
ax.scatter3D(x, y, z, color='magenta', s=80, label='$P(r,\\theta,z)$')

# ------------------- 绘制辅助线 -------------------
# 从原点到 (r,θ,0) 的线段（长度r）
ax.plot3D([0, x], [0, y], [0, 0], 'r-', lw=2)
# 从 (r,θ,0) 到 P(r,θ,z) 的垂直线段（长度z）
ax.plot3D([x, x], [y, y], [0, z], 'm-', lw=2)

# ------------------- 标注角度θ -------------------
# 绘制角度圆弧（xy平面上，原点为中心）
theta_range = np.linspace(0, theta, 50)
arc_x = 0.5 * np.cos(theta_range)  # 半径0.5的圆弧
arc_y = 0.5 * np.sin(theta_range)
ax.plot3D(arc_x, arc_y, np.zeros_like(arc_x), 'b--', lw=1.5)
# 标注θ
ax.text(0.3, 0.2, 0, '$\\theta$', fontsize=12)

# ------------------- 标注r和z -------------------
ax.text(x/2, y/2, 0, '$r$', fontsize=12, color='red')
ax.text(x, y, z/2, '$z$', fontsize=12, color='magenta')

# ------------------- 图表设置 -------------------
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
ax.set_title('Cylindrical Coordinates of a Point', fontsize=14)
ax.legend()
ax.set_box_aspect([1,1,1])  # 等比例显示
plt.show()
