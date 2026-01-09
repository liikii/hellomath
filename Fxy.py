import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义函数 f(x, y) = x^2 + y^2 + xy
def f(x, y):
    return x**2 + y**2 + x*y

# 创建数据网格
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 创建图形
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

# 标出最小值点 (0,0) 和其函数值
min_point = [0, 0, f(0, 0)]  # f(0,0) = 0
ax.scatter(min_point[0], min_point[1], min_point[2], color='red', s=100, label='Minimum (0,0)')
ax.text(min_point[0]+0.2, min_point[1]+0.2, min_point[2]+0.5, 'Minimum', color='red', fontsize=10)

# 设置坐标轴标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title(r'$f(x,y) = x^2 + y^2 + xy$ — minima，non-saddle')

# 调整视角，使“碗状”更明显
ax.view_init(elev=30, azim=45)

# 显示图形
plt.legend()
plt.show()
