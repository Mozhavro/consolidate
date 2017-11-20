from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.widgets import Frame, Text, Layout
from asciimatics.exceptions import ResizeScreenError



class GameFrame(Frame):
    def __init__(self, screen, content):
        super(GameFrame, self).__init__(screen,
                                        screen.height * 2 // 3,
                                        screen.width * 2 // 3,
                                        on_load=self._reload_list,
                                        hover_focus=True,
                                        title="AGIRL")
        self._content = content
        layout = Layout([100], fill_frame=True)
        self.add_layout(layout)
        self._answer_options = ListBox(
            Widget.FILL_FRAME,
            ['wup', 'dup'],
            name="contacts",
            on_change=self._on_pick)


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