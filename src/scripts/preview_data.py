
""" 
preview_data.py
Simple script to preview rows from a CSV file.

Brendan Dileo, August 2025
"""

import pandas as pd

def preview_csv(filepath, rows=20):
    """
    Load and print the first 'rows' lines of a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        rows (int): Number of rows to read for preview.
    """
    try:

        df = pd.read_csv(filepath, nrows=rows)
        print(df.head(rows))
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    path_to_file = "data/song_lyrics.csv"
    preview_csv(path_to_file)
