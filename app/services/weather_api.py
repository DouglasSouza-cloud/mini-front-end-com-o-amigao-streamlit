import requests

from app.utils.config import WEATHER_API_KEY


BASE_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather(city: str) -> dict:
    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "lang": "pt",
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=10,
    )

    if response.status_code != 200:
        try:
            error_data = response.json()
            error_message = error_data.get("error", {}).get(
                "message",
                "Erro desconhecido"
            )
            error_code = error_data.get("error", {}).get(
                "code",
                "Sem código"
            )

            raise RuntimeError(
                f"Erro ao consultar a API. "
                f"HTTP {response.status_code} | "
                f"Código {error_code} | "
                f"{error_message}"
            )

        except ValueError:
            raise RuntimeError(
                f"Erro ao consultar a API. "
                f"HTTP {response.status_code}"
            )

    return response.json()