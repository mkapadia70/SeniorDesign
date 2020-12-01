from Apps import WindowsVolumeMixerControl
from Apps import SpotifyControl
import time


def updateDevices():
    WindowsVolumeMixerControl.updateDevices()


def setupApps():
    SpotifyControl.setup()


def callFunctions(json):
    for i in json:
        for f in i["Funcs"]:
            # this lines finds a function in a module matching the function string given by the json and calls it
            return getattr(globals()[i["Name"]], f["Name"])(*f["Params"])


def getProcsAsJson():
    procs = WindowsVolumeMixerControl.getAllSoundDevices()
    procsJSONlist = []
    for p in procs:
        addition = {"Name": p.DisplayName, "Id": p.ProcessId}
        procsJSONlist.append(addition)
    return procsJSONlist
