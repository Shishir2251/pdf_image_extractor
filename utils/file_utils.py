import os


def get_file_extension(path: str) -> str:
    return os.path.splitext(path)[1].lower()
