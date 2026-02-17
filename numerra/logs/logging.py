from importlib import resources
from datetime import datetime

LOG_FILE = 'numerra.log'

def logging(string: str):
 with resources.files('numerra.logs').joinpath(LOG_FILE).open('w') as file:
    file.write(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] -> {string}\n')
