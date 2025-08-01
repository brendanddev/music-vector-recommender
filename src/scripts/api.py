
""" 
api.py
Handles API interactions with the Spotify Web API, providing functions to search for songs, artists, and albums using client credentials. 

Brendan Dileo, August 2025
"""

import requests
from typing import Dict, Any 
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

def format_search_results(results: dict) -> str:
    """
    Formats Spotify search results into a readable string for display.

    Args:
        results (dict): Raw JSON response from Spotify's search API.

    Returns:
        str: Formatted string of track info.
    """
    tracks = results.get('tracks', {}).get('items', [])
    if not tracks:
        return "No tracks found for the given query."
    
    formatted_results = []
    for track in tracks:
        track_name = track.get('name')
        artists = ", ".join(artist['name'] for artist in track.get('artists', []))
        album_name = track.get('album', {}).get('name', 'Unknown Album')
        formatted_results.append(f"Track: {track_name}\nArtists: {artists}\nAlbum: {album_name}\n")

    return "\n".join(formatted_results)




if __name__ == "__main__":
    results = search_songs("Nirvana")
    print(format_search_results(results))
