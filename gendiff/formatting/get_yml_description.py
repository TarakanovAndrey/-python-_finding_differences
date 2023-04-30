import re

description = {"True": 'true', "False": 'false', 'None': '~', ': \n': ':\n'}


def get_yml_description(output):
    for key in description:
        if key in output:
            output = re.sub(key, description[key], output)

    return output
