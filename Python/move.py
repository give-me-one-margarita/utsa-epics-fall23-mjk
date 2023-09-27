import os
import shutil

# Replace with your source folder path
source_folder = "C:\\Users\\marit\\Downloads\\Picture"

# Create destination folders
destination_base = "path/to/destination/folder"
num_folders = 5
for i in range(num_folders):
    dest_folder = os.path.join(destination_base, f"folder_{i + 1}")
    os.makedirs(dest_folder, exist_ok=True)

# List all files in the source folder
file_list = os.listdir(source_folder)

# Filter out only image files
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
image_files = [file for file in file_list if any(file.lower().endswith(ext) for ext in image_extensions)]

# Sort the image files
image_files.sort()

# Iterate through the image files and move them to destination folders
for idx, image_name in enumerate(image_files):
    source_path = os.path.join(source_folder, image_name)
    dest_folder = os.path.join(destination_base, f"folder_{(idx % num_folders) + 1}")
    dest_path = os.path.join(dest_folder, image_name)
    
    shutil.move(source_path, dest_path)
    
    print(f"Moved {image_name} to {dest_folder}")

print("Moving and organizing complete.")
