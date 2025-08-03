
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


def get_similar_songs(sorted_indices, songs, num_similar=10):
    """ 
    Filters out duplicate song titles and returns the top N unique song indices.

    Args:
        sorted_indices (list): List of song indices sorted by similarity (highest to lowest).
        songs (list): List of song dictionaries.
        num_similar (int): Number of unique similar songs to return.
        
    Returns:
        list: Indices of unique recommended songs.
    """
    
    # Track titles already seen to avoid duplicates
    unique_titles = set()
    recommendations = []
    
    for idx in sorted_indices:
        # Get title of the current song
        title = songs[idx].get("title", "")
        if title and title not in unique_titles:
            # Add to results if unique
            recommendations.append(idx)
            unique_titles.add(title)
        if len(recommendations) >= num_similar:
            break
    return recommendations


def generate_recommendations(selected_index, tfidf_matrix, songs, num_recs=10):
    """
    Generates new song recommendations based on similarity to a selected song.

    Args:
        selected_index (int): Index of the song chosen by the user.
        tfidf_matrix (scipy sparse matrix): Matrix of TF-IDF vectors for all songs.
        songs (list): List of song dictionaries.
        num_recs (int): Number of similar songs to recommend.

    Returns:
        list: Indices of recommended songs.
    """
    
    # Compute similarity scores for the selected song
    sim_scores = calculate_similarity(selected_index, tfidf_matrix)
    
    # Sort by descending similarity, excluding the selected song itself
    sorted_indices = np.argsort(sim_scores)[::-1]
    sorted_indices = sorted_indices[1:]
    return get_similar_songs(sorted_indices, songs, num_recs)