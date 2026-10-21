import pandas as pd

data = {
    "Name": ["Rohan", "Amit", "Priya", "Sneha", "Rahul"],
    "Python": [85, 65, 90, 72, 55],
    "DBMS": [80, 70, 88, 75, 60],
    "OS": [78, 68, 92, 80, 58]
}

df = pd.DataFrame(data)

subjects = ["Python", "DBMS", "OS"]

df["Average"] = df[subjects].mean(axis=1)
df["Result"] = df["Average"].apply(
    lambda avg: "Pass" if avg >= 35 else "Fail"
)

print("Student Performance Analysis:")
print(df)

print("\nClass average by subject:")
print(df[subjects].mean())

print("\nTop performer:")
print(df.loc[df["Average"].idxmax()])

print("\nStudents with average above 75:")
print(df[df["Average"] > 75])
