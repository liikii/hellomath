import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import proj3d  # 关键：补充proj3d导入
from matplotlib.patches import FancyArrowPatch


# ===================== 1. 自定义3D箭头类（修复proj3d引用） =====================
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        # 正确引用proj3d，修复NameError
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


# ===================== 2. 定义参数化曲面（抛物面示例） =====================
# 参数u, v范围
u = np.linspace(1, 2, 5)
v = np.linspace(1, 2, 5)
u_mesh, v_mesh = np.meshgrid(u, v)

# 曲面r(u,v) = (u, v, u² + v²)（模拟原曲面）
x_surf = u_mesh
y_surf = v_mesh
z_surf = u_mesh ** 2 + v_mesh ** 2

# 选择中心点P_ij（u=1.5, v=1.5）
u0, v0 = 1.5, 1.5
x0, y0, z0 = u0, v0, u0 ** 2 + v0 ** 2

# ===================== 3. 计算切向量（偏导数） =====================
# 偏导数r_u* = (1, 0, 2u)，r_v* = (0, 1, 2v)
ru = np.array([1, 0, 2 * u0])  # r_u*在(u0,v0)处的值
rv = np.array([0, 1, 2 * v0])  # r_v*在(u0,v0)处的值

# 切向量Δu r_u*和Δv r_v*（取Δu=Δv=0.3）
delta_u, delta_v = 0.3, 0.3
vec_ru = delta_u * ru
vec_rv = delta_v * rv

# 平行四边形的四个顶点（切平面内）
para_verts = [
    [x0, y0, z0],
    [x0 + vec_ru[0], y0 + vec_ru[1], z0 + vec_ru[2]],
    [x0 + vec_ru[0] + vec_rv[0], y0 + vec_ru[1] + vec_rv[1], z0 + vec_ru[2] + vec_rv[2]],
    [x0 + vec_rv[0], y0 + vec_rv[1], z0 + vec_rv[2]]
]

# 原曲面片S_ij的四个顶点（曲面上）
surf_patch_verts = [
    [x_surf[2, 2], y_surf[2, 2], z_surf[2, 2]],
    [x_surf[2, 3], y_surf[2, 3], z_surf[2, 3]],
    [x_surf[3, 3], y_surf[3, 3], z_surf[3, 3]],
    [x_surf[3, 2], y_surf[3, 2], z_surf[3, 2]]
]

# ===================== 4. 绘制图形 =====================
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# 绘制原曲面（浅灰色网格）
ax.plot_wireframe(x_surf, y_surf, z_surf, color='gray', alpha=0.5, linewidth=1)

# 绘制原曲面片S_ij（浅蓝色）
surf_patch = Poly3DCollection([surf_patch_verts], facecolors='lightblue', alpha=0.7, edgecolors='blue')
ax.add_collection3d(surf_patch)

# 绘制切平面内的平行四边形（浅绿色）
para_patch = Poly3DCollection([para_verts], facecolors='lightgreen', alpha=0.8, edgecolors='green')
ax.add_collection3d(para_patch)

# 绘制切向量Δu r_u*和Δv r_v*（粉色箭头）
arrow_ru = Arrow3D([x0, x0 + vec_ru[0]], [y0, y0 + vec_ru[1]], [z0, z0 + vec_ru[2]],
                   arrowstyle='->', color='pink', linewidth=2, mutation_scale=15)
arrow_rv = Arrow3D([x0, x0 + vec_rv[0]], [y0, y0 + vec_rv[1]], [z0, z0 + vec_rv[2]],
                   arrowstyle='->', color='pink', linewidth=2, mutation_scale=15)
ax.add_artist(arrow_ru)
ax.add_artist(arrow_rv)

# 标注向量
ax.text(x0 + vec_ru[0] / 2, y0 + vec_ru[1] / 2, z0 + vec_ru[2] / 2, r'$\Delta u \mathbf{r}_u^*$', fontsize=12,
        color='pink')
ax.text(x0 + vec_rv[0] / 2, y0 + vec_rv[1] / 2, z0 + vec_rv[2] / 2, r'$\Delta v \mathbf{r}_v^*$', fontsize=12,
        color='pink')

# 样式设置
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(r'(Tangent Plane)$\sum_{i=1}^{m} \sum_{j=1}^{n} \left| \mathbf{r}_u^* \times \mathbf{r}_v^* \right| \Delta u \Delta v$')
ax.view_init(elev=20, azim=45)  # 调整视角匹配原图
ax.set_xlim(1, 2)
ax.set_ylim(1, 2)
ax.set_zlim(2, 8)
plt.tight_layout()
plt.show()
