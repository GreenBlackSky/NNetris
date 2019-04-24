"""MainMenuFrame class."""

from tkinter import Frame, Button, Listbox


class MainMenuFrame(Frame):
    """Frame contains buttons to new game and options, and record table."""

    def __init__(self, app):
        """Create MainMenuFrame."""
        super().__init__(app)

        Button(
            self,
            text="New game",
            command=self.master.game
        ).grid(column=0, row=0, sticky="nsew")

        Button(
            self,
            text="Options",
            command=self.master.options
        ).grid(column=0, row=1, sticky="nsew")

        Button(
            self,
            text="Quit",
            command=self.master.destroy
        ).grid(column=0, row=2, sticky="nsew")

        Listbox(self).grid(column=1, row=0, rowspan=3, sticky="nsew")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
