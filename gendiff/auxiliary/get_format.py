import os


def get_format(path: str) -> str:
    _, file_format = os.path.splitext(path)
    return file_format
