"""Module contains Controller and Move classes."""

from enum import Enum, auto


class Move(Enum):
    """Accessible moves."""

    DoNothing = auto()
    RotateLeft = auto()
    RotateRight = auto()
    MoveLeft = auto()
    MoveRight = auto()
    Drop = auto()


class Controller:
    """Bridge-class, which provides behaviour from user to game."""

    def __init__(self):
        """Inittalize Controller with Move.DoNothing."""
        self.descision = Move.DoNothing

    def set_descision(self, descision: Move):
        """Set controllers current descision."""
        self.descision = descision

    def get_descision(self):
        """Return controllers current descision and sets it to DoNothing."""
        ret = self.descision
        self.descision = Move.DoNothing
        return ret
