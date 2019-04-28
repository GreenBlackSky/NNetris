"""GameFrame class."""

from tkinter import Frame, Entry, Button
from gamescene import GameScene


class GameFrame(Frame):
    """Frame contains game field to play on."""

    def __init__(self, app):
        """Create GameFrame."""
        super().__init__(app)

        Entry(self).grid(column=0, row=0, sticky="nsew")
        Entry(self).grid(column=1, row=0, sticky="nsew")
        Button(
            self,
            text="Menu",
            command=self.master.main_menu
        ).grid(column=1, row=0, sticky='e')

        GameScene(self).grid(column=0, columnspan=2, row=1, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
