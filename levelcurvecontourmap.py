import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置中文字体（可选）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False


# 定义函数 f(x, y) = 45 - x² - y²
def f(x, y):
    return 45 - x ** 2 - y ** 2


# 创建网格数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 创建图形
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维曲面
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, edgecolor='none')

# 设置等高线 k 值（如 20, 25, 30, 35, 40, 45）
k_values = [20, 25, 30, 35, 40, 45]

# 绘制水平截面（horizontal traces）和对应的 level curves
for k in k_values:
    # 找到 z = k 的点
    Z_k = (Z >= k).astype(float) * 1e-6  # 微小高度，用于显示
    ax.contour(X, Y, Z_k, levels=[0], colors=['red'], linewidths=2, zdir='z', offset=k)

    # 在 xy 平面上投影等值线（level curve）
    ax.contour(X, Y, Z, levels=[k], colors=['red'], linewidths=2, zdir='z', offset=k)

# 添加标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Surface and Level Curves of $f(x,y) = 45 - x^2 - y^2$')

# 设置视角（类似教材图）
ax.view_init(elev=20, azim=-45)

# 显示图形
plt.show()
