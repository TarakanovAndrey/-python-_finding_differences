from gendiff.formatting.stylish import get_stylish
from gendiff.formatting.get_plain_format import get_plain
from gendiff.formatting.get_json_format import get_json_format_for_output


def return_format(diff, format_style):
    match format_style:
        case 'plain':
            root_children = diff['children']
            return get_plain(root_children)
        case 'json':
            return get_json_format_for_output(diff)
        case _:
            return get_stylish(diff)
