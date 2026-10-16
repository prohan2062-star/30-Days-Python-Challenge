# Student Result System Using Functions

def calculate_percentage(marks, total_marks):
    if total_marks <= 0:
        return None

    return (marks / total_marks) * 100


def get_result(percentage):
    if percentage is None or not 0 <= percentage <= 100:
        return "Invalid marks"

    if percentage >= 75:
        return "Distinction"
    elif percentage >= 60:
        return "First Class"
    elif percentage >= 35:
        return "Pass"
    else:
        return "Fail"


marks = float(input("Enter marks obtained: "))
total = float(input("Enter total marks: "))

percentage = calculate_percentage(marks, total)

print("Percentage:", percentage)
print("Result:", get_result(percentage))
