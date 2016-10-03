import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.garden.router import AppRouter

import chordwise.conf
import chordwise.router
import chordwise.uix

# Load our kv files.
for root, dirs, files in os.walk(chordwise.conf.KV_DIR):
    for filename in files:
        Builder.load_file(os.path.join(root, filename))


class ChordwiseApp(AppRouter):
    def build(self):
        self.root = chordwise.router.MainRouter()
        self.route = '/'

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    ChordwiseApp().run()
