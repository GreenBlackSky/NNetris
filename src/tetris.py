from random import choice, randint
from enum import Enum, auto

from controller import Controller


class Tetris:
    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y

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
            Type.LeftHook: {(0, 0), (1, 0), (1, 1), (1, 2)},
            Type.RightHook: {(1, 0), (2, 0), (1, 1), (1, 2)},
            Type.LeftZigzag: {(0, 1), (1, 1), (1, 2), (2, 2)},
            Type.RightZigzag: {(0, 2), (1, 2), (1, 1), (2, 1)},
            Type.Triangle: {(0, 2), (1, 1), (1, 2), (2, 2)},
            Type.Line: {(1, 0), (1, 1), (1, 2), (1, 3)}
        }

        def __init__(self, figure_type, fig_x, fig_y):
            self.size = Tetris.Figure.sizes[figure_type]
            self.cells = {Tetris.Cell(x + fig_x, y + fig_y) for x, y in Tetris.Figure.configurations[figure_type]}

        def rotate_left(self):
            for cell in self.cells:
                cell.x, cell.y = self.size - cell.y - 1, cell.x

        def rotate_right(self):
            for cell in self.cells:
                cell.x, cell.y = cell.y, self.size - cell.x - 1

        def move_left(self):
            for cell in self.cells:
                cell.x -= 1

        def move_right(self):
            for cell in self.cells:
                cell.x += 1

        def move_down(self):
            for cell in self.cells:
                cell.y += 1

    moves = {
        Controller.Move.Drop: Figure.move_down,
        Controller.Move.MoveLeft: Figure.move_left,
        Controller.Move.MoveRight: Figure.move_right,
        Controller.Move.TurnLeft: Figure.rotate_left,
        Controller.Move.TurnRight: Figure.rotate_right
    }

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.mind = Controller()
        self.current_figure = None
        self.occupied = list()
        self.top_occupied = None
        self.occupied_lines = dict()

    def update(self):
        if not self.current_figure:
            self.new_figure()
        self.make_move()
        self.current_figure.move_down()
        if self.figure_at_bottom():
            self.incorporate_figure()
        if self.has_full_lines():
            deleted_lines = self.clear_lines()
            self.drop_lines(deleted_lines)

    def new_figure(self):
        figure_type = choice(list(Tetris.Figure))
        figure_pos = (randint(0, self.w - Tetris.Figure.sizes[figure_type] - 1), 0)
        figure_rotation = randint(0, 3)
        self.current_figure = Tetris.Figure(figure_type, *figure_pos)
        for _ in range(figure_rotation):
            self.current_figure.rotate_left()

    def make_move(self):
        if self.mind.descision == Controller.Move.DoNothing:
            return
        Tetris.moves[self.mind.descision](self.current_figure)

    def figure_at_bottom(self):
        if choice(self.current_figure.cells).y < self.top_occupied.y - 3:
            return False

        for fig_cell in self.current_figure:
            for occupied_cell in self.occupied:
                if fig_cell.x == occupied_cell.x and fig_cell.y == occupied_cell.y - 1:
                    return True
        return False

    def incorporate_figure(self):
        for cell in self.current_figure.cells:
            self.occupied.append(cell)
            if not self.top_occupied or cell.y > self.top_occupied.y:
                self.top_occupied = cell
            self.occupied_lines[cell.y] = self.occupied_lines.get(cell.y, list()) + [cell]
        self.current_figure = None

    def has_full_lines(self):
        for line in self.occupied_lines.values():
            if len(line) == self.w:
                return True
        return False

    def clear_lines(self):
        deleted_lines = list()
        for y, line in self.occupied_lines.items():
            if len(line) == self.w:
                self.occupied_lines[y].clear()
                deleted_lines.append(y)
        return deleted_lines

    def drop_lines(self, deleted_lines):
        for cell in self.occupied:
            for line_n in deleted_lines:
                if line_n < cell.y:
                    cell.y -= 1
            
    def field_is_filled(self):
        return (self.top_occupied.y <= 0)