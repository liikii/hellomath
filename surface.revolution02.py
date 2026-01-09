import numpy as np
import matplotlib.pyplot as plt

# 1. 定义x的范围（[-1,1]）
x = np.linspace(-1, 1, 200)  # 取200个点让曲线更平滑

# 2. 计算y值（上半圆）
y = np.sqrt(1 - x**2)

# 3. 绘制图形
plt.figure(figsize=(6, 6))  # 正方形画布，保证圆的比例正确
plt.plot(x, y, color='blue', linewidth=2, label=r'$f(x) = \sqrt{1-x^2}$')

# 4. 标记关键点（圆心、端点）
plt.scatter(0, 0, color='black', s=50, label='center (0,0)')
plt.scatter(-1, 0, color='red', s=50, label='left (-1,0)')
plt.scatter(1, 0, color='red', s=50, label='right (1,0)')
plt.scatter(0, 1, color='green', s=50, label='top (0,1)')

# 5. 样式设置（保证圆的比例）
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Upper Semicircle: $f(x) = \sqrt{1-x^2}$', fontsize=14)
plt.axis('equal')  # 等比例坐标轴，避免半圆变形
plt.grid(alpha=0.3)
plt.legend()
plt.xlim(-1.2, 1.2)  # 适当扩大范围，方便查看
plt.ylim(-0.2, 1.2)

plt.show()
