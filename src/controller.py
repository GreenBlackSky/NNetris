from enum import Enum, auto


class Controller:
    class Move(Enum):
        DoNothing = auto()
        TurnLeft = auto()
        TurnRight = auto()
        MoveLeft = auto()
        MoveRight = auto()
        Drop = auto()

    def __init__(self):
        self.descision = Controller.Move.DoNothing