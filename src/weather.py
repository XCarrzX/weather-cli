import requests
import os


def get_weather(city: str, unit: str = "metric") -> dict:
    """
    Ambil data cuaca dari OpenWeatherMap API.

    Args:
        city: Nama kota (misal: "Jakarta")
        unit: "metric" (Celsius) atau "imperial" (Fahrenheit)

    Returns:
        Dictionary berisi data cuaca yang sudah dirapikan

    Raises:
        ValueError: Jika kota tidak ditemukan / API key salah
        ConnectionError: Jika gagal koneksi ke API
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        raise ValueError(
            "❌ API Key tidak ditemukan!\n"
            "   Buat file .env dan isi OPENWEATHER_API_KEY=key_kamu"
        )

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": unit,
        "lang": "en"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
    except requests.exceptions.ConnectionError:
        raise ConnectionError("❌ Gagal koneksi. Cek internet kamu!")
    except requests.exceptions.Timeout:
        raise ConnectionError("❌ Timeout. Coba lagi!")

    if response.status_code == 404:
        raise ValueError(f"❌ Kota '{city}' tidak ditemukan!")
    elif response.status_code == 401:
        raise ValueError("❌ API Key tidak valid!")
    elif response.status_code != 200:
        raise ConnectionError(f"❌ Error dari server: {response.status_code}")

    data = response.json()

    return {
        "city":       data["name"],
        "country":    data["sys"]["country"],
        "temp":       round(data["main"]["temp"]),
        "feels_like": round(data["main"]["feels_like"]),
        "humidity":   data["main"]["humidity"],
        "wind_speed": round(data["wind"]["speed"] * 3.6),
        "wind_dir":   _get_wind_direction(data["wind"]["deg"]),
        "condition":  data["weather"][0]["description"].title(),
        "sunrise":    data["sys"]["sunrise"],
        "sunset":     data["sys"]["sunset"],
        "timezone":   data["timezone"],
        "unit":       unit,
    }


def _get_wind_direction(degrees: int) -> str:
    """Konversi derajat angin ke arah mata angin."""
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return directions[round(degrees / 45) % 8]
