# Day 04 - For Loop
# 30 Days Python Challenge

# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Print even numbers from 1 to 20
print("\nEven Numbers:")

for i in range(2, 21, 2):
    print(i)

# Multiplication table
number = 5

print("\nMultiplication Table of", number)

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
