from kivy import properties
from kivy.uix.image import Image

from chordwise.utils import asset


class Chord(Image):
    chord = properties.StringProperty('')

    def on_chord(self, instance, value):
        self.source = asset('chords/{0}.png'.format(self.chord))
