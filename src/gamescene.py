"""Tetris scene."""


from tkinter import Canvas
from time import sleep

from tetris import Tetris


class GameScene(Canvas):
    """Visual representation of game.

    Needs GameFrame as master.
    """

    def __init__(self, master, cell_size=20, step=5, **kargs):
        """Create GameScene."""
        super().__init__(master, **kargs)
        self._width = 10
        self._height = 20
        self._cell_size = cell_size
        self._step = step

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

        self._game = Tetris(self._width, self._height)
        self.bind("<Key-Up>", lambda event: self._game.rotate_left())
        self.bind("<Shift-Up>", lambda event: self._game.rotate_right())
        self.bind("<Key-Left>", lambda event: self._game.move_left())
        self.bind("<Key-Right>", lambda event: self._game.move_right())
        self._run = False
        self.update()

    def update(self):
        """Update GameScene.

        Schedules call of itself.
        """
        if not self._run:
            self.after(self._step, self.update)
            return

        if self._game.game_is_lost:
            self.after(self._step, self.update)
            self.master.master.you_lost()
            return

        self._game.update()
        self.master.score = self._game.score
        self._clear()
        self._draw_figure()
        self._draw_filled_cells()

        self.after(self._step, self.update)

    def restart_game(self):
        """Restart game.

        New game is held on pause.
        """
        self._game.restart()
        self._run = False
        self._clear()

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

# TODO fix size
# TODO move bindings into controller
# TODO move update scheduling into controller
