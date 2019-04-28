"""Tetris scene."""


from tkinter import Canvas
from time import sleep

from tetris import Tetris
from controller import Move


class GameScene(Canvas):
    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.config(background='white')
        self._game = Tetris(1, 10, 20)
        self.update()

    def update(self):
        self._game.update()
        self.delete('all')
        fig_x, fig_y = self._game.current_figure.x, self._game.current_figure.y
        for x, y in self._game.current_figure:
            self._draw_rect(fig_x + x, fig_y + y)
        for y, line in enumerate(self._game.field):
            for x, val in enumerate(line):
                if val:
                    self._draw_rect(x, y)
        self.after(100, self.update)

    def _draw_rect(self, x, y):
        cell_size = 10
        args = [arg*cell_size for arg in [x, y, x + 1, y + 1]]
        self.create_rectangle(*args, fill='green')

# Speed
# Cell size
# Field size
# Colors
# Keys
