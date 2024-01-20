from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

client_id = 'your_client_id'
client_secret = 'your_client_secret'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
