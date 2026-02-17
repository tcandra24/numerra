from numerra.models.config import Config
from importlib import resources
import json

FILE = 'config.json'

def load_config():
  with resources.files('numerra.config').joinpath(FILE).open('r') as file:
    data = json.load(file)
    return Config(**data)