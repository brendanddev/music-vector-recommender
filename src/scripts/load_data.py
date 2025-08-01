
""" 
load_data.py
...

Brendan Dileo, August 2025
"""

from csv import DictReader, Error as CSVError
from random import shuffle
import json

def load_songs(filename, num=None, filetype='csv'):
    
    
    