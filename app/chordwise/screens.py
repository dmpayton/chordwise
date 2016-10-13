from kivy import properties
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen

from chordwise.store import chord_store
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
    time = '4/4'
    bpm = 100
    click = SoundLoader.load(asset('click.wav'))

    def __init__(self, **kwargs):
        super(PracticeScreen, self).__init__(**kwargs)
        self.chords = random_cycle(list(chord_store.chords))

        # Update the main chord when the current chord is updated
        self.ids['current'].bind(chord=self.ids['main-chord'].setter('chord'))

        # Intialize the playlist
        self.ids['current'].chord = next(self.chords)
        self.ids['future-1'].chord = next(self.chords)
        self.ids['future-2'].chord = next(self.chords)

        self.beats, self.bar = map(int, self.time.split('/'))
        self.playing = False
        self.counter = 0
        self.event = None
        self.start()

    def on_leave(self):
        self.stop()

    def start(self, dt=None):
        self.playing = True
        self.counter = self.counter = (self.bar - 1)
        self.event = Clock.schedule_once(lambda dt: self.ticker(initial=True), 2)

    def stop(self, dt=None):
        self.playing = False
        if self.event:
            Clock.unschedule(self.event)

    def toggle(self, dt=None):
        (self.stop if self.playing else self.start)()

    def ticker(self, dt=None, initial=False):
        if self.playing is False:
            return
        if (self.counter + 1) == self.bar:
            self.counter = 0
            if initial is False:
                self.next_chord()
        else:
            self.counter += 1

        if self.counter % self.beats:
            self.click.volume = .3
        else:
            self.click.volume = 1
        self.click.play()

        self.time = int((60 / (self.bpm / .5) - 0.1) * 1000)

        delay = {
            4: 60. / self.bpm,
            6: 60. / (self.bpm / .5),
        }[self.beats]

        self.event = Clock.schedule_once(self.ticker, delay)


    def next_chord(self):
        self.ids['previous-2'].chord = self.ids['previous-1'].chord
        self.ids['previous-1'].chord = self.ids['current'].chord
        self.ids['current'].chord = self.ids['future-1'].chord
        self.ids['future-1'].chord = self.ids['future-2'].chord
        self.ids['future-2'].chord = next(self.chords)



class ScalesScreen(Screen):
    pass
