from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import config
import dotenv
import os
import json

dotenv.load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
def get_spotify_client():
    return spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())