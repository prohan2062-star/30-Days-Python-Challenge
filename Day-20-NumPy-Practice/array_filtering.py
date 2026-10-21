import numpy as np

numbers = np.array([12, 25, 8, 40, 17, 30, 5, 50])

print("Original Array:", numbers)

# Filter numbers greater than 20
filtered = numbers[numbers > 20]
print("Numbers greater than 20:", filtered)

# Find even numbers
even_numbers = numbers[numbers % 2 == 0]
print("Even numbers:", even_numbers)

# Find numbers between 10 and 40
selected = numbers[(numbers >= 10) & (numbers <= 40)]
print("Numbers between 10 and 40:", selected)
