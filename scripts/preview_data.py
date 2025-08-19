
""" 
preview_data.py 
A simple script for previewing rows from a CSV file.

Brendan Dileo, August 2025
"""

import pandas as pd 

def preview_csv(filepath, rows=20):
    """ Loads and prints the first 'rows' lines of a CSV file """
    try:
        df = pd.read_csv(filepath, nrows=rows)
        print(df)
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    path_to_file = "data/song_lyrics.csv"
    preview_csv(path_to_file)