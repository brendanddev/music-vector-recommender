
""" 
config.py
Loads and validates configuration settings for the music vector recommender system

Brendan Dileo, August 2025
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    
    @classmethod
    def validate(cls):
        if not Config.SPOTIFY_CLIENT_ID or not Config.SPOTIFY_CLIENT_SECRET:
            raise ValueError("Missing SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET environment variables")
     
    @classmethod
    def _debug_print(cls):
        print("SPOTIFY_CLIENT_ID:", cls.SPOTIFY_CLIENT_ID)
        print("SPOTIFY_CLIENT_SECRET:", cls.SPOTIFY_CLIENT_SECRET)