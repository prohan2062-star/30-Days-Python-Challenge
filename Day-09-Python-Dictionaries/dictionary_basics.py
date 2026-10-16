# Day 9: Dictionary Basics

student = {
    "name": "Rohan",
    "age": 19,
    "course": "BSc Computer Science",
    "language": "Python"
}

print("Student Details:", student)
print("Name:", student["name"])
print("Course:", student["course"])

# Access a value safely
print("City:", student.get("city", "Not provided"))
