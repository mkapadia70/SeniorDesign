import Apps/WindowsVolumeMixerControl

def callFunctions(json):
    for i in json:
        if(i["Name"] == "Windows"): WindowsVolumeMixerControl(i["Funcs"])

testData = [{"Name":"Windows","Funcs":[{"Name":"SetMasterVolume","params":["1","2"]},{"Name":"Mute","params":["1","2","3"]}]},{"Name":"Spotify","Funcs":{"Func1":{"Name":"SkipSongy","params":["1","2"]},"Func2":{"Name":"FindTriPham","params":["1","2","3"]}}}]
callFunctions(testData)

# WindowsVolumeMixerControl
def WindowsVolumeMixerControl(funcs):
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
            WindowsVolumeMixerControl.setApplicationVolume(i["Params"][0], i["Params"][1])