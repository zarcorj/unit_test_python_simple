import json


def json_reader(file_location):
    """Reads a json file and returns a dictionary"""
    with open(file_location) as f:
        return json.load(f)
