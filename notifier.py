# notifier.py

from config import EMAIL_CONFIG
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.message import EmailMessage
from config import EMAIL_CONFIG



def send_email(subject: str, body_text: str, body_html: str = None) -> None:
    """
    Invia un'email con soggetto `subject`.
    body_text: testo semplice (fallback)
    body_html: testo HTML opzionale (se fornito, email multipart)
    """

    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_CONFIG['sender']
    msg['To'] = EMAIL_CONFIG['recipient']
    msg['Subject'] = subject


    # Aggiunge il testo semplice (obbligatorio)
    part1 = MIMEText(body_text, 'plain')
    msg.attach(part1)

    # Se fornito, aggiunge il contenuto HTML
    if body_html:
        part2 = MIMEText(body_html, 'html')
        msg.attach(part2)

    # Invia tramite SMTP
    with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['port']) as server:
        server.starttls()
        server.login(EMAIL_CONFIG['sender'], EMAIL_CONFIG['password'])
        server.send_message(msg)
