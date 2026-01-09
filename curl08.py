"""
整体逆进针旋转
"""
import numpy as np
import matplotlib.pyplot as plt

# 1. 设置绘图区域，生成网格点（x轴、y轴范围）
x = np.linspace(-3, 3, 15)  # x轴范围：-3到3，生成15个均匀点
y = np.linspace(-3, 3, 15)  # y轴范围：-3到3，生成15个均匀点
X, Y = np.meshgrid(x, y)    # 生成二维网格，用于绘制矢量场

# 2. 定义矢量场 F=(P, Q)，满足 ∂P/∂y=0，∂Q/∂x>0
P = np.ones_like(X)  # P=1（常数），∂P/∂y=0
Q = X                # Q=x，∂Q/∂x=1>0

# 3. 设置绘图样式
plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文显示
plt.rcParams['axes.unicode_minus'] = False    # 支持负号显示
fig, ax = plt.subplots(figsize=(8, 8))

# 4. 绘制矢量场（quiver函数：绘制箭头矢量图）
# 参数说明：X/Y=网格点坐标，P/Q=矢量场分量，color=箭头颜色，scale=箭头缩放比例，width=箭头宽度
ax.quiver(X, Y, P, Q, color='royalblue', scale=20, width=0.005)

# 5. 添加标注和样式优化
ax.set_xlabel('x 轴', fontsize=12)
ax.set_ylabel('y 轴', fontsize=12)
ax.set_title(r'矢量场 $\vec{F}=(1, x)$（满足 $\frac{\partial P}{\partial y}=0$，$\frac{\partial Q}{\partial x}=1>0$）', fontsize=14)
ax.grid(True, alpha=0.3)  # 添加网格线
ax.axhline(y=0, color='black', linewidth=1)  # 绘制x轴
ax.axvline(x=0, color='black', linewidth=1)  # 绘制y轴

# 6. 显示图像
plt.show()
