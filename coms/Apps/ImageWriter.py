import requests
import base64
from PIL import Image
import win32api
import win32con
import win32gui
import win32ui

# ImageWriter.py
# currently this is only used by our spotify driver to store and convert album art data

# this function downloads an image from a url to the path specified
def writeImage(writepath, pic_url):
    try:
        with open(writepath, 'wb') as handle:
            response = requests.get(pic_url, stream=False)
            if not response.ok:
                print(response)
            for block in response.iter_content(None):
                if not block:
                    break
                handle.write(block)
            return True
    except Exception as e:
        print(e)
    return False

# this function encodes an image using base64 encoding and return a string of the encoding
# this is being used to send an image, as text, as a json object
def imageTo64String(path):
    try:
        with open(path, "rb") as image_file:
            return str(base64.b64encode(image_file.read()))
    except Exception as e:
        print(e)
    return None


# given a path, extract an exe's icon image and save it to the output path
# from here: https://stackoverflow.com/questions/32341661/getting-a-windows-program-icon-and-saving-it-as-a-png-python/39811146
def getAndWriteProgImage(input_path, output_path):

    input_path = input_path.replace("\\", "/")
    icoX = win32api.GetSystemMetrics(win32con.SM_CXICON)
    icoY = win32api.GetSystemMetrics(win32con.SM_CXICON)

    large, small = win32gui.ExtractIconEx(input_path, 0)
    win32gui.DestroyIcon(small[0])

    hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
    hbmp = win32ui.CreateBitmap()
    hbmp.CreateCompatibleBitmap(hdc, icoX, icoX)
    hdc = hdc.CreateCompatibleDC()

    hdc.SelectObject(hbmp)
    hdc.DrawIcon((0,0), large[0])
    
    bmpstr = hbmp.GetBitmapBits(True)
    img = Image.frombuffer(
        'RGBA',
        (32,32),
        bmpstr, 'raw', 'BGRA', 0, 1
    )
    img.save(output_path)