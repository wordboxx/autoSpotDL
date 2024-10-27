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

# DL_DIR Check
if [[ ! -d $DL_DIR ]]; then
	mkdir $DL_DIR
fi

# Downloading Songs
echo "Enter URL:"
read USER_URL

if [[ $USER_URL == *"spotify"* ]]; then
	echo "Spotify url detected"
	cd $DL_DIR
	spotdl $USER_URL
	cd ..
fi

# Sort files in DL_DIR
python3 sorter.py $DL_DIR $MUSIC_DIR

# Deactivate Venv
deactivate
