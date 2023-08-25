class Point:
    color = 'red'
    circle = 2

    def set_coords():
        print('Вызов метода set_coords')


"""Класс может содержать свойства (данные) либо методы (действия), благодаря методам внутри класса можно реализовывать
самые разные алгоритмы. Т.е. методы - это действия, поэтому в названиях методов используют глаголы. А именами свойств
выступает существительное."""

print(Point.set_coords)
Point.set_coords()

pt = Point()
print(pt.set_coords)
pt.set_coords()
"""Выйдет ошибка, ибо мы в классе Point в функции set_coords не прописали self, а при создании pt этот параметр
передаётся автоматически."""


class Point:
    color = 'red'
    circle = 2

    def set_coords(self):
        print('Вызов метода set_coords' + str(self))


pt = Point()
print(pt.set_coords)
pt.set_coords()
"""Теперь всё работает, однако при вызове Point.set_coords(), выдаст ошибку, ибо мы не передали параметр, однако можно
передать в параметрах pt, тогда всё будет работать."""

Point.set_coords(pt)


class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y


"""Параметр self используется, чтобы мы могли работать с атрибутами локального экземпляра класса."""

pt = Point()
pt.set_coords(1, 2)
print(pt.__dict__)
"""В экземпляре класса pt через self были добавлены свойства со значением x = 1 и y = 2."""

pt2 = Point()
pt2.set_coords(10, 20)
print(pt2.__dict__)
"""pt и pt2 работают независимо друг от друга благодаря параметру self."""


class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point()
pt.set_coords(1, 2)
f = getattr(pt, 'get_coords')
print(f())
"""Т.к. функция тоже является атрибутом, то её можно вызвать через метод getattr. Однако обычно используется 
синтаксис через точку - pt.get_coords()""".
