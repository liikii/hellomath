import matplotlib.pyplot as plt
import numpy as np

# 定义x范围
x = np.linspace(-10, 10, 400)

# 斜率为-2的直线方程 y = mx + b，这里m=-2, b=0（因为通过原点）
y_slope_minus_2 = -2 * x

# 斜率为-4的直线方程 y = mx + b，这里m=-4, b=0（因为通过原点）
y_slope_minus_4 = -4 * x

# 创建图形
plt.figure(figsize=(8, 6))

# 绘制斜率为-2的直线
plt.plot(x, y_slope_minus_2, label='Slope -2', color='blue')

# 绘制斜率为-4的直线
plt.plot(x, y_slope_minus_4, label='Slope -4', color='red')

# 添加图例
plt.legend()

# 添加网格
plt.grid(True)

# 设置x轴和y轴标签
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 设置标题
plt.title('Lines with Slopes -2 and -4')

# 显示图形
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
