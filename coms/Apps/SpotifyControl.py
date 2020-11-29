import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import SpotifyAuth

# MAX PLZ HELP ME FIGURE THIS SHIT OUT
# https://github.com/plamere/spotipy/issues/287
# https://github.com/plamere/spotipy/issues/262

#https://developer.spotify.com/documentation/general/guides/scopes/#app-remote-control
scope = "user-modify-playback-state user-read-currently-playing"

auth_manager = SpotifyAuth.auth_manager # make sure to update your credentials in SpotifyAuth.py

sp = spotipy.Spotify(auth_manager=auth_manager)

def pausePlayback():
    global sp
    sp.pause_playback()

def startPlayback():
    global sp
    sp.start_playback()

#params: newVolume - the new volume for the player (0-100)
def setVolume(newVolume):
    global sp
    sp.volume(newVolume)

def getVolume():
    #Not sure this is possible
    return

#params: shuffleState - true for shuffle false for linear
def setShuffle(shuffleState):
    global sp
    sp.shuffle(shuffleState)

def skipSong():
    global sp
    sp.next_track()

def previousSong():
    global sp
    sp.previous_track()

#params:
# repeatState - the new state for repeat
#   "track" - repeat the current track
#   "context" - repeat the current context (NO IDEA WHAT THIS MEANS)
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