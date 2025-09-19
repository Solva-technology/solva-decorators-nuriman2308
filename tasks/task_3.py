from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for num in list(args) + list(kwargs.values()):
            if isinstance(num, int):
                if num <= 0:
                    raise ValueError(f"Все аргументы должны быть положительными. {num}")
            else:
                raise TypeError(f"Аргументы {num} должен быть целым числом.")
        return func(*args, **kwargs)
    return wrapper
