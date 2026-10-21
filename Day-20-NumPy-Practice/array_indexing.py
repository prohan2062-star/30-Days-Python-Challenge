import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Matrix:")
print(matrix)

print("First row:", matrix[0])
print("Second column:", matrix[:, 1])
print("Element at row 2, column 3:", matrix[1, 2])

# Unique values
values = np.array([1, 2, 2, 3, 4, 4, 5])
print("Unique values:", np.unique(values))
