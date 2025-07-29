# weather.py

from datetime import datetime, timedelta
import requests
from datetime import datetime,timedelta
from collections import defaultdict
from config import OPENWEATHER_API_KEY, CITY, UNITS
import locale
locale.setlocale(locale.LC_TIME, 'it_IT.UTF-8')


def get_forecast_summary(city: str = CITY) -> str:
    url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": UNITS,
        "lang": "it"
    }

    response = requests.get(url, params=params)
    data = response.json()
    print(data)

    if response.status_code != 200:
        raise Exception(
            f"Errore API: {data.get('message', 'Errore sconosciuto')}")

    # Raggruppiamo le previsioni per giorno
    days = defaultdict(list)
    for entry in data["list"]:
        date = datetime.fromtimestamp(entry["dt"])
        day = date.date()
        days[day].append(entry)

    today = datetime.now().date()
    selected_days = [today + timedelta(days=i) for i in range(6)]  # oggi + 5

    emoji_map = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Snow": "❄️",
        "Thunderstorm": "⛈️",
        "Drizzle": "🌦️",
        "Mist": "🌫️"
    }


    giorni_settimana = {
        "Monday": "Lunedì",
        "Tuesday": "Martedì",
        "Wednesday": "Mercoledì",
        "Thursday": "Giovedì",
        "Friday": "Venerdì",
        "Saturday": "Sabato",
        "Sunday": "Domenica"
    }

    
    summary = f"📍 Previsioni meteo per {city}:\n\n"
    for day in selected_days:
        nome_giorno = giorni_settimana[day.strftime('%A')]
        entries = days.get(day)
        if not entries:
            continue

        temps = [e["main"]["temp"] for e in entries]
        avg_temp = sum(temps) / len(temps)
        main_weather = entries[0]["weather"][0]["main"]
        description = entries[0]["weather"][0]["description"]
        emoji = emoji_map.get(main_weather, "")

        summary += f"📅 {nome_giorno:<9} {day.strftime('%d/%m')} — 🌡️ {round(avg_temp):>2}°C  — {emoji}  {description.capitalize()}\n"

    return summary


def get_hourly_forecast_html(city: str = "Lecco") -> str:
    url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "it"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        raise Exception(
            f"Errore API: {data.get('message', 'Errore sconosciuto')}")

    # Raggruppiamo per giorno (data)
    days = defaultdict(list)
    for entry in data["list"]:
        date = datetime.fromtimestamp(entry["dt"])
        day = date.date()
        days[day].append(entry)

    today = datetime.now().date()
    selected_days = [today + timedelta(days=i)
                     for i in range(6)]  # oggi + 5 giorni

    emoji_map = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Snow": "❄️",
        "Thunderstorm": "⛈️",
        "Drizzle": "🌦️",
        "Mist": "🌫️"
    }

    # Costruiamo l'html
    html = f"""<html>
    <head>
    <style>
    body {{ font-family: Arial, sans-serif; color: #333; }}
    h2 {{ color: #2a9df4; }}
    table {{ border-collapse: collapse; width: 100%; max-width: 300px; }}
    th, td {{ border: 1px solid #ccc; padding: 6px 10px; text-align: center; }}
    th {{ background-color: #f0f8ff; text-align: center; }}
    td.temp {{ text-align: center; font-weight: bold; }}
    </style>
    </head>
    <body>
    <h2>📍 Previsioni meteo per {city}</h2>
    """

    for day in selected_days:
        entries = days.get(day)
        if not entries:
            continue

        day_str = day.strftime("%A %d/%m").capitalize()
        html += f"<h3>{day_str}</h3>"
        html += "<table><thead><tr><th>Ora</th><th>Temperatura</th><th>Descrizione</th></tr></thead><tbody>"

        for entry in entries:
            dt = datetime.fromtimestamp(entry["dt"])
            ora = dt.strftime("%H:%M")
            temp = round(entry["main"]["temp"])
            weather_main = entry["weather"][0]["main"]
            description = entry["weather"][0]["description"].capitalize()
            emoji = emoji_map.get(weather_main, "")

            html += f"<tr><td>{ora}</td><td class='temp'>{temp}°C</td><td>{emoji} {description}</td></tr>"

        html += "</tbody></table>"

    html += "</body></html>"
    return html
