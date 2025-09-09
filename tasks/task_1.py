# ЗАДАНИЕ 1: Логирование вызова функции
# Напиши декоратор log, который:
# - печатает имя вызываемой функции и переданные ей аргументы,
# - затем вызывает оригинальную функцию,
# - после этого печатает возвращённый результат.
# Пример:
# >>> @log
# >>> def add(a, b): return a + b
# >>> add(2, 3)
# Вывод:
# Вызов: add(2, 3)
# Результат: 5

from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов: {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


@log
def add(a, b):
    return a + b
