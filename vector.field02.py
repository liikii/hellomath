import numpy as np
import matplotlib.pyplot as plt

# 设置图形大小和样式
plt.figure(figsize=(8, 8))

# 定义要画的点 (x, y)
inner_points = [
    (1, 0),   # 右侧
    (0, 1),   # 上方
    (-1, 0),  # 左侧
    (0, -1)   # 下方
]

outer_points = [
    (2, 0),   # 外圈右侧
    (0, 2),   # 外圈上方
    (-2, 0),  # 外圈左侧
    (0, -2),  # 外圈下方
    (np.sqrt(2), np.sqrt(2)),  # 第一象限对角线
    (-np.sqrt(2), np.sqrt(2)), # 第二象限
    (-np.sqrt(2), -np.sqrt(2)),# 第三象限
    (np.sqrt(2), -np.sqrt(2))  # 第四象限
]

# 绘制内圈向量
for (x, y) in inner_points:
    u = -y  # x 分量
    v = x   # y 分量
    plt.arrow(x, y, u, v, head_width=0.05, head_length=0.1,
              fc='blue', ec='blue', lw=2, alpha=0.9)

# 绘制外圈向量
for (x, y) in outer_points:
    u = -y  # x 分量
    v = x   # y 分量
    plt.arrow(x, y, u, v, head_width=0.1, head_length=0.2,
              fc='red', ec='red', lw=2, alpha=0.9)

# 添加坐标轴和原点
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.plot(0, 0, 'ko', markersize=5)  # 原点标记

# 添加辅助圆（可选）
circle_inner = plt.Circle((0, 0), 1, fill=False, linestyle='--', color='gray', alpha=0.6)
plt.gca().add_patch(circle_inner)
circle_outer = plt.Circle((0, 0), 2, fill=False, linestyle='--', color='gray', alpha=0.4)
plt.gca().add_patch(circle_outer)

# 设置图形属性
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.gca().set_aspect('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Vector Field with Inner and Outer Vectors $\mathbf{F}(x, y) = \langle -y,\ x \rangle$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()