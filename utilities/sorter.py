# Modules
import sys
import os
import shutil
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
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
                if file.lower().endswith('.mp3') or file.lower() in ['cover.jpg', 'cover.jpeg', 'folder.jpg', 'folder.jpeg']:
                    full_path = os.path.join(root, file)
                    file_history.append(full_path)

def check_file_history(file_path):
    """Check if any files in the given path are in history"""
    if os.path.isfile(file_path):
        return file_path in file_history
    elif os.path.isdir(file_path):
        for root, dirs, files in os.walk(file_path):
            for file in files:
                if file.lower().endswith('.mp3') or file.lower() in ['cover.jpg', 'cover.jpeg', 'folder.jpg', 'folder.jpeg']:
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

def embed_cover(mp3_path, cover_path):
    """Embed cover art into MP3 file"""
    try:
        audio = MP3(mp3_path, ID3=ID3)
        if audio.tags is None:
            audio.add_tags()
        
        with open(cover_path, 'rb') as cover_file:
            cover_data = cover_file.read()
        
        audio.tags.add(
            APIC(
                encoding=3,  # UTF-8
                mime='image/jpeg',
                type=3,  # Cover (front)
                desc='Cover',
                data=cover_data
            )
        )
        audio.save()
        print(f"Embedded cover art into {os.path.basename(mp3_path)}")
    except Exception as e:
        print(f"Error embedding cover art in {mp3_path}: {str(e)}")

def process_file(file_path, MUSIC_DIR, cover_path=None):
    """Process and move a single file to its new location"""
    print(f"Now sorting: {os.path.basename(file_path)}")
    
    if not file_path.lower().endswith('.mp3'):
        return

    try:
        file_tags = EasyID3(file_path)
        file_artist = file_tags["albumartist"][0]
        file_album = file_tags["album"][0]

        # Create target directories
        artist_dir = os.path.join(MUSIC_DIR, file_artist)
        album_dir = os.path.join(artist_dir, file_album)
        os.makedirs(album_dir, exist_ok=True)

        target_path = os.path.join(album_dir, os.path.basename(file_path))
        
        # Handle cover art
        if cover_path and os.path.exists(cover_path):
            embed_cover(file_path, cover_path)
            cover_target = os.path.join(album_dir, os.path.basename(cover_path))
            if not os.path.exists(cover_target):
                shutil.move(cover_path, cover_target)
                print(f"Moved cover art to {album_dir}")

        # Move or delete file
        if os.path.exists(target_path):
            print(f"{os.path.basename(file_path)} already exists at {album_dir}; deleting...")
            os.remove(file_path)
        else:
            shutil.move(file_path, album_dir)
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

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
            (os.path.join(root, file) for file in files 
             if file.lower() in ['cover.jpg', 'cover.jpeg', 'folder.jpg', 'folder.jpeg']),
            None
        )
        
        # Process MP3 files
        mp3_files = [file for file in files if file.lower().endswith('.mp3')]
        for file in mp3_files:
            file_path = os.path.join(root, file)
            process_file(file_path, MUSIC_DIR, cover_path)

    # Verify and cleanup
    if verify_files_moved():
        print("All files successfully moved. Cleaning up download directory...")
        clean_directory(DL_DIR)
    else:
        print("Warning: Some files were not moved successfully. Skipping cleanup.")

if __name__ == "__main__":
    sort()
