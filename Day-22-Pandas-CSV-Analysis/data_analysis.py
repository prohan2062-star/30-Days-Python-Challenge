import pandas as pd

df = pd.read_csv("cleaned_students.csv")

subjects = ["Python", "DBMS", "OS"]

# Calculate each student's average
df["Average"] = df[subjects].mean(axis=1)

print("Student averages:")
print(df[["Name", "Average"]])

print("\nSubject-wise averages:")
print(df[subjects].mean())

print("\nStudents scoring above 75 average:")
print(df[df["Average"] > 75][["Name", "Average"]])

print("\nTop performer:")
top_index = df["Average"].idxmax()
print(df.loc[top_index, ["Name", "Average"]])
