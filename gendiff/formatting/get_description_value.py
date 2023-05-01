import re

description = {"True": 'true', "False": 'false', 'None': 'null', ': \n': ':\n', ': ""\n': 'null'}


def get_description_value(output):
    for key in description:
        if key in output:
            output = re.sub(key, description[key], output)

    return output
