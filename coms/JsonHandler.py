from Apps import WindowsVolumeMixerControl

#w = WindowsVolumeMixerControl

# WindowsVolumeMixerControl
def WindowsVolumeMixer(funcs):
    for i in funcs:
        if(i["Name"] == "muteMasterVolume"):
            WindowsVolumeMixerControl.muteMasterVolume()
        elif(i["Name"] == "unmuteMasterVolume"):
            WindowsVolumeMixerControl.unmuteMasterVolume()
        elif(i["Name"] == "setMasterVolume"):
            WindowsVolumeMixerControl.setMasterVolume(i["Params"][0])
        elif(i["Name"] == "muteApplicationVolume"):
            WindowsVolumeMixerControl.muteApplicationVolume(i["Params"][0])
        elif(i["Name"] == "unmuteApplicationVolume"):
            WindowsVolumeMixerControl.unmuteApplicationVolume(i["Params"][0])
        elif(i["Name"] == "setApplicationVolume"):
            processes = WindowsVolumeMixerControl.getAllSoundDevices()
            for process in processes:
                if str(process.ProcessId) == i["Params"][1]:
                    WindowsVolumeMixerControl.setApplicationVolume(process, i["Params"][0])
                    break

def callFunctions(json):

    for i in json:
        if(i["Name"] == "WindowsVolumeMixerControl"):
            WindowsVolumeMixer(i["Funcs"])