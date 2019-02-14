from random import choice, randint
from enum import Enum, auto


class Tetris:

    class Figure:
        class Type(Enum):
            Square = auto()
            LeftHook = auto()
            RightHook = auto()
            LeftZigzag = auto()
            RightZigzag = auto()
            Triangle = auto()
            Line = auto()

        sizes = {
            Type.Square: 2,
            Type.LeftHook: 3,
            Type.RightHook: 3,
            Type.LeftZigzag: 3,
            Type.RightZigzag: 3,
            Type.Triangle: 3,
            Type.Line: 4
        }

        configurations = {
            Type.Square: {(0, 0), (0, 1), (1, 0), (1, 1)},
            Type.LeftHook: {(0, 0), (0, 1), (1, 1), (1, 2)},
            Type.RightHook: {(1, 0), (2, 0), (1, 1), (1, 2)},
            Type.LeftZigzag: {(0, 1), (1, 1), (1, 2), (2, 2)},
            Type.RightZigzag: {(0, 2), (1, 2), (1, 1), (2, 1)},
            Type.Triangle: {(0, 1), (1, 1), (1, 2), (2, 2)},
            Type.Line: {(1, 0), (1, 1), (1, 2), (1, 3)}
        }

        rotate_order = [
            (1, 0),
            (0, 0),
            (2, 1),
            (2, 0),
            (1, 2),
            (2, 2),
            (0, 1),
            (0, 2)
        ]

        def __init__(self, figure_type, x, y):
            self.type = figure_type
            self.x, self.y = x, y
            self.size = Tetris.Figure.sizes[self.type]
            self.cells = [[False]*self.size for _ in range(self.size)]
            for x, y in Tetris.Figure.configurations[self.type]:
                self.cells[x][y] = True

        def rotate_left(self):
            pass

        def rotate_right(self):
            pass

        def move_left(self):
            self.x -= 1

        def move_right(self):
            self.x += 1

        def move_down(self):
            self.y += 1

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.occupied = list()
        self.current_figure = None

    def update(self):
        if not self.current_figure:
            self.new_figure()
        self.current_figure.move_down()
        if self.figure_at_bottom():
            self.incorporate_figure()
        if self.has_full_lines():
            self.clear_lines()

    def new_figure(self):
        figure_type = choice(list(Tetris.Figure))
        figure_pos = (randint(0, self.w - Tetris.Figure.sizes[figure_type] - 1), 0)
        figure_rotation = randint(0, 3)
        self.current_figure = Tetris.Figure(figure_type, *figure_pos)
        for _ in range(figure_rotation):
            self.current_figure.rotate_left()

    def figure_at_bottom(self):
        pass

    def incorporate_figure(self):
        pass

    def has_full_lines(self):
        pass

    def clear_lines(self):
        pass

    def field_is_filled(self):
        pass