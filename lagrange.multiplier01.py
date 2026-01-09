"""
那这只是找   约束曲线上的极点， 还是找约束曲线内的极点?
这是个非常关键的区别！拉格朗日乘数法
∇f=λ∇g
∇f=λ∇g 只找约束曲线上的极值点。

情况一：不在极值点想象你在爬山（f 是高度），但被限制在一条小路（g=0）上行走。如果你还能沿着小路向上或向下走，说明你不在极值点。
        此时，小路的方向（切向）与 f 的梯度方向 不垂直。
情况二：在极值点在极值点，沿着小路走一小步，高度一阶不变。这意味着小路的方向与 f 的等高线方向一致。因此，f 的梯度 ∇f 垂直于小路方向。
    同时，g 的梯度 ∇g 也垂直于小路方向（因为 g 沿小路恒为 0）。
结论：∇f 与 ∇g 平行，即：∇f=λ∇g
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# 目标函数和梯度
def grad_f():
    # f(x, y) = x + y → ∇f = (1, 1)
    return np.array([1.0, 1.0])


def grad_g(x, y):
    # g(x, y) = x^2 + y^2 → ∇g = (2x, 2y)
    return np.array([2 * x, 2 * y])


# 创建图形
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)
ax.set_title(r'Gradient Vectors on Constraint $x^2 + y^2 = 1$', fontsize=14)

# 画单位圆
theta_full = np.linspace(0, 2 * np.pi, 300)
circle_x, circle_y = np.cos(theta_full), np.sin(theta_full)
ax.plot(circle_x, circle_y, 'k-', linewidth=1.5, label=r'$g(x,y)=1$')

# 初始化向量（用 quiver）
point, = ax.plot([], [], 'ro', markersize=8)
vec_f = ax.quiver(0, 0, 0, 0, color='red', scale=5, width=0.005, label=r'$\nabla f = (1,1)$')
vec_g = ax.quiver(0, 0, 0, 0, color='blue', scale=5, width=0.005, label=r'$\nabla g = (2x,2y)$')

# 极值点（最大值处）
max_point = (np.sqrt(2) / 2, np.sqrt(2) / 2)
min_point = (-np.sqrt(2) / 2, -np.sqrt(2) / 2)
ax.plot(*max_point, 'go', markersize=10, label='Max (parallel)')
ax.plot(*min_point, 'mo', markersize=10, label='Min (anti-parallel)')

ax.legend(loc='upper right')


# 动画更新函数
def animate(frame):
    t = frame * 0.05  # angle
    x = np.cos(t)
    y = np.sin(t)

    # 更新点位置
    point.set_data([x], [y])

    # ∇f 是常向量
    gf = grad_f()
    # ∇g 在 (x,y) 处
    gg = grad_g(x, y)

    # 更新向量：从 (x,y) 出发
    vec_f.set_offsets([x, y])
    vec_f.set_UVC(gf[0], gf[1])

    vec_g.set_offsets([x, y])
    vec_g.set_UVC(gg[0], gg[1])

    return point, vec_f, vec_g


# 创建动画
anim = FuncAnimation(fig, animate, frames=250, interval=50, blit=True)

plt.tight_layout()
plt.show()
