import time
from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in cache:
                value, ts = cache[key]
                if now - ts < 30:
                    print("Из кэша")
                    return value
                else:
                    cache.pop(key)
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        except TypeError:
            return NotImplemented

    def clear_cache():
        cache.clear()

    wrapper.clear_cache = clear_cache
    return wrapper
