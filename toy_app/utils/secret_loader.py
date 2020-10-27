import os


def load_secret(path: str):
    """
    Function that simply read as text the file in the given `path` and return it as string.
    It is useful for loading secrets files provided by orchestrators.

    :param str path: Path where to look for the secret file
    :return str: Text content in read from the given path
    """
    secret = None
    with open(path, "rt") as fp:
        secret = fp.read()
    return secret
