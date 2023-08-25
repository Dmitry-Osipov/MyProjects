"""
Идея моно состояния:
Представим, что есть некий многопоточный процесс, и в каждом потоке создаётся свой экземпляр класса ThreadData. Но нам
нужно, чтобы все экземпляры имели единые локальные свойства (например, name, data, id). Едиными в том смысле, чтобы они
были одинаковыми для всех экземпляров класса и изменение любого из них внутри какого-либо экземпляра отражалось бы и
в других экземплярах. Это и есть паттерн Моно состояния.
"""


class ThreadData:
    __shared_attrs = {  # Это и будет словарь с общими локальными свойствами экземпляров этого класса.
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs
        # Когда мы будем создавать новый экземпляр класса, то у нас коллекция __dict__ будет ссылаться на нами
        # созданный словарь, и в итоге мы ожидаем, что у объектов класса будут общие свойства.


th1 = ThreadData()
th2 = ThreadData()
print(th1.__dict__)
print(th2.__dict__)
th2.id = 3
print(th1.__dict__)
print(th2.__dict__)
th1.attr_new = 'new attr'
print(th1.__dict__)
print(th2.__dict__)
# Мы получили ожидаемый вывод, который был описан в начале. Локальное пространство имён едино для любого количества
# объектов данного класса
