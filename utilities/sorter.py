import os.path
from mutagen.easyid3 import EasyID3

HOME_DIRECTORY = os.path.expanduser("~")
CURR_DIR = os.getcwd()
DL_DIR = os.path.join(CURR_DIR, "dl_dir")
DL_DIR_FILES = os.listdir(DL_DIR)
MUSIC_DIR = os.path.join(HOME_DIRECTORY, "Music")


if __name__ == "__main__":
    print("Sorting files in dl_dir...")

    for file in DL_DIR_FILES:
        FILE_PATH = os.path.join(DL_DIR, file)
        FILE_NAME = FILE_PATH.split("/")[-1]

        audio = EasyID3(FILE_PATH)
        artist = audio["albumartist"][0]
        album = audio["album"][0]
        title = audio["title"][0]

        ARTIST_DIR = os.path.join(MUSIC_DIR, artist)
        ALBUM_DIR = os.path.join(ARTIST_DIR, album)

        if not os.path.exists(ARTIST_DIR):
            os.makedirs(ALBUM_DIR)
        if not os.path.exists(ALBUM_DIR):
            os.makedirs(ALBUM_DIR)

        # Check if the title already exists in ALBUM_DIR
        existing_titles = [
            EasyID3(os.path.join(ALBUM_DIR, f))["title"][0]
            for f in os.listdir(ALBUM_DIR)
            if f.endswith(".mp3")
        ]
        if title not in existing_titles:
            os.rename(FILE_PATH, os.path.join(ALBUM_DIR, FILE_NAME))
        else:
            print(f"{title} already in {ALBUM_DIR}, skipping.")

    print("Cleaning dl_dir...")
    for file in os.listdir(DL_DIR):
        os.remove(os.path.join(DL_DIR, file))
