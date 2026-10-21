import numpy as np

marks = np.array([75, 88, 92, 64, 80, 55, 95, 72])

print("Student Marks:", marks)
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Median Marks:", np.median(marks))

passed = marks[marks >= 35]
print("Passed Marks:", passed)
print("Number of students passed:", len(passed))

above_average = marks[marks > np.mean(marks)]
print("Marks Above Average:", above_average)
