"""
弯曲方向 = 切向量的变化方向
切向量的变化方向
T'(t) “ 指向曲线内侧”  ！但只在单位化后（即 N(t)）
"""
import numpy as np
import matplotlib.pyplot as plt

# 定义参数范围
t_vals = np.linspace(-2, 2, 100)

# 曲线 r(t) = (x(t), y(t)) = (t, t^2)
x = t_vals
y = t_vals**2

# 计算导数 r'(t) = (1, 2t)
dx_dt = np.ones_like(t_vals)
dy_dt = 2 * t_vals

# 速度大小 |r'(t)|
speed = np.sqrt(dx_dt**2 + dy_dt**2)

# 单位切向量 T = r'(t) / |r'(t)|
Tx = dx_dt / speed
Ty = dy_dt / speed

# 计算 T 的导数 dT/dt（用于求 N）
# 注意：T = (1/sqrt(1+4t²), 2t/sqrt(1+4t²))
# 我们可以解析求导，但这里用数值微分更通用
dTdt_x = np.gradient(Tx, t_vals)
dTdt_y = np.gradient(Ty, t_vals)

# dT/ds = (dT/dt) / (ds/dt) = (dT/dt) / |r'(t)|
dtds = 1 / speed
NTx = dTdt_x * dtds
NTy = dTdt_y * dtds

# 主法向量 N = (dT/ds) / |dT/ds|，但只在 |dT/ds| ≠ 0 时定义
norm_N = np.sqrt(NTx**2 + NTy**2)
# 避免除零
Nx = np.zeros_like(NTx)
Ny = np.zeros_like(NTy)
nonzero = norm_N > 1e-6
Nx[nonzero] = NTx[nonzero] / norm_N[nonzero]
Ny[nonzero] = NTy[nonzero] / norm_N[nonzero]

# 选择几个点来绘制向量（避免太密集）
indices = np.linspace(0, len(t_vals)-1, 8, dtype=int)

# 绘图
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'k-', label=r'$y = x^2$')

# 绘制 T 和 N 向量
scale = 0.5  # 向量缩放因子，便于观察
for i in indices:
    xi, yi = x[i], y[i]
    # 切向量 T（红色）
    plt.arrow(xi, yi, Tx[i]*scale, Ty[i]*scale,
              head_width=0.1, head_length=0.1, fc='red', ec='red', linewidth=1.5)
    # 主法向量 N（蓝色）
    plt.arrow(xi, yi, Nx[i]*scale, Ny[i]*scale,
              head_width=0.1, head_length=0.1, fc='blue', ec='blue', linewidth=1.5)

plt.axis('equal')
plt.grid(True)
plt.title('Unit Tangent (T, red) and Normal (N, blue) Vectors on $y = x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
