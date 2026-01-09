import matplotlib.pyplot as plt
import numpy as np

# 设置参数
t = np.linspace(0, 10, 1000)  # 时间变量

# 创建子图
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Complex Exponential: $z^t$ where $z = r \\cdot e^{i\\theta}$', fontsize=16)

# 案例1: 纯旋转 (r=1, θ=π/4)
r, theta = 1.0, np.pi/4
z = r * np.exp(1j * theta)
z_t = z ** t
x1, y1 = np.real(z_t), np.imag(z_t)
axes[0,0].plot(x1, y1, 'b-', linewidth=2)
axes[0,0].plot(x1[0], y1[0], 'go', markersize=8, label='Start')
axes[0,0].plot(x1[-1], y1[-1], 'ro', markersize=8, label='End')
axes[0,0].set_title(f'Pure Rotation\n$r={r}$, $\\theta={theta:.2f}$')
axes[0,0].set_xlabel('Real')
axes[0,0].set_ylabel('Imaginary')
axes[0,0].grid(True)
axes[0,0].legend()
axes[0,0].axis('equal')

# 案例2: 发散螺旋 (r=1.1, θ=π/4)
r, theta = 1.1, np.pi/4
z = r * np.exp(1j * theta)
z_t = z ** t
x2, y2 = np.real(z_t), np.imag(z_t)
axes[0,1].plot(x2, y2, 'r-', linewidth=2)
axes[0,1].plot(x2[0], y2[0], 'go', markersize=8, label='Start')
axes[0,1].plot(x2[-1], y2[-1], 'ro', markersize=8, label='End')
axes[0,1].set_title(f'Diverging Spiral\n$r={r}$, $\\theta={theta:.2f}$')
axes[0,1].set_xlabel('Real')
axes[0,1].set_ylabel('Imaginary')
axes[0,1].grid(True)
axes[0,1].legend()
axes[0,1].axis('equal')

# 案例3: 收敛螺旋 (r=0.9, θ=π/4)
r, theta = 0.9, np.pi/4
z = r * np.exp(1j * theta)
z_t = z ** t
x3, y3 = np.real(z_t), np.imag(z_t)
axes[0,2].plot(x3, y3, 'g-', linewidth=2)
axes[0,2].plot(x3[0], y3[0], 'go', markersize=8, label='Start')
axes[0,2].plot(x3[-1], y3[-1], 'ro', markersize=8, label='End')
axes[0,2].set_title(f'Converging Spiral\n$r={r}$, $\\theta={theta:.2f}$')
axes[0,1].set_xlabel('Real')
axes[0,1].set_ylabel('Imaginary')
axes[0,2].grid(True)
axes[0,2].legend()
axes[0,2].axis('equal')

# 案例4: 快速旋转 (r=1, θ=π)
r, theta = 1.0, np.pi
z = r * np.exp(1j * theta)
z_t = z ** t
x4, y4 = np.real(z_t), np.imag(z_t)
axes[1,0].plot(x4, y4, 'purple', linewidth=2)
axes[1,0].plot(x4[0], y4[0], 'go', markersize=8, label='Start')
axes[1,0].plot(x4[-1], y4[-1], 'ro', markersize=8, label='End')
axes[1,0].set_title(f'Fast Rotation\n$r={r}$, $\\theta={theta:.2f}$')
axes[1,0].set_xlabel('Real')
axes[1,0].set_ylabel('Imaginary')
axes[1,0].grid(True)
axes[1,0].legend()
axes[1,0].axis('equal')

# 案例5: 慢速发散 (r=1.05, θ=π/8)
r, theta = 1.05, np.pi/8
z = r * np.exp(1j * theta)
z_t = z ** t
x5, y5 = np.real(z_t), np.imag(z_t)
axes[1,1].plot(x5, y5, 'orange', linewidth=2)
axes[1,1].plot(x5[0], y5[0], 'go', markersize=8, label='Start')
axes[1,1].plot(x5[-1], y5[-1], 'ro', markersize=8, label='End')
axes[1,1].set_title(f'Slow Divergence\n$r={r}$, $\\theta={theta:.2f}$')
axes[1,1].set_xlabel('Real')
axes[1,1].set_ylabel('Imaginary')
axes[1,1].grid(True)
axes[1,1].legend()
axes[1,1].axis('equal')

# 案例6: 负角度旋转 (r=1, θ=-π/4)
r, theta = 1.0, -np.pi/4
z = r * np.exp(1j * theta)
z_t = z ** t
x6, y6 = np.real(z_t), np.imag(z_t)
axes[1,2].plot(x6, y6, 'brown', linewidth=2)
axes[1,2].plot(x6[0], y6[0], 'go', markersize=8, label='Start')
axes[1,2].plot(x6[-1], y6[-1], 'ro', markersize=8, label='End')
axes[1,2].set_title(f'Clockwise Rotation\n$r={r}$, $\\theta={theta:.2f}$')
axes[1,2].set_xlabel('Real')
axes[1,2].set_ylabel('Imaginary')
axes[1,2].grid(True)
axes[1,2].legend()
axes[1,2].axis('equal')

plt.tight_layout()
plt.show()
