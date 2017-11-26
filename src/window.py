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

        # os.system("mode con cols=30") # TODO move value to config
        # os.system("mode con lines=50") # TODO move value to config
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
        self._answer_options.palette = defaultdict(lambda: (Screen.COLOUR_RED, Screen.A_NORMAL, Screen.COLOUR_GREEN))

        self._picture_display = TextBox(14, as_string=True)
        # self._picture.palette = (Screen.COLOUR_RED, Screen.A_NORMAL, Screen.COLOUR_GREEN)
        self._picture_display.disabled = True
        # self._picture = Text()
        # # self._picture._value = picture
        # self.reset()

        # import pudb; pudb.set_trace()

        layout.add_widget(self._picture_display)
        layout.add_widget(self._answer_options)
        layout.add_widget(
                Label("Press `q` to quit."))


        self.canvas.print_at(
            picture,
            0, #self.canvas._x, #+ self.canvas._offset,
            0, #self.canvas._y,
            Screen.COLOUR_BLACK, Screen.A_BOLD, Screen.COLOUR_WHITE)
        
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


# class Window:
#     """
#     Representation of game screen.
#     Consists of a scene picture frame and dialog
#     """

#     def __init__(self, screen, dialog):
#         self.screen = screen
#         self.dialog = dialog
#         while True:
#             try:
#                 Screen.wrapper(self.scrn, arguments=[None])
#             except ResizeScreenError:
#                 pass

#     def scrn(self, screen, scene):
#         # frame = Frame(screen, screen.height * 2 // 3, screen.width * 2 // 3, has_border=True, title="AGIRL")
#         frame = Frame(screen, 100, 100, has_border=True, title="AGIRL")
#         layout = layout = Layout([100], fill_frame=True)
#         frame.add_layout(layout)
#         layout.add_widget(Text("Name:", "name"))
#         scenes = [
#             Scene([frame], -1, name="Main"),
#             Scene([frame], -1, name="Main")
#         ]

#         screen.play(scenes, stop_on_resize=True, start_scene=scene)
        

#     def update(self, frame=None, dialog=None):
#         if frame: self.frame = frame
#         if dialog: self.dialog = dialog
#         self.render()

#     def render(self):
#         self.render_screen()
#         self.render_dialog()

#     def render_screen(self):
#         self.stdscr.addstr(0, 0, self.screen)
#         self.stdscr.refresh()

#     def render_dialog(self):
#         print(self.dialog)

#     # def teardown(self):
#     #     # reverse everything that you changed about the terminal
#     #     nocbreak()
#     #     self.stdscr.keypad(False)
#     #     echo()
#     #     # restore the terminal to its original state
#     #     endwin()