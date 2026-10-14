# Day 8: Set Basics

numbers = {10, 20, 30, 20, 10}

print("Set with duplicates removed:", numbers)

numbers.add(40)
print("After adding 40:", numbers)

numbers.discard(20)
print("After removing 20:", numbers)

print("Is 30 present?", 30 in numbers)

# Create an empty set
empty_set = set()
print("Empty set:", empty_set)
