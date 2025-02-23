# autoSpotDL
### Easy Automated Music Downloading & Sorting (for Arch Linux)
Just `cd` into the `autoSpotDL` directory and run `./start.sh`. The installer should create the python venv and install the dependencies in the `installer.sh`.\
\
From there, it will prompt you to input a Spotify URL. SpotDL will be ran on that URL (can be albums!) and download the music from YouTube but tag each file using Spotify metadata.\
\
Then, the `sorter.py` script will attempt to sort the music into a `Artist -> Album` hierarchy in your Music folder.\
(If you want it to download and sort to a different directory, just change the `MUSIC_DIR` filepath in `start.sh`.)
\
\
### NOTE:
For whatever reason, sometimes the Python venv doesn't install correctly the first time. If something is amiss, first delete the venv folder in the project directory and then rerun the `start.sh` file.
