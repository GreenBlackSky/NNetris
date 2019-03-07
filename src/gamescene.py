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
        self._cell_size = cell_size
        self._game = Tetris(speed, w//cell_size, h//cell_size)
        self._triggers = {
            **self._triggers,
            "move_right": self.move_right,
            "move_left": self.move_left,
            "rotate_right": self.rotate_right,
            "rotate_left": self.rotate_left,
            "drop": self.drop
        }

    def move_right(self):
        self._game.mind.descision = Move.MoveRight

    def move_left(self):
        self._game.mind.descision = Move.MoveLeft

    def rotate_right(self):
        self._game.mind.descision = Move.RotateRight

    def rotate_left(self):
        self._game.mind.descision = Move.RotateLeft

    def drop(self):
        self._game.mind.descision = Move.Drop

    def update(self, events):
        """Update scene, pass it events."""
        super().update(events)
        self._game.update()
        if self._game.field_is_filled():
            self.emmit_event(Event.Type.Quit())

    def redraw(self):
        """Update visual look of scene."""
        self.clear()
        fig_x, fig_y = self._game.current_figure.x, self._game.current_figure.y
        for x, y in self._game.current_figure:
            self._draw_cell(fig_x + x, fig_y + y, Color.WHITE)
        for y, line in enumerate(self._game.field):
            for x, val in enumerate(line):
                if val:
                    self._draw_cell(x, y, Color.WHITE)

    def _draw_cell(self, x, y, color):
        rect = (x*self._cell_size,
                y*self._cell_size,
                self._cell_size,
                self._cell_size)
        self.draw_rect(rect, Color.WHITE)

# TODO Implement reaction on long pressing the buttons
