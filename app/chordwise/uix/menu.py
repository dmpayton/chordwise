from kivy import properties
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class MenuButton(Button):
    icon = properties.StringProperty('')
    text = properties.StringProperty('')

    def on_icon(self, instance, value):
        self.ids['icon'].source = self.icon

    def on_text(self, instance, value):
        self.ids['text'].source = self.text
