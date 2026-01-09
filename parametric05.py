import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. 定义参数v的范围（0到2π，覆盖三角函数完整周期）
v = np.linspace(0, 2 * np.pi, 200)  # 200个点让曲线更平滑

# 2. 计算三维坐标
x = 2 + np.sin(v)
y = 2 + np.sin(v)
z = np.cos(v)

# 3. 创建3D绘图环境
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 4. 绘制三维参数曲线
ax.plot(x, y, z, color='blue', linewidth=2, label=r'$x=2+\sin v,\ y=2+\sin v,\ z=\cos v$')

# 5. 标记关键特征点（方便理解曲线形态）
# v=0时：x=2, y=2, z=1
ax.scatter(2, 2, 1, color='red', s=80, label='v=0: (2,2,1)')
# v=π/2时：x=3, y=3, z=0
ax.scatter(3, 3, 0, color='green', s=80, label='v=π/2: (3,3,0)')
# v=π时：x=2, y=2, z=-1
ax.scatter(2, 2, -1, color='orange', s=80, label='v=π: (2,2,-1)')
# v=3π/2时：x=1, y=1, z=0
ax.scatter(1, 1, 0, color='purple', s=80, label='v=3π/2: (1,1,0)')

# 6. 样式与标签设置
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)
# ax.set_title('3D Parametric Curve: $x=2+\sin v,\ y=2+\sin v,\ z=\cos v  $', fontsize=14)
ax.set_title(r'3D Parametric Curve: $\mathbf{r}(u, v) = \langle (2 + \sin v)\cos u,\ (2 + \sin v)\sin u,\ u + \cos v \rangle$', fontsize=14)
# ax.set_title(
#     r'Parametric Surface: $\mathbf{r}(u,v) = \langle (2+\sin v)\cos u,\ (2+\sin v)\sin u,\ u+\cos v \rangle$',
#     fontsize=14,
#     pad=20  # 增加标题与图的间距，避免遮挡
# )
ax.legend(loc='upper right')
ax.grid(alpha=0.3)
# 等比例显示坐标轴，避免视觉变形
ax.set_box_aspect([1, 1, 1])

plt.show()
