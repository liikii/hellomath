import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. 定义参数u的范围（控制螺旋的圈数）
u = np.linspace(0, 6 * np.pi, 200)  # 0到6π，对应3圈螺旋

# 2. 计算三维坐标
x = np.cos(u)
y = np.sin(u)
z = u

# 3. 创建3D绘图环境
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 4. 绘制螺旋线
ax.plot(x, y, z, color='blue', linewidth=2, label=r'$x=\cos u,\ y=\sin u,\ z=u$')

# 5. 标记起点和关键圈数点
ax.scatter(np.cos(0), np.sin(0), 0, color='red', s=80, label='start (u=0)')
ax.scatter(np.cos(2*np.pi), np.sin(2*np.pi), 2*np.pi, color='green', s=80, label='1round (u=2π)')
ax.scatter(np.cos(4*np.pi), np.sin(4*np.pi), 4*np.pi, color='orange', s=80, label='2round (u=4π)')
ax.scatter(np.cos(6*np.pi), np.sin(6*np.pi), 6*np.pi, color='purple', s=80, label='3round (u=6π)')

# 6. 样式与标签设置
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title(r'3D Helix: $x=\cos u,\ y=\sin u,\ z=u$', fontsize=14)
ax.legend(loc='upper right')
ax.grid(alpha=0.3)
ax.set_box_aspect([1, 1, 1])  # 等比例显示，避免螺旋变形

plt.show()
