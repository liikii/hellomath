import numpy as np
import matplotlib.pyplot as plt


# 设置一个一般的复指数 (a + bi)，其中 a != 0
a = -0.1  # 实部，控制增长/衰减
b = 1.0   # 虚部，控制振荡

t = np.linspace(0, 10 * np.pi, 1000)
z = np.exp((a + 1j * b) * t)  # e^{(a+bi)t}
x = np.real(z)
y = np.imag(z)

plt.figure(figsize=(8, 8))
plt.plot(x, y, linewidth=1.5)
plt.title(f"Complex Exponential:", fontsize=14)
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.grid(True, linestyle='--', alpha=0.7)
plt.axis('equal')
plt.show()