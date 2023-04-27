import json
import yaml
from yaml.loader import SafeLoader
import os


def extract_data_from_file(first_file_path, second_file_path):
    filename_1, file_extension_1 = os.path.splitext(first_file_path)
    filename_2, file_extension_2 = os.path.splitext(second_file_path)

    if file_extension_1 == '.json' and file_extension_2 == '.json':
        data_file_1 = json.load(open(first_file_path))
        data_file_2 = json.load(open(second_file_path))
    elif file_extension_1 in ['.yml', '.yaml'] and file_extension_2 in ['.yml', '.yaml']:
        data_file_1 = yaml.load(open(first_file_path), Loader=SafeLoader)
        data_file_2 = yaml.load(open(second_file_path), Loader=SafeLoader)

    return data_file_1, data_file_2


def generate_diff(first_file_path, second_file_path):
    file_1, file_2 = extract_data_from_file(first_file_path, second_file_path)

    keys = sorted(file_1.keys() | file_2.keys())
    result = '{\n'
    for key in keys:
        if key not in file_1:
            result += f'  + {key}: {file_2[key]}\n'
        elif key not in file_2:
            result += f'  - {key}: {file_1[key]}\n'
        elif file_1[key] == file_2[key]:
            result += f'    {key}: {file_1[key]}\n'
        elif file_1[key] != file_2[key]:
            result += f'  - {key}: {file_1[key]}\n'
            result += f'  + {key}: {file_2[key]}\n'

    return result + '}'
