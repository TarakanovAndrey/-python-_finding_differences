from gendiff.formatting.get_description_value import get_description_value


def get_plain(output):
    result = []
    for item in output:
        path = '.'.join(item['path'])
        action = item['action']
        value = item['value']
        match action:
            case 'deleted':
                result.append(f"Property '{path}' was removed")
            case 'added':
                if isinstance(value, dict):
                    value = str('[complex value]')
                result.append(f"Property '{path}' was added with value: {value}")
            case 'changed':
                value_before = value['before_changes']
                value_after = value['after_changes']
                if isinstance(value_before and value_after, dict):
                    value_before = str('[complex value]')
                    value_after = str('[complex value]')
                elif isinstance(value_before, dict) and not isinstance(value_after, dict):
                    value_before = str('[complex value]')
                    value_after = f"'{value_after}'"
                elif not isinstance(value_before, dict) and isinstance(value_after, dict):
                    value_before = f"'{value_before}'"
                    value_after = str('[complex value]')
                elif not isinstance(value_before, dict) and not isinstance(value_after, dict):
                    value_before = f"'{value_before}'"
                    value_after = f"'{value_after}'"
                result.append(f"Property '{path}' was updated. From {value_before} to {value_after}")
    join_result = '\n'.join(result)
    return get_description_value(join_result)