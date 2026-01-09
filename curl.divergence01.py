import numpy as np
import matplotlib.pyplot as plt

# Set up the grid
x = np.linspace(-4, 4, 15)
y = np.linspace(-4, 4, 15)
X, Y = np.meshgrid(x, y)

# Vector field 1: F1 = x i + y j (Radial Divergence Field)
U1 = X
V1 = Y

# Vector field 2: F2 = -y i + x j (Rotational Field)
U2 = -Y
V2 = X

# Total vector field: F = F1 + F2
U_total = U1 + U2
V_total = V1 + V2

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1: F1
axs[0].quiver(X, Y, U1, V1, color='blue', scale=10)
axs[0].set_xlim(-5, 5)
axs[0].set_ylim(-5, 5)
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].set_title(r'$\mathbf{F}_1 = x\,\mathbf{i} + y\,\mathbf{j}$ (Radial Divergence)')
axs[0].grid(True)
axs[0].axhline(0, color='black', linewidth=0.5)
axs[0].axvline(0, color='black', linewidth=0.5)

# Plot 2: F2
axs[1].quiver(X, Y, U2, V2, color='green', scale=10)
axs[1].set_xlim(-5, 5)
axs[1].set_ylim(-5, 5)
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].set_title(r'$\mathbf{F}_2 = -y\,\mathbf{i} + x\,\mathbf{j}$ (Rotational)')
axs[1].grid(True)
axs[1].axhline(0, color='black', linewidth=0.5)
axs[1].axvline(0, color='black', linewidth=0.5)

# Plot 3: F = F1 + F2
axs[2].quiver(X, Y, U_total, V_total, color='red', scale=10)
axs[2].set_xlim(-5, 5)
axs[2].set_ylim(-5, 5)
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].set_title(r'$\mathbf{F} = \mathbf{F}_1 + \mathbf{F}_2$ (Divergence and Rotation)')
axs[2].grid(True)
axs[2].axhline(0, color='black', linewidth=0.5)
axs[2].axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.show()
