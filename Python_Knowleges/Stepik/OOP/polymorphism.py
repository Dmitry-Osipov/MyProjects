"""
Полиморфизм - это возможность работы с совершенно разными объектами языка Python единым образом. Т.е. через единый
интерфейс.
"""


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_rect_pr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4 * self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)

# Представим, что мы хотим представить все эти объекты в виде одного списка.
geom = [r1, r2, s1, s2]
for g in geom:
    print(g.get_rect_pr())  # При выборе функции видим 2 разных метода для прямоугольника и для квадрата.
    # Ожидаемо получаем ошибку AttributeError: 'Square' object has no attribute 'get_rect_pr'

# Но как можно решить нашу проблему? Можно решить в лоб:
geom = [r1, r2, s1, s2]
for g in geom:
    if isinstance(g, Rectangle):
        print(g.get_rect_pr())
    else:
        print(g.get_sq_pr())

# Это не лучшая реализация. Представим, что в нашей программе добавляется ещё один графический примитив: треугольник:


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_rect_pr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_tr_pr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)
geom = [r1, r2, s1, s2, t1, t2]

for g in geom:
    if isinstance(g, Rectangle):
        print(g.get_rect_pr())
    else:
        print(g.get_sq_pr())  # Снова получили ошибку # AttributeError, ибо у треугольника такого метода нет.
"""
В итоге наша программа получается корявой. В ней нет ни красоты, ни гибкости. И чтобы получить красоту и гибкость,
требуется применить полиморфизм. Как это сделать? Договоримся, что в каждом классе функция для получения периметра 
будет называться одинаково. Пусть будет get_pr().
"""


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)
geom = [r1, r2, s1, s2, t1, t2]

for g in geom:
    print(g.get_pr())
"""
Теперь можем убрать все проверки. Это будет логично, ибо каждая ссылка списка ведёт на свой объект. Соответственно,
вызывая метод get_pr() мы вызываем этот метод у соответствующего объекта соответствующего класса, потому и ошибок нет. 
Это и есть пример полиморфизма - когда к разным объектам мы обращаемся через единый интерфейс.
Более того, формирование списка geom в этой программе можно улучшить.
"""

geom = [Rectangle(1, 2), Rectangle(3, 4), Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)]

for g in geom:
    print(g.get_pr())

"""
Так программа выглядит приятнее и читаемее. Но даже в таком варианте есть недостатки в нашей программе. Что если в одном 
из классов мы забудем реализовать один из геттеров? Снова вылетит ошибка AttributeError. Как можно поправить этот 
момент, что даже если мы забыли определить метод, то программа бы работала? Один из способов - это создать базовый класс
для всех графически примитивов и внутри базового класса определить метод get_pr(): 
"""


class Geom:
    def get_pr(self):
        return -1


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


geom = [Rectangle(1, 2), Rectangle(3, 4), Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)]

for g in geom:
    print(g.get_pr())  # Для треугольников по умолчанию вывело -1

"""
Однако и это не самое лучшее решение! Нам всё же хочется, чтобы каждый дочерний класс имел бы обязательную реализацию 
метода get_pr(). Как это сделать? Один из рекомендуемых способов - это добавить в метод get_pr() генерацию специального 
исключения NotImplementedError. Таким образом, теперь мы знаем, с чем связано такое исключение, и не нужно будет долго 
выискивать причину ошибки.
"""


class Geom:
    def get_pr(self):
        raise NotImplementedError('В дочернем классе должен быть переопределён метод get_pr()')


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


geom = [Rectangle(1, 2), Rectangle(3, 4), Square(10), Square(20),
        Triangle(1, 2, 3), Triangle(4, 5, 6)]

for g in geom:
    print(g.get_pr())  # NotImplementedError('В дочернем классе должен быть переопределён метод get_pr()')

"""
В языках программирования методы, которые обязательно нужно переопределять в дочерних классах и которые не имеют своей 
собственной реализации, называются абстрактами. Конечно, в Python нет чисто абстрактных методов, здесь мы лишь выполняем 
имитацию их поведения, заставляя программиста переопределять метод get_pr() в дочерних классах, самостоятельно генерируя 
исключение NotImplementedError
"""
