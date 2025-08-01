
""" 
api.py
...

Brendan Dileo, August 2025
"""

import requests
from typing import Dict, List, Any 
from src.scripts.spotify_auth import get_spotify_token

def search_songs(query: str, types: str = "track,artist", limit: int = 10) -> Dict[str, Any]: