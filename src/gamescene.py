"""Tetris scene."""

from MWidgets import Scene
from MWidgets import Event
from MWidgets import Color

from tetris import Tetris
from controller import Move


class GameScene(Scene):
    """Tetris scene."""

    def __init__(self, rect, fps, cell_size, parent):
        """Initialize scene with given arguments."""
        super().__init__(rect, fps, cell_size, parent)
        _, _, w, h = self.rect
        self.game = Tetris(w//cell_size, h//cell_size)
        self.triggers = {
            **self.triggers,
            "move_right": self.move_right,
            "move_left": self.move_left,
            "rotate_right": self.rotate_right,
            "rotate_left": self.rotate_left
        }

    def move_right(self):
        """Move current falling figure one step right."""
        self.game.mind.set_descision(Move.MoveRight)

    def move_left(self):
        """Move current falling figure one step left."""
        self.game.mind.set_descision(Move.MoveLeft)

    def rotate_right(self):
        """Rotate current falling figure left one turn."""
        self.game.mind.set_descision(Move.RotateRight)

    def rotate_left(self):
        """Rotate current falling figure left one turn."""
        self.game.mind.set_descision(Move.RotateLeft)

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
            self.draw_cell((fig_x + x, fig_y + y), Color.WHITE)
        for y, line in enumerate(self.game.field):
            for x, val in enumerate(line):
                if val:
                    self.draw_cell((x, y), Color.WHITE)
