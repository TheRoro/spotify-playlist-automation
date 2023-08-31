# Spotify Playlist Automation

This Python script allows you to automate the process of creating a new Spotify playlist, filtering songs from an existing playlist, and adding specific songs to the new playlist based on a defined filter criteria (in this case, songs added in 2023).

## Prerequisites

Before you can use this script, you need to set up a few things:

1.  **Spotify Developer Account**: You need to have a Spotify Developer account and create an app to get your `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI`. You can create a Spotify Developer account and app [here](https://developer.spotify.com/dashboard/applications).
2.  **Spotify Username**: Replace `SPOTIFY_USERNAME` with your Spotify username.
3.  **Spotify Playlist ID**: Replace `SPOTIFY_PLAYLIST_ID` with the ID of the existing playlist from which you want to filter songs.

## How it works

This script performs the following steps:

1.  **Authentication**: It authenticates with the Spotify API using your app's credentials.
2.  **Get all songs from the old playlist**: It fetches all the songs from the specified old playlist.
3.  **Filter songs added in 2023 (or any other filter)**: It filters the songs based on the year they were added, in this case, 2023. You can modify the filter criteria as needed.
4.  **Create a new playlist**: It creates a new playlist with the name "Music 2023" and a description mentioning that it's automated by the script.
5.  **Add filtered songs to the new playlist**: It adds the filtered songs to the newly created playlist, making it easy for you to access the songs that meet your criteria.

## Usage

1.  Set up the prerequisites as mentioned above.
2.  Install the required Python libraries. You can do this using pip:
    ```bash
    pip install spotipy
    ```
3.  Replace the placeholders in the script with your Spotify username, client ID, client secret, redirect URI, and the ID of the old playlist.
4.  Modify the filter criteria in the script if you want to filter songs based on a different condition (e.g., a different year).
5.  Run the script. It will create a new playlist, filter the songs from the old playlist, and add the filtered songs to the new playlist.
6.  You can then access the new playlist named "Music 2023" on your Spotify account.

**Note**: Make sure to keep your credentials and sensitive information secure. Do not share them publicly or commit them to version control systems.

Made with 🦔 by [@sadaakisz](https://github.com/sadaakisz) and [@TheRoro](https://github.com/TheRoro)
