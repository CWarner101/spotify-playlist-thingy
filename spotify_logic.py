import spotipy as spy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

from environs import Env


# Set up ENV
env = Env()
env.read_env()

def main():
    sp = spy.Spotify(auth_manager=SpotifyOAuth(client_id=env.str("YOUR_APP_CLIENT_ID"),
                                                   client_secret=env.str("YOUR_APP_CLIENT_SECRET"),
                                                   redirect_uri=env.str("YOUR_APP_REDIRECT_URI"),
                                                   scope="user-library-read"))

    # Uses playlist URI to pull each track item
    hmmm_playlist_uri = 'spotify:playlist:3YdF6Sm8GGvfs8oiB5YOyw'
    results = sp.playlist_tracks(hmmm_playlist_uri, limit=5)
    items = results['items']

    #print(items[0]['track']['artists'][0])
    # Priming read
    i = 0
    # Iterates over each track in items and displays title and artist
    for item in items:
        track = items[i]['track']
        title = track['name']
        artist = track['artists'][0]['name']
        print(f'Title: {title} - Artist: {artist}')
        i += 1

if __name__ == "__main__":
    main()