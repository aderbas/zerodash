"""Main window module."""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from .layout import MainLayout
#from .clock import MainClock
#from app.modules.wheater import Weather

class MainWindow(QWidget):
    """Main window class."""

    def __init__(self):
        super().__init__()

        # this will hide the title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #11083b")
        self.setGeometry(100, 100, 800, 400)
        self.setLayout(MainLayout(self))
        self.showMaximized()
