import spotipy
from spotipy.oauth2 import SpotifyOAuth
from Apps import SpotifyAuth

# make sure to update your credentials in SpotifyAuth.py
auth_manager = SpotifyAuth.getAuthManager()

sp = spotipy.Spotify(auth_manager=auth_manager)

def setup():
    # setup 
    global sp
    global auth_manager
    sp = spotipy.Spotify(auth_manager=auth_manager)
    auth_manager = SpotifyAuth.getAuthManager()

def pausePlayback():
    global sp
    sp.pause_playback()


def startPlayback():
    global sp
    sp.start_playback()

# params: newVolume - the new volume for the player (0-100)


def setVolume(newVolume):
    global sp
    sp.volume(int(newVolume))


def getVolume():
    global sp
    return int(sp.devices()[0]["volume_percent"])

# params: shuffleState - true for shuffle false for linear
def setShuffle(shuffleState):
    global sp
    sp.shuffle(shuffleState == "true")


def skipSong():
    global sp
    sp.next_track()


def previousSong():
    global sp
    sp.previous_track()

# params:
# repeatState - the new state for repeat
#   "track" - repeat the current track
#   "context" - repeat the current context (NO IDEA WHAT THIS MEANS) ***update: this means to loop the entire album/playlist***
#   "off" - no repeat
def setRepeatStatus(repeatState):
    global sp
    sp.repeat(repeatState)


def getCurrentlyPlaying():
    global sp
    return sp.currently_playing()


def getPlaybackStatus():
    global sp
    return sp.currently_playing()['is_playing']

def seek(pos):
    # seek to position in percentage of track
    global sp
    pos_ms = int(float(pos) * sp.currently_playing()['item']['duration_ms'])
    sp.seek_track(pos_ms)
