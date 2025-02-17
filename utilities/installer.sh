#!/bin/bash

# Python Management
# - make venv if it doesn't exist
if [[ ! -d venv ]]; then
	echo "Making venv"
	python3 -m venv venv
fi

# - activate venv
source venv/bin/activate

# - install requirements
echo "Installing from 'requirements.txt'"
if [[ -f requirements.txt ]]; then
	pip install -r requirements.txt
else
	echo "No 'requirements.txt' found"
	echo "Download 'requirements.txt' from:"
	echo "https://github.com/wordboxx/autoSpotDL.git"
	exit 1
fi
echo "Installation complete"

# Download-ffmpeg to SpotDL directory
echo "Installing ffmpeg to SpotDL directory"
spotdl --download-ffmpeg

# Deactivate venv
deactivate

# DL_DIR Management
DL_DIR=${PWD}/dl_dir
if [[ ! -d $DL_DIR ]]; then
	mkdir $DL_DIR
fi
