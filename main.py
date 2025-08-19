
""" 
main.py
Main entry point for the music vector recommender system.

Brendan Dileo, August 2025
"""


from src.load_data import load_songs
from src.vectorizer import vectorize_songs
from src.recommender import generate_recommendations, display_recommendations
import numpy as np

def get_user_choice(recs):
    while True:
        try:
            choice = int(input(f"Select a song (1-{len(recs)}): ")) - 1
            if 0 <= choice < len(recs):
                return choice
            print("Invalid choice.")
        except ValueError:
            print("Enter a number.")

def main():
    path = "data/song_lyrics.csv"
    print(f"Loading songs from: {path}")
    
    songs = load_songs("data/song_lyrics.csv", num=1000)
    if not songs:
        return

    tfidf_matrix, _ = vectorize_songs(songs)

    # Start with random recommendations
    recommended_indices = np.random.choice(len(songs), 5, replace=False).tolist()

    while True:
        display_recommendations(recommended_indices, songs)
        selected_choice = get_user_choice(recommended_indices)
        selected_index = recommended_indices[selected_choice]

        song = songs[selected_index]
        print(f"\nNow Playing: {song['title']} - {song['artist']}")

        # Generate recommendations based on the user’s selected song
        recommended_indices = generate_recommendations(selected_index, tfidf_matrix, songs, num_recs=5)

if __name__ == "__main__":
    main()