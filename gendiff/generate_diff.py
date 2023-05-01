from gendiff.auxiliary.extract_data import extract_data_from_file
from gendiff.auxiliary.get_diff import get_diff
from gendiff.formatting.get_nested_format import get_nested_format_for_output
from gendiff.formatting.get_plain_format import get_plain
from gendiff.formatting.get_json_format import get_json_format_for_output


def generate_diff(path_file1, path_file2, format_style='stylish'):
    data_file1, data_file2 = extract_data_from_file(path_file1, path_file2)
    diff = get_diff(data_file1, data_file2)
    match format_style:
        case 'plain':
            return get_plain(diff)
        case 'json':
            return get_json_format_for_output(diff)
        case _:
            return get_nested_format_for_output(diff)
