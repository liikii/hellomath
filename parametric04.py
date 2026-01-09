import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数范围
u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, 2*np.pi, 50)
U, V = np.meshgrid(u, v)

# 计算曲面点
x = (2 + np.sin(V)) * np.cos(U)
y = (2 + np.sin(V)) * np.sin(U)
z = U + np.cos(V)

# 创建图形
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# 绘制整个曲面
# surf = ax.plot_surface(x, y, z, cmap='viridis', alpha=0.6, edgecolor='none')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('Surface: r(u,v) = ((2+sin v)cos u, (2+sin v)sin u, u + cos v)', fontsize=14)

# ==================== 固定 u 的曲线（u 常数，v 变化）====================
# 选几个不同的 u 值
u_values = [0, np.pi/2, np.pi, 3*np.pi/2]
colors = ['red', 'green', 'blue', 'purple']

for u_val, color in zip(u_values, colors):
    v_line = np.linspace(0, 2*np.pi, 100)
    x_line = (2 + np.sin(v_line)) * np.cos(u_val)
    y_line = (2 + np.sin(v_line)) * np.sin(u_val)
    z_line = u_val + np.cos(v_line)
    ax.plot(x_line, y_line, z_line, color=color, linewidth=2, label=f'u={u_val:.1f}')

# ==================== 固定 v 的曲线（v 常数，u 变化）====================
# 选几个不同的 v 值
v_values = [0, np.pi/2, np.pi, 3*np.pi/2]
colors2 = ['orange', 'cyan', 'magenta', 'yellow']

for v_val, color in zip(v_values, colors2):
    u_line = np.linspace(0, 2*np.pi, 100)
    x_line = (2 + np.sin(v_val)) * np.cos(u_line)
    y_line = (2 + np.sin(v_val)) * np.sin(u_line)
    z_line = u_line + np.cos(v_val)
    ax.plot(x_line, y_line, z_line, color=color, linewidth=2, label=f'v={v_val:.1f}')

# 添加图例
ax.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

# 设置视角
ax.view_init(elev=20, azim=45)

# 显示
plt.tight_layout()
plt.show()
