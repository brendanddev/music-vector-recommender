
""" 
api.py
...

Brendan Dileo, August 2025
"""

import requests
from typing import Dict, List, Any 
from src.scripts.spotify_auth import get_spotify_token

def search_songs(query: str, types: str = "track,artist", limit: int = 10) -> Dict[str, Any]:
    """
    Searches Spotify for songs, artists, or albums based on a query string using the client credentials token.

    Args:
        query (str): Search query string (e.g., artist name, song title).
        types (str): Comma-separated types to search for (e.g., 'track,artist,album').
        limit (int): Maximum number of results to return per type. Defaults to 10.

    Returns:
        Dict[str, Any]: Parsed JSON response from Spotify API containing search results.
    """
    # Fetch spotify auth token
    token = get_spotify_token()
    
    # Setup auth header with bearer token
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # Prepare query params
    params = {
        "q": query,
        "type": types,
        "limit": limit
    }
    
    # Make GET request to Spotify search endpoint
    response = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)

    # Raise an HTTPError if the request returned an unsuccessful status code
    response.raise_for_status()
    
    # Return the parsed JSON response content
    return response.json()
