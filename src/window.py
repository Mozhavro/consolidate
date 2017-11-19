class Window:
    """
    Representation of game screen.
    Consists of a scene picture frame and dialog
    """

    def __init__(self, screen, dialog):
        self.screen = screen
        self.dialog = dialog

    def update(self, frame=None, dialog=None):
        if frame: self.frame = frame
        if dialog: self.dialog = dialog
        self.render()

    def render(self):
        self.render_screen()
        self.render_dialog()

    def render_screen(self):
        print(self.screen)

    def render_dialog(self):
        print(self.dialog)