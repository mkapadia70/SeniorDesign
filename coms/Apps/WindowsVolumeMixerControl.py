from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Master Volume
def muteMasterVolume():
    volume.SetMute(1,None)

def unmuteMasterVolume():
    volume.SetMute(0,None)

# param: new level of volume from 0.0 to 1.0
def setMasterVolume(newVolume):
    volume.SetMasterVolumeLevelScalar(newVolume, None)

# Application Volume
# param: application session
def muteApplicationVolume(session):
    session.SimpleAudioVolume.SetMute(1, None)

# param: application session
def unmuteApplicationVolume(session):
    session.SimpleAudioVolume.SetMute(0, None)

# param: application session, and new level from 0.0 to 1.0
def setApplicationVolume(session, newVolume):
    session.SimpleAudioVolume.SetMasterVolume(newVolume, None)

def getAllSoundDevices():
    return AudioUtilities.GetAllSessions()
