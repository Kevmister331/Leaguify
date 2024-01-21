import json
import requests
import urllib.parse

class SpotifyService:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client

    def search_artist(self, artist_name):
        # Use self.spotify_client to call the Spotify API
        # For example, search for an artist
        return self.spotify_client.search(q='artist:' + artist_name, type='artist')

    # Add other methods for different Spotify queries

    def retrieve_song_data(self, song_artist_pairs): 
        tracks = {
            "songs": []
        }

        for pair in song_artist_pairs:
            artist = pair['artist']
            song = pair['song']
            query = 'artist:' + artist + ' track:' + song

            search_result = self.spotify_client.search(q=query, type='track', limit=1)

            items = search_result['tracks']['items']
            if items:
                track_json = {
                    "artist": artist,
                    "song": song,
                    "searchResult": search_result,
                }
                tracks['songs'].append(track_json)
            else:
                print(f"No results found for {artist} - {song}")

        return tracks