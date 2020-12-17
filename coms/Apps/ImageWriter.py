import requests
import base64

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