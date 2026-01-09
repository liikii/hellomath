import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数设置
a = 1.0  # 抛物面参数：z = (x^2 + y^2) / (4f)，这里设 f = a => z = (x^2 + y^2)/(4a)
f = a  # 焦点在 (0, 0, f)

# 创建抛物面网格
theta = np.linspace(0, 2 * np.pi, 30)
r = np.linspace(0, 2, 20)
R, Theta = np.meshgrid(r, theta)
X = R * np.cos(Theta)
Y = R * np.sin(Theta)
Z = (X ** 2 + Y ** 2) / (4 * f)  # 标准抛物面：焦点在 (0,0,f)

# 设置入射光线（平行于 z 轴，从上方射下）
num_rays = 6
ray_r = np.linspace(0.5, 1.8, num_rays)
incident_rays = []
reflected_rays = []

for r_val in ray_r:
    # 入射光线：从 (r, 0, z_top) 到 抛物面上的点 (r, 0, z_surface)
    x0, y0 = r_val, 0
    z_surface = (x0 ** 2 + y0 ** 2) / (4 * f)
    z_top = z_surface + 2  # 光线起点在曲面上方

    # 入射方向向量（向下）
    incident_dir = np.array([0, 0, -1])

    # 抛物面上该点的法向量（梯度）
    # F(x,y,z) = z - (x^2 + y^2)/(4f) = 0
    # ∇F = (-x/(2f), -y/(2f), 1)
    normal = np.array([-x0 / (2 * f), -y0 / (2 * f), 1])
    normal = normal / np.linalg.norm(normal)  # 单位化

    # 反射公式：r = d - 2(d·n)n
    d = incident_dir
    n = normal
    reflected_dir = d - 2 * np.dot(d, n) * n
    reflected_dir = reflected_dir / np.linalg.norm(reflected_dir)  # 单位化

    # 延长反射光线（从交点出发，沿反射方向）
    t = np.linspace(0, 3, 50)
    refl_x = x0 + reflected_dir[0] * t
    refl_y = y0 + reflected_dir[1] * t
    refl_z = z_surface + reflected_dir[2] * t

    # 存储光线
    incident_rays.append(([x0, x0], [y0, y0], [z_top, z_surface]))
    reflected_rays.append((refl_x, refl_y, refl_z))

# 绘图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 画抛物面
ax.plot_surface(X, Y, Z, alpha=0.2, color='lightblue', linewidth=0)

# 画入射光线（红色）
for x, y, z in incident_rays:
    ax.plot(x, y, z, 'r-', linewidth=1.5)

# 画反射光线（绿色）
for x, y, z in reflected_rays:
    ax.plot(x, y, z, 'g--', linewidth=1.5)

# 画焦点
ax.scatter([0], [0], [f], color='black', s=50, label=f'Focus (0,0,{f})')

# 设置视角和标签
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(0, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Paraboloid Reflecting Parallel Rays to Focus')
ax.legend()
ax.view_init(elev=20, azim=-60)  # 调整视角

plt.tight_layout()
plt.show()
