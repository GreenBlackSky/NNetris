from enum import Enum, auto


class Move(Enum):
    DoNothing = auto()
    TurnLeft = auto()
    TurnRight = auto()
    MoveLeft = auto()
    MoveRight = auto()
    Drop = auto()

class Controller:

    def __init__(self):
        self.descision = Move.DoNothing

    def set_descision(self, descision):
        self.descision = descision
    
    def get_descision(self):
        ret = self.descision
        self.descision = Move.DoNothing
        return ret