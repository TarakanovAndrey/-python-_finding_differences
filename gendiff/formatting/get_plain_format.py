from gendiff.formatting.get_description_value import get_description_value


def get_right_value_format(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif not isinstance(value, (bool, int, type(None))):
        return f"'{value}'"
    return value


def get_action_changed(path, value):
    value_before = get_right_value_format(value['before_changes'])
    value_after = get_right_value_format(value['after_changes'])
    return f"Property '{path}' was updated. From {value_before} to {value_after}"


def get_action_added(path, value):
    if isinstance(value, dict):
        value = '[complex value]'
    elif value not in [False, True, None] and not isinstance(value, int):
        value = f"'{value}'"
    return f"Property '{path}' was added with value: {value}"


def get_action_deleted(path):
    return f"Property '{path}' was removed"


def get_plain(output):
    result = []
    for item in output:
        path = '.'.join(item['path'])
        action = item['action']
        value = item['value']
        match action:
            case 'changed':
                result.append(get_action_changed(path, value))
            case 'added':
                result.append(get_action_added(path, value))
            case 'deleted':
                result.append(get_action_deleted(path))

    join_result = '\n'.join(result)
    return get_description_value(join_result)
