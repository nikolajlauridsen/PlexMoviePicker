from plexapi.server import PlexServer
from random import choice
import os
import json

def get_genre_string(genre_list):
    genres = "Genre: "
    for genre in genre_list:
        genres += genre.tag
        if len(genre_list) > 1:
            genres += " | "
    return genres

def get_director_list(director_list):
    directors = "Director: "
    for director in director_list:
        directors += director.tag
        if len(director_list) > 1:
            directors += " | "
    return directors

def print_movie_info(movie):
    print("-"*40)
    print("Tiel: " + movie.title)
    print("Rating: " + movie.rating)
    print(get_director_list(movie.directors))

    if movie.studio:
        print("Studio: " + movie.studio)
    print("Year: " + str(movie.year))
    print(get_genre_string(movie.genres))
    print()

    try:
        print("Summary:\n" + movie.summary)
    except UnicodeEncodeError:
        print("Summary:\n" + str(movie.summary.encode('utf-8', 'replace')))
    print("-"*40)

def clear_screen():
    """Clears the commandline window"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

with open('settings.json', 'r') as f:
    config = json.loads("".join(f.readlines()))

plex = PlexServer(config["base_url"], config["api_key"])

section = plex.library.section('Film')
movies = section.search(unwatched=True)

while True:
    print("Feeling bored eh? I'll pick out a movie for ya.")
    print_movie_info(choice(movies))
    try:
        answer = input("Press enter to pick a new movie, e to exit\n")
    except KeyboardInterrupt:
        break;
    if answer.lower() == "e":
        break;
    clear_screen()
