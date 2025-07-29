# Weather Notifier ☀️📬

Script Python che invia ogni mattina via email le previsioni meteo per la città di Lecco, utilizzando le API gratuite di OpenWeatherMap.

## 🚀 Funzionalità

- Previsioni dettagliate per oggi + 5 giorni
- Email HTML giornaliera, in italiano 🇮🇹
- Informazioni orarie (ogni 3 ore): temperatura, descrizione, icone
- Design minimale con emoji ☁️🌤️🌧️❄️
- Configurazione tramite `.env` per proteggere le credenziali

## 🛠️ Setup

1. **Clona la repo**:
   ```bash
   git clone https://github.com/tuo-username/weather_notifier.git
   cd weather_notifier
   ```

2. **Installa le dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Crea un file `.env`** nella root del progetto, con questi parametri:
   ```env
   OPENWEATHER_API_KEY=your_api_key
   CITY=Lecco
   UNITS=metric

   EMAIL_SENDER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   EMAIL_RECIPIENT=recipient_email@gmail.com
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   ```

4. **Esegui lo script**:
   ```bash
   python main.py
   ```

## 📬 Output email

L’email ricevuta conterrà una tabella ordinata, con le previsioni meteo della giornata ora per ora, più una sintesi dei prossimi giorni.

## 📌 Note

- Usa un'app password per Gmail (2FA necessario)
- Il progetto è pensato per l’automazione (puoi schedularlo con `crontab`)

---

**Made with ❤️ by [Luca Marrazzo](https://github.com/tuo-username)**  
