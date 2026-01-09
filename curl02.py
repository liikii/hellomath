import numpy as np
import matplotlib.pyplot as plt

# 定义新的向量场
def vector_field(y, z):
    Q = -z        # y方向分量
    R = y         # z方向分量
    return Q, R

# 关键点
points = [
    (1, 0), (0, 1), (-1, 0), (0, -1),
    (1, 1), (1, -1), (-1, -1), (-1, 1)
]

# 创建图形
plt.figure(figsize=(8, 8))

# 绘制每个点的向量
for y, z in points:
    Q, R = vector_field(y, z)
    plt.arrow(y, z, Q, R, head_width=0.15, head_length=0.2, fc='green', ec='green', alpha=0.7)

# 坐标轴
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, alpha=0.3)

# 设置范围
plt.xlim(-2, 2)
plt.ylim(-2, 2)

# 标签
plt.xlabel('y')
plt.ylabel('z')
plt.title('Vector Field $\\mathbf{F} = \\langle 0, -z, y \\rangle$ on yz-plane\n(Rotating counterclockwise around +x axis)')
plt.axis('equal')

# 添加点标注
for i, (y, z) in enumerate(points):
    plt.annotate(f'({y},{z})', (y, z), xytext=(10, 10), textcoords='offset points',
                 fontsize=9, color='red')

plt.show()
