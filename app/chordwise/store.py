import json
import os

from kivy.app import App

class ChordStore(list):
    def __init__(self):
        self.load()

    @property
    def path(self):
        # app = App.get_running_app()
        return os.path.join(os.getcwd(), 'activated-chords.json')

    def add(self, chord):
        self.chords.add(chord)
        self.save()

    def remove(self, chord):
        self.chords.remove(chord)
        self.save()

    def toggle(self, chord):
        (self.remove if chord in self.chords else self.add)(chord)

    def load(self):
        if os.path.exists(self.path):
            with open(self.path) as f:
                self.chords = set(json.loads(f.read()))
        else:
            self.chords = set(['A', 'D', 'E', 'G'])
            self.save()

    def save(self):
        with open(self.path, 'w') as f:
            f.write(json.dumps(list(self.chords)))

chord_store = ChordStore()
