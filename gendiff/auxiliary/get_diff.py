import copy
actions_list = []
path_storage = []


def get_diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    temp_result = dict()

    for key in keys:
        path_storage.append(key)
        temp_result['path'] = copy.deepcopy(path_storage)
        match key in dict1, key in dict2:
            case True, True if isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict):
                temp_result[key] = get_diff(dict1[key], dict2[key])
            case True, True if dict1.get(key) == dict2.get(key):
                temp_result['value'] = dict1[key]
                temp_result['action'] = 'not changed'
                actions_list.append(temp_result)
            case True, True if dict1.get(key) != dict2.get(key):
                temp_result['value'] = {'before_changes': dict1[key], 'after_changes': dict2[key]}
                temp_result['action'] = 'changed'
                actions_list.append(temp_result)
            case False, True:
                temp_result['value'] = dict2[key]
                temp_result['action'] = 'added'
                actions_list.append(temp_result)
            case True, False:
                temp_result['value'] = dict1[key]
                temp_result['action'] = 'deleted'
                actions_list.append(temp_result)
        temp_result = dict()
        del path_storage[-1]

    return actions_list
