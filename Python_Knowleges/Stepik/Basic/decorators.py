import time
import math
from functools import wraps


def func_decorator(func):
    def wrapper():
        print('--------------- Что-то делаем перед вызовом функции ---------------')
        func()
        print('--------------- Что-то делаем после вызова функции ---------------')

    return wrapper


def some_func():
    print('Вызов функции some_func')


some_func()  # Вызов функции some_func


@func_decorator  # Это самый простой способ использовать декоратор, но есть такой - f = func_decorator(some_func) -> f()
def some_func():
    print('Вызов функции some_func')


some_func()  # А вот теперь мы дополнили функционал декоратором:
# --------------- Что-то делаем перед вызовом функции ---------------
# Вызов функции some_func
# --------------- Что-то делаем после вызова функции ---------------

"""
Однако проблема в том, что если передать функции some_func хотя бы 1 аргумент, то выбросится исключение. Преобразуем 
программу с использованием *args и **kwargs:
"""


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print('--------------- Что-то делаем перед вызовом функции ---------------')
        res = func(*args, **kwargs)  # Переменная нам необходима, чтобы возвращать значения (иначе если func возвращает
        # что-то, то мы этого не получим)
        print('--------------- Что-то делаем после вызова функции ---------------')
        return res

    return wrapper


@func_decorator
def some_func(title, tag):
    print(f'title = <{tag}>{title}</{tag}>')
    return f'title = <{tag}>{title}</{tag}>'


print(some_func('Python навсегда', 'h1'))

"""
Допустим, мы хотим протестировать различные функции на скорость их работы:
"""


def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f'Время работы функции: {dt} сек.')
        return res

    return wrapper


@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a

    while b:
        a, b = b, a % b

    return a


print(get_nod(2, 10000000))
print(get_fast_nod(2, 10000000))


# Декораторы функций с параметрами:
def func_decorator(func):
    def wrapper(x, *args, **kwargs):
        dx = 0.001
        res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
        return res
    return wrapper


@func_decorator
def sin_df(x):
    return math.sin(x)


df = sin_df(math.pi / 3)
print(df)

"""
Результат получен, но мы хотим передавать dx в аргумент декоратора, чтобы dx можно было бы изменить. Для этого нам 
требуется дополнительно описать ещё одну функцию, а оставшиеся вложить в неё:
"""


def df_decorator(dx=0.01):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper
    return func_decorator


@df_decorator(dx=0.00001)
def sin_df(x):
    return math.sin(x)


df = sin_df(math.pi / 3)
print(df)  # Всё отработало, точность по итогу получили больше.


"""
Единственная проблема возникает при получении имени функции. Без декоратора имя функции sin_df (sin_df.__name__) таким и 
останется, а вот с декоратором будет уже wrapper. Исправим описание и имя функции:
"""


def df_decorator(dx=0.01):
    def func_decorator(func):
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        wrapper.__name__ = func.__name__  # Теперь имя декорированной функции останется нетронутым.
        wrapper.__doc__ = func.__doc__  # Теперь описание декорированной функции останется нетронутым.
        return wrapper
    return func_decorator


@df_decorator(dx=0.00001)
def sin_df(x):
    """Функция для вычисления производной синуса"""
    return math.sin(x)


print(sin_df.__name__)
print(sin_df.__doc__)


"""
Выше написанное является базовыми задачами. Соответственно, они уже вшиты в сам язык. Импортируем wraps и преобразуем код:
"""


def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)  # В декоратор передали ссылку на функцию, соответственно, всё сохранилось.
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        return wrapper
    return func_decorator


@df_decorator(dx=0.00001)
def sin_df(x):
    """Функция для вычисления производной синуса"""
    return math.sin(x)


print(sin_df.__name__)
print(sin_df.__doc__)
