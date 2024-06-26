import spotipy
from spotipy.oauth2 import SpotifyOAuth

from environs import Env

# Set up ENV
env = Env()
env.read_env()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = env.str("YOUR_APP_CLIENT_ID"),
                                               client_secret = env.str("YOUR_APP_CLIENT_SECRET"),
                                               redirect_uri = env.str("YOUR_APP_REDIRECT_URI"),
                                               scope="user-library-read"))


soad_uri = 'spotify:artist:5eAWCfyUhZtHHtBdNk56l1'
results = sp.artist_albums(soad_uri, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
