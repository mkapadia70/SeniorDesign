from spotipy.oauth2 import SpotifyOAuth

auth_manager = SpotifyOAuth(
    scope=scope,
    client_id='<youridhere>', 
    client_secret='<yoursecrethere>', 
    redirect_uri='<yourredirecturi>')