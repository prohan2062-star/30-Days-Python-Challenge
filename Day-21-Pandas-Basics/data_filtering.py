import pandas as pd

data = {
    "Name": ["Rohan", "Amit", "Priya", "Sneha", "Rahul"],
    "Marks": [85, 45, 78, 92, 30],
    "City": ["Nashik", "Pune", "Mumbai", "Nashik", "Pune"]
}

df = pd.DataFrame(data)

print("All Students:")
print(df)

print("\nStudents with marks above 75:")
print(df[df["Marks"] > 75])

print("\nStudents from Nashik:")
print(df[df["City"] == "Nashik"])

print("\nSelected columns:")
print(df[["Name", "Marks"]])
