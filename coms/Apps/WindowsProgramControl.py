from pywinauto.application import Application
# https://github.com/pywinauto/pywinauto

app = Application()

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
    