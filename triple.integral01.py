import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches


def draw_3d_cuboid_grid(x_dim, y_dim, z_dim):
    """
    Draws a 3D cuboid with a grid mesh using matplotlib.
    """
    # Create the figure and a 3D subplot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Define the dimensions of the cuboid
    axes = [x_dim, y_dim, z_dim]

    # Create data array (1s represent occupied voxels)
    data = np.ones(axes, dtype=bool)

    # Define colors and transparency (blue color for all voxels)
    alpha = 0.7  # transparency
    # Note: data array size is axes, the colors array needs to match that size for voxels call
    colors = np.empty(axes + [4], dtype=np.float32)
    colors[:] = [0.1, 0.5, 0.8, alpha]  # A shade of blue

    # Plot the voxels
    ax.voxels(data, facecolors=colors, edgecolor='skyblue', linewidth=0.5)

    # Set axis limits
    ax.set_xlim(0, x_dim)
    ax.set_ylim(0, y_dim)
    ax.set_zlim(0, z_dim)

    # Set axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # Position the axes to look like the image (adjust elevation and azimuth)
    ax.view_init(elev=20, azim=-45)  # Adjust viewing angle

    # Add the label 'B' (approximated position)
    ax.text(0, 0, z_dim * 1.1, 'B', color='black', fontsize=14, ha='center', va='bottom')

    # Add arrows to represent positive axis direction
    # *** MODIFIED: Increased length here ***
    ax.quiver(0, 0, 0, 1, 0, 0, length=x_dim * 1.3, color='k', arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, 1, 0, length=y_dim * 1.3, color='k', arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, 0, 1, length=z_dim * 1.3, color='k', arrow_length_ratio=0.08)

    plt.title('3D Cuboid Grid Visualization with Longer Axes')
    plt.show()


# Example usage: Creates a 10x6x5 cuboid grid
draw_3d_cuboid_grid(10, 6, 5)
