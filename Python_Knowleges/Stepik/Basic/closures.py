def say_name(name):
    def say_goodbye():
        return "Don't say me goodbye, " + str(name) + "!"

    return say_goodbye()


f = say_name('Dmitry')
print(f)

"""
Ссылка на say_goodbye не пропадает потому что:
f -> say_goodbye -> say_name(name='Dmitry') -> myprog -
^                                                      |
|                                                      |
 ------------------------------------------------------

Все эти окружения не пропадают, ибо ссылка f их как бы держит. Соответственно, функция say_goodbye может обращаться к 
глобальной переменной имени функции say_name.

Такой эффект, когда мы держим локальные окружения и имеем возможность продолжать использовать переменные из внешних 
окружений (например, say_name), называется замыканием. Замыкания в том смысле, что мы держим окружения как бы по цепочке
(см. выше зарисовку). 

Кроме того, каждый раз будет создаваться своё независимое локальное окружение при вызове функции (т.е. при создании f и 
f2, f != f2):
"""

f2 = say_name('Sergey')
print(f, f2)  # Получили 2 разные строчки.

"""
Создадим функцию-счётчик, которая при каждом новом запуске увеличивает своё значение на единицу:
"""


def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = counter(10)
c2 = counter()
print(c1(), c2())  # 11 1
print(c1(), c2())  # 12 2
print(c1(), c2())  # 13 3

"""
Создадим функцию, которая удалит ненужные символы в начале и конце строки:
"""


def strip_string(strip_chars=" "):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


strip1 = strip_string()
strip2 = strip_string(' !?,.;')

print(strip1(' hello python!.. '))  # Удалили только пробелы.
print(strip2(' hello python!.. '))  # Удалили и указанные символы.
