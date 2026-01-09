import numpy as np
import matplotlib.pyplot as plt

# 设置图形大小
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# ====== 1. 绕 x 轴旋转 (yz 平面) ======
def F_x(y, z):
    return -z, y  # Q, R

points_yz = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,-1), (-1,1)]
ax = axes[0]
for y, z in points_yz:
    Q, R = F_x(y, z)
    ax.arrow(y, z, Q, R, head_width=0.15, head_length=0.2, fc='red', ec='red', alpha=0.7)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, alpha=0.3)
ax.set_xlabel('y')
ax.set_ylabel('z')
ax.set_title('x axis rotation \n$\\mathbf{F} = \\langle 0, -z, y \\rangle$')
ax.axis('equal')

# ====== 2. 绕 y 轴旋转 (xz 平面) ======
def F_y(x, z):
    return z, -x  # P, R

points_xz = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,-1), (-1,1)]
ax = axes[1]
for x, z in points_xz:
    P, R = F_y(x, z)
    ax.arrow(x, z, P, R, head_width=0.15, head_length=0.2, fc='green', ec='green', alpha=0.7)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, alpha=0.3)
ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_title('y axis rotation \n$\\mathbf{F} = \\langle z, 0, -x \\rangle$')
ax.axis('equal')

# ====== 3. 绕 z 轴旋转 (xy 平面) ======
def F_z(x, y):
    return -y, x  # P, Q

points_xy = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,-1), (-1,1)]
ax = axes[2]
for x, y in points_xy:
    P, Q = F_z(x, y)
    ax.arrow(x, y, P, Q, head_width=0.15, head_length=0.2, fc='blue', ec='blue', alpha=0.7)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, alpha=0.3)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('z axis rotation \n$\\mathbf{F} = \\langle -y, x, 0 \\rangle$')
ax.axis('equal')

plt.tight_layout()
plt.show()
