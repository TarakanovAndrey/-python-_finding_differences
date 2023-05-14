from gendiff.formatting.get_description_value import get_description_value


def get_right_value_format(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif not isinstance(value, (bool, int, type(None))):
        return f"'{value}'"
    return value


def get_action_changed(path, value):
    value_before = get_right_value_format(value['before'])
    value_after = get_right_value_format(value['after'])
    return f"Property '{'.'.join(path)}' was updated. From {value_before} to {value_after}"


def get_action_added(path, value):
    need_value = get_right_value_format(value)
    return f"Property '{'.'.join(path)}' was added with value: {need_value}"


def get_action_deleted(path):
    return f"Property '{'.'.join(path)}' was removed"


def get_plain(diff, storage=None):
    if storage is None:
        storage = {'path': [], 'result': []}
    for dict_ in diff:
        feature = dict_['type']
        storage['path'].append(dict_['key'])
        match feature:
            case 'nested':
                get_plain(dict_['children'], storage)
            case 'added':
                storage['result'].append(get_action_added(storage['path'], dict_['value']))
                del storage['path'][-1]
            case 'changed':
                storage['result'].append(get_action_changed(storage['path'], dict_['value']))
                del storage['path'][-1]
            case 'deleted':
                storage['result'].append(get_action_deleted(storage['path']))
                del storage['path'][-1]
            case 'unchanged':
                del storage['path'][-1]
    if storage['path']:
        del storage['path'][-1]
    return get_description_value('\n'.join(storage['result']))
