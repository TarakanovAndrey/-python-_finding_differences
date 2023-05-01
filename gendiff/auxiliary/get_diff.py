import copy


def get_diff(file_1, file_2):
    def walk(dictionary1, dictionary2, acc_keys, list_of_differences):
        keys = sorted(dictionary1.keys() | dictionary2.keys())
        temp_result = {}
        for key in keys:
            acc_keys.append(key)
            temp_result['path'] = copy.deepcopy(acc_keys)

            match key in dictionary1, key in dictionary2:
                case True, True if isinstance(dictionary1.get(key), dict) and isinstance(dictionary2.get(key), dict):
                    walk(dictionary1[key], dictionary2[key], acc_keys, list_of_differences)
                case True, True if dictionary1.get(key) == dictionary2.get(key):
                    temp_result['value'] = dictionary1[key]
                    temp_result['action'] = 'not changed'
                    list_of_differences.append(temp_result)
                case True, True if dictionary1.get(key) != dictionary2.get(key):
                    temp_result['value'] = {'before_changes': dictionary1[key], 'after_changes': dictionary2[key]}
                    temp_result['action'] = 'changed'
                    list_of_differences.append(temp_result)
                case False, True:
                    temp_result['value'] = dictionary2[key]
                    temp_result['action'] = 'added'
                    list_of_differences.append(temp_result)
                case True, False:
                    temp_result['value'] = dictionary1[key]
                    temp_result['action'] = 'deleted'
                    list_of_differences.append(temp_result)
            temp_result = dict()
            del acc_keys[-1]

        return list_of_differences
    return walk(file_1, file_2, [], [])
