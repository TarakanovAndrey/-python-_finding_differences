import json
from yaml import load
from yaml.loader import SafeLoader
import os


def extract_data_from_file(file_path: str) -> dict:
    filename, file_extension = os.path.splitext(file_path)

    if file_extension == '.json':
        return json.load(open(file_path))
    elif file_extension in ['.yml', '.yaml']:
        return load(open(file_path), Loader=SafeLoader)
