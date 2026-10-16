# Adding, Updating, and Deleting Dictionary Items

student = {
    "name": "Rohan",
    "age": 19,
    "course": "BSc Computer Science"
}

# Add a new key-value pair
student["city"] = "Maharashtra"

# Update an existing value
student["age"] = 20

print("After adding and updating:", student)

# Remove a key
student.pop("city")

print("After removing city:", student)
print("Number of items:", len(student))+
