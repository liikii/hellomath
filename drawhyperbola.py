import numpy as np
import matplotlib.pyplot as plt

# 设置图形大小
plt.figure(figsize=(8, 8))

# 定义 k 的几个值
k_vals = [-4, -1, 0, 1, 4]
colors = ['purple', 'blue', 'red', 'green', 'orange']

# 生成 x 值
x = np.linspace(-5, 5, 400)

# 逐个 k 画图
for k, color in zip(k_vals, colors):
    if k > 0:
        # y^2 - x^2 = k => y = ±sqrt(x^2 + k)
        # 但这样画会出现不连续，直接用隐函数方式不方便，这里分两支画
        y_upper = np.sqrt(x**2 + k)
        y_lower = -np.sqrt(x**2 + k)
        plt.plot(x, y_upper, color=color, label=f'k = {k}')
        plt.plot(x, y_lower, color=color, linestyle='--')
    elif k < 0:
        # y^2 - x^2 = k => x^2 = y^2 - k，所以 x = ±sqrt(y^2 - k)
        y = np.linspace(-5, 5, 400)
        x_right = np.sqrt(y**2 - k)
        x_left = -np.sqrt(y**2 - k)
        plt.plot(x_right, y, color=color, label=f'k = {k}')
        plt.plot(x_left, y, color=color, linestyle='--')
    else:  # k = 0
        # y^2 - x^2 = 0 => y = x 或 y = -x
        plt.plot(x, x, color=color, label=f'k = {k}')
        plt.plot(x, -x, color=color, linestyle='--')

# 设置坐标轴范围
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# 添加网格、标签、标题
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y^2 - x^2 = k$ for different k')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')

# 显示图形
plt.show()
