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


# 创建动画
fig_anim, ax_anim = plt.subplots(figsize=(8, 8))
ax_anim.set_aspect('equal')
ax_anim.set_xlim(-2, 5)
ax_anim.set_ylim(-2, 5)
ax_anim.set_xlabel('x')
ax_anim.set_ylabel('y')
ax_anim.set_title('lagrange multiplier: point move on the restricted line')

levels = np.linspace(0, 30, 20)

# 绘制等高线
contour_anim = ax_anim.contour(X, Y, Z, levels=levels, colors='gray', alpha=0.6, linewidths=0.5)

# 绘制约束曲线
ax_anim.plot(x_constraint, y_constraint, 'r-', linewidth=2, label='restricted: x+y=3')

# 初始化移动点和向量
moving_point, = ax_anim.plot([], [], 'go', markersize=10, label='move point')
f_vector = FancyArrowPatch((0, 0), (0, 0), arrowstyle='->',
                           mutation_scale=20, color='blue', linewidth=2, label='∇f')
g_vector = FancyArrowPatch((0, 0), (0, 0), arrowstyle='->',
                           mutation_scale=20, color='red', linewidth=2, label='∇g')
ax_anim.add_patch(f_vector)
ax_anim.add_patch(g_vector)

# 标记极值点
ax_anim.plot(optimal_x, optimal_y, 'ro', markersize=10, label='critical point')

# 添加文本框显示信息
info_text = ax_anim.text(0.05, 0.95, '', transform=ax_anim.transAxes,
                         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax_anim.legend(loc='lower right')
ax_anim.grid(True, alpha=0.3)


# 动画初始化函数
def init():
    moving_point.set_data([], [])
    f_vector.set_positions((0, 0), (0, 0))
    g_vector.set_positions((0, 0), (0, 0))
    info_text.set_text('')
    return moving_point, f_vector, g_vector, info_text



# 动画更新函数
def update(frame):
    # 在约束曲线上移动点
    t = frame / 100  # 参数化约束曲线
    x_move = -1 + t * 6  # 从-1到5
    y_move = 3 - x_move

    moving_point.set_data([x_move], [y_move])

    # 计算当前点的梯度
    grad_f_current = gradient_f(x_move, y_move)
    grad_g_current = gradient_g(x_move, y_move)

    # 更新向量箭头（缩放以便可视化）
    scale_f = 0.5 / np.linalg.norm(grad_f_current) if np.linalg.norm(grad_f_current) > 0 else 0
    scale_g = 0.5 / np.linalg.norm(grad_g_current) if np.linalg.norm(grad_g_current) > 0 else 0

    f_vector.set_positions((x_move, y_move),
                           (x_move + grad_f_current[0] * scale_f,
                            y_move + grad_f_current[1] * scale_f))
    g_vector.set_positions((x_move, y_move),
                           (x_move + grad_g_current[0] * scale_g,
                            y_move + grad_g_current[1] * scale_g))

    # 计算角度差（判断是否平行）
    if np.linalg.norm(grad_f_current) > 0 and np.linalg.norm(grad_g_current) > 0:
        cos_angle = np.dot(grad_f_current, grad_g_current) / (
                    np.linalg.norm(grad_f_current) * np.linalg.norm(grad_g_current))
        angle_deg = np.degrees(np.arccos(np.clip(cos_angle, -1, 1)))
    else:
        angle_deg = 0

    # 更新信息文本
    f_val = f(x_move, y_move)
    info_text.set_text(f'position: ({x_move:.2f}, {y_move:.2f})\n'
                       f'f: {f_val:.2f}\n'
                       f'grad angle: {angle_deg:.1f}°\n'
                       f'∇f: ({grad_f_current[0]:.2f}, {grad_f_current[1]:.2f})\n'
                       f'∇g: ({grad_g_current[0]:.2f}, {grad_g_current[1]:.2f})')

    # 接近极值点时改变颜色
    distance_to_opt = np.sqrt((x_move - optimal_x) ** 2 + (y_move - optimal_y) ** 2)
    if distance_to_opt < 0.3:
        moving_point.set_color('yellow')
        info_text.set_bbox(dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    else:
        moving_point.set_color('green')
        info_text.set_bbox(dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    return moving_point, f_vector, g_vector, info_text


# 创建动画
ani = animation.FuncAnimation(fig_anim, update, frames=np.linspace(0, 100, 101),
                              init_func=init, blit=True, interval=100)

plt.tight_layout()
plt.show()

# 保存动画（可选）
# ani.save('lagrange_multiplier_animation.gif', writer='pillow', fps=10)
"""
# 创建动画 - 增加帧数使动画更平滑
ani = animation.FuncAnimation(
    fig_anim, update,
    frames=np.linspace(0, 150, 151),  # 151帧，更平滑
    init_func=init,
    blit=True,
    interval=50,  # 每帧50毫秒
    repeat_delay=2000  # 重复前暂停2秒
)

plt.tight_layout()

# 显示动画
plt.show()

# 保存为MP4文件
print("正在保存动画为MP4文件...")

# 方法1: 使用FFmpegWriter（需要安装ffmpeg）
try:
    # 设置视频参数
    writer = animation.FFmpegWriter(
        fps=20,  # 帧率
        metadata=dict(artist='拉格朗日乘数法演示'),
        bitrate=1800
    )

    # 保存为MP4
    ani.save('lagrange_multiplier_demo.mp4', writer=writer)
    print("✅ 动画已保存为 'lagrange_multiplier_demo.mp4'")

except Exception as e:
    print(f"保存MP4时出错: {e}")
    print("请确保已安装ffmpeg:")
    print("  Windows: 从 https://ffmpeg.org/download.html 下载")
    print("  Mac: brew install ffmpeg")
    print("  Linux: sudo apt-get install ffmpeg")

    # 方法2: 如果FFmpeg不可用，尝试保存为GIF
    print("\n尝试保存为GIF格式...")
    try:
        ani.save('lagrange_multiplier_demo.gif', writer='pillow', fps=20)
        print("✅ 动画已保存为 'lagrange_multiplier_demo.gif'")
    except Exception as e2:
        print(f"保存GIF时也出错: {e2}")

"""