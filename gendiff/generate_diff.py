from gendiff.auxiliary.extract_data import extract_data_from_file
from gendiff.auxiliary.get_diff import get_diff
from gendiff.auxiliary.return_format import return_format


def generate_diff(path_file1, path_file2, format_style='stylish'):
    data_file1 = extract_data_from_file(path_file1)
    data_file2 = extract_data_from_file(path_file2)
    diff = get_diff(data_file1, data_file2)
    return return_format(diff, format_style)
