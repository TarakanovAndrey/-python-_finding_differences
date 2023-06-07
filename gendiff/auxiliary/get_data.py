import json
from yaml import load
from yaml.loader import SafeLoader


def get_data(file_format: str, file_path: str) -> dict:
    if file_format == '.json':
        return json.load(open(file_path))
    elif file_format in ['.yml', '.yaml']:
        return load(open(file_path), Loader=SafeLoader)
