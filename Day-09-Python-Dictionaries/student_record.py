# Simple Student Record Program

student = {}

student["name"] = input("Enter student name: ")
student["roll_number"] = input("Enter roll number: ")
student["course"] = input("Enter course: ")

while True:
    try:
        student["marks"] = float(input("Enter marks (0-100): "))

        if 0 <= student["marks"] <= 100:
            break

        print("Marks must be between 0 and 100.")

    except ValueError:
        print("Please enter a valid number.")

print("\n--- Student Record ---")

for key, value in student.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
