"""Main window module."""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from .clock import MainClock

class MainWindow(QWidget):
    """Main window class."""

    def __init__(self):
        super().__init__()

        # this will hide the title bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        # change background color
        self.setStyleSheet("background-color: #11083b")

        # setting geometry of main window
        self.setGeometry(100, 100, 800, 400)

        # setting the clock to main window
        self.setLayout(MainClock(self))
