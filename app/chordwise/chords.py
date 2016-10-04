from .utils import asset


class Chord(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def image_path(self):
        return asset('chords/{0}.png'.format(self.name))


chord_list = []
for root in 'ABCDEFG':
    chord_list.append(Chord(root, type='major'))
    chord_list.append(Chord('{0}m'.format(root), type='minor'))
    chord_list.append(Chord('{0}5'.format(root), type='power'))
