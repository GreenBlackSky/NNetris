from basecontoller import BaseController
from tkinter import Frame


class TKController(BaseController, Frame):
    def __init__(self, master, **kargs):
        Frame.__init__(self, master, **kargs)
        BaseController.__init__(self)
        self.bind("<Key-Up>", lambda event: self.rotate_left())
        self.bind("<Shift-Up>", lambda event: self.rotate_right())
        self.bind("<Key-Left>", lambda event: self.move_left())
        self.bind("<Key-Right>", lambda event: self.move_right())
        self.bind("<Key-Down>", lambda event: self.super_speed_on())
        self.bind("<KeyRelease-Down>", lambda event: self.super_speed_off())
