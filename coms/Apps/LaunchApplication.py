# Ref: https://stackoverflow.com/questions/53132434/list-of-installed-programs/54825112
import os
import winreg
from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto import warnings
import re
import copy

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
        winreg.HKEY_CURRENT_USER, 0)

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


def checkDirPath(dirPath=None):
    list = os.listdir(dirPath)
    exe_list = []
    if list:
        for e in list:
            e_copy = copy.copy(e)
            r = re.compile('\.exe$')
            if r.search(e_copy):
                # e_copy = e.replace('.exe', '')
                exe_list.append(e)
    return exe_list


if __name__ == '__main__':
    apps = getInstalledApps()
    for app in apps:
        for key, value in list(app.items()):
            if key == 'install_location':
                print(value, ' ', checkDirPath(value))
            # if value == 'C:\Microsoft VS Code\\':
            #     v = checkDirPath(value)
            #     # launchApp(value + '/' + v[0])
            #     os.startfile(value + '/' + v[0])