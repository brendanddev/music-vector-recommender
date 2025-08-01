
""" 
vectorizer.py
Vectorizes song lyrics using TF-IDF and caches the result via pickle.

Brendan Dileo, August 2025
"""

import pickle 
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.text_utils import clean_text


def vectorize_songs(songs, save_path="vectors.pkl"):
    
    try:
        with open(save_path, "rb") as file:
            tfidf_matrix, vectorizer = pickle.load(file)
    except FileNotFoundError:

        docs = [song.get("lyrics", "") for song in songs]
        cleaned_docs = [clean_text(doc) for doc in docs]
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), min_df=2, max_df=0.9)
        tfidf_matrix = vectorizer.fit_transform(cleaned_docs)
        
        with open(save_path, "wb") as file:
            pickle.dump((tfidf_matrix, vectorizer), file)
            
    return tfidf_matrix, vectorizer