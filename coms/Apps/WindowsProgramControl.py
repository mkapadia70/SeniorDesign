from pywinauto.application import Application
from pywinauto import Desktop
# https://github.com/pywinauto/pywinauto

# WindowsProgramControl.py
# this uses a very powerful library that can execute many windows api calls
# many different apps may take use from the functions in this file
# e.g the spotify app will call this library to open spotify if it is not open yet



app = None
windows = None

def setup():
    global app
    global windows
    app = Application()
    windows = Desktop(backend="uia").windows()

def startNotepad():
    app = Application().start("notepad.exe")
    app.UntitledNotepad.Edit.type_keys("Hello Jace, python is writing this...", with_spaces = True)

def openProgram(path):
    global app
    try:
        app = app.connect(path=path)
    except Exception as e:
        print(e)
        try:
            app = Application().start(path)
        except Exception as ex:
            print(ex)

# returns a list of open windows (for alt-tabbing purposes)
def getOpenWindows():
    global windows
    openWindowsString = [w.window_text() for w in windows]
    # print(openWindowsString)
    # also get the icon images????
    return openWindowsString

# if the given program is open, switches the focus to it
def switchFocus(newFocus):
    try:
        app.connect(title_re=".*%s" % newFocus)
        app_dialog = app.window(title_re=".*%s.*" % newFocus)
        if app_dialog.exists():
            app_dialog.set_focus()
    except Exception as e:
        print(e)