import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义函数 f(x, y)
def f(x, y):
    return x**2 + y**2 - 2*x - 6*y + 14

# 创建数据网格
x = np.linspace(-2, 6, 100)  # x 范围从 -2 到 6，包含顶点 x=1
y = np.linspace(-2, 8, 100)  # y 范围从 -2 到 8，包含顶点 y=3
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 创建图形
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面
surf = ax.plot_surface(X, Y, Z, cmap='Blues', alpha=0.8, edgecolor='none')

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

# 标出最小值点 (1, 3, 4)
min_point = [1, 3, 4]
ax.scatter(min_point[0], min_point[1], min_point[2], color='red', s=100, label='Minimum (1,3,4)')
ax.text(min_point[0]+0.2, min_point[1]+0.2, min_point[2]+0.5, 'Minimum', color='red', fontsize=10)

# 设置坐标轴标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Elliptic Paraboloid: $z = x^2 + y^2 - 2x - 6y + 14$')

# 设置视角（让图像更像教材中的图）
ax.view_init(elev=20, azim=45)

# 显示图形
plt.legend()
plt.show()
