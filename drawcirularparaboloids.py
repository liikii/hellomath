import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 创建网格数据
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

# 1. 椭圆抛物面 (向上开口) - 旋转抛物面
Z_elliptic_up = X**2 + Y**2

# 2. 椭圆抛物面 (向下开口)
Z_elliptic_down = -X**2 - Y**2

# 3. 双曲抛物面 (马鞍面)
Z_hyperbolic = X**2 - Y**2

# 4. 带系数的椭圆抛物面
Z_scaled = 0.3*X**2 + 0.7*Y**2

# 设置图形
fig = plt.figure(figsize=(16, 12))

# 1. 椭圆抛物面（向上）
ax1 = fig.add_subplot(221, projection='3d')
surf1 = ax1.plot_surface(X, Y, Z_elliptic_up,
                        cmap='viridis',
                        alpha=0.9,
                        rstride=3,
                        cstride=3,
                        linewidth=0.1,
                        antialiased=True)
# 添加等高线
ax1.contour(X, Y, Z_elliptic_up, zdir='z', offset=-2, cmap='viridis', alpha=0.3)
ax1.contour(X, Y, Z_elliptic_up, zdir='x', offset=-3.5, cmap='viridis', alpha=0.3)
ax1.contour(X, Y, Z_elliptic_up, zdir='y', offset=3.5, cmap='viridis', alpha=0.3)

ax1.set_title('Elliptic Paraboloid (Upward)\n$z = x^2 + y^2$', fontsize=12, pad=20)
ax1.set_xlabel('X', labelpad=10)
ax1.set_ylabel('Y', labelpad=10)
ax1.set_zlabel('Z', labelpad=10)
ax1.set_zlim(-2, 10)
ax1.view_init(elev=25, azim=45)

# 2. 椭圆抛物面（向下）
ax2 = fig.add_subplot(222, projection='3d')
surf2 = ax2.plot_surface(X, Y, Z_elliptic_down,
                        cmap='plasma',
                        alpha=0.9,
                        rstride=3,
                        cstride=3,
                        linewidth=0.1,
                        antialiased=True)
ax2.contour(X, Y, Z_elliptic_down, zdir='z', offset=-10, cmap='plasma', alpha=0.3)
ax2.set_title('Elliptic Paraboloid (Downward)\n$z = -x^2 - y^2$', fontsize=12, pad=20)
ax2.set_xlabel('X', labelpad=10)
ax2.set_ylabel('Y', labelpad=10)
ax2.set_zlabel('Z', labelpad=10)
ax2.set_zlim(-10, 2)
ax2.view_init(elev=25, azim=45)

# 3. 双曲抛物面（马鞍面）
ax3 = fig.add_subplot(223, projection='3d')
surf3 = ax3.plot_surface(X, Y, Z_hyperbolic,
                        cmap='coolwarm',
                        alpha=0.9,
                        rstride=3,
                        cstride=3,
                        linewidth=0.1,
                        antialiased=True)
ax3.contour(X, Y, Z_hyperbolic, zdir='z', offset=-5, cmap='coolwarm', alpha=0.3)
ax3.set_title('Hyperbolic Paraboloid (Saddle)\n$z = x^2 - y^2$', fontsize=12, pad=20)
ax3.set_xlabel('X', labelpad=10)
ax3.set_ylabel('Y', labelpad=10)
ax3.set_zlabel('Z', labelpad=10)
ax3.set_zlim(-5, 5)
ax3.view_init(elev=25, azim=45)

# 4. 缩放椭圆抛物面
ax4 = fig.add_subplot(224, projection='3d')
surf4 = ax4.plot_surface(X, Y, Z_scaled,
                        cmap='summer',
                        alpha=0.9,
                        rstride=3,
                        cstride=3,
                        linewidth=0.1,
                        antialiased=True)
ax4.contour(X, Y, Z_scaled, zdir='z', offset=-2, cmap='summer', alpha=0.3)
ax4.set_title('Scaled Elliptic Paraboloid\n$z = 0.3x^2 + 0.7y^2$', fontsize=12, pad=20)
ax4.set_xlabel('X', labelpad=10)
ax4.set_ylabel('Y', labelpad=10)
ax4.set_zlabel('Z', labelpad=10)
ax4.set_zlim(-2, 6)
ax4.view_init(elev=25, azim=45)

plt.tight_layout()
plt.show()

# 单独展示旋转抛物面（经典圆抛物面）的细节图
fig2 = plt.figure(figsize=(10, 8))
ax5 = fig2.add_subplot(111, projection='3d')

# 创建更精细的网格
x_fine = np.linspace(-2.5, 2.5, 100)
y_fine = np.linspace(-2.5, 2.5, 100)
X_fine, Y_fine = np.meshgrid(x_fine, y_fine)
Z_fine = X_fine**2 + Y_fine**2

# 绘制旋转抛物面
surf5 = ax5.plot_surface(X_fine, Y_fine, Z_fine,
                         cmap=cm.viridis,
                         alpha=0.95,
                         rstride=2,
                         cstride=2,
                         linewidth=0.25,
                         antialiased=True,
                         shade=True)

# 添加等高线投影
ax5.contour(X_fine, Y_fine, Z_fine, zdir='z', offset=0,
           colors='black', linewidths=0.5, linestyles='solid', alpha=0.5)

# 设置坐标轴和视角
ax5.set_title('Circular Paraboloid (Rotational Paraboloid)\n$z = x^2 + y^2$',
              fontsize=14, pad=20, fontweight='bold')
ax5.set_xlabel('X', fontsize=12, labelpad=15)
ax5.set_ylabel('Y', fontsize=12, labelpad=15)
ax5.set_zlabel('Z', fontsize=12, labelpad=15)
ax5.set_zlim(0, 12)

# 添加网格线
ax5.xaxis.pane.fill = False
ax5.yaxis.pane.fill = False
ax5.zaxis.pane.fill = False
ax5.xaxis.pane.set_edgecolor('w')
ax5.yaxis.pane.set_edgecolor('w')
ax5.zaxis.pane.set_edgecolor('w')

# 设置不同视角查看
ax5.view_init(elev=30, azim=35)

# 添加颜色条
fig2.colorbar(surf5, ax=ax5, shrink=0.5, aspect=20, pad=0.1, label='Z value')

plt.tight_layout()
plt.show()
