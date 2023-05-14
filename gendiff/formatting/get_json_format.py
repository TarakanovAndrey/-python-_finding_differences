import json


def get_json_format_for_output(items):
    return json.dumps(items, indent=1)
