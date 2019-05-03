"""Module contains all of game logic."""

from random import randint, choice
from enum import Enum, auto


class Tetris:
    """Tetris game logic."""

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
            Type.Triangle: {(0, 1), (1, 0), (1, 1), (2, 1)},
            Type.Line: {(1, 0), (1, 1), (1, 2), (1, 3)}
        }

        def __init__(self, figure_type, x, y):
            """Create figure of given type in given position."""
            self._x, self._y = x, y
            self._size = Tetris.Figure.sizes[figure_type]
            self._cells = Tetris.Figure.configurations[figure_type]

        def __iter__(self):
            """Return iterator of cells."""
            return iter(self._cells)

        def rotate_left(self):
            """Rotate figure left."""
            new_cells = set()
            for x, y in self._cells:
                new_cells.add((self._size - y - 1, x))
            self._cells = new_cells

        def rotate_right(self):
            """Rotate figure right."""
            new_cells = set()
            for x, y in self._cells:
                new_cells.add((y, self._size - x - 1))
            self._cells = new_cells

        @property
        def x(self):
            """Get x coordinate of figure top left corner."""
            return self._x

        @x.setter
        def x(self, value):
            """Set x coordinate of figure top left corner."""
            self._x = value

        @property
        def y(self):
            """Get y coordinate of figure top left corner."""
            return self._y

        @y.setter
        def y(self, value):
            """Set y coordinate of figure top left corner."""
            self._y = value

    class Move(Enum):
        """Accessible moves."""

        DoNothing = auto()
        RotateLeft = auto()
        RotateRight = auto()
        MoveLeft = auto()
        MoveRight = auto()
        Drop = auto()

    def __init__(self, speed, w, h):
        """Create game of tetris with field of given size."""
        self._w, self._h = w, h
        self._field = [[False]*self._w for _ in range(self._h)]
        self._current_figure = None
        self._new_figure()
        self._last_move = Tetris.Move.DoNothing
        self._speed = speed
        self._step_count = 0

    def rotate_left(self):
        """Set next move to be rotate left.

        Command is executed after update is called and
        only if possible.
        """
        self._last_move = Tetris.Move.RotateLeft

    def rotate_right(self):
        """Set next move to be rotate right.

        Command is executed after update is called and
        only if possible.
        """
        self._last_move = Tetris.Move.RotateRight

    def move_left(self):
        """Set next move to be move left.

        Command is executed after update is called and
        only if possible.
        """
        self._last_move = Tetris.Move.MoveLeft

    def move_right(self):
        """Set next move to be move right.

        Command is executed after update is called and
        only if possible.
        """
        self._last_move = Tetris.Move.MoveRight

    def drop(self):
        """Set next move to be drop.

        Command is executed after update is called and
        only if possible.
        """
        self._last_move = Tetris.Move.Drop

    def update(self):
        """Update the situation in the game.

        All the basics of game logic implemented here.
        """
        clear_below, clear_to_right, clear_to_left = self._get_borders()

        self._step_count = (self._step_count + 1) % self._speed
        if self._step_count == 0:
            self._pull_figure_down(clear_below)
            self._drop_full_lines()

        self._make_move(clear_to_right, clear_to_left)
        self._last_move = Tetris.Move.DoNothing

    def field_is_filled(self):
        """Check if game is over."""
        return any(self._field[0])

    def _new_figure(self):
        figure_type = choice(list(Tetris.Figure.Type))
        figure_rotation = randint(0, 3)
        self._current_figure = Tetris.Figure(
            figure_type,
            randint(0, self._w - Tetris.Figure.sizes[figure_type]),
            0
        )
        for _ in range(figure_rotation):
            self._current_figure.rotate_left()

    def _get_borders(self):
        clear_below = True
        clear_to_right = True
        clear_to_left = True
        for x, y in self._figure_cells():
            if y == self._h - 1 or self._field[y + 1][x]:
                clear_below = False
            if x == 0 or self._field[y][x - 1]:
                clear_to_left = False
            if x == self._w - 1 or self._field[y][x + 1]:
                clear_to_right = False
        return clear_below, clear_to_right, clear_to_left

    def _pull_figure_down(self, clear_below):
        if clear_below:
            self._current_figure.y += 1
        else:
            for x, y in self._figure_cells():
                self._field[y][x] = True
            self._new_figure()

    def _drop_full_lines(self):
        full_lines = [y for y in range(self._h) if all(self._field[y])]
        if not full_lines:
            return

        for y in full_lines:
            self._field[y] = [False]*self._w
        top = min(full_lines)
        bottom = max(full_lines)
        fall = bottom - top + 1
        for y in range(top - 1, -1, -1):
            self._field[y + fall], self._field[y] = \
                self._field[y], self._field[y + fall]

    def _make_move(self, clear_to_right, clear_to_left):
        descision = self._last_move

        if descision == Tetris.Move.RotateLeft:
            self._current_figure.rotate_left()
            if self._figure_intersects():
                self._current_figure.x += 1
            if self._figure_intersects():
                self._current_figure.x -= 2
            if self._figure_intersects():
                self._current_figure.x += 1
                self._current_figure.rotate_right()

        elif descision == Tetris.Move.RotateRight:
            self._current_figure.rotate_right()
            if self._figure_intersects():
                self._current_figure.x -= 1
            if self._figure_intersects():
                self._current_figure.x += 2
            if self._figure_intersects():
                self._current_figure.x -= 1
                self._current_figure.rotate_left()

        elif descision == Tetris.Move.MoveLeft and clear_to_left:
            self._current_figure.x -= 1

        elif descision == Tetris.Move.MoveRight and clear_to_right:
            self._current_figure.x += 1

        elif descision == Tetris.Move.Drop:
            pass

        elif descision == Tetris.Move.DoNothing:
            pass

    def _figure_cells(self):
        for fig_x, fig_y in self._current_figure:
            yield self._current_figure.x + fig_x, \
                  self._current_figure.y + fig_y

    def _figure_intersects(self):
        for x, y in self._figure_cells():
            if x < 0 or x >= self._w \
                or y < 0 or y >= self._h \
                    or self._field[y][x]:
                return True
        return False

    @property
    def current_figure(self):
        """Get current falling figure."""
        return self._current_figure

    @property
    def field(self):
        """Get game field."""
        return self._field
