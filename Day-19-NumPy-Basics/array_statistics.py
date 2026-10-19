import numpy as np

marks = np.array([75, 85, 90, 65, 80])

print("Marks:", marks)
print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))
print("Sorted marks:", np.sort(marks))

if np.mean(marks) >= 75:
    print("Result: Good performance!")
else:
    print("Result: Keep practicing!")
