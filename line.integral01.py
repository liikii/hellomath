"""
以曲线 C 为底、高度为 f(x,y) 的“篱笆”或“窗帘”
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数范围
t = np.linspace(0, np.pi, 100)
x = np.cos(t)
y = np.sin(t)

# 定义函数 f(x,y)
f = 1 + np.sin(x + y)

# 构建“篱笆”的网格点（每个点对应一个垂直条）
# 我们用两个表面来表示“篱笆”：前侧和后侧（但这里只画一侧）
# 使用小步长创建矩形条
dt = t[1] - t[0]
N = len(t)

# 创建三维坐标
X = np.zeros((N, 2))
Y = np.zeros((N, 2))
Z = np.zeros((N, 2))

for i in range(N):
    X[i, :] = [x[i], x[i]]
    Y[i, :] = [y[i], y[i]]
    Z[i, :] = [0, f[i]]

# 绘图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 画出“篱笆”（多个垂直条）
for i in range(N):
    ax.plot(X[i], Y[i], Z[i], color='skyblue', linewidth=2, alpha=0.7)

# 画出底部曲线 C
ax.plot(x, y, np.zeros_like(x), 'r-', linewidth=2, label='Curve $C$')
ax.plot(x[0], y[0], 0, 'ro', markersize=6)
ax.plot(x[-1], y[-1], 0, 'ro', markersize=6)

# 标注
ax.text(x[0]+0.1, y[0]-0.1, 0, r'$\text{Start}$', fontsize=10)
ax.text(x[-1]-0.1, y[-1]+0.1, 0, r'$\text{End}$', fontsize=10)

# 添加标签
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title(r'Line Integral as Area of a "Fence" $\int_C f(x,y)\,ds$', fontsize=14)

# 设置视角
ax.view_init(elev=20, azim=45)

# 显示
plt.show()
