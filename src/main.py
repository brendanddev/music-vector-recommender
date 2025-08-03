
""" 
main.py 
The main entry point for the music vector recommender system.

Brendan Dileo, August 2025
"""

from utils.vectorizer import vectorize_songs
from utils.load_data import load_songs
from config.config import Config

def get_user_choice(recs):
    """ Prompts the user to select a song from the list of recommendations """
    while True:
        try:
            choice = int(input("\nYour choice? (1-{}) ".format(len(recs)))) - 1
            if 0 <= choice < len(recs):
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and {}.".format(len(recs)))
        except ValueError:
            print("Invalid input. Please enter a number.")\
                
def display_song(idx, songs):
    """ Displays the selected song's title, artist, and lyrics """
    song = songs[idx]
    print("\nNow Playing:")
    print(f"{song.get('title', 'Unknown Title')} - {song.get('artist', 'Unknown Artist')}")
    print("-" * 40)
    print(song.get("lyrics", "[No lyrics available]"))
    print("-" * 40)