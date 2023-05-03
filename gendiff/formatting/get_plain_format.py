from gendiff.formatting.get_description_value import get_description_value


def get_action_changed(path, value):
    value_before = value['before_changes']
    value_after = value['after_changes']
    value_before_is_dict = isinstance(value_before, dict)
    value_after_is_dict = isinstance(value_after, dict)
    is_type_before_value = isinstance(value_before, (bool, int, type(None)))
    is_type_after_value = isinstance(value_after, (bool, int, type(None)))

    match value_before_is_dict, value_after_is_dict, is_type_before_value, is_type_after_value:
        # case True, True, False, False:
        #     value_before = '[complex value]'
        #     value_after = '[complex value]'
        case True, False, False, False:
            value_before = '[complex value]'
            value_after = f"'{value_after}'"
        case True, False, False, True:
            value_before = '[complex value]'
        case False, True, False, False:
            value_before = f"'{value_before}'"
            value_after = '[complex value]'
        case False, True, True, False:
            value_after = '[complex value]'
        case False, False, False, False:
            value_before = f"'{value_before}'"
            value_after = f"'{value_after}'"
        case False, False, True, False:
            value_after = f"'{value_after}'"
        case False, False, False, True:
            value_before = f"'{value_before}'"
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
