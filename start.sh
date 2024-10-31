#!/bin/bash

# Directories
VENV_DIR=venv/bin/activate
DL_DIR=${PWD}/dl_dir
MUSIC_DIR=~/Music

# Activate Venv
source venv/bin/activate

# Get URL from user
echo "Enter URL:"
read USER_URL

# Moving to download directory
cd $DL_DIR

# Action from URL
if [[ $USER_URL == *"spotify"* ]]; then
	echo "Spotify URL detected"
	spotdl $USER_URL
elif [[ $USER_URL == *"youtube"* ]]; then
	echo "YouTube URL detected"
	yt-dlp -x --audio-format mp3 $USER_URL
elif [[ $USER_URL == "" ]]; then
	echo "No download URL given; Sorting files"
fi

# Back out to main project directory
cd ..

# Sort files in DL_DIR
echo "Sorting files"
python3 sorter.py $DL_DIR $MUSIC_DIR

# Deactivate Venv
deactivate

# Exit
exit 0
