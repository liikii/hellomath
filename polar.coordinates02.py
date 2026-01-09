import numpy as np
import matplotlib.pyplot as plt

# 创建图形
fig, ax = plt.subplots(figsize=(6, 5))

# 设置坐标轴
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 设置范围
ax.set_xlim(-1.2, 3.5)
ax.set_ylim(-1.2, 2.5)

# 标注坐标轴
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)

# 添加原点标注
ax.text(-0.1, -0.1, 'O', ha='right', va='top', fontsize=10)

# 设定一个点 P(x,y)，比如 (2, 1.5)
x = 2.0
y = 1.5
r = np.sqrt(x**2 + y**2)  # 极径
theta = np.arctan2(y, x)  # 极角（弧度）

# 绘制从原点到 P 的向量
ax.plot([0, x], [0, y], 'b-', linewidth=2, label=r'$r$')

# 绘制垂线（形成直角三角形）
ax.plot([x, x], [0, y], 'k-', alpha=0.7)
ax.plot([0, x], [y, y], 'k-', alpha=0.7)

# 添加直角符号
ax.plot([x-0.1, x], [y-0.1, y-0.1], 'k-', linewidth=1)
ax.plot([x, x], [y-0.1, y], 'k-', linewidth=1)

# 标注各部分
ax.text(0.8, 0.2, r'$\theta$', fontsize=14, color='red')
ax.text(x/2, -0.1, r'$x$', fontsize=12, ha='center')
ax.text(x+0.1, y/2, r'$y$', fontsize=12, va='center')
ax.text(x/2, y/2, r'$r$', fontsize=12, color='blue', ha='center', va='center')

# 标注点 P
ax.plot(x, y, 'ko', markersize=5)
ax.text(x+0.1, y+0.1, r'$P(r,\theta)=P(x,y)$', fontsize=12)

# 添加箭头表示角度 θ
arrow_theta = np.linspace(0, theta, 10)
x_arrow = 0.8 * np.cos(arrow_theta)
y_arrow = 0.8 * np.sin(arrow_theta)
ax.plot(x_arrow, y_arrow, 'r-', linewidth=1.5, alpha=0.8)
ax.plot(x_arrow[-1], y_arrow[-1], 'ro', markersize=3)

# 网格和样式
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
