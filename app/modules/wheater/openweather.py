"""Wheater module."""
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from app.config import Config
from .service import WeatherService

class Weather(QHBoxLayout):
    """OpenWheater class."""

    def __init__(self, window: QWidget, config=Config) -> None:
        super().__init__()

        self.config = config
        self.window = window
        self.service = WeatherService(config=self.config)

        font = QFont('Arial', 12, QFont.Bold)

        self.label: QLabel = QLabel()
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #CCCCCC;")
        self.label.setText('Waiting...')

        # adding label to the layout
        self.addWidget(self.label)

        if not self.config.OPEN_WEATHER_APP_KEY or \
            not self.config.OPEN_WEATHER_LOCATION:
            self.label.setText('OpenWeather config missing.')
        else:
            weather_text = self.service.weather_simple_text()

            self.label.setText(weather_text)
           