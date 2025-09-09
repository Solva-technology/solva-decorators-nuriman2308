# ЗАДАНИЕ 2: Кэширование результатов
# Напиши декоратор simple_cache, который:
# - запоминает результат функции при вызове с конкретными аргументами,
# - при повторном вызове с теми же аргументами — возвращает сохранённый результат без повторного вычисления,
# - печатает "Из кэша" при использовании кэшированного значения.
# Подсказка: используй словарь для хранения результатов.

from functools import wraps


def simple_cache(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache.keys():
            print("Из кэша")
            return cache[*args]
        else:
            cache[*args] = func(*args)
            return cache[*args]
    return wrapper

@simple_cache
def add(a, b):
    return a + b
