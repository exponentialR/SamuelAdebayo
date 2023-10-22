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

# Original and Barrel Distortion
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
fig1.suptitle('Original Grid vs Barrel Distortion')

plot_grid(ax1, x, y)
ax1.set_title('Original Grid')
ax1.axis('equal')

x_barrel = x * (1 + 0.5 * r ** 2)
y_barrel = y * (1 + 0.5 * r ** 2)
plot_grid(ax2, x_barrel, y_barrel, 'r-')
ax2.set_title('Barrel Distortion')
ax2.axis('equal')

# Original and Pincushion Distortion
fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(10, 5))
fig2.suptitle('Original Grid vs Pincushion Distortion')

plot_grid(ax3, x, y)
ax3.set_title('Original Grid')
ax3.axis('equal')

x_pincushion = x * (1 - 0.5 * r ** 2)
y_pincushion = y * (1 - 0.5 * r ** 2)
plot_grid(ax4, x_pincushion, y_pincushion, 'g-')
ax4.set_title('Pincushion Distortion')
ax4.axis('equal')

plt.show()
