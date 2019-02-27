"""Module contains all of game logic."""

from random import randint, choice
from enum import Enum, auto
from copy import deepcopy

from controller import Controller, Move


class Figure:
    """Falling figure."""

    class Type(Enum):
        """Type of figure."""

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

    def __init__(self, speed, w, h):
        """Create game of tetris with field of given size."""
        self.w, self.h = w, h
        self.mind = Controller()
        self.field = [[False]*self.w for _ in range(self.h)]
        self.current_figure = None
        self.__new_figure()

        self.normal_speed = speed
        self.speed = self.normal_speed
        self.step_count = 0

    def update(self):
        """Update the situation in the game.

        All the basics of game logic implemented here.
        """
        clear_below, clear_to_right, clear_to_left = self.__get_borders()

        self.step_count = (self.step_count + 1) % self.speed
        if self.step_count == 0:
            self.__pull_down(clear_below)
            filled_lines = self.__check_filled_lines()
            if filled_lines:
                self.__remove_lines(filled_lines)
                self.__drop_lines(filled_lines)

        self.__make_move(clear_to_right, clear_to_left)

    def field_is_filled(self):
        """Check if game is over."""
        return any(self.field[0])

    def __get_borders(self):
        clear_below = True
        clear_to_right = True
        clear_to_left = True
        for x, y in self.__figure_blocks():
            if y == self.h - 1 or self.field[y + 1][x]:
                clear_below = False
            if x == 0 or self.field[y][x - 1]:
                clear_to_left = False
            if x == self.w - 1 or self.field[y][x + 1]:
                clear_to_right = False
        return clear_below, clear_to_right, clear_to_left

    def __figure_blocks(self):
        for fig_x, fig_y in self.current_figure:
            x, y = self.current_figure.x + fig_x, self.current_figure.y + fig_y
            yield x, y

    def __pull_down(self, clear_below):
        if clear_below:
            self.current_figure.y += 1
        else:
            self.__incorporate_figure()
            self.__new_figure()

    def __incorporate_figure(self):
        for x, y in self.__figure_blocks():
            self.field[y][x] = True

    def __new_figure(self):
        figure_type = choice(list(Figure.Type))
        figure_pos = (randint(0, self.w - Figure.sizes[figure_type]), 0)
        figure_rotation = randint(0, 3)
        self.current_figure = Figure(figure_type, *figure_pos)
        for _ in range(figure_rotation):
            self.current_figure.rotate_left()

    def __check_filled_lines(self):
        filled_lines = list()
        for y, line in enumerate(self.field):
            if all(line):
                filled_lines.append(y)
        return filled_lines

    def __remove_lines(self, filled_lines):
        for y in filled_lines:
            self.field[y] = [False]*self.w

    def __drop_lines(self, deleted_lines):
        top = min(deleted_lines)
        bottom = max(deleted_lines)
        fall = bottom - top + 1
        for y in range(top - 1, -1, -1):
            self.field[y + fall], self.field[y] = \
                self.field[y], self.field[y + fall]
            if not any(self.field[y + fall]):
                break

    def __make_move(self, clear_to_right, clear_to_left):
        descision = self.mind.get_descision()
        x, y = self.current_figure.x, self.current_figure.y

        self.speed = self.normal_speed

        if descision == Move.RotateLeft:
            self.current_figure.rotate_left()

        elif descision == Move.RotateRight:
            self.current_figure.rotate_right()

        elif descision == Move.MoveLeft and clear_to_left:
            self.current_figure.x -= 1

        elif descision == Move.MoveRight and clear_to_right:
            self.current_figure.x += 1

        elif descision == Move.Drop:
            self.speed = 2

        elif descision == Move.DoNothing:
            pass

# TODO Rotation near the edge can crash the game
# TODO Figure slowers down near the bottom
