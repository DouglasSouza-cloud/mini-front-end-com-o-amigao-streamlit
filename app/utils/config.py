import os

from dotenv import load_dotenv


load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


if not WEATHER_API_KEY:
    raise ValueError(
        "A variável WEATHER_API_KEY não foi configurada."
    )