"""Entry point for tetris game."""

from MWidgets import Window
from MWidgets import PygameGUI
from MWidgets import KeyEvent, KeyPressedEvent

from gamescene import GameScene


def play_tetris():
    """All game logic here."""
    cell_size = 20
    speed = 20
    w, h = 10, 15
    gui = PygameGUI(w*cell_size, h*cell_size)
    win = Window(gui)

    scn = GameScene((0, 0, 1, 1), cell_size, speed, win)
    scn.set_trigger(KeyPressedEvent, win, "move_left", KeyEvent.Key.K_LEFT)
    scn.set_trigger(KeyPressedEvent, win, "move_right", KeyEvent.Key.K_RIGHT)
    scn.set_trigger(KeyPressedEvent, win, "rotate_left", KeyEvent.Key.K_UP)
    scn.set_trigger(KeyPressedEvent, win, "drop", KeyEvent.Key.K_DOWN)
    win.add_widget(scn)

    win.exec()


if __name__ == "__main__":
    play_tetris()
