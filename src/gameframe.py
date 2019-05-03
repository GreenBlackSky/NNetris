"""GameFrame class."""

from tkinter import Frame, Label, Button
from gamescene import GameScene


class GameFrame(Frame):
    """Frame contains game field to play on."""

    def __init__(self, app):
        """Create GameFrame."""
        super().__init__(app)

        Label(self, text='Score:').grid(column=0, row=0)
        Label(self, text='0').grid(column=1, row=0)
        Button(
            self,
            text="Menu",
            command=self.master.main_menu,
            takefocus=False
        ).grid(column=2, row=0)
        self._game_scene = GameScene(self)
        self._game_scene.grid(column=0, columnspan=3, row=1)
        self._game_scene.focus_force()

    def pack(self, *args, **kargs):
        self._game_scene.run = True
        Frame.pack(self, *args, **kargs)

    def pack_forget(self, *args, **kargs):
        self._game_scene.run = False
        Frame.pack_forget(self, *args, **kargs)
