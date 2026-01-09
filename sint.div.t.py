import numpy as np
import matplotlib.pyplot as plt

# 定义 t 的更大范围（避免 t=0 除零）
t = np.linspace(-20, 20, 1000)
t[t == 0] = np.nan  # 先设为 NaN，稍后处理

# 计算 sinc(t)
sinc_t = np.sin(t) / t

# 在 t=0 处补上极限值 1
sinc_t[np.isnan(sinc_t)] = 1

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(t, sinc_t, 'b-', linewidth=2, label=r'$\frac{\sin t}{t}$')
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)  # x轴
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)  # y轴

# 标注关键点
plt.annotate('1', xy=(0, 1), xytext=(0.5, 1.2), arrowprops=dict(arrowstyle='->', color='red'), fontsize=10)

# 设置标题和标签
plt.title(r'Graph of $\frac{\sin t}{t}$ (sinc function)', fontsize=16)
plt.xlabel('t', fontsize=12)
plt.ylabel(r'$\frac{\sin t}{t}$', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.xlim(-20, 20)  # 增大x轴范围
plt.ylim(-0.4, 1.2)

# 显示图像
plt.tight_layout()
plt.show()
