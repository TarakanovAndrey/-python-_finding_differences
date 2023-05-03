import re


def get_description_value(output):
    description = {'True': 'true', 'False': 'false', 'None': 'null'}
    for key in description:
        if key in output:
            output = re.sub(key, description[key], output)
    return output
