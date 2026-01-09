import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


# 自定义3D箭头类（解决matplotlib原生3D箭头不支持问题）
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        kwargs['color'] = 'blue'
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

# 设置全局样式
plt.rcParams['font.size'] = 10
plt.rcParams['figure.figsize'] = (18, 6)
plt.rcParams['font.family'] = 'DejaVu Sans'  # 支持数学符号

# 定义共用参数
axis_len = 2.5  # 坐标轴长度
rho_range = np.linspace(0, 2, 50)
theta_range = np.linspace(0, 2 * np.pi, 50)
z_range = np.linspace(-2, 2, 50)
arrow_prop = dict(arrowstyle='->', linewidth=2, color='black', mutation_scale=15)  # 箭头样式

# 创建画布和3个子图（1行3列）
fig = plt.figure()

# -------------------------- 子图1：半平面 θ=c --------------------------
ax1 = fig.add_subplot(131, projection='3d')
c_theta = np.pi / 4  # θ固定值
RHO, Z = np.meshgrid(rho_range, z_range)
X1 = RHO * np.cos(c_theta)
Y1 = RHO * np.sin(c_theta)

# 绘制半平面
ax1.plot_surface(X1, Y1, Z, color='lightblue', alpha=0.8, edgecolor='white', rstride=5, cstride=5)

# 绘制带箭头的坐标轴
# X轴
arrow_x1 = Arrow3D([-axis_len, axis_len], [0, 0], [0, 0], **arrow_prop)
ax1.add_artist(arrow_x1)
ax1.text(axis_len + 0.1, 0, 0, 'x', fontsize=12, color='black', weight='bold')
# Y轴
arrow_y1 = Arrow3D([0, 0], [-axis_len, axis_len], [0, 0], **arrow_prop)
ax1.add_artist(arrow_y1)
ax1.text(0, axis_len + 0.1, 0, 'y', fontsize=12, color='black', weight='bold')
# Z轴
arrow_z1 = Arrow3D([0, 0], [0, 0], [-axis_len, axis_len], **arrow_prop)
ax1.add_artist(arrow_z1)
ax1.text(0, 0, axis_len + 0.1, 'z', fontsize=12, color='black', weight='bold')

# 标记原点
ax1.scatter(0, 0, 0, color='black', s=50)
ax1.text(0.1, 0.1, 0.1, '(0,0,0)', fontsize=10, color='black')

# 设置范围和标题
ax1.set_xlim(-axis_len, axis_len)
ax1.set_ylim(-axis_len, axis_len)
ax1.set_zlim(-axis_len, axis_len)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title(r'$\theta = c$ (Half-plane, $c=\pi/4$)')

# -------------------------- 子图2：上半圆锥 φ=c (0<c<π/2) --------------------------
ax2 = fig.add_subplot(132, projection='3d')
c_phi_upper = np.pi / 6  # 上半圆锥φ固定值
THETA, RHO = np.meshgrid(theta_range, rho_range)
X2 = RHO * np.sin(c_phi_upper) * np.cos(THETA)
Y2 = RHO * np.sin(c_phi_upper) * np.sin(THETA)
Z2 = RHO * np.cos(c_phi_upper)  # Z≥0 上半圆锥

# 绘制上半圆锥
ax2.plot_surface(X2, Y2, Z2, color='lightblue', alpha=0.8, edgecolor='white', rstride=5, cstride=5)

# 绘制带箭头的坐标轴
# X轴
arrow_x2 = Arrow3D([-axis_len, axis_len], [0, 0], [0, 0], **arrow_prop)
ax2.add_artist(arrow_x2)
ax2.text(axis_len + 0.1, 0, 0, 'x', fontsize=12, color='black', weight='bold')
# Y轴
arrow_y2 = Arrow3D([0, 0], [-axis_len, axis_len], [0, 0], **arrow_prop)
ax2.add_artist(arrow_y2)
ax2.text(0, axis_len + 0.1, 0, 'y', fontsize=12, color='black', weight='bold')
# Z轴
arrow_z2 = Arrow3D([0, 0], [0, 0], [-axis_len, axis_len], **arrow_prop)
ax2.add_artist(arrow_z2)
ax2.text(0, 0, axis_len + 0.1, 'z', fontsize=12, color='black', weight='bold')

# 标记原点
ax2.scatter(0, 0, 0, color='black', s=50)
ax2.text(0.1, 0.1, 0.1, '(0,0,0)', fontsize=10, color='black')

# 设置范围和标题
ax2.set_xlim(-axis_len, axis_len)
ax2.set_ylim(-axis_len, axis_len)
ax2.set_zlim(-axis_len, axis_len)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title(r'$\phi = c$ (Upper cone, $0<c<\pi/2$, $c=\pi/6$)')

# -------------------------- 子图3：下半圆锥 φ=c (π/2<c<π) --------------------------
ax3 = fig.add_subplot(133, projection='3d')
c_phi_lower = 5 * np.pi / 6  # 下半圆锥φ固定值
THETA, RHO = np.meshgrid(theta_range, rho_range)
X3 = RHO * np.sin(c_phi_lower) * np.cos(THETA)
Y3 = RHO * np.sin(c_phi_lower) * np.sin(THETA)
Z3 = RHO * np.cos(c_phi_lower)  # Z≤0 下半圆锥

# 绘制下半圆锥
ax3.plot_surface(X3, Y3, Z3, color='lightblue', alpha=0.8, edgecolor='white', rstride=5, cstride=5)

# 绘制带箭头的坐标轴
# X轴
arrow_x3 = Arrow3D([-axis_len, axis_len], [0, 0], [0, 0], **arrow_prop)
ax3.add_artist(arrow_x3)
ax3.text(axis_len + 0.1, 0, 0, 'x', fontsize=12, color='black', weight='bold')
# Y轴
arrow_y3 = Arrow3D([0, 0], [-axis_len, axis_len], [0, 0], **arrow_prop)
ax3.add_artist(arrow_y3)
ax3.text(0, axis_len + 0.1, 0, 'y', fontsize=12, color='black', weight='bold')
# Z轴
arrow_z3 = Arrow3D([0, 0], [0, 0], [-axis_len, axis_len], **arrow_prop)
ax3.add_artist(arrow_z3)
ax3.text(0, 0, axis_len + 0.1, 'z', fontsize=12, color='black', weight='bold')

# 标记原点
ax3.scatter(0, 0, 0, color='black', s=50)
ax3.text(0.1, 0.1, 0.1, '(0,0,0)', fontsize=10, color='black')

# 设置范围和标题
ax3.set_xlim(-axis_len, axis_len)
ax3.set_ylim(-axis_len, axis_len)
ax3.set_zlim(-axis_len, axis_len)
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')
ax3.set_title(r'$\phi = c$ (Lower cone, $\pi/2<c<\pi$, $c=5\pi/6$)')

# 调整子图间距，避免重叠
plt.tight_layout()
# 显示画布
plt.show()