import pandas as pd

df = pd.read_csv("students.csv")

print("Missing values before cleaning:")
print(df.isnull().sum())

# Fill missing DBMS marks with the column average
df["DBMS"] = df["DBMS"].fillna(df["DBMS"].mean())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned dataset:")
print(df)

df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned data saved to cleaned_students.csv")
