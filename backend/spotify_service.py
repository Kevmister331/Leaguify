import json

class SpotifyService:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client

    def search_artist(self, artist_name):
        # Use self.spotify_client to call the Spotify API
        # For example, search for an artist
        return self.spotify_client.search(q='artist:' + artist_name, type='artist')

    # Add other methods for different Spotify queries

    def create_playlist(self, song_artist_pairs):
        tracks = {
            "songs": [

            ]
        }
        for pair in song_artist_pairs:
            artist = pair['artist']
            song = pair['song']
            query = 'artist:' + artist + '&track:' + song
            print(artist)
            print(song)
            print(query)
            search_result = self.spotify_client.search(q=query, type='track', limit=1)
            print(json.dumps(search_result, indent=2))
            spotify_track = self.spotify_client.track(track_id=search_result['tracks']['href'])
            print(json.dumps(spotify_track, indent=2))
            track_json = {
                "artist" : artist,
                "song": song,
                "searchResult" : search_result,
                "spotifyTrack" : spotify_track
            }
            tracks['songs'].append(track_json)
        return tracks