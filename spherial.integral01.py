"""
 1° 的弧长在不同纬度确实是不同的
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建3D绘图对象
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 生成球体的坐标（球坐标转直角坐标）
radius = 1.0  # 球体半径（小于轴长，轴长设为2）
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = radius * np.outer(np.cos(u), np.sin(v))
y = radius * np.outer(np.sin(u), np.sin(v))
z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

# 绘制球体（浅蓝色，带网格线）
ax.plot_surface(x, y, z, color='lightblue', alpha=0.8, rstride=5, cstride=5, edgecolor='white')

# 绘制坐标轴（x、y、z轴，长度设为2，超过球体半径）
axis_length = 2.0
ax.plot3D([-axis_length, axis_length], [0, 0], [0, 0], 'k-', lw=2, label='x-axis')
ax.plot3D([0, 0], [-axis_length, axis_length], [0, 0], 'k-', lw=2, label='y-axis')
ax.plot3D([0, 0], [0, 0], [-axis_length, axis_length], 'k-', lw=2, label='z-axis')

# 标记原点
ax.scatter(0, 0, 0, color='black', s=50, label='Origin (0,0,0)')

# 设置坐标轴范围、标签和标题
ax.set_xlim(-axis_length, axis_length)
ax.set_ylim(-axis_length, axis_length)
ax.set_zlim(-axis_length, axis_length)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'$\rho = c$ (Sphere with Radius $c=1$)')
ax.legend()

# 显示图像
plt.show()