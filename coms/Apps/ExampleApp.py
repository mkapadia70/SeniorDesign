
def getExampleData():
    jason = {
                "text": "this is text from python"
            }
    return jason

def numberOfLetters(text):
    # returns a json object with number of letters in the given text
    jason = {
                "numberVal": str(len(text))
            }
    return jason
