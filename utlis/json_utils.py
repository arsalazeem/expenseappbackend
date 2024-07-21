import json


def load_json_as_dict(path: str) -> dict:
    with open(path, "r") as outfile:
        data = json.load(outfile)
    return data
