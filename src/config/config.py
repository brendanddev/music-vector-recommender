
""" 
config.py
Loads and validates configuration settings for the music vector recommender system

Brendan Dileo, August 2025
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    # Spotify API credentials
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    
    # Data and vectorizer config
    DATA_PATH = "data/song_lyrics.csv"
    NUM_SONGS = 100
    VECTORS_PATH = f"data/vectors_{NUM_SONGS or 'all'}.pkl"
    
    @classmethod
    def validate(cls):
        if not cls.SPOTIFY_CLIENT_ID or not cls.SPOTIFY_CLIENT_SECRET:
            raise ValueError("Missing SPOTIFY_CLIENT_ID or SPOTIFY_CLIENT_SECRET environment variables")
    
    @classmethod
    def _debug_print(cls):
        print("SPOTIFY_CLIENT_ID:", cls.SPOTIFY_CLIENT_ID)
        print("SPOTIFY_CLIENT_SECRET:", cls.SPOTIFY_CLIENT_SECRET)
        print("DATA_PATH:", cls.DATA_PATH)
        print("NUM_SONGS:", cls.NUM_SONGS)
        print("VECTORS_PATH:", cls.VECTORS_PATH)
        