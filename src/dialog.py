class Dialog:
    def __init__(self, _current_statement=None, history=None):
        self._current_statement = current_statement
        self._history = history or list()

    def add_item_to_history(self, actor=None, text):
        if actor:
            item_string = "{actor}: {text}".format(actor=actor, text=text)
        else:
            item_string = text

        self._history.append(item_string)

    def get_history_as_text(self):
        reurn "\n".join(self._history)
