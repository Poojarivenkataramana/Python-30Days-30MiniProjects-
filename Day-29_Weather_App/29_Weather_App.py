# ----------------------------------------------------
# Day 29: Weather Forecast Formatter & CLI Viewer
# Concepts: HTTP requests (urllib.request / json), Offline Fallback Dictionaries, Formatting
# ----------------------------------------------------

import json
import urllib.request
import urllib.error

# Offline fallback weather database for testing without internet
OFFLINE_WEATHER_DB = {
    "london": {"city": "London", "country": "UK", "temp_c": 18, "condition": "Cloudy ☁️", "humidity": 72, "wind_kmh": 14},
    "new york": {"city": "New York", "country": "USA", "temp_c": 24, "condition": "Partly Cloudy ⛅", "humidity": 65, "wind_kmh": 18},
    "tokyo": {"city": "Tokyo", "country": "Japan", "temp_c": 28, "condition": "Sunny ☀️", "humidity": 60, "wind_kmh": 10},
    "mumbai": {"city": "Mumbai", "country": "India", "temp_c": 31, "condition": "Thunderstorms ⛈️", "humidity": 85, "wind_kmh": 22},
    "paris": {"city": "Paris", "country": "France", "temp_c": 22, "condition": "Clear Sky 🌤️", "humidity": 55, "wind_kmh": 12},
    "sydney": {"city": "Sydney", "country": "Australia", "temp_c": 20, "condition": "Breezy 💨", "humidity": 58, "wind_kmh": 25},
    "delhi": {"city": "Delhi", "country": "India", "temp_c": 34, "condition": "Hot & Sunny ☀️", "humidity": 45, "wind_kmh": 8}
}

def fetch_live_weather(city_name):
    url = f"https://wttr.in/{urllib.parse.quote(city_name)}?format=j1"
    req = urllib.request.Request(url, headers={"User-Agent": "PythonMiniProject/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            current = data["current_condition"][0]
            area = data["nearest_area"][0]
            
            temp_c = int(current["temp_C"])
            condition = current["weatherDesc"][0]["value"]
            humidity = current["humidity"]
            wind_kmh = current["windspeedKmph"]
            city = area["areaName"][0]["value"]
            country = area["country"][0]["value"]

            return {
                "city": city,
                "country": country,
                "temp_c": temp_c,
                "condition": condition,
                "humidity": humidity,
                "wind_kmh": wind_kmh
            }
    except Exception:
        # Fallback to offline database if offline or API limit reached
        key = city_name.strip().lower()
        if key in OFFLINE_WEATHER_DB:
            return OFFLINE_WEATHER_DB[key]
        return None

def display_weather_card(info):
    temp_c = info["temp_c"]
    temp_f = round((temp_c * 9 / 5) + 32, 1)

    print("\n" + "=" * 48)
    print(f"🌍 WEATHER IN {info['city'].upper()}, {info['country'].upper()} 🌍".center(48))
    print("=" * 48)
    print(f"{'Condition':<20}: {info['condition']}")
    print(f"{'Temperature':<20}: {temp_c}°C / {temp_f}°F")
    print(f"{'Humidity':<20}: {info['humidity']}%")
    print(f"{'Wind Speed':<20}: {info['wind_kmh']} km/h")
    print("-" * 48)

    if temp_c >= 30:
        print("💡 Suggestion: It's hot outside! Stay hydrated. 🥤")
    elif temp_c <= 10:
        print("💡 Suggestion: Cold weather! Wear warm clothing. 🧥")
    else:
        print("💡 Suggestion: Pleasant weather for outdoor activities! 🚶")
    print("=" * 48)

def main():
    print("=" * 50)
    print("🌤️  WEATHER FORECAST CLI VIEWER  🌤️".center(50))
    print("=" * 50)

    while True:
        city = input("\nEnter City Name (or 'q' to quit): ").strip()
        if city.lower() in ("q", "quit"):
            print("\nStay weather-wise! Goodbye! 🌈\n")
            break

        if not city:
            print("❌ City name cannot be empty.")
            continue

        print(f"Fetching weather for '{city}'...")
        info = fetch_live_weather(city)

        if info:
            display_weather_card(info)
        else:
            print(f"❌ Could not retrieve weather data for '{city}'.")
            print("Try major cities like: London, Tokyo, New York, Mumbai, Paris, Sydney, Delhi.")

if __name__ == "__main__":
    main()
