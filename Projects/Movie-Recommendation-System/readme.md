## Movie Recommendation System
This code uses the concepts of content-based filtering to recommend movies to a user based on the movies that the user likes.

## My learning goal
- Obtain an already written code
- Understand the code with the help of ChatGPT and google
- Replicate or recreate the same code
- Get a new dataset and achieve the same
- Create an app?

## Code Description
The code reads in a csv file containing movie data, and uses the following features to recommend similar movies:

keywords
cast
genres
director
These features are combined into a new column called "combined_features". A count matrix is then created from this column, and the cosine similarity between movies is computed based on this matrix.

The user can input the name of a movie that they like, and the code will then recommend 50 similar movies in descending order of similarity score.

## Required Libraries
pandas
numpy
sklearn

## Use Instructions

Replace "movie_dataset.csv"  with the path to your movie dataset csv file.
Run the code and enter the title of a movie that the user likes when prompted.
The code will print the titles of the recommended movies.

The raw code was obtained from [code heroku](https://github.com/codeheroku/Introduction-to-Machine-Learning/blob/cb915bab2892a0cf4e60da956c493a83753af3cb/Building%20a%20Movie%20Recommendation%20Engine/movie_recommender_completed.py). 

