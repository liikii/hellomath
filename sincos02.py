import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 设置图形大小
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# 单位圆的角度t从0到2π
t = np.linspace(0, 2 * np.pi, 100)
circle_x = np.cos(t)
circle_y = np.sin(t)

# sin和cos曲线的数据
x_vals = np.linspace(0, 2 * np.pi, 100)
sin_vals = np.sin(x_vals)
cos_vals = np.cos(x_vals)

# 绘制静态背景：单位圆和sin/cos曲线，并添加坐标轴线
for a in ax:
    a.axhline(0, color='black', linewidth=0.5)  # 添加y轴线
    a.axvline(0, color='black', linewidth=0.5)  # 添加x轴线
    a.grid(True, linestyle='--', alpha=0.7)  # 显示网格线

ax[0].plot(circle_x, circle_y, label='Unit Circle')
ax[1].plot(x_vals, sin_vals, label='sin(x)')
ax[1].plot(x_vals, cos_vals, label='cos(x)')

# 初始化动态点
point_circle, = ax[0].plot([], [], 'ro')  # 圆上的红点
point_sin, = ax[1].plot([], [], 'bo')  # sin曲线上的蓝点
point_cos, = ax[1].plot([], [], 'go')  # cos曲线上的绿点


def init():
    """初始化函数"""
    point_circle.set_data([], [])
    point_sin.set_data([], [])
    point_cos.set_data([], [])
    return point_circle, point_sin, point_cos,


def update(frame):
    """更新函数"""
    # 确保传递给set_data的是序列
    point_circle.set_data([np.cos(frame)], [np.sin(frame)])

    # 更新sin和cos曲线上点的位置
    point_sin.set_data([frame], [np.sin(frame)])
    point_cos.set_data([frame], [np.cos(frame)])

    return point_circle, point_sin, point_cos,


# 创建动画
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100),
                    init_func=init, blit=True)

plt.legend()
plt.show()
