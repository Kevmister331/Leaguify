from spotify_service import SpotifyService
import json
from spotify_client import get_spotify_client

pairs = [
    {
        "artist" : "Iron+Maiden",
        "song" : "The+Trooper"
    }
]

service = SpotifyService(get_spotify_client())

# spotify_artist = service.search_artist(pairs[0]['artist'])
# print(json.dumps(spotify_artist))

res = service.create_playlist(song_artist_pairs=pairs)
print(json.dumps(res, indent=2))