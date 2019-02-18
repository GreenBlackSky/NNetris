from MWidgets import Window
from MWidgets import PygameGUI
from MWidgets import Event

from gamescene import GameScene


if __name__ == "__main__":
    cell_size = 20
    w, h = 9, 10
    win = Window((0, 0, w*cell_size, h*cell_size), layout_name="game")
    
    scn = GameScene((0, 0, 1, 1), fps=10, cell_size=cell_size, parent=win)
    scn.set_trigger(Event.Key.K_LEFT, win, "move_left")
    scn.set_trigger(Event.Key.K_RIGHT, win, "move_right")
    win.add_child("game", scn)

    gui = PygameGUI(w*cell_size, h*cell_size)
    win.set_gui(gui)
    
    win.exec()