import itertools
import copy
from gendiff.formatting.get_description_value import get_description_value


def prepared_data(items_original):
    items = copy.deepcopy(items_original)
    acc_dicts = []
    for item in items:
        path = item['path']
        action = item['action']
        match action:
            case 'added':
                path[-1] = f'+ {path[-1]}'
                del item['action']
                acc_dicts.append(item)
            case 'deleted':
                path[-1] = f'- {path[-1]}'
                del item['action']
                acc_dicts.append(item)
            case 'not changed':
                path[-1] = f'  {path[-1]}'
                del item['action']
                acc_dicts.append(item)
            case 'changed':
                item_before = copy.deepcopy(item)
                item_before['path'][-1] = f"- {item_before['path'][-1]}"
                item_before['value'] = item_before['value']['before_changes']
                del item_before['action']
                acc_dicts.append(item_before)
                item_after = copy.deepcopy(item)
                item_after['path'][-1] = f"+ {item_after['path'][-1]}"
                item_after['value'] = item_after['value']['after_changes']
                del item_after['action']
                acc_dicts.append(item_after)
    return acc_dicts


def get_dict(items):
    dicts = []
    for item in items:
        path = item['path']
        value = item['value']
        for key in path[::-1]:
            result = {key: value}
            value = result
        dicts.append(value)
    return dicts


def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(value, dict):
                merge_dicts(dict1[key], value)
        else:
            dict1[key] = value


def get_nested_format(value):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        replacer = ' '
        spaces_count = 4
        deep_indent_size = depth + spaces_count
        lines = []
        for key, val in current_value.items():
            if str(key)[0] in ['+', '-', ' ']:
                deep_indent = replacer * (deep_indent_size - 2)
                lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
            else:
                deep_indent = replacer * deep_indent_size
                lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')

        output = itertools.chain("{", lines, [replacer * depth + "}"])
        return '\n'.join(output)

    return iter_(value, 0)


def get_nested_format_for_output(items):
    prepared_datas = prepared_data(items)
    list_dicts = get_dict(prepared_datas)
    combined_dict = list_dicts[0]
    for d in list_dicts[1:]:
        merge_dicts(combined_dict, d)
    nested_format = get_nested_format(combined_dict)
    return get_description_value(nested_format)
