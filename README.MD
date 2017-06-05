# PlexMoviePicker
Don't know, don't care what to watch? Choose randomly 

Was feeling particularly bored a slow monday afernoon, I felt like watching a movie, but really couldn't make up my mind.

So I cracked open my editor and wrote this really simple script which uses the plexapi module to query your plex server for all your unwatched movies, and then pick out a random one and display it to you.

## Setting up
This script uses the api key prvovided by your plex server for authentication, so a plex account is required, futher more the scripts reads the api key from a a settings.json file, I've included a template in the repository, simply open it up and past your api key, and then hit save. 

It's commonly not needed to fiddle with the base_url property of the json file, but if you're using a remote server, or a different port, you need to change it to whatever you use to acess your plex server.

After that you just run the script with:
```
py PlexMoviePicker.py
```
(Make sure settings.json is in the path enviroment)

## Requirements
### Third party
* [plexapi](https://github.com/pkkid/python-plexapi)
### Should be built in
* random
* os
* json
