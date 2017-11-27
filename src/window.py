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
    def __init__(self, model, additional_scenes=None):
        self._additional_scenes = additional_scenes
        self._model = model

    def start(self):
        while True:
            try:
                Screen.wrapper(self.play_scenes, catch_interrupt=True)
                sys.exit(0)
            except ResizeScreenError as e:
                pass

    def play_scenes(self, screen):
        scenes = [
            Scene([GameFrame(screen, self._model)], -1, name="Controls"),
        ]
        if self._additional_scenes: scenes += self._additional_scenes
        
        screen.play(scenes, stop_on_resize=True)



class GameFrame(Frame):
    def __init__(self, screen, model):
        super(GameFrame, self).__init__(screen,
                                        screen.height,
                                        screen.width,
                                        on_load=self._reload)

        self._model = model
        self._statement = self._model.get_statement(1)
        self._picture = self._model.get_scene("start")

        self.palette = defaultdict(
            lambda: (Screen.COLOUR_WHITE, Screen.A_NORMAL, Screen.COLOUR_BLACK))
        for key in ["selected_focus_field", "label"]:
            self.palette[key] = (Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_WHITE)
        self.palette["title"] = (Screen.COLOUR_BLACK, Screen.A_NORMAL, Screen.COLOUR_WHITE)

        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)

        self._answer_options_list = self._format_options(self._statement["answers"])
        self._answer_options = ListBox(
            Widget.FILL_FRAME,
            self._answer_options_list,
            name="answer_options",
            on_select=self._on_select)

        self._picture_display = TextBox(16, as_string=True)
        self._picture_display.disabled = True

        self._remark = Text()
        self._remark.value = self._statement['remark']
        self._remark.disabled = True

        self._statement_text = Text()
        self._statement_text.value = "{}: {}".format(self._model.partner_name,
                                                     self._statement['text'])

        self._statement_text.disabled = True

        layout.add_widget(self._picture_display)
        layout.add_widget(self._remark)
        layout.add_widget(self._statement_text)
        layout.add_widget(self._answer_options)
        layout.add_widget(
                Label("Press `q` to quit."))
        
        # self._qsfdsf=1
        self.fix()

    def _on_select(self):
        list_value = self._answer_options.value
        answer = self._statement["answers"][list_value -1]
        next_statement_id = answer["next_statement"]
        self._statement = self._model.get_statement(next_statement_id)
        self._picture = self._model.get_scene(self._statement["emotion"])
        self._answer_options.options = self._format_options(self._statement["answers"])
        # self._answer_options = ListBox(
        #     Widget.FILL_FRAME,
        #     self._answer_options_list,
        #     name="answer_options",
        #     on_select=self._on_select)

    def _reload(self):
        self._answer_options.options = self._format_options(self._statement["answers"])

    def _treceback(self):
        import pudb; pudb.set_trace()

    def _update(self, frame_no):
        self._picture_display.value = self._picture
        self._remark.value = self._statement['remark']
        if self._statement['text']:
            self._statement_text.value = "{}: {}".format(self._model.partner_name,
                                                         self._statement['text'])
        else:
            self._statement_text.value = ""

        # self._answer_options.options = self._format_options(self._statement["answers"])
        # Now redraw as normal
        super(GameFrame, self)._update(frame_no)

    def process_event(self, event):
        # Do the key handling for this Frame.
        if isinstance(event, KeyboardEvent):
            if event.key_code in [ord('q'), ord('Q'), Screen.ctrl("c")]:
                self._quit()

            elif event.key_code in [ord('t'), ord('T')]:
                self._treceback()

            # Force a refresh for improved responsiveness
            self._last_frame = 0

        # Now pass on to lower levels for normal handling of the event.
        return super(GameFrame, self).process_event(event)

    def _format_options(self, options):
        answer_options = []
        for key, option in enumerate(options, 1):
            text = "{num}. {label}".format(num=key, label=option["text"])
            value = key
            answer_options.append((text, value))

        return answer_options


    @staticmethod
    def _quit():
        raise StopApplication("User pressed quit")
