"""Tetris scene."""


from tkinter import Canvas
from time import sleep

from tetris import Tetris
from controller import Move


class GameScene(Canvas):
    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self._width = 10
        self._height = 20
        self._scale = 10
        self._step = 100

        self.config(
            width=(self._width*self._scale),
            height=(self._height*self._scale),
            background='white'
        )

        self._game = Tetris(1, self._width, self._height)
        self._run = False
        self.update()

    def update(self):
        if not self._run:
            self.after(self._step, self.update)
            return

        self._game.update()
        self.delete('all')
        fig_x, fig_y = self._game.current_figure.x, self._game.current_figure.y
        for x, y in self._game.current_figure:
            self._draw_rect(fig_x + x, fig_y + y)
        for y, line in enumerate(self._game.field):
            for x, val in enumerate(line):
                if val:
                    self._draw_rect(x, y)
        self.after(self._step, self.update)

    def _draw_rect(self, x, y):
        args = [arg*self._scale for arg in [x, y, x + 1, y + 1]]
        self.create_rectangle(*args, fill='green')

    @property
    def run(self):
        return self._run

    @run.setter
    def run(self, value):
        self._run = value

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value


# Speed
# Keys
# Change colors instead of create/destroy
