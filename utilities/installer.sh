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

# Install ffmpeg if it's not installed
if ! command -v ffmpeg &> /dev/null; then
    echo "Installing ffmpeg"
    spotdl --download-ffmpeg
fi

# Deactivate venv
deactivate

# DL_DIR Management
if [[ ! -d $DL_DIR ]]; then
    mkdir $DL_DIR
fi
