# Modules
import sys
import os
import shutil
from mutagen.easyid3 import EasyID3

# Directories
DL_DIR = sys.argv[1]
MUSIC_DIR = sys.argv[2]

# Get Tags
for file in os.listdir(DL_DIR):
    try:
        file_tags = EasyID3(DL_DIR + "/" + file)
        file_title = file_tags["title"][0]
        file_artist = file_tags["artist"][0]
        file_album = file_tags["album"][0]
    except KeyError:
        # TODO: fix this part
        print("No tags for " + file)
        file_title = input("Song Title:")
        file_artist = input("Artist:")
        file_album = input("Album:")

    # Artist and Album Directories
    artist_dir = MUSIC_DIR + "/" + file_artist
    album_dir = artist_dir + "/" + file_album

    # - if there isn't a directory, create it
    if not os.path.exists(artist_dir):
        os.makedirs(artist_dir)
    if not os.path.exists(album_dir):
        os.makedirs(album_dir)

    # - move file to artist/album directory
    # shutil.move(DL_DIR + "/" + file, album_dir)
