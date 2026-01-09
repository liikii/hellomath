import numpy as np
import matplotlib.pyplot as plt

# 设置参数
omega = 1.0  # 角频率，控制绕圈的速度
t = np.linspace(0, 4 * np.pi, 1000)  # 时间变量 t，取足够多的点以保证平滑

# 计算复指数函数 e^(i*omega*t)
z = np.exp(1j * omega * t)  # 1j 是 Python 中的虚数单位

# 分解实部和虚部
x = np.real(z)  # 实部，即 cos(omega*t)
y = np.imag(z)  # 虚部，即 sin(omega*t)

# 开始绘图
plt.figure(figsize=(8, 8))
plt.plot(x, y, linewidth=2, label=r'$e^{i\omega t}$')
plt.title("Complex Exponential Function on the Complex Plane", fontsize=14)
plt.xlabel("Real Part (Re)", fontsize=12)
plt.ylabel("Imaginary Part (Im)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axis('equal')  # 保证 x, y 轴比例相同，圆才不会变成椭圆

# 添加一些说明箭头
arrow_idx = 250  # 选择一个点来画箭头
plt.arrow(0, 0, x[arrow_idx], y[arrow_idx],
          head_width=0.05, head_length=0.1,
          fc='red', ec='red', label='Vector at a specific t')
plt.legend()
plt.show()
