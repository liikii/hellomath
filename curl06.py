import numpy as np
import matplotlib.pyplot as plt

# 1. 定义 y-z 平面的网格（x固定为0）
y = np.linspace(-2, 2, 10)  # y的范围
z = np.linspace(-2, 2, 10)  # z的范围
Y, Z = np.meshgrid(y, z)

# 2. 计算向量场的 y、z 分量（x分量为0，不展示）
Fy = 2 * Z  # Q=2z
Fz = 3 * Y  # R=3y

# 3. 绘制向量场（quiver：箭头图）
plt.figure(figsize=(6, 6))
# quiver(起点y, 起点z, y方向向量, z方向向量)
plt.quiver(Y, Z, Fy, Fz, color='b', scale=20, width=0.005)

# 4. 设置图表样式
plt.xlabel('y')
plt.ylabel('z')
plt.title('Vector field in y-z plane (x=0): $\\vec{F} = \\langle 0, 2z, 3y \\rangle$')
plt.axis('equal')  # 等比例显示，避免向量变形
plt.grid(alpha=0.3)
plt.show()
