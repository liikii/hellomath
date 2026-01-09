import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置参数
t = np.linspace(0, 10 * np.pi, 1000) # 时间参数

# 摆线（Cycloid）
x_cycloid = t - np.sin(t)
y_cycloid = 1 - np.cos(t)
z_cycloid = t

# 创建图形对象
fig = plt.figure(figsize=(7, 7))

# 绘制摆线
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_cycloid, y_cycloid, z_cycloid, label='Cycloid', color='blue')

# 设置坐标轴标签
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# 显示图例
ax.legend()

# 设置图表标题
ax.set_title('Cycloid in 3D Space')

# 调整布局并显示图表
plt.tight_layout()
plt.show()
