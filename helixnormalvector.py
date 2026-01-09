"""
N(t)=(−cost, −sint, 0), 向量与z轴无关， 只与当前xy平面有关。 上下无波动
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数范围
t = np.linspace(0, 4 * np.pi, 50)
x = np.cos(t)
y = np.sin(t)
z = t

# 法向量 N(t) = (-cos t, -sin t, 0)
Nx = -np.cos(t)
Ny = -np.sin(t)
Nz = np.zeros_like(t)

# 副法向量 B(t) = (1/sqrt(2)) * (sin t, -cos t, 1)
Bx = (1 / np.sqrt(2)) * np.sin(t)
By = (1 / np.sqrt(2)) * (-np.cos(t))
Bz = (1 / np.sqrt(2)) * np.ones_like(t)

# 创建3D图形
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# 绘制螺旋线
ax.plot(x, y, z, 'b-', linewidth=2, label='Helix')

# 选择几个关键点画向量
indices = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]  # 选10个点

for i in indices:
    # 画法向量（红色）
    ax.quiver(x[i], y[i], z[i], Nx[i], Ny[i], Nz[i],
              color='red', length=0.5, arrow_length_ratio=0.1,
              label='N(t)' if i == 0 else "")

    # 画副法向量（绿色）
    ax.quiver(x[i], y[i], z[i], Bx[i], By[i], Bz[i],
              color='green', length=0.7, arrow_length_ratio=0.1,
              label='B(t)' if i == 0 else "")

# 绘制 z 轴（中心柱）
ax.plot([0, 0], [0, 0], [0, 4 * np.pi], 'k--', linewidth=2, label='z-axis (center)')

# 设置标签和标题
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title(r'Helix with Normal $\mathbf{N}(t)$ and Binormal $\mathbf{B}(t)$ Vectors')
ax.legend()
ax.grid(True)

# 视角调整（让能看到方向）
ax.view_init(elev=30, azim=45)

plt.show()
