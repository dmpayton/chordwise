import os

from . import conf


def asset(path):
    return os.path.join(conf.ASSETS_DIR, path)
