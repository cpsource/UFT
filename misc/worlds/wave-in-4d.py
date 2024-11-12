import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define wave parameters
A = 1  # amplitude
k_x, k_y, k_z = 1, 1, 1  # wave numbers for each dimension
omega = 1  # angular frequency
w_values = np.linspace(0, 2 * np.pi, 100)  # different w-slices over time

# Set up the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate 3D grid
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
z = np.linspace(-5, 5, 50)
X, Y, Z = np.meshgrid(x, y, z)

# Function to update the wave for each frame
def update(frame):
    ax.clear()
    w = w_values[frame]
    wave = A * np.sin(k_x * X + k_y * Y + k_z * Z - omega * frame + w)
    # Plot the 3D wave at this slice
    ax.scatter(X, Y, Z, c=wave, cmap='viridis', marker='o', alpha=0.3)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)

# Create the animation
ani = FuncAnimation(fig, update, frames=len(w_values), interval=50)
plt.show()

