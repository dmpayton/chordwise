from kivy import properties

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout

from ..utils import asset

# chords = {
#     'Major': ('A', 'B', 'C', 'D', 'E', 'F', 'G'),
#     'Minor': ('Am', 'Bm', 'Cm', 'Dm', 'Em', 'Fm', 'Gm'),
#     '5 (Power chords)': ('A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5'),
# }


chords = {
    'major': {
        'title': 'Major',
        'chords': ('A', 'B', 'C', 'D', 'E', 'F', 'G'),
    },
    'minor': {
        'title': 'Minor',
        'chords': ('Am', 'Bm', 'Cm', 'Dm', 'Em', 'Fm', 'Gm'),
    },
    '5': {
        'title': '5 (Power chords)',
        'chords': ('A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5'),
    }
}


class ChordList(StackLayout):
    section = properties.StringProperty()

    def on_section(self, instance, value):
        data = chords[self.section]
        self.ids['label'].text = data['title']
        for chord in data['chords']:
            self.ids['chords'].add_widget(ChordImage(chord=chord))


class ChordImage(Image):
    chord = properties.StringProperty('')

    def on_chord(self, instance, value):
        self.source = asset('chords/{0}.png'.format(value))
