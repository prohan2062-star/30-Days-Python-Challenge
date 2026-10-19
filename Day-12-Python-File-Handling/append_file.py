# Day 12: Appending Data to a File

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("I am improving my Python skills every day.\n")

print("New data appended successfully!")
