from kivy import properties
from kivy.graphics import Line, Color
from kivy.uix.widget import Widget


class BorderBehavior(Widget):
    DEFAULT_WIDTH = 1
    DEFAULT_STYLE = 'solid'
    DEFAULT_COLOR = (0, 0, 0, 0)

    border = properties.ListProperty([DEFAULT_WIDTH, DEFAULT_STYLE, DEFAULT_COLOR])

    cap = 'square'
    joint = 'miter'

    styles = {
        'dashed': {
            'dash_length': 10,
            'dash_offset': 5
        },
        'dotted': {
            'dash_length': 1,
            'dash_offset': 1
        },
        'solid': {
            'dash_length': 1,
            'dash_offset': 0
        }
    }

    def __init__(self, **kwargs):
        self._borders = {}
        super(BorderBehavior, self).__init__(**kwargs)

        width, style, color = self.border
        kwargs = {
            'points': [],
            'close': True,
            'width': width,
            'cap': self.cap,
            'joint': self.joint,
            'dash_length': self.styles[style]['dash_length'],
            'dash_offset': self.styles[style]['dash_offset'],
        }

        with self.canvas.after:
            self._color = Color(*color)
            self._border = Line(**kwargs)

    def on_border(self, instance, value):
        self.update_border()

    def on_size(self, instance, value):
        self.update_border()

    def on_pos(self, instance, value):
        self.update_border()

    def update_border(self):
        if not hasattr(self, '_border'):
            return

        width, style, color = self.border

        self._color.rgba = color
        self._border.dash_length = self.styles[style]['dash_length']
        self._border.dash_offset = self.styles[style]['dash_offset']
        self._border.width = width

        origin_x = self.x + width
        origin_y = self.y + width

        # origin_w = self.norm_image_size[0]
        # origin_h = self.norm_image_size[1]

        self._border.points = [
            # bottom left
            origin_x,
            origin_y,

            # bottom right
            origin_x + self.width,
            origin_y,

            # top right
            origin_x + self.width,
            origin_y + self.height,

            # top left
            origin_x,
            origin_y + self.height,
        ]
