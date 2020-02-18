import os
from PIL import Image

FILENAME = os.path.join(os.path.dirname(__file__),
                        'morse.gif')

morseAlphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}


def get_morse_time(PIL_Image_object):
    """ Returns the average framerate of a PIL Image object """
    PIL_Image_object.seek(0)
    frames = duration = 0
    morse = ""
    on = False
    while True:
        try:
            if PIL_Image_object.info['duration'] == 250 and on:
                morse += "."
            elif PIL_Image_object.info['duration'] == 750 and on:
                morse += "-"
            elif PIL_Image_object.info['duration'] == 1750:
                morse += " "
            elif PIL_Image_object.info['duration'] == 750 and not on:
                morse += " "
            if on:
                on = False
            else:
                on = True
            PIL_Image_object.seek(PIL_Image_object.tell() + 1)
        except EOFError:
            return morse
    return morseAlphabet

img_obj = Image.open(FILENAME)
morse = get_morse_time(img_obj)
print(morse)
i = 0
while True:
    morseKey = ""
    try:
        while morse[i] != " ":
            morseKey += morse[i]
            i += 1
        i += 1
    except IndexError:
        break
    for name, key in morseAlphabet.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if key == morseKey:
            print(name, end="")
