import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the unit sphere: F(x,y,z) = x^2 + y^2 + z^2 - 1 = 0
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, np.pi, 20)
x_s = np.outer(np.cos(u), np.sin(v))
y_s = np.outer(np.sin(u), np.sin(v))
z_s = np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(x_s, y_s, z_s, color='lightblue', alpha=0.3, linewidth=0)

# Point on the sphere: P = (1, 0, 0)
P = np.array([1.0, 0.0, 0.0])
ax.scatter(P[0], P[1], P[2], color='red', s=80, label='Point P')

# Gradient of F = <2x, 2y, 2z> at P
grad_F = np.array([2*P[0], 2*P[1], 2*P[2]])  # = [2, 0, 0]

# Draw the normal vector (gradient direction) from P
ax.quiver(P[0], P[1], P[2], grad_F[0], grad_F[1], grad_F[2],
          color='red', linewidth=2, arrow_length_ratio=0.1, label='Normal vector (∇F)')

# Draw the full normal line (extend in both directions)
t_line = np.linspace(-1.5, 1.5, 100)
normal_line = P + np.outer(t_line, grad_F)
ax.plot(normal_line[:, 0], normal_line[:, 1], normal_line[:, 2],
        color='red', linestyle='--', linewidth=1.5, label='Normal line')

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Surface and Normal Line at Point P\n(Gradient is normal to level surface)')

# Set equal aspect ratio for better visualization
max_range = 1.5
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

# Add legend
ax.legend()

# Adjust viewing angle
ax.view_init(elev=20, azim=40)

plt.tight_layout()
plt.show()
