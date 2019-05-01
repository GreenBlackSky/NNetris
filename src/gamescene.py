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
        self._cell_size = 30
        self._step = 100

        self.config(
            width=(self._width*self._cell_size),
            height=(self._height*self._cell_size),
            background='white'
        )

        for y in range(self._height):
            for x in range(self._width):
                self.create_rectangle(
                    x*self._cell_size,
                    y*self._cell_size,
                    x*self._cell_size + self._cell_size,
                    y*self._cell_size + self._cell_size
                )

        self._game = Tetris(1, self._width, self._height)
        self._run = False
        self.update()

    def update(self):
        if not self._run:
            self.after(self._step, self.update)
            return

        self._game.update()
        self._clear()
        self._draw_figure()
        self._draw_filled_cells()
        self.after(self._step, self.update)

    def _clear(self):
        for item in self.find_all():
            self.itemconfig(item, fill='white')

    def _draw_figure(self):
        fig_x, fig_y = self._game.current_figure.x, self._game.current_figure.y
        for x, y in self._game.current_figure:
            item = self.find_closest(
                (fig_x + x + 0.5)*self._cell_size,
                (fig_y + y + 0.5)*self._cell_size
            )
            self.itemconfig(item, fill='green')

    def _draw_filled_cells(self):
        for y, line in enumerate(self._game.field):
            for x, val in enumerate(line):
                if val:
                    item = self.find_closest(
                        (x + 0.5)*self._cell_size,
                        (y + 0.5)*self._cell_size
                    )
                    self.itemconfig(item, fill='green')

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
