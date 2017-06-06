from plexapi.server import PlexServer
from random import choice
import sys
import os
import json


def get_tag_list(itera):
    """
    Multiple items has the name as a tag value, this includes directors 
    and genres, this function creates a horizontal string list of the tag 
    attribute from all objects in a list
    :param itera: iterable containing elements with a tag attribute
    :return: horizontal string list of with the tag attribute from each 
    element
    """
    taglist = ""

    for item in itera:
        taglist += item.tag
        if len(itera) > 1:
            taglist += " | "

    return taglist


def convert_duration(milliseconds):
    """
    Convert milliseconds to a timestamp
    Format: HH:MM:SS
    """
    # it's easier to wrap your head around seconds
    seconds = milliseconds / 1000

    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    s = (seconds % 3600) % 60

    return "{:02}:{:02}:{:02}".format(int(hrs), int(mins), int(s))


def print_movie_info(movie):
    """
    Prints relevant information about a movie in a pretty-ish manner
    Takes a plexapi movie opbject as parameter
    """
    print("-"*40)
    print("Tiel: " + movie.title)
    print("Runtime: " + convert_duration(movie.duration))
    print("Rating: " + movie.rating)
    print("Director: " + get_tag_list(movie.directors))

    # Sometimes plex doesn't have information about the studio.
    if movie.studio:
        print("Studio: " + movie.studio)
    print("Year: " + str(movie.year))
    print("Genre: " + get_tag_list(movie.genres))
    print()

    try:
        print("Summary:\n" + movie.summary)
    except UnicodeEncodeError:  # The dreaded UnicodeEncodeError :(
        # Encode it to utf-8 replacing invalid characters
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
# Commands to exit the script
EXIT_COMMANDS = ['e', 'exit', 'q', 'quit']

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
        break
    # If the user entered e, exit, q or quit they probably want to quit
    if answer.lower() in EXIT_COMMANDS:
        break
    # Clearing the terminal keeps things from getting messy
    clear_screen()
