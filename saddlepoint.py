"""
临界点可能是极大值、极小值，也可能是鞍点！
critical point may be maxima or minima or saddle point
局部最大值：如果在该点的周围小范围内，所有其他点的函数值都不大于该点的函数值，则称该点为局部最大值。
局部最小值：如果在该点的周围小范围内，所有其他点的函数值都不小于该点的函数值，则称该点为局部最小值。
鞍点：如果一个临界点既不是局部最大值也不是局部最小值，那么它可能是一个鞍点。鞍点的特点是在某些方向上函数值增加，而在另一些方向上函数值减少。
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# Define the function f(x, y) = x^2 - y^2
def f(x, y):
    return x**2 - y**2

# Generate data points
x = np.linspace(-5, 5, 100)  # Create an array of 100 equally spaced values from -5 to 5 for x
y = np.linspace(-5, 5, 100)  # Create an array of 100 equally spaced values from -5 to 5 for y
x, y = np.meshgrid(x, y)     # Create a grid of points representing all combinations of x and y values
z = f(x, y)                  # Compute the z values by applying the function to each point on the grid

# Create a figure and a 3D axis
fig = plt.figure(figsize=(10, 7))  # Set the size of the figure
ax = fig.add_subplot(111, projection='3d')  # Add a 3D subplot to the figure

# Plot the surface on the 3D axis
surf = ax.plot_surface(x, y, z, cmap='viridis')  # Plot the surface using the x, y, z coordinates and apply colormap

# Add a color bar which maps values to colors
fig.colorbar(surf)  # Add a color bar to the side of the plot

# Set labels for axes
ax.set_xlabel('X Axis')  # Label for X axis
ax.set_ylabel('Y Axis')  # Label for Y axis
ax.set_zlabel('Z Axis (f(x,y))')  # Label for Z axis, representing the function value

# Display the plot
plt.show()  # Show the plot on screen
