import os
import shutil
from pathlib import Path
from datetime import datetime

def organize_files(directory):
    """
    Automatically organize files into folders by type
    """
    
    # Define file categories
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
        'Audio': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.7z', '.tar'],
        'Code': ['.py', '.js', '.html', '.css', '.java'],
        'programs': ['.exe', '.msi', '.bat', '.rdp']
    }
    
    directory_path = Path(directory)
    
    for file in directory_path.iterdir():
        if file.is_file():
            file_ext = file.suffix.lower()
            
            # Find the right category
            moved = False
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    # Create category folder if it doesn't exist
                    category_path = directory_path / category
                    category_path.mkdir(exist_ok=True)
                    
                    # Move the file
                    try:
                        shutil.move(str(file), str(category_path / file.name))
                        print(f"Moved: {file.name} → {category}/")
                        moved = True
                        break
                    except Exception as e:
                        print(f"Error moving {file.name}: {e}")
            
            if not moved and file_ext:
                # Create 'Others' folder for unrecognized types
                others_path = directory_path / 'Others'
                others_path.mkdir(exist_ok=True)
                try:
                    shutil.move(str(file), str(others_path / file.name))
                    print(f"Moved: {file.name} → Others/")
                except Exception as e:
                    print(f"Error moving {file.name}: {e}")
# HOW TO USE:
# 1. Change this to your messy folder (Downloads, Desktop, etc.)
organize_files("C:/Users/bmogambi/Downloads")
print("✓ Organization complete!")