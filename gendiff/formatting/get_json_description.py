import re

description = {"True": 'true', "False": 'false', 'None': 'null', ': \n': ':\n'}


def get_json_description(output):
    for key in description:
        if key in output:
            output = re.sub(key, description[key], output)

    return output
