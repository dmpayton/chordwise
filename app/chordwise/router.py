from kivy.garden.router import Router, route
from kivy.uix.screenmanager import FadeTransition

from . import screens


class MainRouter(Router):
    def __init__(self, *args, **kwargs):
        super(MainRouter, self).__init__(*args, **kwargs)
        self.ids.screenmanager.transition = FadeTransition(clearcolor=(1,1,1,1))

    @route('/')
    def index(self):
        return screens.MenuScreen()

    @route('/chords')
    def chord_list(self):
        return screens.ChordListScreen()

    @route('/chords/<path:chord>')
    def chord_detail(self, chord):
        return screens.ChordDetailScreen(chord=chord.strip('/'))

    @route('/practice')
    def practice(self):
        return screens.PracticeScreen()

    @route('/scales')
    def scales(self):
        return screens.ScalesScreen()
