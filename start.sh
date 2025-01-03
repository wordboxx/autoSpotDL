#!/bin/bash

# Directories
DL_DIR=${PWD}/dl_dir
MUSIC_DIR=~/Music

# Activate Venv
source venv/bin/activate

# Get URL from user
echo "Enter URL:"
read -r USER_URL

# Moving to download directory (or exit if directory non-existent)
cd "$DL_DIR" || exit

# Action from URL
if [[ $USER_URL == *"spotify"* ]]; then
	spotdl "$USER_URL"
elif [[ $USER_URL == *"youtu"* ]]; then
	yt-dlp -x --audio-format mp3 "$USER_URL"
	echo "No download URL given; Sorting files"
fi

# Back out to main project directory
cd ..

# Sort files in DL_DIR
echo "Sorting files"
python3 sorter.py "$DL_DIR" "$MUSIC_DIR"

# Deactivate Venv
deactivate

# Exit
exit 0
