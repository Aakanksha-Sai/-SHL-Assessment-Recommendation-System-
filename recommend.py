import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv('data/shl_assessments.csv')

# Combine relevant fields for better matching
df['search_text'] = df['Assessment Name'] + ' ' + df['Test Type']

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['search_text'])

def recommend(query, top_n=10):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = scores.argsort()[-top_n:][::-1]
    return df.iloc[top_indices]
