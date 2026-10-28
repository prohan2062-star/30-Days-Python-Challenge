import pandas as pd

df = pd.read_csv("cleaned_data.csv")

# Rename columns
df = df.rename(columns={
    "Name": "Student_Name",
    "Marks": "Total_Marks"
})

# Filter students scoring 80 or above
top_students = df[df["Total_Marks"] >= 80]

print("Students scoring 80 or above:")
print(top_students)

# Sort by marks in descending order
sorted_students = df.sort_values(
    by="Total_Marks",
    ascending=False
)

print("\nStudents sorted by marks:")
print(sorted_students)

# Basic statistics
print("\nAverage Marks:", df["Total_Marks"].mean())
print("Highest Marks:", df["Total_Marks"].max())
print("Lowest Marks:", df["Total_Marks"].min())

# Save final dataset
sorted_students.to_csv(
    "final_student_data.csv",
    index=False
)

print("\nFinal dataset exported successfully!")
