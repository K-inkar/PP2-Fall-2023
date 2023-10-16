movies = [
{
"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"
},
{
"name": "Hitman", "imdb": 6.3, "category": "Action"
},
{
"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"
},
{
"name": "The Help", "imdb": 8.0, "category": "Drama"
},
{
"name": "The Choice", "imdb": 6.2, "category": "Romance"
},
{
"name": "Colonia", "imdb": 7.4, "category": "Romance"
},
{
"name": "Love", "imdb": 6.0, "category": "Romance"
},
{
"name": "Bride Wars", "imdb": 5.4, "category": "Romance"
},
{
"name": "AlphaJet", "imdb": 3.2, "category": "War"
},
{
"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"
},
{
"name": "Joking muck", "imdb": 7.2, "category": "Comedy"
},
{
"name": "What is the name", "imdb": 9.2, "category": "Suspense"
},
{
"name": "Detective", "imdb": 7.0, "category": "Suspense"
},
{
"name": "Exam", "imdb": 4.2, "category": "Thriller"
},
{ 
"name": "We Two", "imdb": 7.2, "category": "Romance" 
 }
]



#1
def is_high_imdb(movie_name, dataset):
    movie = next((movie for movie in dataset if movie["name"] == movie_name), None)
    return movie is not None and movie["imdb"] > 5.5

movie_name = input("MOVIE:")

result = is_high_imdb(movie_name, movies)
print(result)

#2
def filter_high_imdb_movies(movie_list):
    high_imdb_movies = [movie for movie in movie_list if movie["imdb"] > 5.5]
    return high_imdb_movies

high_imdb_movies = filter_high_imdb_movies(movies)

for movie in high_imdb_movies:
   print (f"{movie['name']}, IMDB: {movie['imdb']}")

#3
def movies_category(movie_list, category):
    filtered_movies = [movie["name"] for movie in movie_list if movie["category"] == category]
    return filtered_movies

category = input("Category: ")
category_movies = movies_category(movies, category)

if category_movies:
    print(category)
    for movie_name in category_movies:
        print(movie_name)
else:
    print(category)

#4
def calculate_average_imdb(selected_movies, movie_list):
    selected_movies = [name.strip() for name in selected_movies]
    valid_movies = [movie for movie in movie_list if movie["name"] in selected_movies]

    if valid_movies:
        average_imdb = sum(movie["imdb"] for movie in valid_movies) / len(valid_movies)
        return average_imdb
    return 0.0

selected_movie_names = input().split(',')
average_imdb = calculate_average_imdb(selected_movie_names, movies)

print(average_imdb)

#5
def average_category(category, movie_list):
    category_movies = [movie for movie in movie_list if movie["category"] == category]
    
    if category_movies:
        average_imdb = sum(movie["imdb"] for movie in category_movies) / len(category_movies)
        return average_imdb
    return 0.0

category = input()
average_imdb = average_category(category, movies)

print(average_imdb)