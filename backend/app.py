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

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    result = api_request_handler.handle_request('search_artist', data['artist_name'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

