import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# ===================== 自定义3D箭头类（实现坐标轴箭头） =====================
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

# 球半径
a = 1
# 坐标轴长度（略大于球半径，保证箭头在球面外）
axis_len = 1.5
# 箭头样式配置
arrow_prop = dict(arrowstyle='->', linewidth=2, color='black', mutation_scale=15)

# 创建图形（调整hspace和top，为总标题预留空间）
fig = plt.figure(figsize=(12, 6))  # 高度从5调整为6，预留标题空间
fig.suptitle(r'$\mathbf{r}(\phi, \theta) = a \sin\phi \cos\theta\,\mathbf{i} + a \sin\phi \sin\theta\,\mathbf{j} + a \cos\phi\,\mathbf{k}$',
             fontsize=16, fontweight='bold', y=0.98)  # 全局总标题

# ========================
# 左图：不同 phi 的固定
# ========================
ax1 = fig.add_subplot(121, projection='3d')

# 绘制背景球面
phi_mesh = np.linspace(0, np.pi, 30)
theta_mesh = np.linspace(0, 2 * np.pi, 30)
phi_m, theta_m = np.meshgrid(phi_mesh, theta_mesh)
x_s = a * np.sin(phi_m) * np.cos(theta_m)
y_s = a * np.sin(phi_m) * np.sin(theta_m)
z_s = a * np.cos(phi_m)
ax1.plot_surface(x_s, y_s, z_s, color='lightblue', alpha=0.2, linewidth=0)

# 固定 phi 并画线
phis = [np.pi / 6, np.pi / 4, np.pi / 3]  # 添加更多phi值
for phi_fixed in phis:
    theta = np.linspace(0, 2 * np.pi, 100)
    x1 = a * np.sin(phi_fixed) * np.cos(theta)
    y1 = a * np.sin(phi_fixed) * np.sin(theta)
    z1 = a * np.cos(phi_fixed) * np.ones_like(theta)
    ax1.plot(x1, y1, z1, label=f'φ = {phi_fixed:.2f} rad')

# 左图添加带箭头的坐标轴
arrow_x1 = Arrow3D([-axis_len, axis_len], [0, 0], [0, 0], **arrow_prop)
ax1.add_artist(arrow_x1)
ax1.text(axis_len + 0.1, 0, 0, 'x', fontsize=12, weight='bold', color='black')
arrow_y1 = Arrow3D([0, 0], [-axis_len, axis_len], [0, 0], **arrow_prop)
ax1.add_artist(arrow_y1)
ax1.text(0, axis_len + 0.1, 0, 'y', fontsize=12, weight='bold', color='black')
arrow_z1 = Arrow3D([0, 0], [0, 0], [-axis_len, axis_len], **arrow_prop)
ax1.add_artist(arrow_z1)
ax1.text(0, 0, axis_len + 0.1, 'z', fontsize=12, weight='bold', color='black')
# 标记原点
ax1.scatter(0, 0, 0, color='black', s=50)

# 左图样式设置
ax1.set_title('Fixed φ (Multiple Latitude Circles)', y=1.0)  # 微调子图标题位置
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_xlim(-axis_len, axis_len)
ax1.set_ylim(-axis_len, axis_len)
ax1.set_zlim(-axis_len, axis_len)
ax1.legend()

# ========================
# 右图：不同 theta 的固定
# ========================
ax2 = fig.add_subplot(122, projection='3d')

# 绘制背景球面
ax2.plot_surface(x_s, y_s, z_s, color='lightblue', alpha=0.2, linewidth=0)

# 固定 theta 并画线
thetas = [np.pi / 8, np.pi / 4, 3 * np.pi / 8]  # 添加更多theta值
for theta_fixed in thetas:
    phi = np.linspace(0, np.pi, 100)
    x2 = a * np.sin(phi) * np.cos(theta_fixed)
    y2 = a * np.sin(phi) * np.sin(theta_fixed)
    z2 = a * np.cos(phi)
    ax2.plot(x2, y2, z2, label=f'θ = {theta_fixed:.2f} rad')

# 右图添加带箭头的坐标轴
arrow_x2 = Arrow3D([-axis_len, axis_len], [0, 0], [0, 0], **arrow_prop)
ax2.add_artist(arrow_x2)
ax2.text(axis_len + 0.1, 0, 0, 'x', fontsize=12, weight='bold', color='black')
arrow_y2 = Arrow3D([0, 0], [-axis_len, axis_len], [0, 0], **arrow_prop)
ax2.add_artist(arrow_y2)
ax2.text(0, axis_len + 0.1, 0, 'y', fontsize=12, weight='bold', color='black')
arrow_z2 = Arrow3D([0, 0], [0, 0], [-axis_len, axis_len], **arrow_prop)
ax2.add_artist(arrow_z2)
ax2.text(0, 0, axis_len + 0.1, 'z', fontsize=12, weight='bold', color='black')
# 标记原点
ax2.scatter(0, 0, 0, color='black', s=50)

# 右图样式设置
ax2.set_title(r'Fixed θ (Multiple Longitude Meridians)', y=1.0)  # 微调子图标题位置
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_xlim(-axis_len, axis_len)
ax2.set_ylim(-axis_len, axis_len)
ax2.set_zlim(-axis_len, axis_len)
ax2.legend()

# 调整布局（避免标题重叠）
plt.tight_layout(rect=[0, 0, 1, 0.95])  # 预留顶部空间给总标题
plt.show()
