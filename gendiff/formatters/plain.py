import copy


def get_right_value(value):
    description = {'True': 'true', 'False': 'false', 'None': 'null'}
    if isinstance(value, dict):
        return "[complex value]"
    else:
        if str(value) in description.keys():
            return description[str(value)]
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
            value = get_right_value(diff['value'])
            result = f"Property '{'.'.join(path_copy)}' was added with value: {value}"
            path.pop()
            return result
        case 'deleted':
            path.append(diff['key'])
            path_copy = copy.deepcopy(path)
            result = f"Property '{'.'.join(path_copy)}' was removed"
            path.pop()
            return result
        case 'changed':
            path.append(diff['key'])
            value_1 = get_right_value(diff['value']['before'])
            value_2 = get_right_value(diff['value']['after'])
            path_copy = copy.deepcopy(path)
            path.pop()
            result = f"Property '{'.'.join(path_copy)}' was updated. From {value_1} to {value_2}"
            return result
    if path and depth == 1:
        path.pop()
    elif depth > 1 and diff['type'] == 'nested':
        path.pop()
    return '\n'.join(list(lines))
