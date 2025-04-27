# Modules
import sys
import os
import shutil
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3
from mutagen.mp3 import MP3

# Global variables
file_history = []


def add_to_history(file_path):
    """Add all files in the given path to history"""
    if os.path.isfile(file_path):
        file_history.append(file_path)
    elif os.path.isdir(file_path):
        for root, dirs, files in os.walk(file_path):
            for file in files:
                if file.lower().endswith(".mp3") or file.lower() in [
                    "cover.jpg",
                    "cover.jpeg",
                    "folder.jpg",
                    "folder.jpeg",
                ]:
                    full_path = os.path.join(root, file)
                    file_history.append(full_path)


def check_file_history(file_path):
    """Check if any files in the given path are in history"""
    if os.path.isfile(file_path):
        return file_path in file_history
    elif os.path.isdir(file_path):
        for root, dirs, files in os.walk(file_path):
            for file in files:
                if file.lower().endswith(".mp3") or file.lower() in [
                    "cover.jpg",
                    "cover.jpeg",
                    "folder.jpg",
                    "folder.jpeg",
                ]:
                    full_path = os.path.join(root, file)
                    if full_path in file_history:
                        return True
    return False


def verify_files_moved():
    """Verify all files in history have been moved to their new locations"""
    for file_path in file_history:
        if os.path.exists(file_path):
            print(f"Warning: File still exists in original location: {file_path}")
            return False
    return True


def clean_directory(directory):
    """Remove empty subdirectories while preserving the root directory"""
    try:
        for root, dirs, files in os.walk(directory, topdown=False):
            if root == directory:
                continue
            if not os.listdir(root):
                os.rmdir(root)
                print(f"Removed empty directory: {root}")
    except Exception as e:
        print(f"Error cleaning directory {directory}: {str(e)}")


def sort():
    """Main sorting function"""
    DL_DIR = sys.argv[1]
    MUSIC_DIR = sys.argv[2]

    # Collect files to process
    add_to_history(DL_DIR)

    # Process all files
    for root, dirs, files in os.walk(DL_DIR, topdown=False):
        # Find cover art
        cover_path = next(
            (
                os.path.join(root, file)
                for file in files
                if file.lower()
                in ["cover.jpg", "cover.jpeg", "folder.jpg", "folder.jpeg"]
            ),
            None,
        )

        # Process MP3 files
        mp3_files = [file for file in files if file.lower().endswith(".mp3")]
        for file in mp3_files:
            file_path = os.path.join(root, file)

    # Verify and cleanup
    if verify_files_moved():
        print("All files successfully moved. Cleaning up download directory...")
        clean_directory(DL_DIR)
    else:
        print("Warning: Some files were not moved successfully. Skipping cleanup.")


if __name__ == "__main__":
    sort()

