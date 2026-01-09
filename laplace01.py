import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义网格
x = np.linspace(-2, 2, 100)
y = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)

# 计算函数值
Z = np.exp(X) * np.sin(Y)

# 创建三维图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲面
surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolor='none')

# 添加颜色条
m = plt.cm.ScalarMappable(cmap='viridis')
m.set_array(Z.flatten())
cbar = plt.colorbar(m, ax=ax, shrink=0.5)
cbar.set_label('u(x,y)', rotation=270)

# 设置标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('u(x,y)')
ax.set_title(r'$u(x, y) = e^x \sin y$')

# 调整视角
ax.view_init(elev=20, azim=45)

# 显示图形
plt.tight_layout()
plt.show()
