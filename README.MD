# PlexMoviePicker
Don't know, don't care what to watch? Choose randomly 

Was feeling particularly bored a slow monday afernoon, I felt like watching a movie, but really couldn't make up my mind.

So I cracked open my editor and wrote this really simple script which uses the plexapi module to query your plex server for all your unwatched movies, and then pick out a random one and display it to you.

## Setting up
For the script to work it needs to know a few things.
1. Who are you?
2. Where is the server?
3. Where should I look on the server? 

### Who are you?
This script uses the api key prvovided by your plex server for authentication, so a plex account is required, futher more the scripts reads the api key from a a settings.json file, I've included a template in the repository, simply open it up and paste your api key, and then hit save. 

[Can't find your token? Click here](https://support.plex.tv/hc/en-us/articles/204059436-Finding-an-authentication-token-X-Plex-Token)

### Where is the server?
It's commonly not needed to fiddle with the base_url property of the json file, but if you're using a remote server, or a different port, you need to change it to whatever you use to acess your plex server.

### Where should I look on the server?
The script needs to know what section to look in, in the json file it's the library_name property, simply write the name of your movie plex library, by default I've set it to "Movie" but just change that to whatever your library is called.

After that you just run the script with:
```
py PlexMoviePicker.py
```
(Make sure settings.json is in the path enviroment, also most linux distros use python3 instead of py)

## Requirements
You can install requirements with pip 

``` py -m pip install -r requirements.txt ```
### Third party
* [plexapi](https://github.com/pkkid/python-plexapi)
### Should be built in
* random
* os
* sys
* json
