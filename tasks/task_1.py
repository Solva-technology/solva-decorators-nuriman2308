from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов: {func.__name__}{args}{kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"Результат: {result}")
            return result
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
    return wrapper
