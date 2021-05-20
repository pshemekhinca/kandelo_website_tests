import os
import json


def load():
    config_path = os.path.join(os.path.dirname(__file__), '', 'web.json')
    with open(config_path, 'r') as file:
        config = file.read()
        return json.loads(config)
