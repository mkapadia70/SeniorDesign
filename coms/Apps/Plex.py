from plexapi.myplex import MyPlexAccount


username = "username"
password = "password"
serverName = "Jace Plex V3"
def getPassword():
    global password
    return password

def getUsername():
    global username 
    return username

def getServerName():
    global serverName 
    return serverName


account = MyPlexAccount(getUsername(), getPassword())
plex = account.resource(getServerName()).connect()
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

