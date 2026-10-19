import numpy as np

# Creating a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Matrix:")
print(matrix)

print("Dimensions:", matrix.ndim)
print("Shape:", matrix.shape)
print("Element at row 1, column 2:", matrix[0, 1])
print("Second row:", matrix[1])
