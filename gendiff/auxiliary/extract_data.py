import json
from yaml import load
from yaml.loader import SafeLoader
import os


def extract_data_from_file(first_file_path, second_file_path):
    filename_1, file_extension_1 = os.path.splitext(first_file_path)
    filename_2, file_extension_2 = os.path.splitext(second_file_path)

    if file_extension_1 == '.json' and file_extension_2 == '.json':
        data_file_1 = json.load(open(first_file_path))
        data_file_2 = json.load(open(second_file_path))
        return data_file_1, data_file_2
    elif file_extension_1 in ['.yml', '.yaml'] and file_extension_2 in ['.yml', '.yaml']:
        data_file_1 = load(open(first_file_path), Loader=SafeLoader)
        data_file_2 = load(open(second_file_path), Loader=SafeLoader)
        return data_file_1, data_file_2
