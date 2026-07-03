import os
import shutil

path_file = input("Enter the folder path you want to organize: ")

categories = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".txt": "Documents",
    ".docx": "Documents",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".zip": "Archives",
    ".rar": "Archives"
}

files = os.listdir(path_file)
moved_count = 0

for file in files:
    folder_path = os.path.join(path_file, file)

    if os.path.isdir(folder_path):
        continue

    name, extension = os.path.splitext(file)
    extension = extension.lower()

    if extension in categories:
        category_folder = categories[extension]

    else:
        category_folder = 'Others'

    category_path = os.path.join(path_file, category_folder)

    if not os.path.exists(category_path):
        os.makedirs(category_path)

    destination = os.path.join(category_path, file)
    shutil.move(folder_path, destination)
    moved_count += 1


    print(file, "moved to", category_folder)

print(f"\nDone! {moved_count} files organized.")