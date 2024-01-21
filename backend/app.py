from flask import Flask
from spotify_client import get_spotify_client
from spotify_service import SpotifyService
from api_request_handler import APIRequestHandler
import jsonify

app = Flask(__name__)
spotify_client = get_spotify_client()
spotify_service = SpotifyService(spotify_client)
api_request_handler = APIRequestHandler(spotify_service)

# Define your Flask routes here
@app.route('/', methods=['GET'])
def ping():
    return "server up"

@app.route('/getsongs/<champion>')
def getSongs(champion):
    data = generate('songs', champion) 
    return jsonify(data)


@app.route('/getplaylists/<champion>')
def getPlaylists(champion):
    data = generate('playlists', champion)
    return jsonify(data)

@app.route('/getartists/<champion>')
def getArtists(champion):
    data = generate('artists', champion)
    return jsonify(data)


def generate(typeContent, champion):
    # - Grab the champion's attributes 
    # - Insert the correct attributes and content type that we want in the ChatGPT prompt
    # - Send chatGPT the prompt, and on return, check if it is in the correct format: 
    #   - An array of JSONs, each JSON represents a song
    #   - [{artist: <artist name>, song: <song title>}, {etc.}]
    # - After receiving the array of JSONs, check if it is in the valid format
    #   - If it is in the correct format, use retrieve_song_data() to get all the songs
    #       - If something goes wrong while fetching a song, exclude it from the final list and make a note of it
    # - After getting the song info, return the data JSON
    
    #return api_request_handler.handle_request
    return (champion + " " + typeContent)



@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    result = api_request_handler.handle_request('search_artist', data['artist_name'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

