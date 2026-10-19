# Day 12: Reading from a File

with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("File Content:")
print(content)
