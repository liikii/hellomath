import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建图形和3D坐标轴
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')

# 参数范围
t = np.linspace(0, 4 * np.pi, 1000)  # 螺旋线绕两圈

# 第一个螺旋线：r1(t) = (cos t, sin t, t)
x1 = np.cos(t)
y1 = np.sin(t)
z1 = t  # Z轴位置随参数变化

# 第二个螺旋线：与第一个螺旋线在X、Y轴上相同，在Z轴上有固定偏移
offset_z = 2.0  # Z轴上的偏移量，可根据需要调整
x2 = x1  # X轴坐标相同
y2 = y1  # Y轴坐标相同
z2 = z1 + offset_z  # 在Z轴上增加一个固定的偏移值

# 绘制两条螺旋线，分别指定不同颜色
ax.plot(x1, y1, z1, 'b-', linewidth=1.5, label='Helix 1')  # 蓝色代表第一条螺旋线
ax.plot(x2, y2, z2, 'r-', linewidth=1.5, label='Helix 2')  # 红色代表第二条螺旋线

# 设置坐标轴标签
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# 设置图表标题
plt.title('Parallel Helixes with Fixed Offset in Z Axis')

# 添加图例
ax.legend()

# 显示图表
plt.show()
