import itertools


REPLACER = ' '
SPACES_COUNT = 4


def check_value(value):
    description = {'True': 'true', 'False': 'false', 'None': 'null'}
    if value in description.keys():
        return description[value]
    else:
        return value


def get_right_value(value, depth):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return check_value(str(current_value))
        deep_indent_size = depth + SPACES_COUNT
        lines = []
        for key, val in current_value.items():
            deep_indent = REPLACER * deep_indent_size
            lines.append(f'{deep_indent+"   "}{key}: {iter_(val, deep_indent_size)}')

        output = itertools.chain("{", lines, [REPLACER * (deep_indent_size - 1) + "}"])
        return '\n'.join(output)

    return iter_(value, depth)


def get_stylish_format(diff, depth=0, lines=None):
    deep_indent_size = depth + SPACES_COUNT

    match diff['type']:
        case 'root':
            lines = map(lambda child: get_stylish_format(child, depth), diff['children'])
        case 'nested':
            deep_indent = REPLACER * deep_indent_size
            lines = map(lambda child: get_stylish_format(child, deep_indent_size), diff['children'])
            result = '\n'.join(lines)
            return f"{deep_indent}{diff['key']}: {'{'}\n{result}\n{deep_indent}{'}'}"
        case 'added':
            deep_indent = REPLACER * (deep_indent_size - 2)
            key = diff['key']
            value = get_right_value(diff['value'], depth + 1)
            return f"{deep_indent}+ {key}: {value}"
        case 'unchanged':
            deep_indent = REPLACER * deep_indent_size
            key = diff['key']
            value = get_right_value(diff['value'], depth + 1)
            return f"{deep_indent}{key}: {value}"
        case 'deleted':
            deep_indent = REPLACER * (deep_indent_size - 2)
            key = diff['key']
            value = get_right_value(diff['value'], depth + 1)
            return f"{deep_indent}- {key}: {value}"
        case 'changed':
            deep_indent = REPLACER * (deep_indent_size - 2)
            key = diff['key']
            value_1 = get_right_value(diff['value']['before'], depth + 1)
            value_2 = get_right_value(diff['value']['after'], depth + 1)
            return f"{deep_indent}- {key}: {value_1}\n{deep_indent}+ {key}: {value_2}"

    return '{\n' + '\n'.join(list(lines)) + '\n}'
