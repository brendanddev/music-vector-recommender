
""" 
vectorizer.py
Vectorizes song lyrics using TF-IDF and caches the result via pickle.

Brendan Dileo, August 2025
"""

import pickle 
from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_songs(songs, save_path="vectors.pkl", lyrics_w=3, artist_w=2, album_w=1):
    """ 
    Vectorizes song lyrics, artists, and albums using TF-IDF, combining lyrics, artist, and album fields with weighted contributions.

    Args:
        songs (list): List of song dicts with keys 'lyrics', 'artist', 'album'.
        save_path (str): Filepath to save/load cached TF-IDF matrix.
        lyrics_w (int): Weight for lyrics.
        artist_w (int): Weight for artist.
        album_w (int): Weight for album.

    Returns:
        tfidf_matrix (scipy.sparse matrix): TF-IDF representation of songs.
        vectorizer (TfidfVectorizer): Fitted vectorizer object.
    """
    try:
        with open(save_path, "rb") as file:
            # Load the pickled TF-IDF matrix and vectorizer
            tfidf_matrix, vectorizer = pickle.load(file)
    except FileNotFoundError:
        # Build combined documents with weighted fields
        docs = []
        for song in songs:
            lyrics = (song.get("lyrics", "") + " ") * lyrics_w
            artist = (song.get("artist", "") + " ") * artist_w
            album = (song.get("album", "") + " ") * album_w
            combined = lyrics + artist + album
            docs.append(combined)
        
        # Create TF-IDF vectorizer
        vectorizer = TfidfVectorizer(
            stop_words='english', 
            ngram_range=(1, 2), 
            min_df=2, 
            max_df=0.9
        )
        # Fit and transform the documents
        tfidf_matrix = vectorizer.fit_transform(docs)
        print(f"Created new TF-IDF vectors (shape: {tfidf_matrix.shape})")
        
        # Save the TF-IDF matrix and vectorizer to a pickle file
        with open(save_path, "wb") as file:
            pickle.dump((tfidf_matrix, vectorizer), file)
    
    return tfidf_matrix, vectorizer