from plexapi.myplex import MyPlexAccount
from Apps import PlexAuth


account = MyPlexAccount(PlexAuth.getUsername(), PlexAuth.getPassword())
plex = account.resource(PlexAuth.getServerName()).connect()

movies = plex.library.section('Movies')

def getUnwatchedMovies():
    global movies
    arr = []
    for video in movies.search(unwatched=True):
        arr.append(video.title)
    return arr

def getMovieByDirector(director):
    global movies
    arr = []
    for movie in movies.search(None, director=director):
        arr.append(movie.title)
    return arr

def getMovieByTitle(title):
    global movies
    arr = []
    for movie in movies.search(title):
        arr.append(movie.title)
    return arr

