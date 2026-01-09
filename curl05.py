"""
这两个偏导数确实可以理解为“沿不同方向的剪切力”或“速度梯度”，它们共同决定了绕 x 轴的旋转趋势。
"""
import numpy as np
import matplotlib.pyplot as plt


# 定义向量场函数
def vector_field(y, z):
    Q = z        # y方向分量
    R = 0        # z方向分量
    return Q, R


# 给定的关键点
points = [
    (1,0), (0,1), (-1,0), (0,-1),
    (1,1), (1,-1), (-1,-1), (-1,1),
    (2,0), (0,2), (-2,0), (0,-2),
    (2,2), (2,-2), (-2,-2), (-2,2)
]

# 创建图形
plt.figure(figsize=(10, 10))

# 绘制每个点的向量
for y, z in points:
    Q, R = vector_field(y, z)
    plt.arrow(y, z, Q, R, head_width=0.2, head_length=0.3, fc='blue', ec='blue', alpha=0.8)

# 添加坐标轴和网格
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, alpha=0.3)

# 设置范围
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# 标签
plt.xlabel('y')
plt.ylabel('z')
plt.title('Vector Field $\\mathbf{F} = \\langle 0, z, 0 \\rangle$ on yz-plane\n(Only y-direction velocity depends on z)')
plt.axis('equal')  # 等比例显示

# 添加点标注（可选）
for i, (y, z) in enumerate(points):
    plt.annotate(f'({y},{z})', (y, z), xytext=(10, 10), textcoords='offset points',
                 fontsize=8, color='red')

plt.show()
