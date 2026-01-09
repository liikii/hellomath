import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建网格数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# 计算 z 值
z = x**2 + y**2

# 创建图像
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面
surf = ax.plot_surface(x, y, z, cmap='viridis')

# 添加颜色条以显示高度
fig.colorbar(surf, shrink=0.5, aspect=5)

# 设置轴标签
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis (f(x,y))')

# 显示图像
plt.title(r'func $f(x,y) = x^2 + y^2$')
plt.show()
