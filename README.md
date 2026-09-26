# 🎬 Movie Recommendation System

A simple **content-based Movie Recommendation System** built using Python and Machine Learning concepts. The system recommends movies similar to a movie entered by the user by analyzing movie genres and calculating their similarity.

## 🚀 Features

- 🎬 Accepts a movie name as user input
- 🔍 Searches for the selected movie in the dataset
- 🎭 Analyzes movie genres to identify similar movies
- 🤖 Uses **CountVectorizer** for converting genres into feature vectors
- 📊 Uses **Cosine Similarity** to measure similarity between movies
- ⭐ Displays the top 10 recommended movies
- 📈 Shows a similarity score for each recommendation
- ❌ Handles movies that are not available in the dataset
- 🔄 Allows users to continue searching for different movies
- 🚪 Type `exit` to close the application

## 🧠 How It Works

The recommendation system follows a simple content-based filtering approach:

1. The movie dataset is loaded using **Pandas**.
2. Missing values are handled.
3. Movie genres are converted into numerical feature vectors using **CountVectorizer**.
4. **Cosine Similarity** is calculated between the genre vectors.
5. The user enters a movie name.
6. The system finds the selected movie in the dataset.
7. Movies are ranked according to their similarity score.
8. The top 10 similar movies are displayed.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- CountVectorizer
- Cosine Similarity
- CSV Dataset

## 📁 Project Structure

```text
Movie-Recommendation/
│
├── recommendation.py    # Main recommendation program
├── movies.csv           # Movie information and genres
├── ratings.csv          # Movie ratings dataset
├── links.csv            # Movie-related links/IDs
├── tags.csv             # Movie tags
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
