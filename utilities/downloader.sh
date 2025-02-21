#!/bin/bash

# Move into DL_DIR for downloading.
cd "$DL_DIR" || exit

# Get URL from user.
read -rp "Enter URL: " USER_URL

# Use SpotDL to download if Spotify URL.
if [[ $USER_URL == *"spot"* ]]; then
  echo "Downloading from Spotify."
  spotdl "$USER_URL"
fi

# Back out of DL_DIR.
cd ..
