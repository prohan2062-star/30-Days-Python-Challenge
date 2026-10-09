# Day 03 - Conditional Statements
# 30 Days Python Challenge

# Example 1: if statement
age = 20

if age >= 18:
    print("You are an adult.")

# Example 2: if-else statement
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# Example 3: if-elif-else
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Needs Improvement")

# Example 4: Logical operators
age = 22
has_license = True

if age >= 18 and has_license:
    print("Can drive")
else:
    print("Cannot drive")
