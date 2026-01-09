"""
保守场是‘有源’的场——它的每一个箭头都来自一个‘势’的坡度。
可以，但要明确：梯度描述的是「势函数」的变化趋势，而不是「向量场本身」的变化趋势。
梯度 ∇f 是标量场 f 的变化趋势，不是向量场 F 的变化趋势。
∇f 指出：在某一点，f 增长得最快的方向和速率
因为 F=∇f，所以这个“增长方向”就变成了力的方向
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 设置图形大小和样式
fig, ax = plt.subplots(figsize=(10, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')  # 隐藏坐标轴

# 设置字体和颜色
font_size = 14
color = 'black'

# 步骤 1: 定义势函数 f
step1 = r"$f(x, y, z) = \dfrac{mMG}{\sqrt{x^2 + y^2 + z^2}}$"
ax.text(1, 11, step1, fontsize=font_size, color=color, ha='left', va='center')

# 步骤 2: 梯度定义
step2 = r"$\nabla f(x, y, z) = \dfrac{\partial f}{\partial x}\,\mathbf{i} + \dfrac{\partial f}{\partial y}\,\mathbf{j} + \dfrac{\partial f}{\partial z}\,\mathbf{k}$"
ax.text(1, 9.5, step2, fontsize=font_size, color=color, ha='left', va='center')

# 步骤 3: 计算 ∂f/∂x
step3_x = r"$\dfrac{\partial f}{\partial x} = mMG \cdot \left(-\dfrac{1}{2}\right)(x^2 + y^2 + z^2)^{-3/2} \cdot 2x = \dfrac{-mMGx}{(x^2 + y^2 + z^2)^{3/2}}$"
ax.text(1, 8, step3_x, fontsize=font_size, color=color, ha='left', va='center')

# 步骤 4: 计算 ∂f/∂y
step3_y = r"$\dfrac{\partial f}{\partial y} = \dfrac{-mMGy}{(x^2 + y^2 + z^2)^{3/2}}$"
ax.text(1, 6.5, step3_y, fontsize=font_size, color=color, ha='left', va='center')

# 步骤 5: 计算 ∂f/∂z
step3_z = r"$\dfrac{\partial f}{\partial z} = \dfrac{-mMGz}{(x^2 + y^2 + z^2)^{3/2}}$"
ax.text(1, 5, step3_z, fontsize=font_size, color=color, ha='left', va='center')

# 步骤 6: 汇总为 F
step4 = r"$\nabla f = \dfrac{-mMGx}{(x^2 + y^2 + z^2)^{3/2}}\,\mathbf{i} + \dfrac{-mMGy}{(x^2 + y^2 + z^2)^{3/2}}\,\mathbf{j} + \dfrac{-mMGz}{(x^2 + y^2 + z^2)^{3/2}}\,\mathbf{k}$"
ax.text(1, 3.5, step4, fontsize=font_size, color=color, ha='left', va='center')

# 步骤 7: 结论
step5 = r"$= \mathbf{F}(x, y, z)$"
ax.text(1, 2, step5, fontsize=font_size, color=color, ha='left', va='center')

# 添加标题
title = r"Derivation: Gravitational Field is Conservative $\mathbf{F}(x,y,z) = \nabla f(x,y,z)$"
ax.text(1, 11.5, title, fontsize=16, fontweight='bold', color='darkblue', ha='left')

# 添加虚线框（可选）标记关键区域
rect = Rectangle((0.5, 2), 9, 9.5, fill=False, edgecolor='gray', linestyle='--', linewidth=1)
ax.add_patch(rect)

# 调整布局并显示
plt.tight_layout()
plt.show()
