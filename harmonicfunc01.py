import numpy as np
import matplotlib.pyplot as plt

# 创建网格
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# 调和函数（平滑，无源）
Z_harmonic = X**2 - Y**2

# 非调和函数（有源，"不平滑"）
Z_non_harmonic = X**2 + Y**2

# 创建子图
fig, axes = plt.subplots(1, 2, figsize=(14, 6), subplot_kw={'projection': '3d'})

# 左图：调和函数（马鞍形）
surf1 = axes[0].plot_surface(X, Y, Z_harmonic, cmap='coolwarm', alpha=0.9)
axes[0].set_title(r'Harmonic: $u = x^2 - y^2$' '\n$\nabla^2 u = 0$')
axes[0].set_xlabel('x'); axes[0].set_ylabel('y'); axes[0].set_zlabel('u')

# 右图：非调和函数（碗形）
surf2 = axes[1].plot_surface(X, Y, Z_non_harmonic, cmap='viridis', alpha=0.9)
axes[1].set_title(r'Non-Harmonic: $u = x^2 + y^2$' '\n$\nabla^2 u = 4 \neq 0$')
axes[1].set_xlabel('x'); axes[1].set_ylabel('y'); axes[1].set_zlabel('u')

# 调整视角
for ax in axes:
    ax.view_init(elev=20, azim=45)

plt.tight_layout()
plt.show()