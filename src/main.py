"""Entry point for tetris game."""

from mainwindow import MainWindow

if __name__ == '__main__':
    app = MainWindow(title="Netris", size="450x800")
    app.mainloop()
