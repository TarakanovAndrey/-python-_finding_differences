from gendiff.auxiliary.get_format import get_format
from gendiff.auxiliary.get_data import get_data


def extract_data_from_file(file_path: str) -> dict:
    file_format = get_format(file_path)
    data = get_data(file_format, file_path)
    return data
