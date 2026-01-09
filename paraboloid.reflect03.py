"""
Parabolic Reflector - Optical Focusing Property
Demonstrates how a parabolic surface reflects parallel rays to a single focal point.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):
    """Custom 3D arrow for ray visualization"""

    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        super().draw(renderer)


def parabolic_reflection(x, y, focus_distance=0.25):
    """
    Calculate reflection of parallel rays from parabolic surface.

    Parameters:
    x, y: Coordinates on parabolic surface
    focus_distance: Distance from vertex to focus (f in z = (x²+y²)/(4f))

    Returns:
    incident_dir: Direction vector of incoming parallel ray
    normal: Surface normal vector
    reflected_dir: Direction vector of reflected ray
    """
    # Parabolic surface equation: z = (x² + y²) / (4f)
    f = focus_distance
    z = (x ** 2 + y ** 2) / (4 * f)

    # Gradient of surface (partial derivatives)
    dz_dx = x / (2 * f)
    dz_dy = y / (2 * f)

    # Surface normal vector (pointing outward)
    normal = np.array([-dz_dx, -dz_dy, 1])
    normal = normal / np.linalg.norm(normal)  # Normalize

    # Incoming parallel rays (vertical downward)
    incident_dir = np.array([0, 0, -1])

    # Reflection direction: R = I - 2*(I·N)*N
    dot_product = np.dot(incident_dir, normal)
    reflected_dir = incident_dir - 2 * dot_product * normal
    reflected_dir = reflected_dir / np.linalg.norm(reflected_dir)  # Normalize

    return incident_dir, normal, reflected_dir, z


# ============================================
# SIMPLIFIED VERSION - Main visualization
# ============================================

# Create parabolic surface
f = 0.25  # Focal length
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)
Z = (X ** 2 + Y ** 2) / (4 * f)

# Create figure
fig = plt.figure(figsize=(14, 6))

# ============================================
# Subplot 1: 3D visualization WITHOUT Arrow3D
# ============================================
ax1 = fig.add_subplot(121, projection='3d')

# Plot parabolic surface
surf = ax1.plot_surface(X, Y, Z,
                        cmap='viridis',
                        alpha=0.7,
                        rstride=2,
                        cstride=2,
                        linewidth=0.1,
                        antialiased=True)

# Add focus point
focus_point = [0, 0, f]
ax1.scatter(*focus_point, color='red', s=100, label='Focus Point', zorder=5)
ax1.text(0, 0, f + 0.05, 'Focus', color='red', fontsize=10, fontweight='bold')

# Add vertex (lowest point of parabola)
vertex = [0, 0, 0]
ax1.scatter(*vertex, color='blue', s=50, label='Vertex', zorder=5)
ax1.text(0, 0, -0.05, 'Vertex', color='blue', fontsize=10, fontweight='bold')

# Draw incoming parallel rays and reflected rays (simplified)
num_rays = 8
ray_start_z = 2.0  # Starting height for incoming rays

# Create rays symmetrically distributed
ray_positions = np.linspace(-0.8, 0.8, num_rays)

for i, pos in enumerate(ray_positions):
    # Alternate between x and y directions for better visualization
    if i % 2 == 0:
        x_pos, y_pos = pos, 0
    else:
        x_pos, y_pos = 0, pos

    # Calculate surface intersection
    z_surface = (x_pos ** 2 + y_pos ** 2) / (4 * f)

    # Incoming ray (vertical) - blue dashed
    ax1.plot([x_pos, x_pos], [y_pos, y_pos], [ray_start_z, z_surface],
             'b--', linewidth=1, alpha=0.7)

    # Get reflection direction
    _, _, reflected_dir, _ = parabolic_reflection(x_pos, y_pos, f)

    # Draw reflected ray - red solid (longer to show convergence)
    scale = 2.0  # Length of reflected ray
    ax1.plot([x_pos, x_pos + reflected_dir[0] * scale],
             [y_pos, y_pos + reflected_dir[1] * scale],
             [z_surface, z_surface + reflected_dir[2] * scale],
             'r-', linewidth=2, alpha=0.8)

    # Add arrowhead manually (simple line with a small marker)
    arrow_length = 0.15
    ax1.plot([x_pos + reflected_dir[0] * (scale - arrow_length),
              x_pos + reflected_dir[0] * scale],
             [y_pos + reflected_dir[1] * (scale - arrow_length),
              y_pos + reflected_dir[1] * scale],
             [z_surface + reflected_dir[2] * (scale - arrow_length),
              z_surface + reflected_dir[2] * scale],
             'r-', linewidth=3, alpha=0.8)

# Draw optical axis
ax1.plot([0, 0], [0, 0], [-0.5, 2.5], 'k--', linewidth=1, alpha=0.5, label='Optical Axis')

# Add focal plane (dashed circle at focus)
theta = np.linspace(0, 2 * np.pi, 100)
focal_circle_radius = 0.1
ax1.plot(focal_circle_radius * np.cos(theta),
         focal_circle_radius * np.sin(theta),
         [f] * 100, 'r--', linewidth=1, alpha=0.5)

# Configuration
ax1.set_title('3D Parabolic Reflector - Ray Focusing\n$z = \\frac{x^2 + y^2}{4f}$, $f = 0.25$',
              fontsize=12, pad=20)
ax1.set_xlabel('X', labelpad=10)
ax1.set_ylabel('Y', labelpad=10)
ax1.set_zlabel('Z', labelpad=10)
ax1.set_xlim(-1.2, 1.2)
ax1.set_ylim(-1.2, 1.2)
ax1.set_zlim(-0.5, 2.5)
ax1.view_init(elev=25, azim=45)
ax1.legend(loc='upper right', fontsize=9)

# ============================================
# Subplot 2: 2D cross-section for clarity
# ============================================
ax2 = fig.add_subplot(122)

# 2D parabolic cross-section (y=0)
x_2d = np.linspace(-1, 1, 100)
z_2d = x_2d ** 2 / (4 * f)

# Plot parabolic curve
ax2.plot(x_2d, z_2d, 'g-', linewidth=2, label='Parabolic Curve')

# Focus point in 2D
ax2.scatter(0, f, color='red', s=80, zorder=5, label='Focus')
ax2.text(0.05, f, 'Focus', color='red', fontsize=10, fontweight='bold')

# Vertex
ax2.scatter(0, 0, color='blue', s=60, zorder=5, label='Vertex')
ax2.text(0.05, 0, 'Vertex', color='blue', fontsize=10, fontweight='bold')

# Draw sample rays
ray_heights = np.linspace(-0.8, 0.8, 6)

for height in ray_heights:
    if abs(height) < 0.05:  # Skip very close to center
        continue

    # Surface intersection
    z_intersect = height ** 2 / (4 * f)

    # Incoming ray (vertical from top)
    ax2.plot([height, height], [2.0, z_intersect], 'b--', linewidth=1, alpha=0.6)

    # Reflected ray to focus
    ax2.plot([height, 0], [z_intersect, f], 'r-', linewidth=1.5, alpha=0.8)

    # Add arrowhead
    ax2.arrow(height * 0.6, z_intersect + (f - z_intersect) * 0.4,
              0, (f - z_intersect) * 0.2,
              head_width=0.03, head_length=0.05,
              fc='red', ec='red', alpha=0.8)

# Draw optical axis
ax2.axvline(x=0, color='k', linestyle='--', linewidth=1, alpha=0.5, label='Optical Axis')

# Add focal length indicator
ax2.plot([0, 0], [0, f], 'k:', linewidth=1, alpha=0.7)
ax2.text(0.1, f / 2, f'f = {f}', fontsize=9, verticalalignment='center')

# Draw parallel rays at top with arrowheads
for height in ray_heights:
    ax2.arrow(height, 2.1, 0, -0.05, head_width=0.03, head_length=0.05,
              fc='blue', ec='blue', alpha=0.7)

# Configuration
ax2.set_title('2D Cross-Section (y=0)\nAll Reflected Rays Converge to Focus',
              fontsize=12, pad=15)
ax2.set_xlabel('X Position', fontsize=10)
ax2.set_ylabel('Z Height', fontsize=10)
ax2.set_xlim(-1.2, 1.2)
ax2.set_ylim(-0.2, 2.2)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.legend(loc='upper right', fontsize=9)
ax2.set_aspect('equal', adjustable='box')

# Add informative text
fig.text(0.02, 0.98,
         'Optical Principle: Parallel rays incident on a parabolic reflector\n'
         'are all reflected to pass through a single focal point.',
         fontsize=10,
         verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()

# ============================================
# Additional: Clean high-density visualization
# ============================================

fig2, ax3 = plt.subplots(figsize=(10, 8))
ax3 = fig2.add_subplot(111, projection='3d')

# Create denser grid for smoother surface
x_dense = np.linspace(-1, 1, 80)
y_dense = np.linspace(-1, 1, 80)
X_dense, Y_dense = np.meshgrid(x_dense, y_dense)
Z_dense = (X_dense ** 2 + Y_dense ** 2) / (4 * f)

# Plot surface with contour
surf2 = ax3.plot_surface(X_dense, Y_dense, Z_dense,
                         cmap='summer',
                         alpha=0.8,
                         rstride=1,
                         cstride=1,
                         linewidth=0.2,
                         antialiased=True)

# Mark focus with larger point
ax3.scatter(0, 0, f, color='red', s=200, edgecolors='black', linewidth=1.5,
            label='Focal Point', zorder=10)

# Draw many reflected rays to show convergence (simplified)
ray_density = 12  # Reduced for clarity
x_rays = np.linspace(-0.9, 0.9, ray_density)
y_rays = np.linspace(-0.9, 0.9, ray_density)

for x_r in x_rays:
    for y_r in y_rays:
        # Only draw if within circular aperture
        if np.sqrt(x_r ** 2 + y_r ** 2) <= 0.9:
            # Calculate surface point
            z_r = (x_r ** 2 + y_r ** 2) / (4 * f)

            # Draw incoming ray
            ax3.plot([x_r, x_r], [y_r, y_r], [2.0, z_r],
                     'b', linewidth=0.5, alpha=0.4)

            # Draw reflected ray to focus
            ax3.plot([x_r, 0], [y_r, 0], [z_r, f],
                     'r', linewidth=0.8, alpha=0.6)

# Configuration
ax3.set_title('Parabolic Reflector: Perfect Light Focusing\n$z = (x^2 + y^2) / 4f$',
              fontsize=14, pad=20)
ax3.set_xlabel('X Axis', labelpad=12)
ax3.set_ylabel('Y Axis', labelpad=12)
ax3.set_zlabel('Z Axis', labelpad=12)
ax3.set_xlim(-1.2, 1.2)
ax3.set_ylim(-1.2, 1.2)
ax3.set_zlim(-0.5, 2.5)
ax3.view_init(elev=20, azim=35)
ax3.legend(loc='upper right', fontsize=10)

# Add colorbar
fig2.colorbar(surf2, ax=ax3, shrink=0.6, aspect=20, pad=0.1, label='Surface Height')

plt.tight_layout()
plt.show()

# ============================================
# BONUS: Simple 2D parabolic reflector diagram
# ============================================

fig3, (ax4, ax5) = plt.subplots(1, 2, figsize=(12, 5))

# Left: Parabolic reflector principle
ax4.set_aspect('equal')
x_para = np.linspace(-2, 2, 200)
y_para = x_para ** 2 / 4

ax4.plot(x_para, y_para, 'k-', linewidth=2)
ax4.plot(x_para, -y_para, 'k-', linewidth=2)  # Mirror image

# Draw focus
ax4.scatter(0, 1, color='red', s=100, zorder=5)
ax4.text(0.1, 1.1, 'Focus (F)', color='red', fontweight='bold')

# Draw sample parallel rays
for x_in in [-1.5, -1, -0.5, 0.5, 1, 1.5]:
    # Incoming ray
    ax4.plot([x_in, x_in], [3, x_in ** 2 / 4], 'b--', alpha=0.6)
    # Reflected ray
    ax4.plot([x_in, 0], [x_in ** 2 / 4, 1], 'r-', alpha=0.8)

ax4.set_xlim(-2.5, 2.5)
ax4.set_ylim(-1, 3.5)
ax4.set_title('Parabolic Reflector Principle', fontsize=12)
ax4.set_xlabel('Horizontal Distance')
ax4.set_ylabel('Vertical Height')
ax4.grid(True, alpha=0.3)

# Right: Real-world applications
ax5.axis('off')
ax5.text(0.1, 0.9, 'Real-World Applications:', fontsize=12, fontweight='bold')
ax5.text(0.1, 0.8, '• Satellite Dishes', fontsize=10)
ax5.text(0.1, 0.7, '• Telescope Mirrors', fontsize=10)
ax5.text(0.1, 0.6, '• Solar Concentrators', fontsize=10)
ax5.text(0.1, 0.5, '• Headlight Reflectors', fontsize=10)
ax5.text(0.1, 0.4, '• Radio Telescopes', fontsize=10)
ax5.text(0.1, 0.3, '• Sound Reflectors', fontsize=10)
ax5.set_title('Applications of Parabolic Reflectors', fontsize=12)

plt.tight_layout()
plt.show()
