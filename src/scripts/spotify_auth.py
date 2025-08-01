
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
