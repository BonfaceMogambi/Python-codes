import shutil
from pathlib import Path

def reverse_organize(directory):
    """
    Move files from subfolders back to the main directory
    and remove empty folders
    """
    directory_path = Path(directory)

    for folder in directory_path.iterdir():
        if folder.is_dir():
            for file in folder.iterdir():
                if file.is_file():
                    try:
                        shutil.move(str(file), str(directory_path / file.name))
                        print(f"Restored: {file.name} ← {folder.name}/")
                    except Exception as e:
                        print(f"Error restoring {file.name}: {e}")

            # Remove folder if empty
            try:
                folder.rmdir()
                print(f"Removed empty folder: {folder.name}/")
            except OSError:
                pass  # Folder not empty or cannot be removed

# HOW TO USE:
reverse_organize("C:/Users/bmogambi/Downloads")
print("✓ Files restored to original folder!")