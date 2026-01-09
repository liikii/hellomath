import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x, y):
    return -x * y * np.exp(-x**2 - y**2)

# 创建网格数据
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 设置等值线的 k 值（从 -0.1 到 0.1，步长小）
k_values = np.linspace(-0.1, 0.1, 50)  # 越多越密

# 创建图形
plt.figure(figsize=(8, 8))

# 绘制等值线（level curves），颜色为粉红
CS = plt.contour(X, Y, Z, levels=k_values, colors='magenta', linewidths=0.8, alpha=0.9)

# 可选：添加填充（等高线区域着色）
# plt.contourf(X, Y, Z, levels=k_values, cmap='magma', alpha=0.3)

# 添加坐标轴
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# 设置标签和标题
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$y$', fontsize=12)
plt.title(r'Level curves of $f(x,y) = -xy e^{-x^2 - y^2}$', fontsize=14)

# 设置比例尺为1:1，居中显示
plt.axis('equal')
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# 隐藏刻度标签（保持简洁）
plt.xticks([])
plt.yticks([])

# 显示图形
plt.tight_layout()
plt.show()
