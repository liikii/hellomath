import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the function
def f(x, y):
    return x**2 - 2*x*y + 2*y

# Create grid
x = np.linspace(0, 3, 50)
y = np.linspace(0, 2, 50)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot surface
surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.7, edgecolor='none')

# Add contour lines on surface
ax.contour(X, Y, Z, zdir='z', offset=-1, colors='black', linewidths=0.5, alpha=0.6)

# Draw boundaries of rectangle D
# L1: x=0 (left side)
ax.plot([0, 0], [0, 2], [f(0,0), f(0,2)], 'r-', linewidth=2, label='$L_1$')
# L2: y=0 (bottom)
ax.plot([0, 3], [0, 0], [f(0,0), f(3,0)], 'g-', linewidth=2, label='$L_2$')
# L3: x=3 (right)
ax.plot([3, 3], [0, 2], [f(3,0), f(3,2)], 'b-', linewidth=2, label='$L_3$')
# L4: y=2 (top)
ax.plot([0, 3], [2, 2], [f(0,2), f(3,2)], 'm-', linewidth=2, label='$L_4$')

# Fill the base rectangle D in xy-plane
verts = [[0, 0, 0], [3, 0, 0], [3, 2, 0], [0, 2, 0]]
poly = Poly3DCollection([verts], alpha=0.3)
poly.set_facecolor('lightgreen')
ax.add_collection3d(poly)

# Labels and title
ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12)
ax.set_zlabel('$z$', fontsize=12)
ax.set_title(r'$f(x,y) = x^2 - 2xy + 2y$', fontsize=14)

# Legend
ax.legend()

# Limits
ax.set_xlim(0, 3)
ax.set_ylim(0, 2)
ax.set_zlim(-1, 9)

# View angle
ax.view_init(elev=20, azim=45)

plt.tight_layout()
plt.show()
