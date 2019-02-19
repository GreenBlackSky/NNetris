"""Module contains all of game logic."""

from random import randint
from enum import Enum, auto
from copy import deepcopy
from typing import List

from controller import Controller, Move


class Figure:
    """Falling figure."""

    class Type(Enum):
        """Type of figure."""

        Block = auto()
        Square = auto()
        LeftHook = auto()
        RightHook = auto()
        LeftZigzag = auto()
        RightZigzag = auto()
        Triangle = auto()
        Line = auto()

    sizes = {
        Type.Block: 1,
        Type.Square: 2,
        Type.LeftHook: 3,
        Type.RightHook: 3,
        Type.LeftZigzag: 3,
        Type.RightZigzag: 3,
        Type.Triangle: 3,
        Type.Line: 4
    }

    configurations = {
        Type.Block: {(0, 0)},
        Type.Square: {(0, 0), (0, 1), (1, 0), (1, 1)},
        Type.LeftHook: {(0, 0), (1, 0), (1, 1), (1, 2)},
        Type.RightHook: {(1, 0), (2, 0), (1, 1), (1, 2)},
        Type.LeftZigzag: {(0, 1), (1, 1), (1, 2), (2, 2)},
        Type.RightZigzag: {(0, 2), (1, 2), (1, 1), (2, 1)},
        Type.Triangle: {(0, 2), (1, 1), (1, 2), (2, 2)},
        Type.Line: {(1, 0), (1, 1), (1, 2), (1, 3)}
    }

    def __init__(self, figure_type, x, y):
        """Create figure of given type in given position."""
        self.x, self.y = x, y
        self.size = Figure.sizes[figure_type]
        self.cells = deepcopy(Figure.configurations[figure_type])

    def __iter__(self):
        """Return iterator of cells."""
        return iter(self.cells)

    def rotate_left(self):
        """Rotate figure left."""
        new_cells = set()
        for x, y in self.cells:
            new_cells.add((self.size - y - 1, x))
        self.cells = new_cells

    def rotate_right(self):
        """Rotate figure right."""
        new_cells = set()
        for x, y in self.cells:
            new_cells.add((y, self.size - x - 1))
        self.cells = new_cells


class Tetris:
    """Tetris game logic."""

    def __init__(self, w, h):
        """Create game of tetris with field of given size."""
        self.w, self.h = w, h
        self.mind = Controller()
        self.field = [[False]*self.w for _ in range(self.h)]
        self.current_figure = None
        self.new_figure()

    def update(self):
        """Update the situation in the game.

        All the basics of game logic implemented here.
        """
        if self.figure_at_bottom():
            self.incorporate_figure()
            self.new_figure()
        self.make_move()
        filled_lines = self.check_filled_lines()
        self.remove_lines(filled_lines)
        self.drop_lines(filled_lines)

    def new_figure(self):
        """Create new falling figure."""
        # figure_type = choice(list(Tetris.Figure))
        figure_type = Figure.Type.Block
        figure_pos = (randint(0, self.w - Figure.sizes[figure_type]), 0)
        figure_rotation = randint(0, 3)
        self.current_figure = Figure(figure_type, *figure_pos)
        for _ in range(figure_rotation):
            self.current_figure.rotate_left()

    def make_move(self):
        """Move falling figure due to controllers state."""
        descision = self.mind.get_descision()
        x, y = self.current_figure.x, self.current_figure.y

        if y < self.h - 1 and not self.field[y + 1][x]:
            self.current_figure.y += 1
            y += 1

        if descision == Move.RotateLeft:
            self.current_figure.rotate_left()

        elif descision == Move.RotateRight:
            self.current_figure.rotate_right()

        elif descision == Move.MoveLeft \
            and x > 0 \
                and not self.field[y][x - 1]:
            self.current_figure.x -= 1

        elif descision == Move.MoveRight \
            and x + self.current_figure.size < self.w \
                and not self.field[y][x + self.current_figure.size]:
            self.current_figure.x += 1

        elif descision == Move.Drop:
            pass
        elif descision == Move.DoNothing:
            pass

    def figure_at_bottom(self) -> bool:
        """Check if figure touches bottom or another block."""
        for fig_x, fig_y in self.current_figure:
            x, y = self.current_figure.x + fig_x, self.current_figure.y + fig_y
            if y == self.h - 1 or self.field[y + 1][x]:
                return True
        return False

    def incorporate_figure(self):
        """Make falling figure part of a games landscape."""
        for fig_x, fig_y in self.current_figure:
            x, y = self.current_figure.x + fig_x, self.current_figure.y + fig_y
            self.field[y][x] = True

    def check_filled_lines(self) -> List[int]:
        """Check if there are full lines."""
        filled_lines = list()
        for y, line in enumerate(self.field):
            if all(line):
                filled_lines.append(y)
        return filled_lines

    def remove_lines(self, filled_lines: List[int]):
        """Remove lines in given coordinates from games landscape."""
        for y in filled_lines:
            line = self.field[y]
            for x in range(len(line)):
                line[x] = False

    def drop_lines(self, deleted_lines: List[int]):
        """Push down blocks after deleting a lines under them."""
        deleted_lines.sort(reverse=True)
        for deleted in deleted_lines:
            self.drop_one_line(deleted)

    def drop_one_line(self, deleted: int):
        """Push down blocks above line with given coordinate."""
        for x in range(self.w):
            for y in range(deleted, 1, -1):
                self.field[y][x] = self.field[y - 1][x]

    def field_is_filled(self):
        """Check if game is over."""
        return any(self.field[0])
