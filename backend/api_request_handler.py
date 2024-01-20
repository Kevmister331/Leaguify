class APIRequestHandler:
    def __init__(self, spotifyService):
        self.spotifyService = spotifyService

    def handle_request(self, request_type, request_data):
        # Parse and validate request data
        # Based on the request type, call the appropriate method of SpotifyService
        if request_type == 'search_artist':
            return self.spotifyService.search_artist(request_data)
        # Add other request types as needed
