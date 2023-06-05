import copy


DESCRIPTION = {'True': 'true', 'False': 'false', 'None': 'null'}


def get_right_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif str(value) in DESCRIPTION.keys():
        return DESCRIPTION[str(value)]
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return f"'{value}'"


def get_plain(diff, path=None, lines=None, depth=0):
    if path is None:
        path = list()

    match diff['type']:
        case 'root':
            lines = map(lambda child: get_plain(child, path, lines, depth + 1), diff['children'])
        case 'nested':
            path.append(diff['key'])
            path_copy = copy.deepcopy(path)
            lines = map(lambda child: get_plain(child, path_copy, lines, depth + 1), diff['children'])
        case 'added':
            path.append(diff['key'])
            path_copy = copy.deepcopy(path)
            path.pop()
            value = get_right_value(diff['value'])
            result = f"Property '{'.'.join(path_copy)}' was added with value: {value}"
            return result
        case 'deleted':
            path.append(diff['key'])
            path_copy = copy.deepcopy(path)
            path.pop()
            result = f"Property '{'.'.join(path_copy)}' was removed"
            return result
        case 'changed':
            path.append(diff['key'])
            path_copy = copy.deepcopy(path)
            path.pop()
            value_1 = get_right_value(diff['value']['before'])
            value_2 = get_right_value(diff['value']['after'])
            result = f"Property '{'.'.join(path_copy)}' was updated. From {value_1} to {value_2}"
            return result

    if depth == 1 or depth > 1 and diff['type'] == 'nested':
        path.pop()

    return '\n'.join(list(lines))
