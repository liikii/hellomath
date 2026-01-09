import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建网格数据
x = np.linspace(0, 1, 50)
y = np.linspace(0, 2, 50)
X, Y = np.meshgrid(x, y)
Z = X + Y**2  # z = x + y^2

# 创建 3D 图像
fig = plt.figure(figsize=(8, 6))
fig.suptitle(r'$\iint_S f(x, y, z) \, dS = \iint_D f(x, y, g(x, y)) \sqrt{\left( \frac{\partial z}{\partial x} '
             r'\right)^2 + \left( \frac{\partial z}{\partial y} \right)^2 + 1} \, dA$')
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', alpha=0.8)

# 设置坐标轴标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# 设置视角（类似你图中的角度）
ax.view_init(elev=20, azim=-60)

# 添加网格线
ax.grid(True)

# 添加颜色条
m = plt.cm.ScalarMappable(cmap='viridis')
m.set_array(Z.flatten())
fig.colorbar(m, ax=ax, shrink=0.5, aspect=5, label='z')

# 调整显示范围
ax.set_xlim(0, 1)
ax.set_ylim(0, 2)
ax.set_zlim(0, 4)

# 去除边框（可选）
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# 显示图像
plt.tight_layout()
plt.show()
