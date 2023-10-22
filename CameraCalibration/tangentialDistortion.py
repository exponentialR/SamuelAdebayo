import matplotlib.pyplot as plt
import numpy as np


# Function to plot original and distorted grid
def plot_grid(ax, x, y, color='b-', linewidth=1):
    for i in range(x.shape[0]):
        ax.plot(x[i, :], y[i, :], color, linewidth=linewidth)
    for i in range(x.shape[1]):
        ax.plot(x[:, i], y[:, i], color, linewidth=linewidth)


# Create a grid
x, y = np.meshgrid(np.linspace(-1, 1, 11), np.linspace(-1, 1, 11))

# Calculate radius
r = np.sqrt(x ** 2 + y ** 2)

# Original and Tangential Distortion
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
fig1.suptitle('Original Grid vs Tangential Distortion')

plot_grid(ax1, x, y)
ax1.set_title('Original Grid')
ax1.axis('equal')

# Tangential Distortion Coefficients (for demonstration, you might want to estimate these in a real scenario)
p1, p2 = 0.2, 0.1

# Apply Tangential Distortion
x_tangential = x + (2 * p1 * x * y + p2 * (r ** 2 + 2 * x ** 2))
y_tangential = y + (p1 * (r ** 2 + 2 * y ** 2) + 2 * p2 * x * y)

plot_grid(ax2, x_tangential, y_tangential, 'm-')
ax2.set_title('Tangential Distortion')
ax2.axis('equal')

plt.show()
