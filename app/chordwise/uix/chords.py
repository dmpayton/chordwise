from kivy import properties
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.stacklayout import StackLayout


from ..utils import asset

chords = {
    'major': {
        'title': 'Major chords',
        'chords': ('A', 'B', 'C', 'D', 'E', 'F', 'G'),
    },
    'minor': {
        'title': 'Minor chords',
        'chords': ('Am', 'Bm', 'Cm', 'Dm', 'Em', 'Fm', 'Gm'),
    },
    '5': {
        'title': 'Power chords',
        'chords': ('A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5'),
    }
}


class ChordThumb(ButtonBehavior, Image):
    chord = properties.StringProperty('')

    def on_chord(self, instance, value):
        self.source = asset('chords/{0}.png'.format(value))

    def on_release(self):
        print(self.chord)
        app = App.get_running_app()
        app.route = '/chords/{0}'.format(self.chord)


class ChordSection(StackLayout):
    section = properties.StringProperty()

    def on_section(self, instance, value):
        data = chords[self.section]
        self.ids['label'].text = data['title']
        for chord in data['chords']:
            self.ids['chords'].add_widget(ChordThumb(chord=chord))
