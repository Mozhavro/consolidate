class Dialog:
    def __init__(self, statement=None, answers=None,  history=None):
        self._statement = statement or ''
        self._answers = answers or list()
        self._history = history or list()

    def add_item_to_history(self, text, actor=None):
        if actor:
            item_string = "{actor}: {text}".format(actor=actor, text=text)
        else:
            item_string = text

        self._history.append(item_string)

    def get_history_as_text(self):
        return "\n".join(self._history)
