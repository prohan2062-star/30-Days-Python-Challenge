# Mini Project: Student Marks Analyzer

marks = []

for i in range(5):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("\n--- Student Result ---")
print("Marks:", marks)
print("Total Marks:", total)
print("Average:", average)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))

marks.sort(reverse=True)
print("Marks in Descending Order:", marks)
