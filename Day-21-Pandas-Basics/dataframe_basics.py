import pandas as pd

data = {
    "Name": ["Rohan", "Amit", "Priya", "Sneha", "Rahul"],
    "Python": [85, 90, 78, 92, 70],
    "DBMS": [80, 88, 82, 95, 75]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nColumn names:")
print(df.columns)

print("\nData information:")
df.info()

print("\nSummary statistics:")
print(df.describe())
