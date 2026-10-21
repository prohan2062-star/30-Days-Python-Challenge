import numpy as np

numbers = np.arange(1, 13)

print("Original Array:")
print(numbers)

matrix = numbers.reshape(3, 4)

print("\nReshaped Array:")
print(matrix)

print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
