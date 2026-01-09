import numpy as np
import matplotlib.pyplot as plt

# 定义函数 f(x, y)
def f(x, y):
    return x**2 + y**2

# 创建 x 和 y 的网格点
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)

# 计算每个网格点上的 z 值
Z = f(X, Y)

# 选择一个点 P = (1, 1)，计算梯度
x0, y0 = 1.0, 1.0
grad_f_x = 2 * x0  # ∂f/∂x = 2x
grad_f_y = 2 * y0  # ∂f/∂y = 2y
grad_vector = [grad_f_x, grad_f_y]

# 绘制等高线图
plt.figure(figsize=(8, 8))
contours = plt.contour(X, Y, Z, levels=[0.5, 1, 2, 4, 9], colors='blue', alpha=0.7, linewidths=1.5)
plt.clabel(contours, inline=True, fontsize=10, fmt='%.1f')

# 标记点 P
plt.scatter(x0, y0, color='red', s=100, label=f'Point $P = ({x0}, {y0})$')

# 画梯度向量（从点 P 出发）
plt.quiver(x0, y0, grad_f_x, grad_f_y, color='red', scale=10, angles='xy', scale_units='xy',
           label=f'$\nabla f = ({grad_f_x}, {grad_f_y})$')

# 添加箭头标签
plt.annotate('', xy=(x0 + grad_f_x*0.2, y0 + grad_f_y*0.2), xytext=(x0, y0),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             ha='center', va='center')

# 设置标题和坐标轴
plt.title('Level Curves and Gradient Vector\n($f(x,y) = x^2 + y^2$)', fontsize=14)
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$y$', fontsize=12)
plt.grid(True, alpha=0.3)
plt.axis('equal')  # 保证比例一致，不拉伸

# 图例
plt.legend()

# 显示图像
plt.tight_layout()
plt.show()