import requests
import base64

def writeImage(pic_url):
    try:
        with open('album.png', 'wb') as handle:
            response = requests.get(pic_url, stream=True)
            if not response.ok:
                print(response)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
            return True
    except Exception as e:
        print(e)
    return False

def imageTo64String(path):
    try:
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read())  
    except Exception as e:
        print(e)
    return None