import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

from spotipy.oauth2 import SpotifyOAuth


# spotify API credentials
CLIENT_ID = "7e0e1e753651455692953fad203065ed"
CLIENT_SECRET = "f4ad38155e2b49ddbe6c1e4670d59eda"
REDIRECT_URI = "http://127.0.0.1:8000/callback"
SCOPE = "user-top-read" 

#clear old cache (if any)
cache_path = ".cache"
if os.path.exists(cache_path):
    os.remove(cache_path)

# set up spotify api
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    open_browser=True  
))

# time_range: 'short_term' (4 weeks), 'medium_term' (6 months), 'long_term' (all time)
top_tracks_data = sp.current_user_top_tracks(limit=20, time_range='medium_term')

track_names = []
artist_names = []

for track in top_tracks_data['items']:
    track_names.append(track['name'])
    artist_names.append(", ".join([artist['name'] for artist in track['artists']]))

# display info
print("Your Top Tracks Across All Artists:\n")
for i, (track, artist) in enumerate(zip(track_names, artist_names), start=1):
    print(f"{i}. {track} by {artist}")