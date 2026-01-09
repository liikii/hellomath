"""
平方为1的原理， 因为sin cos 的对称性
"""
import numpy as np
import matplotlib.pyplot as plt

# 定义参数t
t = np.linspace(0, 2 * np.pi, 1000)

# 单位圆数据
x_circle = np.cos(t)
y_circle = np.sin(t)

# 正弦和余弦数据
sin_t = np.sin(t)
cos_t = np.cos(t)

# 正弦平方和余弦平方数据
sin_sq = np.sin(t)**2
cos_sq = np.cos(t)**2

# 创建图形和子图
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

# 绘制单位圆并添加轴线
axs[0].plot(x_circle, y_circle, label='Unit Circle')
axs[0].axhline(0, color='black',linewidth=0.5)
axs[0].axvline(0, color='black',linewidth=0.5)
axs[0].set_title('Unit Circle')
axs[0].set_xlabel('Cosine')
axs[0].set_ylabel('Sine')
axs[0].axis('equal')
axs[0].legend()

# 绘制正弦和余弦并添加轴线
axs[1].plot(t, sin_t, label='Sine')
axs[1].plot(t, cos_t, label='Cosine')
axs[1].axhline(0, color='black',linewidth=0.5)
axs[1].set_title('Sine and Cosine')
axs[1].set_xlabel('Angle (radians)')
axs[1].set_ylabel('Value')
axs[1].legend()

# 绘制正弦平方和余弦平方并添加轴线
axs[2].plot(t, sin_sq, label='Sin^2')
axs[2].plot(t, cos_sq, label='Cos^2')
axs[2].axhline(0, color='black',linewidth=0.5)
axs[2].set_title('Square of Sine and Cosine')
axs[2].set_xlabel('Angle (radians)')
axs[2].set_ylabel('Value')
axs[2].legend()

plt.tight_layout()
plt.show()
