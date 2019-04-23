"""GameFrame class."""

from tkinter import Frame, Entry, Canvas


class GameFrame(Frame):
    """Frame contains game field to play on."""

    def __init__(self, app):
        """Create GameFrame."""
        super().__init__(app)

        Entry(self).grid(column=0, row=0, sticky="nsew")
        Entry(self).grid(column=1, row=0, sticky="nsew")

        Canvas(self).grid(column=0, columnspan=2, row=1, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
