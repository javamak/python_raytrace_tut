import json
from scene import Scene

def load_scene(file_name):
    with open(file_name) as f:
        data = json.load(f)

    return Scene(data)