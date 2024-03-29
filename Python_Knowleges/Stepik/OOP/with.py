"""
Когда мы открываем файловый поток, то при окончании работы с ним, его желательно закрыть, что делается с помощью метода
close(). При реализации этого с помощью try-except-finally, то получаем очень длинную конструкцию. Чтобы сократить код,
требуется использовать конструкцию with.
"""

try:
    with open('try_except.py', 'r', encoding='utf-8') as f:  # Менеджера контекста with закрывает файл в конце работы
        for line in f:                                       # с ним независимо от факта ошибки.
            print(line)
except FileExistsError as e:
    print(e)
except FileNotFoundError as e:
    print(e)

"""
Менеджер контекста (with) - это класс, в котором реализовано 2 магических метода:
__enter__() - срабатывает в момент создания объекта менеджера контекста;
__exit__() - срабатывает в момент завершения работы менеджера контекста или в момент исключения.
Создадим свой класс менеджера контекста, который будет менять значение вектора. Реализуем так, что если при изменении 
вектора произойдут какие-то ошибки, то мы не хотим вносить эти изменения в конечный результат.
"""


class DefenderVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # Копируем список (v1), чтобы далее менять копию списка, а не сам список.
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:  # Если exc_type is None - то никаких ошибок не произошло.
            self.__v[:] = self.__temp  # В этой строчке мы в уже существующий список (v1) копируем то, что у нас в итоге
                                       # хранит список __temp (результат работы операции цикла for i in enumerate(dv).
        return False  # Если метод __exit__ возвращает False, то исключение, которое возникнет внутри менеджера
        # контекста, обрабатываться не будут. А если вернётся True, то исключения, котороые возникли внутри менеджера
        # контекста, не выходят за его пределы, т.е. они обрабатываются внутри этого менеджера контекста.


v1 = [1, 2, 3]  # Вектор, который надо поменять.
v2 = [2, 3]  # Значения, на которые мы хотим поменять вектор.

try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]  # Тут возникнет исключение из-за несовпадения размеров.
except:
    print('Ошибка')

print(v1)  # По итогу список не поменялся, как мы того и хотели.

try:
    for i, a in enumerate(v1):
        v1[i] += v2[i]
except:
    print('Ошибка')

print(v1)  # Без применения менеджера контекста список изменился.
