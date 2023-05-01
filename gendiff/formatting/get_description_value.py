import re

description = {"True": 'true', "False": 'false', 'None': 'null', ': ""\n': 'null'}


def get_description_value(output):
    for key in description:
        if key in output:
            output = re.sub(key, description[key], output)
        if key == "'null'":
            output = re.sub(key, 'null', output)
    return output
