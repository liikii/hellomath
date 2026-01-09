import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数范围：让 t 走完多个周期，展示完整图案
t = np.linspace(0, 4 * np.pi, 1000)

# 计算 x, y, z
x = (4 + np.sin(20 * t)) * np.cos(t)
y = (4 + np.sin(20 * t)) * np.sin(t)
z = np.cos(20 * t)

# 创建图形和轴
fig = plt.figure(figsize=(15, 12))
ax = fig.add_subplot(221, projection='3d')  # 3D plot
ax_xy = fig.add_subplot(222)  # XY plane
ax_xz = fig.add_subplot(223)  # XZ plane
ax_yz = fig.add_subplot(224)  # YZ plane

# 绘制3D曲线
ax.plot(x, y, z, 'm-', linewidth=2, label=r'$Curve$')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'3D Curve', fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend()
ax.view_init(elev=20, azim=-60)

# 绘制XY平面的投影
ax_xy.plot(x, y, 'b-', linewidth=2, label='Projection on XY')
ax_xy.set_xlabel('X')
ax_xy.set_ylabel('Y')
ax_xy.set_title('Projection on XY Plane', fontsize=12)
ax_xy.grid(True, alpha=0.3)
ax_xy.legend()

# 绘制XZ平面的投影
ax_xz.plot(x, z, 'r-', linewidth=2, label='Projection on XZ')
ax_xz.set_xlabel('X')
ax_xz.set_ylabel('Z')
ax_xz.set_title('Projection on XZ Plane', fontsize=12)
ax_xz.grid(True, alpha=0.3)
ax_xz.legend()

# 绘制YZ平面的投影
ax_yz.plot(y, z, 'g-', linewidth=2, label='Projection on YZ')
ax_yz.set_xlabel('Y')
ax_yz.set_ylabel('Z')
ax_yz.set_title('Projection on YZ Plane', fontsize=12)
ax_yz.grid(True, alpha=0.3)
ax_yz.legend()

plt.tight_layout()
plt.show()
