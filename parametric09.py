import numpy as np
import matplotlib.pyplot as plt

# 1. 定义x的范围（0到2π）
x = np.linspace(0, 2 * np.pi, 200)  # 200个点保证曲线平滑
# 2. 计算sin(x)的y值
y = np.sin(x)

# 3. 创建画布
plt.figure(figsize=(8, 4))
# 绘制正弦曲线
plt.plot(x, y, color='blue', linewidth=2, label=r'$y = \sin x$')

# 4. 标记关键特征点（零点、极值点）
plt.scatter(0, 0, color='red', s=60, label='(0, 0)')
plt.scatter(np.pi/2, 1, color='green', s=60, label=r'$(\pi/2, 1)$ maximum')
plt.scatter(np.pi, 0, color='red', s=60, label=r'$(\pi, 0)$')
plt.scatter(3*np.pi/2, -1, color='orange', s=60, label=r'$(3\pi/2, -1)$minimum')
plt.scatter(2*np.pi, 0, color='red', s=60, label=r'$(2\pi, 0)$')

# 5. 辅助线（x轴、y轴）
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.5)  # x轴
plt.axvline(x=0, color='gray', linestyle='--', alpha=0.5)  # y轴

# 6. 样式与标签
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title(r'Sine Curve: $y = \sin x \ (0 \leq x \leq 2\pi)$', fontsize=14)
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],  # 用π标注x轴刻度
           [r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.ylim(-1.2, 1.2)  # 聚焦正弦曲线范围
plt.grid(alpha=0.3)
plt.legend(loc='upper right')

plt.show()
