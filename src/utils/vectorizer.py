
""" 
vectorizer.py
Vectorizes song lyrics using TF-IDF and caches the result via pickle.

Brendan Dileo, August 2025
"""

import pickle 
from sklearn.feature_extraction.text import TfidfVectorizer
from .text_utils import clean_text

def vectorize_songs(songs, save_path="vectors.pkl"):
    
    try:
        with open(save_path, "rb") as file:
            # Load the pickled TF-IDF matrix and vectorizer
            tfidf_matrix, vectorizer = pickle.load(file)
    except FileNotFoundError:

        # Extract the song lyrics from the song dictionaries
        docs = [song.get("lyrics", "") for song in songs]
        # Clean lyrics to prepare for vectorization
        cleaned_docs = [clean_text(doc) for doc in docs]
        
        # Create a new TF-IDF vectorizer with specific parameters:
        # Ignoring common english stop words, using unigrams and bigrams, and filtering words by minimum and maximum doc frequency
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), min_df=2, max_df=0.9)
        
        # Fit the vectorizer on the cleaned lyrics and transform them into a TF-IDF matrix
        tfidf_matrix = vectorizer.fit_transform(cleaned_docs)
        
        # Save the TF-IDF matrix and vectorizer to a pickle file for later use
        with open(save_path, "wb") as file:
            pickle.dump((tfidf_matrix, vectorizer), file)
            
    return tfidf_matrix, vectorizer