
""" 
load_data.py
Provides a utility function to load songs data from CSV or JSON files, with optional random 
sampling of entries for quick previews or smaller datasets.

Brendan Dileo, August 2025
"""

from csv import DictReader, Error as CSVError
from random import shuffle
import json

def load_songs(filename, num=None, filetype='csv'):
    """ 
    Load songs from a CSV or JSON file with optional random sampling.
    
    Args:
        filename (str): Path to the data file (CSV or JSON).
        num (int, optional): Number of entries to load. If None, load entire file.
        filetype (str): 'csv' or 'json' indicating file format.
        
    Returns:
        list of dict: List of songs, each represented as a dictionary.
    """
    
    songs = []
    try:
        # CSV file handling
        if filetype == 'csv':
            with open(filename, encoding="utf-8") as f:
                reader = DictReader(f)
                for i, row in enumerate(reader):
                    songs.append(row)
                    # If num is set, stop after reading num entries
                    if num is not None and i + 1 >= num:
                        break
                    
        # JSON file handling
        elif filetype == "json":
            with open(filename, encoding="utf-8") as f:
                songs = json.load(f)
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
        return []
    except CSVError:
        print(f"Error: CSV file '{filename}' is malformed.")
        return []
    except json.JSONDecodeError:
        print(f"Error: JSON parsing error in '{filename}'.")
        return []   
    
    if num is not None:
        shuffle(songs)
        songs = songs[:num]
    
    print(f"{len(songs)} songs loaded.")
    return songs
        

if __name__ == "__main__":
    filepath = "data/song_lyrics.csv"
    songs = load_songs(filepath, num=1, filetype='csv')
    if songs:
        print("Sample song:")
        print("Title:", songs[0].get("title", "No title"))
        print("Artist:", songs[0].get("artist", "Unknown artist"))
        print("Lyrics snippet:", songs[0].get("lyrics", "")[:2000])
    else:
        print("No songs loaded.")