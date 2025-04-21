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

# Use YT-DLP to download if YouTube URL.
if [[ $USER_URL == *"youtube"* ]]; then
  echo "Downloading from YouTube."
  yt-dlp -x --audio-format mp3 "$USER_URL"
fi

# Use Bandcamp-DL to download if Bandcamp URL.
if [[ $USER_URL == *"bandcamp"* ]]; then
  echo "Downloading from Bandcamp."
  bandcamp-dl -f --base-dir="$DL_DIR" "$USER_URL"
fi

# Back out of DL_DIR.
cd ..
