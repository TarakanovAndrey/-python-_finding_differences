from gendiff.formatters.stylish import get_stylish_format
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json_format_for_output


def return_format(diff: dict, format_style: str):
    match format_style:
        case 'plain':
            return get_plain(diff)
        case 'json':
            return get_json_format_for_output(diff)
        case _:
            return get_stylish_format(diff)
