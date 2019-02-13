from MWidgets import Window
from MWidgets import Scene
from MWidgets import PygameGUI

if __name__ == "__main__":
    win = Window((0, 0, 200, 100), layout_name="game")
    
    scn = Scene((0, 0, 1, 1), 20, 10)
    win.add_child("game", scn)
    
    gui = PygameGUI(200, 100)
    win.set_gui(gui)
    
    win.exec()