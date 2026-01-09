import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数范围：t 从 -2 到 2，展示对称性
t = np.linspace(-2, 2, 100)

# 计算 x, y, z
x = t
y = t**2
z = t**3

# 创建图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲线
ax.plot(x, y, z, 'm-', linewidth=2, label=r'$x=t,\ y=t^2,\ z=t^3$')

# 添加箭头表示方向（从 t=-2 到 t=2）
ax.quiver(x[0], y[0], z[0], x[1]-x[0], y[1]-y[0], z[1]-z[0], color='m', arrow_length_ratio=0.1)
ax.quiver(x[-1], y[-1], z[-1], x[-2]-x[-1], y[-2]-y[-1], z[-2]-z[-1], color='m', arrow_length_ratio=0.1)

# 标注关键点
ax.scatter([0], [0], [0], color='red', s=50, label='Origin $(0,0,0)$')
ax.text(0.1, 0.1, 0.1, '(0,0,0)', fontsize=10, color='red')

# 设置标签和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'Space Curve: $x=t,\ y=t^2,\ z=t^3$', fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend()

# 调整视角，更好展示结构
ax.view_init(elev=20, azim=-60)

plt.tight_layout()
plt.show()
