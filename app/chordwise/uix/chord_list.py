import math
from collections import OrderedDict

from kivy import properties
from kivy.app import App
from kivy.graphics import Rectangle, Color
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

from .behaviors import BorderBehavior
from .chord import ChordImage
from chordwise.chord import chorddb
from chordwise.store import chord_store
from chordwise.utils import asset


class ChordThumb(ButtonBehavior, BorderBehavior, ChordImage):
    active = properties.BooleanProperty(False)

    def __init__(self, **kwargs):
        super(ChordThumb, self).__init__(**kwargs)
        if self.chord in chord_store.chords:
            self.active = True

    def on_release(self):
        self.active = not self.active

        # app = App.get_running_app()
        # app.route = '/chords/{0}'.format(self.chord)

    def on_active(self, instance, value):
        (self.activate if self.active else self.deactivate)()

    def activate(self):
        if self.chord not in chord_store.chords:
            chord_store.add(self.chord)

        self.border = (5, 'solid', (0, .6, .9, 1))
        self.color = (.9, .9, .9, 1)


    def deactivate(self):
        if self.chord in chord_store.chords:
            chord_store.remove(self.chord)

        self.border = (1, 'solid', (0, 0, 0, 0))
        self.color = (1, 1, 1, 1)


class ChordSection(GridLayout):
    type = properties.StringProperty()

    def __init__(self, **kwargs):
        super(ChordSection, self).__init__(**kwargs)

        self.ids['label'].text = chorddb.types[self.type]['title']

        quality = chorddb.types[self.type]['quality']
        for chord in chorddb.find_chords(quality=quality):
            self.ids['chords'].add_widget(ChordThumb(chord=chord.chord))

        self.ids['chords'].bind(minimum_height=self.ids['chords'].setter('height'))
        self.bind(minimum_height=self.setter('height'))


class ChordList(ScrollView):
    def __init__(self, **kwargs):
        super(ChordList, self).__init__(**kwargs)

        sections = GridLayout(cols=1)
        sections.bind(minimum_height=sections.setter('height'))

        for key in chorddb.types.keys():
            sections.add_widget(ChordSection(
                id='section-{0}'.format(key),
                type=key,
            ))

        self.add_widget(sections)
