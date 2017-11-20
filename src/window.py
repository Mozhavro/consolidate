import sys

from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Text, Layout, ListBox, Widget, Button
from asciimatics.exceptions import ResizeScreenError


class Window:
    def __init__(self, additional_scenes=None):
        self._additional_scenes = additional_scenes

    def start(self):
        while True:
            try:
                Screen.wrapper(self.play_scenes, catch_interrupt=True)
                sys.exit(0)
            except ResizeScreenError as e:
                pass

    def play_scenes(self, screen):
        scenes = [
            Scene([GameFrame(screen)], -1, name="Main"),
        ]
        if self._additional_scenes: scenes += self._additional_scenes
        
        screen.play(scenes, stop_on_resize=True)



class GameFrame(Frame):
    def __init__(self, screen, content=None):
        super(GameFrame, self).__init__(screen,
                                        screen.height * 2 // 3,
                                        screen.width * 2 // 3,
                                        # on_load=self._reload_list,
                                        hover_focus=True,
                                        title="AGIRL")
        self._content = content
        layout = Layout([1,1,1,1], fill_frame=True)
        self.add_layout(layout)
        self._answer_options = ListBox(
            Widget.FILL_FRAME,
            [('1. wup', 1), ('2.dup', 2)],
            name="answer_options",
            on_change=self._on_pick)
        layout.add_widget(self._answer_options)
        self.fix()
        self._on_pick()

    def _on_pick(self):
        pass


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