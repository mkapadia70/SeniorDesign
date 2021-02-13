from spotipy.oauth2 import SpotifyOAuth

def getAuthManager():
    return SpotifyOAuth(
        scope="user-modify-playback-state user-read-currently-playing user-read-playback-state",
        client_id="",
        client_secret="",
        redirect_uri="http://localhost:4444/callback"
        
    )
