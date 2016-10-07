from kivy import properties
from kivy.uix.screenmanager import Screen

from .utils import asset


class MenuScreen(Screen):
    pass


class ChordListScreen(Screen):
    pass


class ChordDetailScreen(Screen):
    chord = properties.StringProperty()

    def __init__(self, **kwargs):
        super(ChordDetailScreen, self).__init__(**kwargs)
        self.ids['chord'].chord = self.chord


class PracticeScreen(Screen):
    pass


class ScalesScreen(Screen):
    pass
