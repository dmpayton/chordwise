import json
import os

# Directories
APP_DIR = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2])
ASSETS_DIR = os.path.join(APP_DIR, 'assets')
KV_DIR = os.path.join(APP_DIR, 'kv')

# Fonts
FONTS = {
    'FreeSans': {
        'fn_regular': 'fonts/freefont/FreeSans.ttf',
        'fn_bold': 'fonts/freefont/FreeSansBold.ttf',
        'fn_italic': 'fonts/freefont/FreeSansOblique.ttf',
        'fn_bolditalic': 'fonts/freefont/FreeSansBoldOblique.ttf'
    },
    'FreeSerif': {
        'fn_regular': 'fonts/freefont/FreeSerif.ttf',
        'fn_bold': 'fonts/freefont/FreeSerifBold.ttf',
        'fn_italic': 'fonts/freefont/FreeSerifItalic.ttf',
        'fn_bolditalic': 'fonts/freefont/FreeSerifBoldItalic.ttf'
    },
    'RobotoThin': {
        'fn_regular': 'fonts/roboto/Roboto-Thin.ttf',
        'fn_bold': 'fonts/roboto/Roboto-Light.ttf',
        'fn_italic': 'fonts/roboto/Roboto-ThinItalic.ttf',
        'fn_bolditalic': 'fonts/roboto/Roboto-LightItalic.ttf'
    },
    'RobotoLight': {
        'fn_regular': 'fonts/roboto/Roboto-Light.ttf',
        'fn_bold': 'fonts/roboto/Roboto-Regular.ttf',
        'fn_italic': 'fonts/roboto/Roboto-LightItalic.ttf',
        'fn_bolditalic': 'fonts/roboto/Roboto-Italic.ttf'
    },
}

# Settings
SETTINGS = [
    {
        'type': 'title',
        'title': 'Settings',
    },
    {
        'type': 'numeric',
        'title': 'BPM',
        'desc': 'Beats Per Minute',
        'section': 'chordwise',
        'key': 'bpm',
    },
    {
        'type': 'options',
        'title': 'Time Signature',
        'desc': 'Time signature',
        'section': 'chordwise',
        'key': 'time_signature',
        'options': ['1/4', '2/4', '3/4', '4/4', '5/4', '6/8', '7/8', '8/8']
    },
    {
        'type': 'options',
        'title': 'Chords',
        'desc': 'Chords',
        'section': 'chordwise',
        'key': 'chords',
        'options': []
    }
]

print(SETTINGS)
