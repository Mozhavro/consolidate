import sys
from collections import defaultdict

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from asciimatics.widgets import Frame, Text, Layout, ListBox, Widget, Button, Label, TextBox
from asciimatics.effects import Print
from asciimatics.renderers import StaticRenderer
from asciimatics.exceptions import ResizeScreenError, StopApplication


class Window:
    def __init__(self, picture=None, additional_scenes=None):
        self._additional_scenes = additional_scenes
        self._picture = picture

    def start(self):
        while True:
            try:
                Screen.wrapper(self.play_scenes, catch_interrupt=True)
                sys.exit(0)
            except ResizeScreenError as e:
                pass

    def play_scenes(self, screen):
        scenes = [
            Scene([GameFrame(screen, self._picture, x=0, y=0)], -1, name="Controls"),
            # Scene([Print(screen, StaticRenderer(images=[self._picture]), 0)], name="Picture"),
        ]
        if self._additional_scenes: scenes += self._additional_scenes
        
        screen.play(scenes, stop_on_resize=True)



class GameFrame(Frame):
    def __init__(self, screen, picture='', x=None, y=None):
        super(GameFrame, self).__init__(screen,
                                        screen.height,
                                        screen.width,
                                        # on_load=self._reload_list,
                                        hover_focus=True,
                                        title="AGIRL",
                                        x=x, y=y)

        self._picture = picture

        self.palette = defaultdict(
            lambda: (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK))
        for key in ["selected_focus_field", "label"]:
            self.palette[key] = (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_WHITE)
        self.palette["title"] = (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE)

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)

        self._answer_options = ListBox(
            Widget.FILL_FRAME,
            [('1. wup', 1), ('2.dup', 2)],
            name="answer_options",
            on_change=self._on_pick)

        self._picture_display = TextBox(14, as_string=True)
        self._picture_display.disabled = True

        layout.add_widget(self._picture_display)
        layout.add_widget(self._answer_options)
        layout.add_widget(
                Label("Press `q` to quit."))
        
        self.fix()
        self._on_pick()

    def _on_pick(self):
        pass

    def _treceback(self):
        import pudb; pudb.set_trace()

    def _update(self, frame_no):
        self._picture_display.value = self._picture

        # Now redraw as normal
        super(GameFrame, self)._update(frame_no)

    def process_event(self, event):
        # Do the key handling for this Frame.
        if isinstance(event, KeyboardEvent):
            if event.key_code in [ord('q'), ord('Q'), Screen.ctrl("c")]:
                self._quit()

            # Force a refresh for improved responsiveness
            self._last_frame = 0

        # Now pass on to lower levels for normal handling of the event.
        return super(GameFrame, self).process_event(event)


    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")
