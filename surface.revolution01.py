"""
旋转曲面（Surfaces of Revolution）的参数化表示方法
latex: x=x,\ y=f(x)\cos\theta,\ z=f(x)\sin\theta
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数范围
x = np.linspace(-1, 1, 50)        # x 从 -1 到 1
theta = np.linspace(0, 2*np.pi, 50)  # θ 从 0 到 2π
X, Theta = np.meshgrid(x, theta)

# 定义 f(x)
f_x = np.sqrt(1 - X**2)  # 上半圆

# 计算旋转曲面的坐标
Y = f_x * np.cos(Theta)
Z = f_x * np.sin(Theta)

# 创建图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面
surf = ax.plot_surface(X, Y, Z, cmap='Blues', alpha=0.7, edgecolor='none')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Surface of Revolution: Rotating $y = \\sqrt{1 - x^2}$ about the x-axis', fontsize=14)

# 设置视角
ax.view_init(elev=20, azim=45)

# 添加网格线（可选）
ax.grid(True)

plt.tight_layout()
plt.show()
