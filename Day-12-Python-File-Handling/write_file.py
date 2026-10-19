# Day 12: Writing to a File

with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Welcome to my Python journey!\n")
    file.write("Today I am learning file handling.\n")
    file.write("Day 12 of my Python Challenge.\n")

print("Data written successfully!")
