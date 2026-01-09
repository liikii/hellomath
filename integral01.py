import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 设置中文字体支持（可选）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 参数设置
a, b = 0, 2 * np.pi
n = 8  # 分割数
x = np.linspace(a, b, n + 1)
dx = (b - a) / n

# 函数定义：f(x) = sin(x) + 1（确保非负）
def f(x):
    return np.sin(x) + 1

# 计算每个区间的左端点、右端点、中点（用于取高）
x_left = x[:-1]
x_right = x[1:]
x_star = (x_left + x_right) / 2  # 中点采样
y_star = f(x_star)

# 创建图形
fig, ax = plt.subplots(figsize=(10, 5))

# 绘制函数曲线
x_smooth = np.linspace(a, b, 300)
ax.plot(x_smooth, f(x_smooth), 'b-', linewidth=2, label=r'$f(x)$')

# 绘制矩形（蓝色填充）
for i in range(n):
    rect = Rectangle((x[i], 0), dx, y_star[i], facecolor='lightblue', edgecolor='black', alpha=0.7)
    ax.add_patch(rect)

# 添加虚线（从矩形顶部到 x 轴）
for i in range(n):
    ax.plot([x_star[i], x_star[i]], [0, y_star[i]], 'k--', linewidth=0.8)

# 添加坐标轴和标签
ax.set_xlim(a - 0.1, b + 0.1)
ax.set_ylim(0, 2.5)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)

ax.set_xlabel(r'$x$', fontsize=12)
ax.set_ylabel(r'$y$', fontsize=12)
ax.grid(True, alpha=0.3)

# 添加箭头和标注
# Δx 标注
ax.annotate(r'$\Delta x$', xy=(x[4] + dx/2, 1.8), xytext=(x[4] + dx/2, 2.2),
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            ha='center', va='bottom', fontsize=12)

# f(x_i*) 标注
ax.annotate(r'$f(x_i^*)$', xy=(x[4] + dx/2, y_star[4]), xytext=(x[4] + dx/2, 1.6),
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            ha='center', va='top', fontsize=12)

# 标注 x_i 和 x_i*
for i in range(n):
    ax.text(x[i], -0.1, r'$x_{}$'.format(i), ha='center', va='top', fontsize=10)
    ax.text(x_star[i], -0.2, r'$x_{}^*$'.format(i+1), ha='center', va='top', fontsize=10)

# 标注 a 和 b
ax.text(a, -0.1, r'$a$', ha='center', va='top', fontsize=10)
ax.text(b, -0.1, r'$b$', ha='center', va='top', fontsize=10)

# 标注原点 O
ax.text(-0.1, 0.1, 'O', ha='right', va='bottom', fontsize=10)

# 隐藏上边和右边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
