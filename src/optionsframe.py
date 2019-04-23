"""OptionsFrame class."""

from tkinter import Frame, Canvas, Label, Listbox, IntVar, Radiobutton, Button
from tkinter import LEFT, BOTH


class OptionsFrame(Frame):
    """Contains widgets to tune game."""

    def __init__(self, app):
        """Create OptionsFrame."""
        super().__init__(app)

        Canvas(self).pack(fill=BOTH, expand=True)

        Label(self, text='Appearance:').pack()
        Listbox(self).pack(fill=BOTH, expand=True)

        Label(self, text='Cell size:').pack()
        cell_size = IntVar()
        cell_size_frame = Frame(self)
        for i in range(5):
            Radiobutton(
                cell_size_frame,
                variable=cell_size,
                value=i
            ).pack(side=LEFT)
        cell_size_frame.pack()
        cell_size.set(0)

        Label(self, text='Speed:').pack()
        speed = IntVar()
        speed_frame = Frame(self)
        for i in range(10):
            Radiobutton(
                speed_frame,
                variable=speed,
                value=i
            ).pack(side=LEFT)
        speed_frame.pack()
        speed.set(0)

        Button(self, text="Drop record table").pack()

        Button(self, text="Back", command=self.master.main_menu).pack()
