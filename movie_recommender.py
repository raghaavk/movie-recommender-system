import pandas as pd

# Load datasets
movies = pd.read_csv('data/movies.csv')
ratings = pd.read_csv('data/ratings.csv')

# Merge them
movie_data = pd.merge(ratings, movies, on='movieId')

# Create user-movie matrix
movie_matrix = movie_data.pivot_table(index='userId', columns='title', values='rating')

# Pick a movie
target_movie = 'Beautiful Mind, A (2001)'
target_ratings = movie_matrix[target_movie]

# Find correlation with other movies
similar_movies = movie_matrix.corrwith(target_ratings)
corr_df = pd.DataFrame(similar_movies, columns=['Correlation'])
corr_df.dropna(inplace=True)

# Add number of ratings
rating_count = movie_data.groupby('title')['rating'].count()
corr_df['rating_count'] = rating_count

# Filter & sort
recommendations = corr_df[corr_df['rating_count'] > 100].sort_values('Correlation', ascending=False).head(10)

print("Recommended movies similar to:", target_movie)
print(recommendations)
