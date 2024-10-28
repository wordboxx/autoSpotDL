#!/bin/bash

# Directories
VENV_DIR=venv/bin/activate
DL_DIR=${PWD}/dl_dir
MUSIC_DIR=~/Music

# Python Management
# - make venv if it doesn't exist
if [[ ! -d venv ]]; then
	echo "Making venv"
	python3 -m venv venv
fi

# - activate venv
source venv/bin/activate

# - (quiet) install requirements
if [[ -f requirements.txt ]]; then
	pip install -q -r requirements.txt
else
	echo "No requirements.txt found"
	exit 1
fi

# DL_DIR Management
if [[ ! -d $DL_DIR ]]; then
	mkdir $DL_DIR
fi

cd $DL_DIR

# Downloading Songs
echo "Enter URL:"
read USER_URL

if [[ $USER_URL == *"spotify"* ]]; then
	echo "Spotify URL detected"
	spotdl $USER_URL
elif [[ $USER_URL == *"youtube"* ]]; then
	echo "YouTube URL detected"
	yt-dlp -x --audio-format mp3 $USER_URL
elif [[ $USER_URL == "" ]]; then
	echo "No download URL given"
fi

# - back out to main project directory
cd ..

# Sort files in DL_DIR
echo "Sorting files"
python3 sorter.py $DL_DIR $MUSIC_DIR

# Deactivate Venv
deactivate

# Exit
exit 0
