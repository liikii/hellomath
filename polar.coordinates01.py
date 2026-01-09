import matplotlib.pyplot as plt
import numpy as np

# 方法1：创建极坐标子图
fig = plt.figure(figsize=(10, 8))

# 标准极坐标图
ax1 = fig.add_subplot(221, projection='polar')
theta = np.linspace(0, 2*np.pi, 200)
r = 2 + np.sin(5*theta)
ax1.plot(theta, r)
ax1.set_title('polar coordinates', pad=20)
ax1.grid(True)

# 极坐标散点图
ax2 = fig.add_subplot(222, projection='polar')
theta = np.random.rand(50) * 2*np.pi
r = np.random.rand(50) * 3
ax2.scatter(theta, r, c=r, cmap='hsv', alpha=0.75)
ax2.set_title('polar scatter', pad=20)

# 极坐标填充图
ax3 = fig.add_subplot(223, projection='polar')
theta = np.linspace(0, 2*np.pi, 100)
r = 1 + 0.5*np.sin(7*theta)
ax3.fill(theta, r, alpha=0.5, color='orange')
ax3.set_title('polar fill', pad=20)

# 极坐标条形图（雷达图）
ax4 = fig.add_subplot(224, projection='polar')
categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
values = [7, 5, 8, 6, 9, 4, 7, 6]
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
angles = np.concatenate((angles, [angles[0]]))  # 闭合
values = np.concatenate((values, [values[0]]))
ax4.plot(angles, values, 'o-', linewidth=2)
ax4.fill(angles, values, alpha=0.25)
ax4.set_xticks(angles[:-1])
ax4.set_xticklabels(categories)
ax4.set_title('polar radia', pad=20)

plt.tight_layout()
plt.show()