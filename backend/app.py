from flask import Flask, make_response, request
from openai_api import get_recommendations
from spotify_client import get_spotify_client
from spotify_service import SpotifyService
from api_request_handler import APIRequestHandler
import jsonify
from flask_cors import CORS
import json
import ast

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*')
# CORS(app)
spotify_client = get_spotify_client()
spotify_service = SpotifyService(spotify_client)
api_request_handler = APIRequestHandler(spotify_service)

# @app.route('/headers')
# def headers():
#     response = make_response("Header data")
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     return response

# Define your Flask routes here
@app.route('/', methods=['GET'])
def ping():
    return "server up"

@app.route('/getsongs/<champion>', methods=['GET'])
def getSongs(champion):
    print("In getSongs: " + champion)
    result = generate('songs', champion)
    print(result)
    return result


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
    champions: json
    with open("league_champs.json", "r") as read_file:
        champions = json.load(read_file)
    
    traits = champions[champion]
    # recommendations = []
    parsedRecs = ast.literal_eval(get_recommendations(traits))
    # for rec in parsedRecs:
    #     recommendation = json.loads(rec)
    #     if not isinstance(recommendation, dict):
    #         print(rec)
    #         raise Exception("Exception encountered: ChatGPT didn't return a JSON, for some reason")
    #     recommendations.append(recommendation)

    res = spotify_service.retrieve_song_data(song_artist_pairs=parsedRecs)

    return res



@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    result = api_request_handler.handle_request('search_artist', data['artist_name'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

