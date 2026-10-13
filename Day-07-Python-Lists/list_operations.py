# Python List Operations

numbers = [10, 20, 30, 40]

# Add elements
numbers.append(50)
numbers.insert(1, 15)
print("After Adding:", numbers)

# Remove elements
numbers.remove(30)
numbers.pop()
print("After Removing:", numbers)

# Sorting and reversing
numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
