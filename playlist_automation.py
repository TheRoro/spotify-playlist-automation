import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'playlist-modify-public' # Name of the Scope of operations to be performed
username = SPOTIFY_USERNAME # Your Spotify Username


# 0. Auth
client_id = CLIENT_ID # Your Spotify Client ID
client_secret = CLIENT_SECRET # Your Spotify Client Secret
redirect_uri = REDIRECT_URI # Your Spotify Redirect URI (Currently set to localhost)
token = SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope, username=username, redirect_uri=redirect_uri)
spotifyObject = spotipy.Spotify(auth_manager=token)


# 1. Get all songs from old playlist
playlist_id = SPOTIFY_PLAYLIST_ID # Your Spotify Playlist ID
playlist_tracks_info = spotifyObject.user_playlist_tracks(user=username, playlist_id=playlist_id, fields=None, limit=50, offset=50, market=None)
total_tracks = playlist_tracks_info['total']

all_playlist_tracks = []
for i in range(0, total_tracks, 50):
  playlist_tracks = spotifyObject.user_playlist_tracks(user=username, playlist_id=playlist_id, fields=None, limit=50, offset=i, market=None)
  all_playlist_tracks = all_playlist_tracks + playlist_tracks['items']


# 2. Filter songs added in 2023 (or any other filter)
# Date Format: '2023-08-26T02:15:44Z'
filtered_songs = list(filter(lambda i: i['added_at'][0:4] == '2023', all_playlist_tracks))
filtered_songs = [x['track']['uri'] for x in filtered_songs]


# 3. Create a new playlist
playlist_name = 'Music 2023'
playlist_description = 'Playlist 2023 (Automated by: sadaakisz and TheRoro)'
new_playlist = spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)
new_playlist_id = new_playlist['id']


# 4. Add the filtered songs to the new playlist
for i in range(0, len(filtered_songs), 100):
  res = spotifyObject.playlist_add_items(new_playlist_id, filtered_songs[i:min(i+100, total_tracks)], position=None)

