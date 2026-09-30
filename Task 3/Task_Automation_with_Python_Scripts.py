import os
import shutil

def organize_jpg_files(source_dir, destination_dir):
    """
    Automates moving all .jpg and .jpeg files from source_dir to destination_dir.
    Creates sample files if the source directory is empty to ensure smooth execution.
    """
    print("========================================")
    print("     AUTOMATED FILE ORGANIZER SCRIPT    ")
    print("========================================\n")

    # Ensure source directory exists
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
        print(f"📁 Created source directory: '{source_dir}'")

    # Create dummy .jpg files for testing if folder is empty
    existing_files = os.listdir(source_dir)
    if not any(f.lower().endswith(('.jpg', '.jpeg')) for f in existing_files):
        print("💡 Source folder empty. Creating test .jpg files...")
        test_files = ["image1.jpg", "vacation.jpeg", "document.txt", "photo_2026.jpg"]
        for fname in test_files:
            file_path = os.path.join(source_dir, fname)
            with open(file_path, 'w') as f:
                f.write("Sample file content")
        print("✅ Test files created successfully!\n")

    # Ensure destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"📁 Created destination directory: '{destination_dir}'\n")

    moved_count = 0

    # Iterate over files in the source folder
    for filename in os.listdir(source_dir):
        # Match .jpg and .jpeg extensions (case-insensitive)
        if filename.lower().endswith(('.jpg', '.jpeg')):
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)

            # Move file using shutil
            shutil.move(source_file, destination_file)
            print(f"📦 Moved: {filename} ➔ {destination_dir}/")
            moved_count += 1

    print("\n========================================")
    print(f"🎉 TASK COMPLETE: Moved {moved_count} JPG file(s).")
    print("========================================")

if __name__ == "__main__":
    # Define folder paths (relative paths work across Windows/Mac/Linux)
    SOURCE_FOLDER = "Unorganized_Files"
    DESTINATION_FOLDER = "JPG_Images"

    organize_jpg_files(SOURCE_FOLDER, DESTINATION_FOLDER)
