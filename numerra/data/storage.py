from importlib import resources
import json

FILE = 'histories.json'

def push_data(data):
  with resources.files('numerra.data').joinpath(FILE).open('w') as file:
    json.dump(data, file, indent=2)

def show_data():
  with resources.files('numerra.data').joinpath(FILE).open('r') as file:
    return json.load(file)