import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id= "",
        client_secret= "",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]