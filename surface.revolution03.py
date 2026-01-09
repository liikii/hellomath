import numpy as np
import matplotlib.pyplot as plt

# 定义 x 范围（从 0 开始）
x = np.linspace(0, 4, 100)  # 从 0 到 4，100 个点
y = np.sqrt(x)

# 绘图
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', linewidth=2, label=r'$f(x) = \sqrt{x}$')
plt.fill_between(x, y, 0, alpha=0.3, color='skyblue')  # 填充下方区域

# 设置标签和样式
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title(r'Graph of $f(x) = \sqrt{x}$', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.axis([0, 4, 0, 2])  # 限制坐标轴范围
plt.tight_layout()
plt.show()
