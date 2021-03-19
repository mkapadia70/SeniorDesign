'''
Ref: https://stackoverflow.com/questions/53132434/list-of-installed-programs/54825112
     https://stackoverflow.com/questions/32341661/getting-a-windows-program-icon-and-saving-it-as-a-png-python/39811146
'''
import copy
import glob
import os
import re
import winreg

import win32api
import win32con
import win32gui
import win32ui
import winshell
from PIL import Image
from pywinauto import Desktop
from pywinauto import warnings
from pywinauto.application import Application

app = None
windows = None


def setup():
    global app
    global windows
    app = Application()
    windows = Desktop(backend="uia").windows()
    warnings.simplefilter('ignore', category=UserWarning)


def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            if winreg.QueryValueEx(asubkey, "InstallLocation")[0]:
                software['install_location'] = winreg.QueryValueEx(asubkey, "InstallLocation")[0]
            else:
                software['install_location'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list


def getInstalledApps():
    apps = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE,
                                                                        winreg.KEY_WOW64_64KEY) + foo(
        winreg.HKEY_CURRENT_USER, 1)

    for app in apps:
        for key, value in list(app.items()):
            if value == 'undefined':
                app.clear()
    apps = list(filter(None, apps))
    return apps


def launchApp(path):
    global app
    try:
        app = app.connect(path=path)
    except Exception as e:
        try:
            app = Application().start(path)
        except Exception as ex:
            print(ex)


def extractFileNames(directory):
    from os import listdir
    from os.path import isfile, join
    files = [f for f in listdir(directory) if isfile(join(directory, f))]

    program_names = []
    if files:
        for f in files:
            f_copy = copy.copy(f)
            r = re.compile('\.lnk$')
            if r.search(f_copy):
                f_copy = f_copy.replace('.lnk', '')
                program_names.append(f_copy)
    return program_names


def fetchExePaths(directory):
    exePaths = []
    for lnk in glob.glob(os.path.join(directory, "*.lnk")):
        shortcut = winshell.shortcut(lnk)
        exePaths.append(shortcut.path.replace("\\", "/" ))
    return exePaths


def extractExeIcons(exePath, exeName):
    path = exePath.replace("\\", "/")
    icoX = win32api.GetSystemMetrics(win32con.SM_CXICON)
    icoY = win32api.GetSystemMetrics(win32con.SM_CYICON)

    large, small = win32gui.ExtractIconEx(path, 0)
    win32gui.DestroyIcon(small[0])

    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap(hdc, icoX, icoY)
    hdc = hdc.CreateCompatibleDC()

    hdc.SelectObject(hbmp)
    hdc.DrawIcon((0, 0), large[0])

    # For original bitmap
    # hbmp.SaveBitmapFile(hdc, 'c:\\temp\\[filename].ico')

    bmpstr = hbmp.GetBitmapBits(True)
    img = Image.frombuffer(
        'RGBA',
        (32, 32),
        bmpstr, 'raw', 'BGRA', 0, 1
    )

    new_img_location = 'C:\\temp\\' + exeName + '.png'
    new_img = img.resize((128, 128), reducing_gap=3.0)
    new_img.save(new_img_location, format("PNG"))
    new_img_location = new_img_location.replace("\\", "/" )
    return new_img_location


def createProgramInfo(list1, list2, list3):
    programs = []
    for a, b, c in zip(list1, list2, list3):
        program = {'exe_path': a, 'name': b, 'icon_path': c}
        programs.append(program)
    return programs


if __name__ == '__main__':
    exe_paths = fetchExePaths(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
    exe_names = extractFileNames(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs')

    icon_paths = []
    for path, name in zip(exe_paths, exe_names):
        icon = extractExeIcons(path, name)
        icon_paths.append(icon)

    print(createProgramInfo(exe_paths, exe_names, icon_paths))
