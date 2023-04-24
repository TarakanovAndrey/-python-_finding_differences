import re
import json


def get_json_string_without_quotes_commas(dict_,):
    return re.sub('"', '', json.dumps(dict_, indent=2, separators=('', ': ')))


def generate_diff(first_file_path, second_file_path):

    file_1 = json.load(open(first_file_path))
    file_2 = json.load(open(second_file_path))

    keys = sorted(file_1.keys() | file_2.keys())
    dict_diff = dict()

    for key in keys:
        if key not in file_1:
            dict_diff[f'+ {key}'] = file_2[key]
        elif key not in file_2:
            dict_diff[f'- {key}'] = file_1[key]
        elif file_1[key] == file_2[key]:
            dict_diff[f'  {key}'] = file_1[key]
        elif file_1[key] != file_2[key]:
            dict_diff[f'- {key}'] = file_1[key]
            dict_diff[f'+ {key}'] = file_2[key]

    result = get_json_string_without_quotes_commas(dict_diff)
    return result
