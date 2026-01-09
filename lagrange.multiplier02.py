"""
极值点出现在“约束线与等高线相切”的地方，而不是任意相交的地方。因为只有在相切时，函数值才无法再沿约束方向增加或减少。
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyArrowPatch
from matplotlib import cm


# 定义函数和约束
def f(x, y):
    """目标函数"""
    return x**2 + 2*y**2

def g(x, y):
    """约束函数"""
    return x + y - 3

# 计算梯度和法向量
def gradient_f(x, y):
    return np.array([2*x, 4*y])

def gradient_g(x, y):
    return np.array([1, 1])

# 创建网格数据
x = np.linspace(-2, 5, 400)
y = np.linspace(-2, 5, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# 约束曲线
x_constraint = np.linspace(-2, 5, 200)
y_constraint = 3 - x_constraint

# 找到极值点 (用拉格朗日乘数法求解)
# ∇f = λ∇g ⇒ 2x = λ, 4y = λ ⇒ x = 2y
# 代入 x + y = 3 ⇒ 2y + y = 3 ⇒ y = 1, x = 2
optimal_x, optimal_y = 2, 1
optimal_f = f(optimal_x, optimal_y)
lambda_val = 2 * optimal_x  # 或 4*optimal_y

# 计算梯度
grad_f = gradient_f(optimal_x, optimal_y)
grad_g = gradient_g(optimal_x, optimal_y)

# 创建图形
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 左侧：等高线图
ax1.set_aspect('equal')
ax1.set_xlim(-2, 5)
ax1.set_ylim(-2, 5)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('lagrange multiplier\n∇f ∥ ∇g ')

# 绘制等高线
levels = np.linspace(0, 30, 20)
contour = ax1.contour(X, Y, Z, levels=levels, colors='black', alpha=0.6, linewidths=0.5)
ax1.clabel(contour, inline=True, fontsize=8)

# 绘制约束曲线
constraint_line, = ax1.plot(x_constraint, y_constraint, 'r-', linewidth=2, label='restricted: x+y=3')
optimal_point, = ax1.plot([], [], 'ro', markersize=10, label='critical point')

# 绘制法向量箭头
arrow_f = FancyArrowPatch((optimal_x, optimal_y),
                          (optimal_x + grad_f[0]/3, optimal_y + grad_f[1]/3),
                          arrowstyle='->', mutation_scale=20,
                          color='blue', linewidth=2, label='∇f')
arrow_g = FancyArrowPatch((optimal_x, optimal_y),
                          (optimal_x + grad_g[0], optimal_y + grad_g[1]),
                          arrowstyle='->', mutation_scale=20,
                          color='red', linewidth=2, label='∇g')

ax1.add_patch(arrow_f)
ax1.add_patch(arrow_g)
ax1.legend(loc='upper right')

# 右侧：3D曲面图
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('f(x,y)')
ax2.set_title('3D curl and restricted ')

# 绘制3D曲面
surf = ax2.plot_surface(X, Y, Z, cmap=cm.viridis, alpha=0.7, linewidth=0, antialiased=True)

# 在3D图上绘制约束曲线
z_constraint = f(x_constraint, y_constraint)
ax2.plot(x_constraint, y_constraint, z_constraint, 'r-', linewidth=3, label='restricted curve')

# 标记极值点
ax2.scatter([optimal_x], [optimal_y], [optimal_f], color='red', s=100, label='critical point')

# 绘制梯度向量
grad_f_3d = np.append(grad_f, 0)  # 在3D中z分量为0
grad_g_3d = np.append(grad_g, 0)
ax2.quiver(optimal_x, optimal_y, optimal_f,
           grad_f[0], grad_f[1], 0,
           color='blue', length=1, normalize=True, label='∇f')
ax2.quiver(optimal_x, optimal_y, optimal_f,
           grad_g[0], grad_g[1], 0,
           color='red', length=1, normalize=True, label='∇g')

ax2.view_init(elev=30, azim=-45)
ax2.legend()

plt.tight_layout()
plt.show()

# 创建动画展示移动点
print(f"最优解: x={optimal_x:.2f}, y={optimal_y:.2f}")
print(f"最优值: f={optimal_f:.2f}")
print(f"拉格朗日乘子: λ={lambda_val:.2f}")
print(f"梯度: ∇f = {grad_f}, ∇g = {grad_g}")
print(f"验证平行性: ∇f / ∇g = {grad_f[0]/grad_g[0]:.2f}, {grad_f[1]/grad_g[1]:.2f}")
