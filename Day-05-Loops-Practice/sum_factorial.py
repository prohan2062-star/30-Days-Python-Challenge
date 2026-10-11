# Day 05 - Sum and Factorial

# Sum of numbers from 1 to 100
total = 0

for number in range(1, 101):
    total += number

print("Sum from 1 to 100:", total)

# Factorial of a number
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative integers.")
else:
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print("Factorial:", factorial)
