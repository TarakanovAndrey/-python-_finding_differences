import copy

# def get_right_value_format(value):
#     if isinstance(value, dict):
#         return '[complex value]'
#     elif not isinstance(value, (bool, int, type(None))):
#         return f"'{value}'"
#     return value
#
#
# def get_action_changed(path: list, value):
#     value_before = get_right_value_format(value['before'])
#     value_after = get_right_value_format(value['after'])
#     return f"Property '{'.'.join(path)}' was updated. From {value_before} to {value_after}"
#
#
# def get_action_added(path: list, value):
#     need_value = get_right_value_format(value)
#     return f"Property '{'.'.join(path)}' was added with value: {need_value}"
#
#
# def get_action_deleted(path: list):
#     return f"Property '{'.'.join(path)}' was removed"
#
#
# def get_plain(diff: dict, storage=None):
#     if storage is None:
#         storage = {'path': [], 'result': []}
#     for dict_ in diff:
#         feature = dict_['type']
#         storage['path'].append(dict_['key'])
#         match feature:
#             case 'nested':
#                 get_plain(dict_['children'], storage)
#             case 'added':
#                 storage['result'].append(get_action_added(storage['path'], dict_['value']))
#                 del storage['path'][-1]
#             case 'changed':
#                 storage['result'].append(get_action_changed(storage['path'], dict_['value']))
#                 del storage['path'][-1]
#             case 'deleted':
#                 storage['result'].append(get_action_deleted(storage['path']))
#                 del storage['path'][-1]
#             case 'unchanged':
#                 del storage['path'][-1]
#     if storage['path']:
#         del storage['path'][-1]
#     return '\n'.join(storage['result'])


def check_value(value):
    description = {'True': 'true', 'False': 'false', 'None': 'null'}
    if value in description.keys():
        return description[value]
    else:
        return f"'{value}'"


def get_right_value(value):
    if not isinstance(value, dict):
        return check_value(str(value))
    elif isinstance(value, dict):
        return "[complex value]"


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
