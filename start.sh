#!/bin/bash

# Directories.
PROJECT_DIR=${PWD}
VENV_DIR=$PROJECT_DIR/venv
UTILITIES_DIR=$PROJECT_DIR/utilities
DL_DIR=$PROJECT_DIR/dl_dir
MUSIC_DIR=~/Music

# Install a Python Venv if there isn't one yet.
if [ ! -d venv ]; then
    . $UTILITIES_DIR/./installer.sh
fi

# Activate Venv.
source $VENV_DIR/bin/activate

# Download songs.
. $UTILITIES_DIR/./downloader.sh

# Back out to main project directory.
cd ..

# Sort files.
echo "Sorting files."
python3 $UTILITIES_DIR/sorter.py "$DL_DIR" "$MUSIC_DIR"

# Deactivate Venv.
deactivate

# Exit.
exit 0
