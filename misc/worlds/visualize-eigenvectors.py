import numpy as np
import matplotlib.pyplot as plt

# Define matrix A
A = np.array([[2, 1], [1, 2]])

# Define grid
X, Y = np.meshgrid(np.linspace(-2, 2, 10), np.linspace(-2, 2, 10))
grid = np.vstack([X.flatten(), Y.flatten()])

# Transform grid using matrix A
transformed_grid = A @ grid

# Plot original grid
plt.quiver(grid[0], grid[1], angles='xy', scale_units='xy', scale=1, color="lightgray")
# Plot transformed grid
plt.quiver(transformed_grid[0], transformed_grid[1], angles='xy', scale_units='xy', scale=1, color="blue")

# Plot eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
for eigenvector in eigenvectors.T:
    plt.plot([0, eigenvector[0]*3], [0, eigenvector[1]*3], color="red", linewidth=2)

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

