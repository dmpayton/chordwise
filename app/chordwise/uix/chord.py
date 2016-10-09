from kivy import properties
from kivy.uix.image import Image

from pychord import Chord

from chordwise.utils import asset


class ChordImage(Image):
    chord = properties.StringProperty()

    def on_chord(self, instance, value):
        # Pass through pychord.Chord to ensure a valid name
        self.source = asset('chords/{0}.png'.format(self.pychord.chord))

    @property
    def pychord(self):
        return Chord(self.chord)
