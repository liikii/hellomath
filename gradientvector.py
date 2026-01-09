import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x, y) = x^2 - y^2
def f(x, y):
    return x**2 - y**2

# Compute gradient: ∇f = <2x, -2y>
def grad_f(x, y):
    return 2*x, -2*y

# Create grid of points
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

# Compute z values and gradients
Z = f(X, Y)
U, V = grad_f(X, Y)  # U = ∂f/∂x, V = ∂f/∂y

# Plot contour lines (level curves)
plt.figure(figsize=(8, 8))
contours = plt.contour(X, Y, Z, levels=[-9, -6, -3, -1, 0, 1, 3, 6, 9], colors='purple', alpha=0.7, linewidths=1.5)
plt.clabel(contours, inline=True, fontsize=10, fmt='%.0f')

# Plot gradient vector field
plt.quiver(X, Y, U, V, color='cyan', scale=15, angles='xy', scale_units='xy',
           label='Gradient vectors $\\nabla f$')

# Add labels and title
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$y$', fontsize=12)
plt.title('Contour Map and Gradient Vector Field\nof $f(x,y) = x^2 - y^2$', fontsize=14)
plt.grid(True, alpha=0.3)
plt.axis('equal')  # Keep aspect ratio equal
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
