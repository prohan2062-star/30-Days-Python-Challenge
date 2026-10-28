import pandas as pd

# Load dataset
df = pd.read_csv("messy_data.csv")

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Marks with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Standardize text columns
df["Name"] = df["Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

# Convert Age to integer
df["Age"] = df["Age"].astype(int)

print("\nCleaned Dataset:")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")
