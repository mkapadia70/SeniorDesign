from Apps import WindowsVolumeMixerControl
from Apps import SpotifyControl
import time

# probably bad but looks super clean
appDict = {
    "SpotifyControl": SpotifyControl,
    "WindowsVolumeMixerControl": WindowsVolumeMixerControl
}

def updateDevices():
    WindowsVolumeMixerControl.updateDevices()

# WindowsVolumeMixerControl

def setupApps():
    SpotifyControl.setup()


def callFunctions(json):
    for i in json:
        for f in i["Funcs"]:
            return appDict[i["Name"]].functionDict.get(f["Name"], lambda: 'Invalid')(*f["Params"])


def getProcsAsJson():
    procs = WindowsVolumeMixerControl.getAllSoundDevices()
    procsJSONlist = []
    for p in procs:
        addition = {"Name": p.DisplayName, "Id": p.ProcessId}
        procsJSONlist.append(addition)
    return procsJSONlist
