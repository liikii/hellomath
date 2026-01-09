import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 设置图形
fig = plt.figure(figsize=(10, 6))
ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=2)  # 复平面（左）
ax2 = plt.subplot2grid((2, 2), (0, 1))  # cos 投影（右上）
ax3 = plt.subplot2grid((2, 2), (1, 1))  # sin 投影（右下）

# 角度范围
theta_max = 4 * np.pi
theta_vals = np.linspace(0, theta_max, 500)

# 单位圆
circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--')
ax1.add_artist(circle)

# 初始化轨迹线
line_complex, = ax1.plot([], [], 'b-', lw=1, alpha=0.5)  # 旋转轨迹
point_complex, = ax1.plot([], [], 'ro', markersize=8)
proj_cos, = ax2.plot([], [], 'g-', lw=2)
proj_sin, = ax3.plot([], [], 'm-', lw=2)
current_line_cos, = ax2.plot([], [], 'g--', alpha=0.7)
current_line_sin, = ax3.plot([], [], 'm--', alpha=0.7)

# 设置坐标轴
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_aspect('equal')
ax1.grid(True)
ax1.set_title(r'complex plane: $e^{i\theta} = \cos\theta + i\sin\theta$')
ax1.set_xlabel('real (Re)')
ax1.set_ylabel('image (Im)')

ax2.set_xlim(0, theta_max)
ax2.set_ylim(-1.2, 1.2)
ax2.grid(True)
ax2.set_ylabel(r'$\cos\theta$')
ax2.axhline(0, color='k', linewidth=0.5)

ax3.set_xlim(0, theta_max)
ax3.set_ylim(-1.2, 1.2)
ax3.grid(True)
ax3.set_xlabel(r'$\theta$ (radian)')
ax3.set_ylabel(r'$\sin\theta$')
ax3.axhline(0, color='k', linewidth=0.5)


# 动画更新函数
def animate(frame):
    if frame == 0:
        return line_complex, point_complex, proj_cos, proj_sin, current_line_cos, current_line_sin

    theta = theta_vals[:frame]
    z = np.exp(1j * theta)  # e^{iθ}

    # 复平面轨迹
    line_complex.set_data(z.real, z.imag)
    point_complex.set_data([z.real[-1]], [z.imag[-1]])

    # 投影到 cos 和 sin
    proj_cos.set_data(theta, np.cos(theta))
    proj_sin.set_data(theta, np.sin(theta))

    # 当前值的辅助线
    current_theta = theta[-1]
    current_cos = np.cos(current_theta)
    current_sin = np.sin(current_theta)

    current_line_cos.set_data([current_theta, current_theta], [0, current_cos])
    current_line_sin.set_data([current_theta, current_theta], [0, current_sin])

    return line_complex, point_complex, proj_cos, proj_sin, current_line_cos, current_line_sin


# 创建动画
anim = FuncAnimation(fig, animate, frames=len(theta_vals), interval=20, blit=True)

plt.tight_layout()
plt.show()
