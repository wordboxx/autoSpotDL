#!/bin/bash

# Directories
PROJECT_DIR=${PWD}
VENV_DIR=$PROJECT_DIR/venv
UTILITIES_DIR=$PROJECT_DIR/utilities
DL_DIR=$PROJECT_DIR/dl_dir
MUSIC_DIR=~/Music

if [ ! -d venv ]; then
    $UTILITIES_DIR/./installer.sh
fi

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
fi

# Back out to main project directory.
cd ..

# Sort files.
echo "Sorting files."
python3 $UTILITIES_DIR/sorter.py "$DL_DIR" "$MUSIC_DIR"

# Deactivate Venv.
deactivate

# Exit.
exit 0
