#!/bin/bash

# Directories.
REQUIREMENTS_FILE=$PROJECT_DIR/requirements.txt

# Make Python venv if it doesn't exist
if [[ ! -d $VENV_DIR ]]; then
    echo "Making venv"
    python3 -m venv $VENV_DIR
fi

# Activate venv
source $VENV_DIR/bin/activate

# Install requirements
echo "Installing from 'requirements.txt'"
if [ -e $REQUIREMENTS_FILE ]; then
    pip install -r $REQUIREMENTS_FILE
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
if [[ ! -d $DL_DIR ]]; then
    mkdir $DL_DIR
fi
