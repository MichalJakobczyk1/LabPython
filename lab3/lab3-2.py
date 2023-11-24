import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def read_file_content():
    file_name = "email/email_file"
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f'Plik o nazwie {file_name} nie istnieje.')
        return None
    except Exception as e:
        print(f'Wystąpił błąd podczas odczytu pliku: {str(e)}')
        return None

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Konfiguracja połączenia SMTP
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        # Utworzenie obiektu MIMEMultipart
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Dodanie treści do wiadomości
        message.attach(MIMEText(body, 'plain', 'utf-8'))

        # Utworzenie obiektu SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            # Rozpoczęcie połączenia TLS
            server.starttls()

            # Logowanie do konta
            server.login(sender_email, sender_password)

            # Wysłanie wiadomości e-mail
            server.send_message(message)

        print('E-mail został wysłany pomyślnie.')
    except Exception as e:
        print(f'Wystąpił błąd podczas wysyłania e-maila: {str(e)}')

if __name__ == "__main__":
    # Dane do wiadomości e-mail
    sender_email = 'michal.jakobczyk2@gmail.com'
    recipient_email = input('Podaj adres e-mail odbiorcy: ')
    subject = input('Podaj tytuł wiadomości: ')

    # Odczyt treści pliku
    file_content = read_file_content()

    if file_content:
        # Hasło do konta e-mailowego pobierane z pliku
        try:
            with open('email/haslo.txt', 'r') as password_file:
                sender_password = password_file.read().strip()
        except FileNotFoundError:
            print('Plik z hasłem nie został znaleziony.')
            sender_password = input('Podaj hasło do konta e-mailowego: ')

        # Wysłanie e-maila
        send_email(sender_email, sender_password, recipient_email, subject, file_content)