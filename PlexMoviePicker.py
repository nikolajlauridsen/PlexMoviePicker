from plexapi.server import PlexServer
from random import choice
import os
import json

# TODO: Why have to functions which do the same? Fix that.
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
    """
    Prints relevant information about a movie in a pretty-ish manner
    Takes a plexapi movie opbject as parameter
    """
    print("-"*40)
    print("Tiel: " + movie.title)
    print("Rating: " + movie.rating)
    print(get_director_list(movie.directors))

    # Sometimes plex doesn't have information about the studio.
    if movie.studio:
        print("Studio: " + movie.studio)
    print("Year: " + str(movie.year))
    print(get_genre_string(movie.genres))
    print()

    try:
        print("Summary:\n" + movie.summary)
    except UnicodeEncodeError:  # The dreaded UnicodeEncodeError :(
        # Encode it to utf-8 replacing invalid charecters
        # (shouldn't be more than a few chars, not really detrimental)
        print("Summary:\n" + str(movie.summary.encode('utf-8', 'replace')))
    print("-"*40)

def clear_screen():
    """Clears the commandline window"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Read config from settings.json
with open('settings.json', 'r') as f:
    config = json.loads("".join(f.readlines()))

# Create a PlexServer opbject we can query.
plex = PlexServer(config["base_url"], config["api_key"])

# Retrieve the relevant library (movies), and search for all unwatched movies
section = plex.library.section(config["library_name"])
movies = section.search(unwatched=True)

while True:
    print("Feeling bored eh? I'll pick out a movie for ya.")
    # Pick a random movie and print relevant information to terminal
    print_movie_info(choice(movies))
    # Wait for the user to finish reading and hit enter.
    # Handling KeyboardInterrupt properly makes for much prettier output
    try:
        answer = input("Press enter to pick a new movie, e to exit\n")
    except KeyboardInterrupt:
        break;
    # If the user entered e, exit, q or quit they probably want to quit
    if answer.lower() == "e" or "exit" or "q" or "quit":
        break;
    # Clearing the terminal keeps things from getting messy
    clear_screen()
