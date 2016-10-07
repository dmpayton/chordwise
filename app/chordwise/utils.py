import os
import random

from . import conf


def asset(path):
    return os.path.join(conf.ASSETS_DIR, path)


def random_cycle(iterable):
    iterable = list(iterable)
    previous, next = (None, None)
    while True:
        previous = next
        while True:
            next = random.choice(iterable)
            if next == previous:
                continue
            yield next
            break
