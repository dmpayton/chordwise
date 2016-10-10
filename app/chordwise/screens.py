from kivy import properties
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen

from .utils import asset, random_cycle


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class ChordListScreen(Screen):
    pass


class ChordDetailScreen(Screen):
    chord = properties.StringProperty()

    def __init__(self, **kwargs):
        super(ChordDetailScreen, self).__init__(**kwargs)
        self.ids['chord'].chord = self.chord


class PracticeScreen(Screen):
    time = (4, 4)
    bpm = 100
    click = SoundLoader.load(asset('click.wav'))

    def __init__(self, **kwargs):
        super(PracticeScreen, self).__init__(**kwargs)
        self.chords = random_cycle(list('CAGED'))

        # Update the main chord when the current chord is updated
        self.ids['current'].bind(chord=self.ids['main-chord'].setter('chord'))

        # Intialize the playlist
        # self.ids['current'].chord = next(self.chords)
        self.ids['future-1'].chord = next(self.chords)
        self.ids['future-2'].chord = next(self.chords)

        self.counter = 4
        # self.beat()

        self.event = Clock.schedule_interval(self.beat, 60. / self.bpm)

    def on_leave(self):
        Clock.unschedule(self.event)

    def beat(self, dt=None):
        if self.counter % 4:
            self.counter += 1
            self.click.volume = .5
        else:
            self.next_chord()
            self.counter = 1
            self.click.volume = 1
        self.click.play()


    def next_chord(self):
        self.ids['previous-2'].chord = self.ids['previous-1'].chord
        self.ids['previous-1'].chord = self.ids['current'].chord
        self.ids['current'].chord = self.ids['future-1'].chord
        self.ids['future-1'].chord = self.ids['future-2'].chord
        self.ids['future-2'].chord = next(self.chords)



class ScalesScreen(Screen):
    pass
