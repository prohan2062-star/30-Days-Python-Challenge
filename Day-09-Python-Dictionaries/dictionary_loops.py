# Looping Through a Dictionary

marks = {
    "Python": 85,
    "DBMS": 78,
    "Operating Systems": 82,
    "Data Structures": 88
}

print("Subjects and Marks:")

for subject, mark in marks.items():
    print(f"{subject}: {mark}")

print("\nAll Subjects:")
for subject in marks.keys():
    print(subject)

print("\nAll Marks:")
for mark in marks.values():
    print(mark)
