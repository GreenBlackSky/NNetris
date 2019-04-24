"""OptionsFrame class."""

from tkinter import Frame, Canvas, Label, Listbox, Button, Scale
from tkinter import LEFT, BOTH, HORIZONTAL, X


class OptionsFrame(Frame):
    """Contains widgets to tune game."""

    def __init__(self, app):
        """Create OptionsFrame."""
        super().__init__(app)

        Canvas(self).pack(fill=BOTH, expand=True)

        Label(self, text='Appearance:').pack()
        Listbox(self).pack(fill=BOTH, expand=True)

        Label(self, text='Cell size:').pack()
        Scale(self, to=5, orient=HORIZONTAL).pack(fill=X, expand=True)

        Label(self, text='Speed:').pack()
        Scale(self, to=10, orient=HORIZONTAL).pack(fill=X, expand=True)

        Button(self, text="Drop record table").pack()

        Button(self, text="Back", command=self.master.main_menu).pack()
