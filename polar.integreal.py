import numpy as np
import matplotlib.pyplot as plt

# 设置参数
a, b = 0.5, 2.0         # r 的范围 [a, b]
alpha, beta = np.pi/6, np.pi/2  # θ 的范围 [α, β]

m = 8                   # r 方向分 m 份
n = 10                  # θ 方向分 n 份

# 计算步长
dr = (b - a) / m
dtheta = (beta - alpha) / n

# 生成 r 和 theta 的分割点
r_values = np.linspace(a, b, m + 1)
theta_values = np.linspace(alpha, beta, n + 1)

# 创建图形
fig, ax = plt.subplots(figsize=(8, 8))

# 设置坐标轴
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 设置范围
ax.set_xlim(0, b * 1.2)
ax.set_ylim(0, b * 1.2)

# 绘制同心圆弧（r = 常数）
for r in r_values:
    theta = np.linspace(alpha, beta, 100)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, 'orange', linewidth=1.2, alpha=0.7)

# 绘制射线（θ = 常数）
for theta in theta_values:
    r = np.linspace(a, b, 100)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, 'orange', linewidth=1.2, alpha=0.7)

# 添加标签
ax.text(0.3, 0.1, r'$\Delta r$', fontsize=12, ha='center', va='center', rotation=90)
ax.text(0.2, 0.4, r'$\Delta\theta$', fontsize=12, ha='center', va='center', rotation=0)

# 标注某一小块区域
i, j = 3, 5  # 选择第 i 个 r 和第 j 个 θ
r_star = (r_values[i] + r_values[i+1]) / 2
theta_star = (theta_values[j] + theta_values[j+1]) / 2
x_star = r_star * np.cos(theta_star)
y_star = r_star * np.sin(theta_star)

ax.plot(x_star, y_star, 'ro', markersize=4)
ax.annotate(r'$(r_i^*, \theta_j^*)$', (x_star, y_star), xytext=(10, 10), textcoords='offset points', fontsize=10)

# 标注一个小区域
ax.text(1.0, 0.8, r'$R_{ij}$', fontsize=12, ha='center', va='center')

# 添加原点
ax.plot(0, 0, 'ko', markersize=4)
ax.text(-0.1, -0.1, 'O', ha='right', va='top', fontsize=10)

# 网格和样式
ax.grid(True, alpha=0.3)
plt.axis('equal')  # 保持比例
plt.tight_layout()
plt.show()
