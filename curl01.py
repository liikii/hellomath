"""
F=⟨0,z,−y⟩
它在 yz 平面上产生顺时针环流（从正 x 方向看）
"""
import numpy as np
import matplotlib.pyplot as plt

# 定义向量场函数
def vector_field(y, z):
    Q = z        # y方向分量
    R = -y       # z方向分量
    return Q, R

# 要绘制的关键点
points = [
    (1, 0), (0, 1), (-1, 0), (0, -1),
    (1, 1), (1, -1), (-1, -1), (-1, 1)
]

# 创建图形
plt.figure(figsize=(8, 8))

# 绘制每个点的向量
for y, z in points:
    Q, R = vector_field(y, z)
    plt.arrow(y, z, Q, R, head_width=0.15, head_length=0.2, fc='blue', ec='blue', alpha=0.7)

# 添加坐标轴和标签
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, alpha=0.3)

# 设置坐标轴范围
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# 标签
plt.xlabel('y')
plt.ylabel('z')
plt.title('Vector Field $\\mathbf{F} = \\langle 0, z, -y \\rangle$ on yz-plane')

# 添加点的标注
for i, (y, z) in enumerate(points):
    plt.annotate(f'({y},{z})', (y, z), xytext=(10, 10), textcoords='offset points',
                 fontsize=9, color='red')

plt.axis('equal')  # 等比例显示
plt.show()
