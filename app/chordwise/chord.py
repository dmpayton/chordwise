from collections import OrderedDict

from pychord import Chord

from .utils import asset


class ChordDB(object):
    types = OrderedDict((
        ('major', {
            'title': 'Major chords',
            'quality': '',
        }),
        ('minor', {
            'title': 'Minor chords',
            'quality': 'm',
        }),
        ('5', {
            'title': '5th (Power) chords',
            'quality': '5',
        })
    ))

    def __init__(self):
        self.chords = []

        for root in 'ABCDEFG':
            self.chords.append(Chord(root))
            self.chords.append(Chord('{0}m'.format(root)))
            self.chords.append(Chord('{0}5'.format(root)))

    def find_chords(self, root=None, quality=None):
        for chord in self.chords:
            root_match = root is None or root == chord.root
            quality_match = quality is None or quality == str(chord.quality)
            if root_match and quality_match:
                yield chord

chorddb = ChordDB()
