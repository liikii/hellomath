import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# ===================== 定义闭合曲线C（豆形曲线，匹配原图） =====================
def bean_curve(t):
    # 参数t∈[0, 2π]，生成豆形闭合曲线
    x = 2 * np.cos(t) + 0.5 * np.cos(2*t)
    y = 1.5 * np.sin(t)
    return x, y

t = np.linspace(0, 2*np.pi, 100)
x_curve, y_curve = bean_curve(t)

# 计算曲线的切向量（单位化，对应T）
dx = np.gradient(x_curve, t)
dy = np.gradient(y_curve, t)
t_mag = np.sqrt(dx**2 + dy**2)
T_x = dx / t_mag
T_y = dy / t_mag

# 选取曲线右上角的点作为向量标注点
idx = 70  # 对应曲线右上角位置
x0, y0 = x_curve[idx], y_curve[idx]
T_x0, T_y0 = T_x[idx], T_y[idx]  # 该点的切向量T


# ===================== 绘制正环流（图a）和负环流（图b） =====================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
for ax in [ax1, ax2]:
    ax.set_aspect('equal')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 2)
    # 绘制闭合曲线C
    ax.plot(x_curve, y_curve, color='blue', linewidth=2, label='$C$')
    # 绘制曲线的箭头（表示环流方向）
    ax.arrow(x_curve[50], y_curve[50], dx[50]*0.2, dy[50]*0.2,
             color='blue', linewidth=1.5, head_width=0.15)
    # 绘制切向量T
    arrow_T = FancyArrowPatch((x0, y0), (x0 + T_x0*0.8, y0 + T_y0*0.8),
                              color='pink', linewidth=2, arrowstyle='->', mutation_scale=15, label='$\\mathbf{T}$ (Tangent)')
    ax.add_patch(arrow_T)


# ---------- 图a：正环流（v与T方向接近，v·T>0） ----------
v_x_a, v_y_a = T_x0 * 0.8, T_y0 * 0.8  # v与T同方向
arrow_v_a = FancyArrowPatch((x0, y0), (x0 + v_x_a, y0 + v_y_a),
                            color='red', linewidth=2, arrowstyle='->', mutation_scale=15, label='$\\mathbf{v}$')
ax1.add_patch(arrow_v_a)
ax1.set_title('(a) $\\int_C \\mathbf{v} \\cdot d\\mathbf{r} > 0$ (Positive Circulation)')
ax1.text(-2.5, 1.5, '$\\mathbf{v}$ direction close to $\\mathbf{T}$', fontsize=10, color='red')
ax1.legend()


# ---------- 图b：负环流（v与T方向相反，v·T<0） ----------
v_x_b, v_y_b = -T_x0 * 0.8, -T_y0 * 0.8  # v与T反方向
arrow_v_b = FancyArrowPatch((x0, y0), (x0 + v_x_b, y0 + v_y_b),
                            color='red', linewidth=2, arrowstyle='->', mutation_scale=15, label='$\\mathbf{v}$')
ax2.add_patch(arrow_v_b)
ax2.set_title('(b) $\\int_C \\mathbf{v} \\cdot d\\mathbf{r} < 0$ (Negative Circulation)')
ax2.text(-2.5, 1.5, '$\\mathbf{v}$ direction opposite to $\\mathbf{T}$', fontsize=10, color='red')
ax2.legend()


plt.tight_layout()
plt.show()
