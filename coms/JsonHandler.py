from Apps import WindowsVolumeMixerControl
from Apps import SpotifyControl
import time
import SerialHandler

def updateDevices():
    WindowsVolumeMixerControl.updateDevices()


def setupApps():
    SpotifyControl.setup()


def callFunctions(json):
    for i in json:
        for f in i["Funcs"]:
            # this lines finds a function in a module matching the function string given by the json and calls it
            try:
                return getattr(globals()[i["Name"]], f["Name"])(*f["Params"])
            except Exception as e:
                print(e)
                return None

