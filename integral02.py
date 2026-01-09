"""
If we choose a sample point (x_ij^*, y_ij^*) in each R_ij, then we can approximate the part of S that lies above each R_ij by a thin rectangular box (or “column”) with base R_ij and height f(x_ij^*, y_ij^*) as shown in Figure 4.

The volume of this box is the height of the box times the area of the base rectangle:

f(x_ij^*, y_ij^*) ΔA
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 设置中文字体支持（可选）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 参数设置
a, b = 1, 4  # x 范围
c, d = 1, 3  # y 范围
m = 5        # x 方向分割数
n = 4        # y 方向分割数

dx = (b - a) / m
dy = (d - c) / n

# 创建图形
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制坐标轴
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)

# 绘制外框矩形 R
rect_R = Rectangle((a, c), b-a, d-c, fill=False, edgecolor='orange', linewidth=2, label='Region $R$')
ax.add_patch(rect_R)

# 绘制网格线（虚线）
for i in range(1, m):
    ax.axvline(a + i * dx, color='black', linestyle='--', linewidth=0.8)
for j in range(1, n):
    ax.axhline(c + j * dy, color='black', linestyle='--', linewidth=0.8)

# 绘制子矩形边界（橙色实线）
for i in range(m):
    for j in range(n):
        rect = Rectangle((a + i*dx, c + j*dy), dx, dy, fill=False, edgecolor='orange', linewidth=1.5)
        ax.add_patch(rect)

# 添加点 (x_i^*, y_j^*)
# 示例：在每个子矩形的中心加一个点
for i in range(m):
    for j in range(n):
        x_star = a + (i + 0.5) * dx
        y_star = c + (j + 0.5) * dy
        ax.plot(x_star, y_star, 'k.', markersize=5)

# 标注 Δx 和 Δy
ax.annotate(r'$\Delta x$', xy=(a + 2*dx, c - 0.1), xytext=(a + 2*dx, c - 0.4),
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            ha='center', va='top', fontsize=12)

ax.annotate(r'$\Delta y$', xy=(a - 0.3, c + 1.5*dy), xytext=(a - 0.6, c + 1.5*dy),
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            ha='left', va='center', fontsize=12)

# 标注 R_ij
ax.annotate(r'$R_{ij}$', xy=(a + 2.5*dx, c + 2.5*dy), xytext=(a + 3*dx, c + 2.7*dy),
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            ha='left', va='bottom', fontsize=12)

# 标注关键点
ax.annotate(r'$(x_i^*, y_j^*)$', xy=(a + 2.5*dx, c + 2.5*dy), xytext=(a + 3.5*dx, c + 2.8*dy),
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            ha='left', va='bottom', fontsize=10)

ax.annotate(r'$(x_1^*, y_2^*)$', xy=(a + 0.5*dx, c + 1.5*dy), xytext=(a + 0.8*dx, c + 1.2*dy),
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            ha='left', va='top', fontsize=10)

ax.annotate(r'$(x_2^*, y_1^*)$', xy=(a + 1.5*dx, c + 0.5*dy), xytext=(a + 1.8*dx, c + 0.2*dy),
            arrowprops=dict(arrowstyle='->', color='black', lw=1),
            ha='left', va='top', fontsize=10)

# 标注坐标轴
ax.set_xlim(a - 0.5, b + 0.5)
ax.set_ylim(c - 0.5, d + 0.5)
ax.set_xlabel(r'$x$', fontsize=12)
ax.set_ylabel(r'$y$', fontsize=12)

# 标注 a, b, c, d
ax.text(a, c - 0.2, r'$a$', ha='center', va='top', fontsize=10)
ax.text(b, c - 0.2, r'$b$', ha='center', va='top', fontsize=10)
ax.text(a - 0.2, c, r'$c$', ha='right', va='center', fontsize=10)
ax.text(a - 0.2, d, r'$d$', ha='right', va='center', fontsize=10)

# 隐藏上边和右边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
