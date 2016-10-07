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

from .behaviors import BorderBehavior
from .chord import Chord
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


class ChordThumb(ButtonBehavior, BorderBehavior, Chord):
    active = properties.BooleanProperty(False)

    def on_release(self):
        self.active = not self.active
        print('on_release')

        # app = App.get_running_app()
        # app.route = '/chords/{0}'.format(self.chord)

    def on_active(self, instance, value):
        (self.activate if self.active else self.deactivate)()

    def activate(self):
        self.borders = (5, 'solid', (0, 0, 0, 1))
        print('activate()')

    def deactivate(self):
        self.borders = (0, 'solid', (0, 0, 0, 1))
        print('deactivate()')


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

        for x in range(2):
            for key in chords.keys():
                sections.add_widget(ChordSection(
                    id='section-{0}'.format(key),
                    section=key,
                ))

        self.add_widget(sections)
