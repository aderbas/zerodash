"""Main layout module."""
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from .clock import MainClock
from app.modules.wheater import Weather

class MainLayout(QVBoxLayout):
    """Main layout class"""

    def __init__(self, window: QWidget):
        super().__init__()

        self.window = window
        self.addItem(Weather(self.window))
        self.addItem(MainClock(self.window))
