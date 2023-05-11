from gendiff.formatting.stylish import get_nested_format_for_output
from gendiff.formatting.get_plain_format import get_plain
from gendiff.formatting.get_json_format import get_json_format_for_output


def return_format(diff, format_style):
    match format_style:
        case 'plain':
            return get_plain(diff)
        case 'json':
            return get_json_format_for_output(diff)
        case _:
            return get_nested_format_for_output(diff)
