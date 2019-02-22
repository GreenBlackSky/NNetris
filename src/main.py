"""Entry point for tetris game."""

from MWidgets import Window
from MWidgets import PygameGUI
from MWidgets import Event

from gamescene import GameScene


def play_tetris():
    """All game logic here."""
    cell_size = 20
    speed = 20
    w, h = 10, 20
    gui = PygameGUI(w*cell_size, h*cell_size)
    win = Window(gui, layout_name="game")

    scn = GameScene((0, 0, 1, 1), cell_size, speed, win)
    scn.set_trigger(Event.Key.K_LEFT, win, "move_left")
    scn.set_trigger(Event.Key.K_RIGHT, win, "move_right")
    scn.set_trigger(Event.Key.K_UP, win, "rotate_left")
    scn.set_trigger(Event.Key.K_DOWN, win, "drop")
    win.add_child(scn, "game")

    win.exec()


if __name__ == "__main__":
    play_tetris()
