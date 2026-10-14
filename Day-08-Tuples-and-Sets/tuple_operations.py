# Tuple Operations

numbers = (10, 20, 30, 40, 50)

print("Original tuple:", numbers)

# Tuple concatenation
more_numbers = numbers + (60, 70)
print("After concatenation:", more_numbers)

# Repetition
repeated = (1, 2) * 3
print("Repeated tuple:", repeated)

# Count and index
values = (10, 20, 10, 30, 10)

print("Count of 10:", values.count(10))
print("Index of 20:", values.index(20))

# Tuple unpacking
name, age, city = ("Rohan", 19, "Maharashtra")

print("Name:", name)
print("Age:", age)
print("City:", city)
