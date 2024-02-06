import sys
from module import log
from functools import wraps


def tryFunction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            log.error(*sys.exc_info())
    return wrapper