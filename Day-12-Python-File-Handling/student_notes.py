# Mini Project: Student Notes Manager

filename = "student_notes.txt"

print("=== Student Notes Manager ===")
print("1. Add a note")
print("2. View all notes")

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    note = input("Enter your note: ")

    with open(filename, "a", encoding="utf-8") as file:
        file.write(note + "\n")

    print("Note saved successfully!")

elif choice == "2":
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        if content.strip():
            print("\nYour Notes:")
            print(content)
        else:
            print("No notes found.")

    except FileNotFoundError:
        print("No notes found. Add your first note!")

else:
    print("Invalid option. Please choose 1 or 2.")
