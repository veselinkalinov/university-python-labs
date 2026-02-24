"""Minimal CLI weather app — fetches live weather for a given city."""

import argparse
import sys

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WEATHER_CONDITIONS = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

TIMEOUT = 5  # seconds


def geocode(city: str) -> tuple[str, float, float, str]:
    """Resolve city name to (display_name, latitude, longitude, country)."""
    resp = requests.get(
        GEOCODING_URL,
        params={"name": city, "count": 1, "language": "en", "format": "json"},
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    data = resp.json()

    if not data.get("results"):
        print(f"Error: City '{city}' not found.")
        sys.exit(1)

    loc = data["results"][0]
    return loc["name"], loc["latitude"], loc["longitude"], loc.get("country", "")


def fetch_weather(lat: float, lon: float) -> dict:
    """Fetch current weather for given coordinates."""
    resp = requests.get(
        WEATHER_URL,
        params={
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m,weather_code",
        },
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    data = resp.json()

    cur = data["current"]
    return {
        "temperature": cur["temperature_2m"],
        "humidity": cur["relative_humidity_2m"],
        "condition": WEATHER_CONDITIONS.get(cur["weather_code"], "Unknown"),
    }


def display(name: str, country: str, weather: dict) -> None:
    """Print weather to stdout."""
    label = f"{name}, {country}" if country else name
    print(f"\n  Weather for {label}")
    print(f"  ───────────────────────")
    print(f"  Condition:   {weather['condition']}")
    print(f"  Temperature: {weather['temperature']} °C")
    print(f"  Humidity:    {weather['humidity']}%")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Get current weather for a city.")
    parser.add_argument("city", nargs="+", help="City name (e.g. London)")
    args = parser.parse_args()
    city = " ".join(args.city)

    try:
        name, lat, lon, country = geocode(city)
        weather = fetch_weather(lat, lon)
    except requests.ConnectionError:
        print("Error: No internet connection.")
        sys.exit(1)
    except requests.Timeout:
        print("Error: Request timed out. Try again.")
        sys.exit(1)
    except requests.HTTPError as e:
        print(f"Error: API request failed ({e.response.status_code}).")
        sys.exit(1)

    display(name, country, weather)


if __name__ == "__main__":
    main()
