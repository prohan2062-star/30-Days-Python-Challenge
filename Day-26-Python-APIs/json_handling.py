import json

student = {
    "name": "Rohan",
    "course": "BSc Computer Science",
    "skills": ["Python", "Pandas", "NumPy"]
}

# Convert Python dictionary to JSON string
json_data = json.dumps(student, indent=4)
print("JSON Data:")
print(json_data)

# Save JSON to a file
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

# Read JSON from the file
with open("student.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("\nStudent Name:", loaded_data["name"])
print("Skills:", loaded_data["skills"])
