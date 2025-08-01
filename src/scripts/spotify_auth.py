
""" 
spotify_auth.py
Handles authentication with Spotifys API using client credentials flow

Brendan Dileo, August 2025
"""

import requests
from base64 import b64encode
from src.config.config import Config

def get_spotify_token() -> str:
    """ Fetches an access token from Spotify using client credentials flow """
    # Ensure configuration is valid
    Config.validate()
    
    # Encode credentials
    auth_header = b64encode(f"{Config.SPOTIFY_CLIENT_ID}:{Config.SPOTIFY_CLIENT_SECRET}".encode()).decode()

    # Make token request
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        headers={
            "Authorization": f"Basic {auth_header}",
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={"grant_type": "client_credentials"}
    )
    
    # Raise exception if HTTP request failed
    response.raise_for_status()  
    
    # Extract token from response
    token = response.json()['access_token']
    return token
