from MWidgets import Scene
from MWidgets import Event
from MWidgets import Color

from tetris import Tetris
from controller import Controller, Move


class GameScene(Scene):
    def __init__(self, rect, fps, cell_size, parent):
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
        self.game.mind.set_descision(Move.MoveRight)

    def move_left(self):
        self.game.mind.set_descision(Move.MoveLeft)

    def rotate_right(self):
        self.game.mind.set_descision(Move.TurnRight)

    def rotate_left(self):
        self.game.mind.set_descision(Move.TurnLeft)

    def update(self, events):
        super().update(events)
        self.game.update()
        if self.game.field_is_filled():
            self.event_queue.append(Event(Event.Type.Quit, self))

    def redraw(self):
        self.clear()
        fig_x, fig_y = self.game.current_figure.x, self.game.current_figure.y
        for x, y in self.game.current_figure:
            self.draw_cell((fig_x + x, fig_y + y), Color.WHITE.value)
        for y, line in enumerate(self.game.field):
            for x, val in enumerate(line):
                if val:
                    self.draw_cell((x, y), Color.WHITE.value)
