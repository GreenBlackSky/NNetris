"""Tetris scene."""

from mwidgets import Scene, Color

from tetris import Tetris
from controller import Move


class GameScene(Scene):
    """Tetris scene."""

    def __init__(self, rect, cell_size, speed, parent):
        """Initialize scene with given arguments."""
        super().__init__(rect, parent)
        _, _, w, h = self.rect
        self.cell_size = cell_size
        self.game = Tetris(speed, w//cell_size, h//cell_size)
        self.triggers = {
            **self.triggers,
            "move_right": self.move_right,
            "move_left": self.move_left,
            "rotate_right": self.rotate_right,
            "rotate_left": self.rotate_left,
            "drop": self.drop
        }

    def move_right(self):
        self.game.mind.set_descision(Move.MoveRight)

    def move_left(self):
        self.game.mind.set_descision(Move.MoveLeft)

    def rotate_right(self):
        self.game.mind.set_descision(Move.RotateRight)

    def rotate_left(self):
        self.game.mind.set_descision(Move.RotateLeft)

    def drop(self):
        self.game.mind.set_descision(Move.Drop)

    def update(self, events):
        """Update scene, pass it events."""
        super().update(events)
        self.game.update()
        if self.game.field_is_filled():
            self.emmit_event(Event.Type.Quit)

    def redraw(self):
        """Update visual look of scene."""
        self.clear()
        fig_x, fig_y = self.game.current_figure.x, self.game.current_figure.y
        for x, y in self.game.current_figure:
            self.__draw_cell(fig_x + x, fig_y + y, Color.WHITE)
        for y, line in enumerate(self.game.field):
            for x, val in enumerate(line):
                if val:
                    self.__draw_cell(x, y, Color.WHITE)

    def __draw_cell(self, x, y, color):
        rect = (x*self.cell_size,
                y*self.cell_size,
                self.cell_size,
                self.cell_size)
        self.draw_rect(rect, Color.WHITE)

# TODO Implement reaction on long pressing the buttons
