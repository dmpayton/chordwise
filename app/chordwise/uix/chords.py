import math
from collections import OrderedDict

from kivy import properties
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

from ..utils import asset

chords = OrderedDict((
    ('major', {
        'title': 'Major chords',
        'chords': ('A', 'B', 'C', 'D', 'E', 'F', 'G'),
    }),
    ('minor', {
        'title': 'Minor chords',
        'chords': ('Am', 'Bm', 'Cm', 'Dm', 'Em', 'Fm', 'Gm'),
    }),
    ('5', {
        'title': 'Power chords',
        'chords': ('A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5'),
    })
))


class ChordThumb(ButtonBehavior, Image):
    chord = properties.StringProperty('')

    def on_chord(self, instance, value):
        self.source = asset('chords/{0}.png'.format(self.chord))

    def on_release(self):
        app = App.get_running_app()
        app.route = '/chords/{0}'.format(self.chord)


class ChordSection(GridLayout):
    section = properties.StringProperty()

    def __init__(self, **kwargs):
        super(ChordSection, self).__init__(**kwargs)

        section = chords[self.section]
        self.ids['label'].text = section['title']

        for chord in section['chords']:
            self.ids['chords'].add_widget(ChordThumb(chord=chord))

        self.ids['chords'].bind(minimum_height=self.ids['chords'].setter('height'))
        self.bind(minimum_height=self.setter('height'))


class ChordList(ScrollView):
    def __init__(self, **kwargs):
        super(ChordList, self).__init__(**kwargs)

        sections = GridLayout(cols=1, size_hint_y=1)
        sections.bind(minimum_height=sections.setter('height'))

        for key in chords.keys():
            sections.add_widget(ChordSection(section=key))

        self.add_widget(sections)
