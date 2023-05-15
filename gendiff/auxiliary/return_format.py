from gendiff.formatting.stylish import get_stylish_format
from gendiff.formatting.get_plain_format import get_plain
from gendiff.formatting.get_json_format import get_json_format_for_output


def return_format(diff: dict, format_style: str):
    root_children: dict = diff['children']
    match format_style:
        case 'plain':
            return get_plain(root_children)
        case 'json':
            return get_json_format_for_output(diff)
        case _:
            return get_stylish_format(root_children)
