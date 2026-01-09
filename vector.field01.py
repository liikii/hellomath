import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# 创建网格点
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

# 定义向量场 F(x, y) = <-y, x>
U = -Y   # x 分量
V = X    # y 分量

# 计算向量模长
vector_magnitude = np.sqrt(U**2 + V**2)

# 绘图
fig, ax = plt.subplots(figsize=(8, 8))
quiver = ax.quiver(X, Y, U, V, vector_magnitude, cmap='viridis', angles='xy', scale_units='xy', scale=1)

# 添加圆圈辅助线（可选）
circle = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--', alpha=0.6)
ax.add_patch(circle)
circle2 = plt.Circle((0, 0), 2, color='gray', fill=False, linestyle='--', alpha=0.4)
ax.add_patch(circle2)

# 设置图形属性
plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal')
plt.title(r'Vector Field $\mathbf{F}(x, y) = \langle -y,\ x \rangle$', fontsize=14)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True, linestyle='--', alpha=0.5)

# 添加颜色条
norm = Normalize()
sm = ScalarMappable(cmap='viridis', norm=norm)
sm.set_array(vector_magnitude)
plt.colorbar(sm, ax=ax, label="Vector Magnitude")

plt.show()
