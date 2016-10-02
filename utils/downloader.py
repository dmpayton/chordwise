import csv
import os
from pprint import pprint

import requests

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def download_chord_image(chord):
    url = 'http://chordgenerator.net/{0}.png'.format(chord['name'])
    query = {
        'p': chord['position'],
        'f': chord['fingers'],
        's': 10
    }

    destination = os.path.join(THIS_DIR, 'chords-raw/{0}.png'.format(chord['name']))
    response = requests.get(url, query)

    with open(destination, 'wb') as f:
        f.write(response.content)


def chord_list():
    chord_data = os.path.join(THIS_DIR, '../data/chords.csv')
    reader = csv.DictReader(open(chord_data))
    yield from reader


def main():
    for chord in chord_list():
        print(chord['long_name'])
        download_chord_image(chord)


if __name__ == '__main__':
    main()
