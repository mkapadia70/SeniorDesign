from Apps import WindowsVolumeMixerControl
from Apps import SpotifyControl

def updateDevices():
    WindowsVolumeMixerControl.updateDevices()

# WindowsVolumeMixerControl

def setupApps():
    SpotifyControl.setup()


def WindowsVolumeMixer(funcs):
    for i in funcs:
        if(i["Name"] == "muteMasterVolume"):
            WindowsVolumeMixerControl.muteMasterVolume()
        elif(i["Name"] == "unmuteMasterVolume"):
            WindowsVolumeMixerControl.unmuteMasterVolume()
        elif(i["Name"] == "setMasterVolume"):
            WindowsVolumeMixerControl.setMasterVolume(i["Params"][0])
        elif(i["Name"] == "getMasterVolume"):
            return WindowsVolumeMixerControl.getMasterVolume()
        elif(i["Name"] == "muteApplicationVolume"):
            WindowsVolumeMixerControl.muteApplicationVolume(i["Params"][1])
        elif(i["Name"] == "unmuteApplicationVolume"):
            WindowsVolumeMixerControl.unmuteApplicationVolume(i["Params"][1])
        elif(i["Name"] == "setApplicationVolume"):
            WindowsVolumeMixerControl.setApplicationVolume(
                i["Params"][1], i["Params"][0])
        elif(i["Name"] == "getAllSoundDeviceData"):
            return WindowsVolumeMixerControl.getAllSoundDeviceData()


def Spotify(funcs):
    for i in funcs:
        if(i["Name"] == "getCurrentData"):
            return SpotifyControl.getCurrentlyPlaying()
        elif(i["Name"] == "skipSong"):
            # mega bad
            x = 1
            current = SpotifyControl.getCurrentlyPlaying()
            SpotifyControl.skipSong()
            newData = current
            while current['item']['id'] == newData['item']['id'] and x < 10:
                x += 1
                newData = SpotifyControl.getCurrentlyPlaying()
            return newData
        elif(i["Name"] == "prevSong"):
            # mega bad
            x = 1
            current = SpotifyControl.getCurrentlyPlaying()
            SpotifyControl.previousSong()
            newData = current
            while current['item']['id'] == newData['item']['id'] and x < 10:
                x += 1
                newData = SpotifyControl.getCurrentlyPlaying()
            return newData
        elif(i["Name"] == "pauseSong"):
           SpotifyControl.pausePlayback()
        elif(i["Name"] == "playSong"):
           SpotifyControl.startPlayback()
        elif(i["Name"] == "seek"):
           SpotifyControl.seek(i["Params"][0])
        elif(i["Name"] == "setShuffle"):
           SpotifyControl.setShuffle(i["Params"][0])
        elif(i["Name"] == "setRepeatStatus"):
           SpotifyControl.setRepeatStatus(i["Params"][0])
        elif(i["Name"] == "setVolume"):
           SpotifyControl.setVolume(i["Params"][0])

def callFunctions(json):
    for i in json:
        name = i["Name"]
        if(name == "WindowsVolumeMixerControl"):
            return WindowsVolumeMixer(i["Funcs"])
        elif(name == "SpotifyControl"):
            return Spotify(i["Funcs"])


def getProcsAsJson():
    procs = WindowsVolumeMixerControl.getAllSoundDevices()
    procsJSONlist = []
    for p in procs:
        addition = {"Name": p.DisplayName, "Id": p.ProcessId}
        procsJSONlist.append(addition)
    return procsJSONlist
