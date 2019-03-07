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
        self._descision = Move.DoNothing

    @property
    def descision(self):
        """Return controllers current descision and sets it to DoNothing."""
        ret = self._descision
        self._descision = Move.DoNothing
        return ret

    @descision.setter
    def descision(self, descision):
        """Set controllers current descision."""
        self._descision = descision
