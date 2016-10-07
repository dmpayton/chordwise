import os

import kivy
kivy.require('1.9.1')

# Config
from kivy.config import Config

if os.environ.get('DEBUG'):
    Config.set('graphics', 'width', '720')
    Config.set('graphics', 'height', '1280')

    # Config.set('modules', 'touchring', '')
    # Config.set('modules', 'monitor', '')

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.garden.router import AppRouter

import chordwise.conf
import chordwise.router
import chordwise.uix
from chordwise.utils import asset

# Register our fonts.
for name, files in chordwise.conf.FONTS.items():
    LabelBase.register(name=name, **{k: asset(v) for k, v in files.items()})

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
