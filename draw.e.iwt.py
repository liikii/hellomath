import numpy as np
import matplotlib.pyplot as plt

# 设置参数
omega = 1.0
t = np.linspace(0, 4 * np.pi, 1000)

# 计算复指数函数
z = np.exp(1j * omega * t)
x = np.real(z)
y = np.imag(z)

# 创建 3D 图像
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制 3D 曲线：x(t), y(t), t
ax.plot(x, y, t, linewidth=2, label=r'$e^{i\omega t}$')

# 在曲线上标记一些点，并画出到复平面的投影
for time_point in [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]:
    idx = np.argmin(np.abs(t - time_point))
    ax.scatter(x[idx], y[idx], t[idx], color='red', s=50)
    # 画垂直线到复平面
    ax.plot([x[idx], x[idx]], [y[idx], y[idx]], [0, t[idx]],
            'r--', alpha=0.5)

ax.set_xlabel('Real Part')
ax.set_ylabel('Imaginary Part')
ax.set_zlabel('Time (t)')
ax.set_title('3D Visualization of $e^{i\omega t}$', fontsize=14)
ax.legend()
plt.show()
