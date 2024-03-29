"""
__getitem__(self, item) - получение значения по ключу item.
__setitem__(self, key, value) - запись значения value по ключу key.
__delitem__(self, key) - удаление элемента по ключу key.
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):  # Ключ, который прописываем (например, 2), передаётся в параметр item.
        if 0 <= item < len(self.marks):  # Внутри можно прописывать свои проверки, что даёт дополнительные удобства.
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):  # Ключом является индекс списка (например, 2), значением - присваиваемая
                                        # перменная (например, 4).
        if not isinstance(key, int) or key < 0:  # Конечно, для списка можно использовать отрицательные индексы, но для
                                                 # простоты обучения опустим это.
            raise TypeError('Индекс должен быть целым неотрицательным числом')

        if key >= len(self.marks):
            temp = key + 1 - len(self.marks)  # Создаём временную переменную.
            self.marks.extend([None] * temp)  # Расширяем список значениями None в количестве temp.

        self.marks[key] = value

    def __delitem__(self, key):  # Вызывается, когда происходит удаление элемента.
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')

        del self.marks[key]


s1 = Student('Dima', [5, 5, 3, 2, 5])
print(s1.marks[2])  # Получаем ожидаемый вывод элемента коллекции. Но что если бы мы хотели сделать то же самое, но
# с таким синтаксисом:
print(s1[2])  # Очевидно, что без объявления магических методов работать ничего не будет. Сначала надо определить
# __getitem__, который позволит через квадратные скобки вернуть определённые значения. Соответственно, указав
# несуществующий индекс, получим ошибку IndexError.

# Предположим, мы хотим менять оценки студентов, используя такой же индекс:
s1[2] = 4  # - без реализации магического метода __setitem__ получаем ошибку TypeError.
print(s1.marks)

# Предположим, мы запишем индекс, превышающий размер списка:
s1[10] = 3  # Вполне ожидаемо, получаем ошибку IndexError. Для этого скорректируем __setitem__.
print(s1.marks)  # Первые элементы уже существовали, далее мы расширяем список с помощью метода extend(), а последним
# элементом списка является наше передаваемое значение.

del s1[5]  # Был удалён элемент с индексом 5 (значением было None).
print(s1.marks)
