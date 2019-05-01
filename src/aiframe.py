"""AIFrame class."""

from tkinter import Frame, Label, Button, Scale, HORIZONTAL, X
from tkinter.ttk import Combobox

from gamescene import GameScene


class AIFrame(Frame):
    """Contains widgets to tune game."""

    def __init__(self, app):
        """Create AIFrame."""
        super().__init__(app)
        Button(
            self,
            text="Menu",
            command=self.master.main_menu
        ).pack()
        self._game_scene = GameScene(self)
        self._game_scene.pack()

    def pack(self, *args, **kargs):
        self._game_scene.run = True
        Frame.pack(self, *args, **kargs)

    def pack_forget(self, *args, **kargs):
        self._game_scene.run = False
        Frame.pack_forget(self, *args, **kargs)
