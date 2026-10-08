# Day 02 - Operators & Expressions
# 30 Days Python Challenge

# 1. Arithmetic Operators

a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 2. Modulus, Floor Division and Power

a = 17
b = 5

print("Remainder:", a % b)
print("Floor Division:", a // b)
print("Power:", a ** b)

# 3. Comparison Operators

x = 10
y = 5

print("x > y:", x > y)
print("x < y:", x < y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)

# 4. Logical Operators

age = 20

print("AND:", age >= 18 and age <= 60)
print("OR:", age < 18 or age > 60)
print("NOT:", not(age < 18))

# 5. Assignment Operators

number = 10

number += 5
print("After +=:", number)

number -= 2
print("After -=:", number)

number *= 2
print("After *=:", number)

# 6. Membership Operators

name = "Rohan"

print("R" in name)
print("z" in name)

# 7. Operator Precedence

result = 10 + 5 * 2
print("Precedence Result:", result)
