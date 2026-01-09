import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. 定义参数
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(-3, 3, 20)
U, V = np.meshgrid(u, v)

# 2. 计算坐标
x = 2 * np.cos(U)
y = V
z = 2 * np.sin(U)

# 3. 绘图（核心：facecolors用单一颜色，不手动索引）
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 关键修复：facecolors直接传颜色名/RGB值，而非需索引的字符串数组
ax.plot_surface(x, y, z,
                facecolor='lightblue',  # 改用facecolor（单数）+ 单一颜色
                edgecolor='blue',
                alpha=0.7,
                linewidth=0.5)

# 标记点+坐标轴设置
ax.scatter(2, 0, 0, color='black', s=50, label='(2, 0, 0)')
ax.scatter(0, 0, 2, color='black', s=50, label='(0, 0, 2)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Circular Cylinder (Axis: y-axis, Radius: 2)')
ax.legend()

plt.show()
