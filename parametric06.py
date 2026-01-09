import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# 1. 定义参数v的范围和步长（0到2π，取200个点）
v = np.linspace(0, 2 * np.pi, 200)
# 计算完整的三维坐标
x = 2 + np.sin(v)
y = 2 + np.sin(v)
z = np.cos(v)

# 2. 创建3D绘图环境
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 3. 初始化绘图元素
# 绘制完整的静态曲线（灰色虚线，作为背景）
line_static, = ax.plot(x, y, z, color='gray', linestyle='--', linewidth=1.5, alpha=0.6)
# 动态移动的点（红色高亮）
point_dynamic, = ax.plot([], [], [], color='red', marker='o', markersize=10, label='Current Point')
# 动态绘制的轨迹（蓝色实线，随v增长逐步显示）
line_dynamic, = ax.plot([], [], [], color='blue', linewidth=2.5)
# 显示当前v值和坐标的文本标注
text_v = ax.text2D(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, bbox=dict(boxstyle='round', facecolor='white'))

# 4. 设置坐标轴和标题
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
ax.set_title(r'Parametric u contant: $\mathbf{r}(u, v) = \langle (2 + \sin v)\cos u,\ (2 + \sin v)\sin u,\ u + \cos v \rangle$', fontsize=14)
ax.set_xlim(0.5, 3.5)  # 适配x/y范围
ax.set_ylim(0.5, 3.5)
ax.set_zlim(-1.5, 1.5)  # 适配z范围
ax.grid(alpha=0.3)
ax.legend(loc='upper right')
ax.set_box_aspect([1, 1, 1])  # 等比例显示

# 5. 初始化函数（动画开始前的初始状态）
def init():
    point_dynamic.set_data([], [])
    point_dynamic.set_3d_properties([])
    line_dynamic.set_data([], [])
    line_dynamic.set_3d_properties([])
    text_v.set_text('')
    return point_dynamic, line_dynamic, text_v

# 6. 更新函数（每一帧的动态变化）
def update(frame):
    # frame对应v的索引，取前frame个点绘制轨迹
    line_dynamic.set_data(x[:frame], y[:frame])
    line_dynamic.set_3d_properties(z[:frame])
    # 更新动态点的位置（当前frame对应的坐标）
    point_dynamic.set_data([x[frame]], [y[frame]])
    point_dynamic.set_3d_properties([z[frame]])
    # 更新v值和坐标文本
    v_current = v[frame]
    text_v.set_text(f'v = {v_current:.2f} rad\n(x,y,z) = ({x[frame]:.2f}, {y[frame]:.2f}, {z[frame]:.2f})')
    return point_dynamic, line_dynamic, text_v

# 7. 创建动画（interval=50表示每50ms更新一帧，blit=True加速渲染）
ani = animation.FuncAnimation(
    fig, update, frames=len(v), init_func=init, interval=50, blit=True, repeat=True
)

# 显示动画
plt.show()

# （可选）保存动画为MP4文件（需要安装ffmpeg）
# ani.save('3d_parametric_curve_animation.mp4', writer='ffmpeg', fps=20, dpi=100)