from gendiff.extract_data import extract_data_from_file


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
