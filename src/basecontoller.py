
from enum import Enum, auto


class Move(Enum):
    """Accessible moves."""

    DoNothing = auto()
    RotateLeft = auto()
    RotateRight = auto()
    MoveLeft = auto()
    MoveRight = auto()
    SuperSpeed = auto()
    NormalSpeed = auto()


class BaseController:

    def __init__(self):
        """Create BaseController."""
        self._last_move = Move.DoNothing

    def rotate_left(self):
        """Set next move to be rotate left."""
        self._last_move = Move.RotateLeft

    def rotate_right(self):
        """Set next move to be rotate right."""
        self._last_move = Move.RotateRight

    def move_left(self):
        """Set next move to be move left."""
        self._last_move = Move.MoveLeft

    def move_right(self):
        """Set next move to be move right."""
        self._last_move = Move.MoveRight

    def super_speed_on(self):
        """Set next move to be drop."""
        self._last_move = Move.SuperSpeed

    def super_speed_off(self):
        """Set next move to be drop."""
        self._last_move = Move.NormalSpeed

    def get_move(self):
        """Get last move made.

        Set next last move to DoNothing.
        """
        move = self._last_move
        self._last_move = Move.DoNothing
        return move
