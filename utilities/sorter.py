# Modules
import sys
import os
import shutil
from mutagen.easyid3 import EasyID3

def sort():
    # Filepaths injected from terminal by "start.sh".
    DL_DIR = sys.argv[1]
    MUSIC_DIR = sys.argv[2]

    # Loop through all files in the download directory, "DL_DIR".
    for file in os.listdir(DL_DIR):
        print(f"Now sorting: {file}")

        # Load file tags.
        file_tags = EasyID3(DL_DIR + "/" + file)
        file_title = file_tags["title"][0]
        file_album = file_tags["album"][0]
        file_artist = file_tags["albumartist"][0]

        # Designate directories for file.
        artist_dir = MUSIC_DIR + "/" + file_artist
        album_dir = artist_dir + "/" + file_album

        # If there aren't artist and album directories, create them.
        if not os.path.exists(artist_dir):
            os.makedirs(artist_dir)
        if not os.path.exists(album_dir):
            os.makedirs(album_dir)

        # If the file already exists,
        # delete newest file and skip.
        if os.path.exists(album_dir + "/" + file):
            print(f"{file} already exists at location {album_dir}; deleting...")
            os.remove(f"{DL_DIR}/{file}")
            continue
        else:
            # Move file to artist/album directory.
            shutil.move(DL_DIR + "/" + file, album_dir)

# If program is called, rather than functions.
if __name__ == "__main__":
    sort()
