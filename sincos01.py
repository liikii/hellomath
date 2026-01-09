"""
sin cos 来自于圆， 又能拼合成圆
"""
import numpy as np
import matplotlib.pyplot as plt

# 参数范围：t 从 0 到 2π
t = np.linspace(0, 4 * np.pi, 100)

# 计算 cos(t) 和 sin(t)
cos_t = np.cos(t)
sin_t = np.sin(t)

# 创建图形和子图
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# 绘制 cos(t)
axs[0].plot(t, cos_t, 'b-', label='cos(t)', linewidth=2)
axs[0].set_title('Cosine Function: cos(t)')
axs[0].set_xlabel('Angle (radians)')
axs[0].set_ylabel('cos(t)')
axs[0].grid(True, linestyle='--', alpha=0.6)
axs[0].legend()

# 绘制 sin(t)
axs[1].plot(t, sin_t, 'r-', label='sin(t)', linewidth=2)
axs[1].set_title('Sine Function: sin(t)')
axs[1].set_xlabel('Angle (radians)')
axs[1].set_ylabel('sin(t)')
axs[1].grid(True, linestyle='--', alpha=0.6)
axs[1].legend()

# 调整布局避免重叠
plt.tight_layout()

# 显示图像
plt.show()
