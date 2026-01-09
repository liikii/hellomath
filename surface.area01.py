import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ===================== 定义通用参数 =====================
# 参数平面范围
u_min, u_max = 0, 4
v_min, v_max = 0, 3
# 分割数量
n_u, n_v = 4, 3
delta_u = (u_max - u_min) / n_u
delta_v = (v_max - v_min) / n_v
# 高亮的子矩形/面片位置
highlight_i, highlight_j = 1, 1

# ===================== 定义参数曲面（马鞍面） =====================
def r(u, v):
    x = u
    y = v
    z = u**2 - v**2  # 马鞍面，可替换为球面/圆柱面
    return x, y, z

# ===================== 创建统一Figure和子图 =====================
fig = plt.figure(figsize=(14, 6))  # 宽14，高6，适配两张图

fig.suptitle(r'$\iint_S 1 \, dS = \int_{0}^{2\pi} \int_{0}^{\pi} \sin\theta \, d\theta \, d\phi$',
             fontsize=16,  # 字体大小（比子图标题大）
             fontweight='bold',  # 加粗（可选）
             y=0.98)  # 位置微调（y=1是顶部，0.98避免超出画布）

# ---- 子图1：参数平面D的矩形分割 ----
ax1 = fig.add_subplot(121)  # 1行2列，第1个子图

# 绘制参数平面网格
for i in range(n_u + 1):
    u = u_min + i * delta_u
    ax1.plot([u, u], [v_min, v_max], color='gray', linewidth=1)
for j in range(n_v + 1):
    v = v_min + j * delta_v
    ax1.plot([u_min, u_max], [v, v], color='gray', linewidth=1)

# 高亮R_ij
u1 = u_min + highlight_i * delta_u
u2 = u1 + delta_u
v1 = v_min + highlight_j * delta_v
v2 = v1 + delta_v
ax1.fill([u1, u2, u2, u1], [v1, v1, v2, v2], color='orange', alpha=0.5)
# 标注
ax1.annotate(r'$\Delta u$', xy=((u1+u2)/2, v1), xytext=((u1+u2)/2, v1-0.2), ha='center')
ax1.annotate(r'$\Delta v$', xy=(u1, (v1+v2)/2), xytext=(u1-0.3, (v1+v2)/2), va='center')
ax1.text((u1+u2)/2, (v1+v2)/2, r'$R_{ij}$', ha='center', va='center', fontsize=12)
# 样式
ax1.set_xlabel('$u$', fontsize=12)
ax1.set_ylabel('$v$', fontsize=12)
ax1.set_title('Parameter Domain $D$ (Subrectangles)', fontsize=14)
ax1.set_xlim(u_min - 0.5, u_max + 0.5)
ax1.set_ylim(v_min - 0.5, v_max + 0.5)
ax1.grid(False)

# ---- 子图2：曲面S的面片分割 ----
ax2 = fig.add_subplot(122, projection='3d')  # 1行2列，第2个子图（3D）

# 绘制曲面网格线
u_grid = np.linspace(u_min, u_max, n_u + 1)
v_grid = np.linspace(v_min, v_max, n_v + 1)
for u in u_grid:
    v = np.linspace(v_min, v_max, 20)
    x, y, z = r(u, v)
    ax2.plot(x, y, z, color='gray', linewidth=1)
for v in v_grid:
    u = np.linspace(u_min, u_max, 20)
    x, y, z = r(u, v)
    ax2.plot(x, y, z, color='gray', linewidth=1)

# 高亮S_ij面片
u_patch = np.linspace(u1, u2, 20)
v_patch = np.linspace(v1, v2, 20)
U_patch, V_patch = np.meshgrid(u_patch, v_patch)
X_patch, Y_patch, Z_patch = r(U_patch, V_patch)
ax2.plot_surface(X_patch, Y_patch, Z_patch, color='cyan', alpha=0.7)

# 标记P_ij点
p_u = (u1+u2)/2
p_v = (v1+v2)/2
p_x, p_y, p_z = r(p_u, p_v)
ax2.scatter(p_x, p_y, p_z, color='red', s=80, label=r'$P_{ij}$')
ax2.text(p_x, p_y, p_z, r'$S_{ij}$', ha='center', va='bottom', fontsize=12)

# 样式
ax2.set_xlabel('$x$', fontsize=12)
ax2.set_ylabel('$y$', fontsize=12)
ax2.set_zlabel('$z$', fontsize=12)
ax2.set_title('Surface $S$ (Corresponding Patches)', fontsize=14)
ax2.legend()
ax2.set_box_aspect([1, 1, 0.8])

# ===================== 整体调整 =====================
# plt.title(r'$\iint_S 1 \, dS = \int_{0}^{2\pi} \int_{0}^{\pi} \sin\theta \, d\theta \, d\phi$')
plt.tight_layout(rect=[0,0,1,1])  # 自动调整子图间距，避免重叠
plt.show()
