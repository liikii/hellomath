import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. 定义参数范围
x = np.linspace(0, 2 * np.pi, 50)  # x的范围（对应原sinx的一个周期）
theta = np.linspace(0, 2 * np.pi, 50)  # 绕x轴旋转的角度（0到2π）
X, Theta = np.meshgrid(x, theta)  # 生成参数网格

# 2. 计算三维坐标
# 注意：原方程中x是自变量，这里用X表示；y和z由sinX与theta的三角函数组合而成
Y = np.sin(X) * np.cos(Theta)
Z = np.sin(X) * np.sin(Theta)

# 3. 创建3D绘图环境
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 4. 绘制旋转曲面（用cmap实现颜色渐变）
surface = ax.plot_surface(
    X, Y, Z,
    cmap='viridis',  # 颜色渐变（随x变化）
    alpha=0.8,       # 透明度
    edgecolor='gray',# 网格线颜色
    linewidth=0.3    # 网格线宽度
)

# 5. 标记原始曲线（θ=0时的截面，即y=sinx, z=0）
ax.plot(x, np.sin(x), np.zeros_like(x),
        color='red', linewidth=3, label=r'$\theta=0$: $y=\sin x, z=0$')

# 6. 样式与标签设置
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title(
    r'Revolution Surface: $x=x,\ y=\sin x \cos\theta,\ z=\sin x \sin\theta$',
    fontsize=14,
    pad=20
)
ax.legend(loc='upper right')
ax.grid(alpha=0.3)
ax.set_box_aspect([1, 1, 1])  # 等比例显示，避免曲面变形

# 添加颜色条（对应x的数值）
fig.colorbar(surface, ax=ax, label='x value')

plt.show()
