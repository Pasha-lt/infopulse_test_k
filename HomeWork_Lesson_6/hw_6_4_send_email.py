# Шаг 1. Включите IMAP-доступ
# Откройте Gmail на компьютере.
# В правом верхнем углу нажмите на значок "Настройки" Настройки затем Все настройки.
# Откройте вкладку Пересылка и POP/IMAP.
# В разделе "Доступ по протоколу IMAP" выберите Включить IMAP.
# Нажмите Сохранить изменения.

# Шаг 2. Разрешаем отправлять с всех приложений
# Откройте Gmail на компьютере.
# В правом верхнем углу нажмите на значок аватара затем управление аккаунтом Google.
# Переходим в вкладку безопасность листаем до вкладки Ненадежные приложения, у которых есть доступ к аккаунту и нажимаем
# открыть доступ вкл.


import smtplib

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML

sender_email = "sender@gmail.com" # почта отправителя.
destination_email = "destination@gmail.com" # почта получателя.
password = "password"

message = MIMEMultipart()  # Создаем сообщение
message['From'] = sender_email  # Адресат
message['To'] = destination_email  # Получатель
message['Subject'] = 'Тема письма'  # Тема сообщения

body = "Текст который будет в теле письма"
message.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Создаем объект SMTP
# server.starttls()             # Начинаем шифрованный обмен по TLS
server.login(sender_email, password)  # Получаем доступ
server.send_message(message)  # Отправляем сообщение
server.quit()  # Выходим
