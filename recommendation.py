# movie_recommendation.py

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load Dataset
# -----------------------------
try:
    movies = pd.read_csv('movies.csv')
except FileNotFoundError:
    print("Error: movies.csv file not found!")
    print("Please place movies.csv in the same folder as this script.")
    exit()

# -----------------------------
# Handle Missing Values
# -----------------------------
movies.fillna('', inplace=True)



# -----------------------------
# Check Required Columns
# -----------------------------
required_columns = ['title', 'genres']

for column in required_columns:
    if column not in movies.columns:
        print(f"Error: '{column}' column not found in dataset.")
        exit()

# -----------------------------
# Convert Genres to Feature Vectors
# -----------------------------
vectorizer = CountVectorizer(token_pattern='[^|]+')

feature_vectors = vectorizer.fit_transform(movies['genres'])

# -----------------------------
# Calculate Cosine Similarity
# -----------------------------
similarity = cosine_similarity(feature_vectors)


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend_movies(movie_name, num_recommendations=10):

    movie_name = movie_name.lower()

    # Find movie in dataset
    matching_movies = movies[
        movies['title'].str.lower().str.contains(movie_name, na=False)
    ]

    if matching_movies.empty:
        print("\nMovie not found in the dataset.")
        return

    # Get first matching movie
    movie_index = matching_movies.index[0]
    selected_movie = movies.iloc[movie_index]['title']

    print(f"\nYou selected: {selected_movie}")
    print("\nRecommended Movies:\n")

    # Get similarity scores
    similarity_scores = list(enumerate(similarity[movie_index]))

    # Sort by similarity score
    sorted_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    count = 0

    for movie in sorted_scores:

        index = movie[0]
        score = movie[1]

        # Skip the selected movie itself
        if index == movie_index:
            continue

        title = movies.iloc[index]['title']

        print(f"{count + 1}. {title} (Similarity: {score:.2f})")

        count += 1

        if count >= num_recommendations:
            break


# -----------------------------
# Main Program
# -----------------------------
print("=" * 50)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

while True:

    user_movie = input(
        "\nEnter a movie name (or type 'exit' to quit): "
    )

    if user_movie.lower() == 'exit':
        print("\nThank you for using the Movie Recommendation System!")
        break

    recommend_movies(user_movie)