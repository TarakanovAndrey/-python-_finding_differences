def get_diff(dict1: dict, dict2: dict, diff=None):
    if diff is None:
        diff: dict = {'type': 'root', 'children': []}
    keys = sorted(dict1.keys() | dict2.keys())
    for key in keys:
        match key in dict1, key in dict2:
            case True, True if isinstance(dict1.get(key), dict) & isinstance(dict2.get(key), dict):
                diff['children'].append({'key': key, 'type': 'nested', 'children': []})
                get_diff(dict1.get(key), dict2.get(key), diff['children'][-1])
            case True, True if dict1.get(key) == dict2.get(key):
                diff['children'].append({'key': key, 'type': 'unchanged', 'value': dict2.get(key)})
            case True, True if dict1.get(key) != dict2.get(key):
                diff['children'].append({'key': key, 'type': 'changed', 'value': {'before': dict1[key],
                                                                                  'after': dict2[key]}})
            case False, True:
                diff['children'].append({'key': key, 'type': 'added', 'value': dict2.get(key)})
            case True, False:
                diff['children'].append({'key': key, 'type': 'deleted', 'value': dict1.get(key)})
    return diff
