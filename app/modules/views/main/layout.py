"""Main layout module."""
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from app.modules.wheater import Weather
from .clock import MainClock

class MainLayout(QVBoxLayout):
    """Main layout class"""

    def __init__(self, window: QWidget):
        super().__init__()

        self.window = window
        self.addItem(Weather(self.window))
        self.addItem(MainClock(self.window))
