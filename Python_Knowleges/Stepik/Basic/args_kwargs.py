def os_path(*args):  # Чтобы передать произвольное число параметров, требуется передать аргументом *args.
    print(args)  # При распечатывании коллекции args мы увидим кортеж.


os_path('F:/~stepik.org', 'Добрый, добрый Python (Питон)', '39/р39. Функции.docx')


def os_path(*args):
    path = '/'.join(args)
    return path


p = os_path('F:/~stepik.org', 'Добрый, добрый Python (Питон)', '39/р39. Функции.docx')
print(p)

"""
Задачу с произвольным числом позиционных аргументов решили. Но если мы постараемся передать именованные? Нам выбросит 
исключение. Тогда нам надо их заранее создавать. Однако если мы не знаем количество и названия поступающих именованных 
аргументов, то следует воспользоваться **kwargs.
"""


def os_path(*args, **kwargs):
    # print(kwargs)  # При распечатывании видим словарь, где ключи это аргументы, а значения - значение аргумента.
    path = kwargs['sep'].join(args)
    return path


p = os_path('F:/~stepik.org', 'Добрый, добрый Python (Питон)', '39/р39. Функции.docx', sep='+', trim=True)
print(p)

"""
Всё отработало, но если убрать sep, то вылетит исключение из словаря. Если требуется указать именно sep, то можно 
передать ему именованным аргументом sep=?, а затем он перезапишется, если в kwargs будет sep. Важно заметить, что 
необходимые формальные параметры должны идти перед **kwargs в аргументах функции. 
"""


def os_path(*args, sep='/', **kwargs):
    path = sep.join(args)
    return path


p = os_path('F:/~stepik.org', 'Добрый, добрый Python (Питон)', '39/р39. Функции.docx', trim=True)
print(p)

p = os_path('F:/~stepik.org', 'Добрый, добрый Python (Питон)', '39/р39. Функции.docx', sep='+', trim=True)
print(p)

"""
Аналогично должны идти сначала позиционные аргументы наши, а затем уже оставшиеся мы засунем в коллекцию args:
"""


def os_path(disk, *args, sep='/', **kwargs):
    args = (disk, ) + args
    path = sep.join(args)
    return path


p = os_path('F:', '~stepik.org', 'Добрый, добрый Python (Питон)', '39/р39. Функции.docx', sep='+', trim=True)
print(p)

"""
Пропишем функцию таким образом, чтобы она удаляла пробелы в маршруте между разделителями, используя kwargs:
"""


def os_path(disk, *args, sep='/', **kwargs):
    args = (disk, ) + args
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]

    path = sep.join(args)
    return path


p = os_path('F:', '~stepik.org ', ' Добрый, добрый Python (Питон) ', ' 39/р39. Функции.docx')
print(p)

p = os_path('F:', '~stepik.org ', ' Добрый, добрый Python (Питон) ', ' 39/р39. Функции.docx', sep='+', trim=True)
print(p)
