# read in the movies.txt file
# - read into array with no newlines
# - process each line and parse into appropriate variables
# - A) create a movie tuple and store in a list of movies
# - B) replace the tuple with a movie class and store in list of movies

from movie import Movie


FILE_NAME = './files/movies.txt'

# list of movie strings
movies_list_str = []
with open(FILE_NAME) as movie_in:
    movies_list_str = movie_in.read().splitlines()
    # print(f'movies_list: {movies_list_str}')

# a list of movie tuples
movies_list = []
for movie_str in movies_list_str:
    #movie_data = movie_str.split("\\t")
    #print(f'movie_data: {movie_data}')
    title, year, rating, director = movie_str.split("\\t")
    #print(f'Movie Data: {title}, {year}, {rating}, {director}')
    movie = Movie(title, year, rating, director)
    # add movie details as a tuple
    #movies_list.append((title, year, rating, director))
    # add movie details as an instance of Movie class
    movies_list.append(movie)
print("+"*20)
print("Movies Summary:")
for m in movies_list:
    print(m.details())