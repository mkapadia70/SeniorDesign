from Apps import WindowsVolumeMixerControl
from Apps import SpotifyControl

def updateDevices():
    WindowsVolumeMixerControl.updateDevices()

# WindowsVolumeMixerControl


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
            current = SpotifyControl.getCurrentlyPlaying()['item']['album']['images'][0]['url']
            SpotifyControl.skipSong()
            newData = current
            while current == newData:
                newData = SpotifyControl.getCurrentlyPlaying()['item']['album']['images'][0]['url']
            return SpotifyControl.getCurrentlyPlaying()
        elif(i["Name"] == "prevSong"):
            # mega bad
            current = SpotifyControl.getCurrentlyPlaying()['item']['album']['images'][0]['url']
            SpotifyControl.previousSong()
            newData = current
            while current == newData:
                newData = SpotifyControl.getCurrentlyPlaying()['item']['album']['images'][0]['url']
            return SpotifyControl.getCurrentlyPlaying()
        elif(i["Name"] == "pauseSong"):
           SpotifyControl.pausePlayback()
        elif(i["Name"] == "playSong"):
           SpotifyControl.startPlayback()


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
