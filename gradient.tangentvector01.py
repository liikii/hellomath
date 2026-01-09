import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot unit sphere: f(x,y,z) = x^2 + y^2 + z^2 = 1
u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 15)
x_s = np.outer(np.cos(u), np.sin(v))
y_s = np.outer(np.sin(u), np.sin(v))
z_s = np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(x_s, y_s, z_s, color='lightblue', alpha=0.2, linewidth=0)

# Choose point P on the sphere: (1, 0, 0)
P = [1.0, 0.0, 0.0]
ax.scatter(P[0], P[1], P[2], color='red', s=100, label='Point P')

# Gradient of f = x^2 + y^2 + z^2 is <2x, 2y, 2z>
grad = [2*P[0], 2*P[1], 2*P[2]]  # = [2, 0, 0]

# Tangent vector: moving along equator (eastward direction)
tangent = [0.0, 1.0, 0.0]  # lies in tangent plane, perpendicular to grad

# Plot gradient vector (normal to surface)
ax.quiver(P[0], P[1], P[2], grad[0], grad[1], grad[2],
          color='blue', linewidth=3, arrow_length_ratio=0.1, label='Gradient (normal)')

# Plot tangent vector (direction of motion on level surface)
ax.quiver(P[0], P[1], P[2], tangent[0], tangent[1], tangent[2],
          color='green', linewidth=3, arrow_length_ratio=0.1, label='Tangent vector')

# Set plot limits and labels
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Gradient and Tangent Vector on Level Surface\n(Dot product = 0)')
ax.legend()

# Adjust viewing angle
ax.view_init(elev=20, azim=30)

plt.tight_layout()
plt.show()
