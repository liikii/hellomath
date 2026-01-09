import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. 创建画布和3D坐标系
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])  # 等比例显示

# 2. 定义柱坐标参数（示例值：r=2, dθ=π/6, dr=0.5, dz=1）
r = 2
dθ = np.pi / 6
dr = 0.5
dz = 1
θ = np.pi / 4  # 初始角度（方便可视化）

# 3. 计算直角坐标下的点（体积元素的四个底面顶点）
# 底面内圈点 (r, θ) 和 (r, θ+dθ)
x1 = r * np.cos(θ)
y1 = r * np.sin(θ)
x2 = r * np.cos(θ + dθ)
y2 = r * np.sin(θ + dθ)
# 底面外圈点 (r+dr, θ) 和 (r+dr, θ+dθ)
x3 = (r + dr) * np.cos(θ)
y3 = (r + dr) * np.sin(θ)
x4 = (r + dr) * np.cos(θ + dθ)
y4 = (r + dr) * np.sin(θ + dθ)
# 顶面点（z=dz）
z_top = dz
x1_top, y1_top = x1, y1
x2_top, y2_top = x2, y2
x3_top, y3_top = x3, y3
x4_top, y4_top = x4, y4


# 4. 绘制体积元素（蓝色半透明柱体）
# 底面（z=0）
bottom_verts = [[x1, y1, 0], [x2, y2, 0], [x4, y4, 0], [x3, y3, 0]]
# 顶面（z=dz）
top_verts = [[x1_top, y1_top, z_top], [x2_top, y2_top, z_top], [x4_top, y4_top, z_top], [x3_top, y3_top, z_top]]
# 侧面（连接底面和顶面）
for i in range(4):
    ax.plot3D([bottom_verts[i][0], top_verts[i][0]],
              [bottom_verts[i][1], top_verts[i][1]],
              [bottom_verts[i][2], top_verts[i][2]], 'b-', alpha=0.8)
# 填充顶面/底面（半透明）
ax.plot3D([x for x, y, z in bottom_verts + [bottom_verts[0]]],
          [y for x, y, z in bottom_verts + [bottom_verts[0]]],
          [z for x, y, z in bottom_verts + [bottom_verts[0]]], 'b-', alpha=0.2)
ax.plot3D([x for x, y, z in top_verts + [top_verts[0]]],
          [y for x, y, z in top_verts + [top_verts[0]]],
          [z for x, y, z in top_verts + [top_verts[0]]], 'b-', alpha=0.2)


# 5. 标注 dr, r dθ, dz
# 标注 dr（径向线段）
ax.plot3D([r*np.cos(θ), (r+dr)*np.cos(θ)],
          [r*np.sin(θ), (r+dr)*np.sin(θ)],
          [0, 0], 'r-', lw=2)
ax.text((r + dr/2)*np.cos(θ), (r + dr/2)*np.sin(θ), 0, '$dr$', fontsize=12, color='r')

# 标注 r dθ（弧线段，用近似直线代替）
ax.plot3D([r*np.cos(θ), r*np.cos(θ+dθ)],
          [r*np.sin(θ), r*np.sin(θ+dθ)],
          [0, 0], 'g-', lw=2)
ax.text(r*np.cos(θ + dθ/2), r*np.sin(θ + dθ/2), 0, '$r d\\theta$', fontsize=12, color='g')

# 标注 dz（高度线段）
ax.plot3D([x1, x1], [y1, y1], [0, dz], 'm-', lw=2)
ax.text(x1, y1, dz/2, '$dz$', fontsize=12, color='m')

# 标注 r（从原点到内圈的线段）
ax.plot3D([0, r*np.cos(θ)], [0, r*np.sin(θ)], [0, 0], 'k--', lw=1)
ax.text(r*np.cos(θ)/2, r*np.sin(θ)/2, 0, '$r$', fontsize=12, color='k')


# 6. 设置坐标轴和标题
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Volume element in cylindrical coordinates: $dV = r\\ dz\\ dr\\ d\\theta$')
plt.show()
