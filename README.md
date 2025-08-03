# Music Vector Recommender

A lightweight command-line music recommendation tool that uses song lyrics to suggest similar tracks based on vectorized semantic similarity.

---

## Features
- Recommends songs based on lyric similarity using TF-IDF vectorization.
- Cosine similarity determines how closely songs match.
- Removes duplicate song titles for clean suggestions.
- Easy to configure number of recommendations, dataset location, etc.
- Optional debug mode to view raw similarity scores for transparency and testing.

--- 

## How It Works
1. Lyrics are cleaned and vectorized using TF-IDF.
2. The selected song's lyrics are compared against all others using cosine similarity.
3. The most similar (non-duplicate) songs are recommended.

---

## Dataset

You can provide your own dataset in CSV format (title, artist, lyrics), or use the sample below.

--- 

## Attributions

- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Kaggle Genius Lyrics Dataset](https://www.kaggle.com/datasets/carlosgdcj genius-song-lyrics-with-language-information)