
""" 
recommender.py
Calculates similarity scores for song vectors using cosine similarity and recommends similar songs
based on TF-IDF vectors representations.

Brendan Dileo, August 2025
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def init_recommendations(n, songs):
    """ Selects 'n' random songs from the provided list of songs """
    return np.random.choice(len(songs), n, replace=False).tolist()


def calculate_similarity(selected_doc, tfidf_matrix):
    """
    Calculates cosine similarity between a selected document and all other documents.

    Args:
        selected_doc (int): Index of the selected document in the TF-IDF matrix.
        tfidf_matrix (scipy.sparse matrix): TF-IDF matrix for all documents.

    Returns:
        np.ndarray: Flattened array of similarity scores.
    """
    cosine_sim = cosine_similarity(tfidf_matrix[selected_doc], tfidf_matrix)
    return cosine_sim.flatten()