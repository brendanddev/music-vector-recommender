
""" 
process_text.py

Brendan Dileo, July 2025
"""


import re
import pickle 

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_text(text) -> str:
    """ 
    Cleans input text by lowecasing, removing html tags, section headers, parentheses content, special chars,
    and collapsing multiple spaces into a single space.
    """
    cleaned_text = text.lower()
    cleaned_text = re.sub(r'<[^>]+>', '', cleaned_text)
    cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)  
    cleaned_text = re.sub(r'\([^)]*\)', '', cleaned_text)
    cleaned_text = re.sub(r'[^a-z0-9\s\']', ' ', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()  
    return cleaned_text


def vectorize_songs(songs, save_path="vectors.pkl"):