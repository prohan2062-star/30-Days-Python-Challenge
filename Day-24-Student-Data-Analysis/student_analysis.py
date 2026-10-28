import pandas as pd

# Load the dataset
df = pd.read_csv("students.csv")

subjects = ["Python", "DBMS", "OS"]

# Calculate each student's average
df["Average"] = df[subjects].mean(axis=1).round(2)

# Assign grades based on average marks
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 35:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Average"].apply(calculate_grade)

# Display student analysis
print("=== STUDENT DATA ANALYSIS ===")
print(df)

# Subject-wise average
print("\n=== SUBJECT-WISE AVERAGE ===")
print(df[subjects].mean().round(2))

# Top-performing student
top_index = df["Average"].idxmax()

print("\n=== TOP PERFORMER ===")
print(df.loc[top_index, ["Name", "Average", "Grade"]])

# Students with an average of 75 or above
print("\n=== STUDENTS WITH AVERAGE >= 75 ===")
print(df[df["Average"] >= 75][["Name", "Average", "Grade"]])

# Save results
df.to_csv("student_analysis_results.csv", index=False)

print("\nAnalysis completed!")
print("Results saved to student_analysis_results.csv")
