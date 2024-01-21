from spotify_service import SpotifyService
import json
from spotify_client import get_spotify_client

pairs = [
    {
        "artist" : "Joji",
        "song" : "Die For You"
    }
]

service = SpotifyService(get_spotify_client())

# spotify_artist = service.search_artist(pairs[0]['artist'])
# print(json.dumps(spotify_artist))

res = service.create_playlist(song_artist_pairs=pairs)
# print(json.dumps(res, indent=2))

# Song name
print("Song Name: " + res['songs'][0]['searchResult']['tracks']['items'][0]['name'])

# song url
print("Song URL: " + res['songs'][0]['searchResult']['tracks']['items'][0]['external_urls']['spotify'])

# Song ID
print("Song ID: " + res['songs'][0]['searchResult']['tracks']['items'][0]['id'])

# Artist Name
print("Artist Name: " + res['songs'][0]['searchResult']['tracks']['items'][0]['artists'][0]['name'])

# Artist URL
print("Artist URL: " + res['songs'][0]['searchResult']['tracks']['items'][0]['artists'][0]['external_urls']['spotify'])

# Artist ID
print("Artist ID: " + res['songs'][0]['searchResult']['tracks']['items'][0]['artists'][0]['id'])

# Album Name
print("Album Name: " + res['songs'][0]['searchResult']['tracks']['items'][0]['album']['name'])

# Album URL
print("Album URL: " + res['songs'][0]['searchResult']['tracks']['items'][0]['album']['external_urls']['spotify'])

# Album ID
print("Album ID: " + res['songs'][0]['searchResult']['tracks']['items'][0]['album']['id'])