"""GameFrame class."""

from tkinter import Frame, Entry, Button
from gamescene import GameScene


class GameFrame(Frame):
    """Frame contains game field to play on."""

    def __init__(self, app):
        """Create GameFrame."""
        super().__init__(app)

        Entry(self).pack()
        Entry(self).pack()
        self._game_scene = GameScene(self)
        self._game_scene.pack()
        Button(self, text="Menu", command=self.master.main_menu).pack()

    def pack(self, *args, **kargs):
        self._game_scene.run = True
        Frame.pack(self, *args, **kargs)

    def pack_forget(self, *args, **kargs):
        self._game_scene.run = False
        Frame.pack_forget(self, *args, **kargs)
