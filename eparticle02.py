import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义时间参数 t
t = np.linspace(0, 6 * np.pi, 500)

# 计算三维坐标
x = t - (3/2) * np.sin(t)
y = 1 - (3/2) * np.cos(t)
z = t  # 沿 z 轴匀速上升

# 创建图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维曲线
ax.plot(x, y, z, color='red', linewidth=2, label='Trajectory')

# 添加辅助曲面（例子）
# 我们可以构造一个围绕轨迹的简单曲面，这里使用 u 参数来生成环绕轨迹的圆柱形曲面
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, 6*np.pi, 100)
u, v = np.meshgrid(u, v)
x_surface = v - (3/2) * np.sin(v) + 0.5 * np.cos(u)
y_surface = 1 - (3/2) * np.cos(v) + 0.5 * np.sin(u)
z_surface = v

# 绘制辅助曲面
ax.plot_surface(x_surface, y_surface, z_surface, color='blue', alpha=0.3)

# 设置标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 添加标题和图例
ax.set_title('3D Trajectory with Surrounding Surface')
ax.legend()

# 设置视角（可选）
ax.view_init(elev=20, azim=45)

# 调整布局并显示
plt.tight_layout()
plt.show()