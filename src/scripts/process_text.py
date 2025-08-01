
""" 
process_text.py

Brendan Dileo, July 2025
"""

import os
import re
import pickle 

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_text(text) -> str:
    """  Cleans input text by converting to lowercase and removing html tags """
    cleaned_text = text.lower()
    cleaned_text = re.sub(r'<[^>]+>', '', cleaned_text)
    return cleaned_text


def vectorize_songs(songs, save_path="vectors.pkl"):