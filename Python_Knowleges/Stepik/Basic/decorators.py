import time


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
