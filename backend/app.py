from flask import Flask, request, jsonify

app = Flask(__name__)
spotify_service = SpotifyService(spotify_client)
api_request_handler = APIRequestHandler(spotify_service)

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    result = api_request_handler.handle_request('search_artist', data['artist_name'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
