"""Entry point for tetris game."""

from MWidgets import Window
from MWidgets import PygameGUI
from MWidgets import Event

from gamescene import GameScene


if __name__ == "__main__":
    CELL_SIZE = 20
    W, H = 10, 20
    WIN = Window((0, 0, W*CELL_SIZE, H*CELL_SIZE), layout_name="game")

    SCN = GameScene((0, 0, 1, 1), fps=5, cell_size=CELL_SIZE, parent=WIN)
    SCN.set_trigger(Event.Key.K_LEFT, WIN, "move_left")
    SCN.set_trigger(Event.Key.K_RIGHT, WIN, "move_right")
    SCN.set_trigger(Event.Key.K_UP, WIN, "rotate_left")
    WIN.add_child("game", SCN)

    GUI = PygameGUI(W*CELL_SIZE, H*CELL_SIZE)
    WIN.set_gui(GUI)

    WIN.exec()
