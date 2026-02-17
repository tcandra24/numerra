from numerra.models.config import Config
import json

FILE = 'numerra/config/config.json'

def load_config():
  with open(FILE, 'r') as file:
    data = json.load(file)
    return Config(**data)