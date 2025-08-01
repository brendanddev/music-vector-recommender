
""" 
main.py

Brendan Dileo, August 2025
"""

from src.utils.load_data import load_songs
from src.utils.vectorizer import vectorize_songs
from src.config.config import Config

Config.validate()

# Load and vectorize
songs = load_songs(Config.DATA_PATH, num=Config.NUM_SONGS, filetype='csv')
tfidf_matrix, vectorizer = vectorize_songs(songs, save_path=Config.VECTORS_PATH)

# Output summary
print("Vectorization complete.")
print("TF-IDF matrix shape:", tfidf_matrix.shape)