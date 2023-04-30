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
                descriptions = {'True': 'True', 'False': 'False', 'None': 'None'}
                if isinstance(value, dict):
                    value = str('[complex value]')
                elif str(value) in descriptions:
                    value = descriptions[str(value)]
                else:
                    value = f"'{value}'"
                result.append(f"Property '{path}' was added with value: {value}")
            case 'changed':
                value_before = value['before_changes']
                value_after = value['after_changes']
                descriptions = {'True': 'True', 'False': 'False', 'None': 'None'}
                if str(value_before) in descriptions:
                    value_before = descriptions[str(value_before)]
                if str(value_after) in descriptions:
                    value_after = descriptions[str(value_after)]
                elif isinstance(value_before and value_after, dict):
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
    return '\n'.join(result)
