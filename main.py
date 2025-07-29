# main.py
from config import CITY
from weather import get_hourly_forecast_html
from notifier import send_email

if __name__ == "__main__":
    html_content = get_hourly_forecast_html(CITY)
    #print(html_content)
    plain_text = "Per favore usa un client email che supporta HTML per vedere le previsioni meteo."

    send_email(
    subject=f"🌤️ Previsioni meteo per {CITY}",
    body_text=plain_text,
    body_html=html_content
    )


