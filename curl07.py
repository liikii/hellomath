import numpy as np
import matplotlib.pyplot as plt

# 1. 定义 y-z 平面网格（x=0）
y = np.linspace(-2, 2, 10)
z = np.linspace(-2, 2, 10)
Y, Z = np.meshgrid(y, z)

# 2. 计算向量场的 y、z 分量（改为负号）
Fy = -2 * Z  # Q=-2z
Fz = -3 * Y  # R=-3y

# 3. 绘制向量场
plt.figure(figsize=(6, 6))
plt.quiver(Y, Z, Fy, Fz, color='r', scale=20, width=0.005)

# 4. 图表样式
plt.xlabel('y')
plt.ylabel('z')
plt.title('Vector field in y-z plane (x=0): $\\vec{F} = \\langle 0, -2z, -3y \\rangle$')
plt.axis('equal')
plt.grid(alpha=0.3)
plt.show()
