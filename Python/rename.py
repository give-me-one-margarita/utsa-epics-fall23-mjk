import os

# Replace with your folder path
folder_path = "C:\\Users\\marit\\Downloads\\Picture"

# List all files in the folder
file_list = os.listdir(folder_path)

# Filter out only image files (you might need to adjust this based on your use case)
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]
image_files = [file for file in file_list if any(file.lower().endswith(ext) for ext in image_extensions)]

# Sort the image files to ensure sequential renaming
image_files.sort()

# Iterate through the image files and rename them sequentially
for idx, old_name in enumerate(image_files):
    extension = os.path.splitext(old_name)[1]
    new_name = f"marita_{idx + 1:03d}{extension}"  # Renaming format: image_001.jpg, image_002.jpg, ...
    
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    
    print(f"Renamed {old_name} to {new_name}")

print("Renaming complete.")
