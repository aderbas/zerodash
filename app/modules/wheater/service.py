# pylint: disable=unused-variable
"""Service for request endpoint API for Weather."""
import requests

from app.config import Config

class WeatherService:
    """Service class."""

    def __init__(self, config:Config) -> None:
        self.config = config

    def fetch_weather(self):
        """Request json data for wheater."""
        try:
            response = requests.get(self.config.OPEN_WEATHER_ENDPOINT)
            response.raise_for_status()
            data = response.json()

            return data
        except requests.exceptions.HTTPError as herror:
            return None
        except requests.exceptions.ConnectionError as errc:
            return None
        except requests.exceptions.Timeout as errt:
            return None
        except requests.exceptions.RequestException as err:
            return None

    def weather_simple_text(self) -> str:
        """Get wheater text."""
        res = self.fetch_weather()
        wt_string = ""
        if res is not None and res['cod'] == 200:
            wt_string = f'{res["name"]}, {res["weather"][0]["main"]}'
            wt_string = f'{wt_string} {str(res["main"]["feels_like"])}ºC'

        return wt_string
