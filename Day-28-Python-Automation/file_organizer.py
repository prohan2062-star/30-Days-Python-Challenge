
import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories
        if not os.path.isfile(file_path):
            continue

        # Get file extension
        extension = os.path.splitext(filename)[1].lower()

        if not extension:
            folder_name = "No Extension"
        else:
            folder_name = extension[1:].upper() + " Files"

        destination_folder = os.path.join(
            folder_path, folder_name
        )
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(
            destination_folder, filename
        )

        # Avoid overwriting an existing file
        if os.path.exists(destination_path):
            print(f"Skipped duplicate: {filename}")
            continue

        shutil.move(file_path, destination_path)
        print(f"Moved: {filename} -> {folder_name}")

    print("\nFile organization completed!")


if __name__ == "__main__":
    folder = input("Enter folder path to organize: ").strip()
    folder = os.path.abspath(
        os.path.expanduser(folder.strip('"'))
    )
    organize_files(folder)
