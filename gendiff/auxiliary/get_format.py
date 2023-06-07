import os


def get_format(path):
    _, file_format = os.path.splitext(path)
    return file_format
