# pylint: disable=too-few-public-methods
"""Config module."""
import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Config class."""
    OPEN_WEATHER_LOCATION = os.environ.get('OPEN_WEATHER_LOCATION')
    OPEN_WEATHER_APP_KEY = os.environ.get('OPEN_WEATHER_APP_KEY')
    OPEN_WEATHER_ENDPOINT = f'https://api.openweathermap.org/data/2.5/ \
        weather?q={urllib.parse.quote(OPEN_WEATHER_LOCATION)}& \
        appid={OPEN_WEATHER_APP_KEY}& \
        units={os.environ.get("OPEN_WEATHER_UNIT")}'.replace(" ", "")
