from openai_api import get_recommendations
from spotify_service import SpotifyService
import json
from spotify_client import get_spotify_client
import ast

pairs = [
    {
        "artist" : "Joji",
        "song" : "Die For You"
    },
    {
        "artist" : "Iron Maiden",
        "song" : "The Trooper"
    }
]

service = SpotifyService(get_spotify_client())

# spotify_artist = service.search_artist(pairs[0]['artist'])
# print(json.dumps(spotify_artist))

res = service.retrieve_song_data(song_artist_pairs=pairs)
# print(json.dumps(res, indent=2))
for song in res['songs']:
    # Song name
    print("Song Name: " + song['searchResult']['tracks']['items'][0]['name'])

    # song url
    print("Song URL: " + song['searchResult']['tracks']['items'][0]['external_urls']['spotify'])

    # Song ID
    print("Song ID: " + song['searchResult']['tracks']['items'][0]['id'])

    # Artist Name
    print("Artist Name: " + song['searchResult']['tracks']['items'][0]['artists'][0]['name'])

    # Artist URL
    print("Artist URL: " + song['searchResult']['tracks']['items'][0]['artists'][0]['external_urls']['spotify'])

    # Artist ID
    print("Artist ID: " + song['searchResult']['tracks']['items'][0]['artists'][0]['id'])

    # Album Name
    print("Album Name: " + song['searchResult']['tracks']['items'][0]['album']['name'])

    # Album URL
    print("Album URL: " + song['searchResult']['tracks']['items'][0]['album']['external_urls']['spotify'])

    # Album ID
    print("Album ID: " + song['searchResult']['tracks']['items'][0]['album']['id'])

champions: json
with open("league_champs.json", "r") as read_file:
    champions = json.load(read_file)

traits = champions["Aatrox"]

recommendations = []
parsedRecs = ast.literal_eval(get_recommendations(traits))
# for rec in parsedRecs:
#     recommendation = json.loads(rec)
#     if not isinstance(recommendation, dict):
#         print(rec)
#         raise Exception("Exception encountered: ChatGPT didn't return a JSON, for some reason")
#     recommendations.append(recommendation)

res2 = service.retrieve_song_data(song_artist_pairs=parsedRecs)
for song in res2['songs']:
    # Song name
    print("Song Name: " + song['searchResult']['tracks']['items'][0]['name'])

    # song url
    print("Song URL: " + song['searchResult']['tracks']['items'][0]['external_urls']['spotify'])

    # Song ID
    print("Song ID: " + song['searchResult']['tracks']['items'][0]['id'])