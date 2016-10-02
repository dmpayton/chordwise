import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.garden.router import AppRouter

import chordwise.conf
import chordwise.router

# Load our kv files.
for filename in os.listdir(chordwise.conf.KV_DIR):
    Builder.load_file(os.path.join(chordwise.conf.KV_DIR, filename))


class ChordwiseApp(AppRouter):
    def build(self):
        self.root = chordwise.router.MainRouter()
        self.route = '/'

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    ChordwiseApp().run()
