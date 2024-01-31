from module import log
from functools import wraps

class tryFunction(object):
    def __init__(self, func):
        self.func = func
        pass
    def __call__(self, *args, **kwargs):
        @wraps(self.func)
        def wrapped_function(*args, **kwargs):
            try:
                return self.func(*args, **kwargs)
            except Exception:
                log.error(Exception)
        return wrapped_function