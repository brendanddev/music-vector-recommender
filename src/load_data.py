
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
    songs = []
    try:
        if filetype == 'csv':
            with open(filename, encoding="utf-8") as f:
                reader = DictReader(f)
                for i, row in enumerate(reader):
                    songs.append(row)
                    # If num is set, stop after reading num entries
                    if num is not None and i + 1 >= num:
                        break
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
