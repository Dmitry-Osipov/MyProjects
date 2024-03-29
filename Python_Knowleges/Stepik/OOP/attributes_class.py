class Point:
    color = 'red'
    circle = 2


"""Переменные класса принято называть атрибутами или свойствами."""

print(Point.color)
Point.color = 'black'
"""Меняем значение атрибута color внутри класса Point."""

print(Point.color)
print(Point.__dict__)
"""Выводит коллекцию с атрибутами класса."""

New_point1 = Point()
New_point2 = Point()
print(New_point1, New_point2)
"""При присваивании переменных создаются 2 разных независимых объекта (в консоли выводится другой адрес объекта)."""

print(type(New_point1) == Point and type(New_point2) == Point)
"""Получаем True, ибо имя класса выступает в кач-ве типа данных."""

Point.circle = 1
print(New_point1.circle)
"""Значение внутри класса New_point поменялось, ибо New_point ссылается на атрибуты класса Point."""

print(New_point2.__dict__)
"""Получим пустой словарь, ибо у New_point нет атрибутов, New_point является пространством имён."""

New_point1.color = 'green'
print(New_point1.color, New_point2.color)
print(New_point1.__dict__)
"""Почему произошла замена цвета: 
       при обращении к New_point.color мы создаём переменную color в пространстве имён New_point."""

Point.type_pt = 'disk'
print(Point.__dict__)
"""Динамически добавили новый атрибут в пространство имён Point (и в New_point, которые ссылаются на Point)."""

setattr(Point, 'prop', 1)
setattr(Point, 'type_pt', 'square')
print(Point.__dict__)
"""Если атрибута нет, то заводит функция новый. Если есть, то обновляет значение."""

print(getattr(Point, 'object', False))
"""При обращении к несуществующему атрибуту класса мы получим ошибку. Чтобы ошибка не вылезла, нужно поспользоваться 
методом getattr(класс, атрибут, возвращаемое значение при отсутствии атрибута)."""

del Point.prop
print(Point.__dict__)
"""Удаляем атрибут. При удалении несуществующего атрибута выдаст ошибку."""

delattr(Point, 'type_pt')
print(Point.__dict__)
"""Аналогично простому del. Тоже выдаст ошибку при отсутствии атрибута."""

print(hasattr(Point, 'prop'), hasattr(Point, 'circle'))
"""Проверяем, есть ли нужный атрибут в классе. False - нет, True - да."""

print(hasattr(New_point1, 'circle'))
"""Данный метод говорит о том, что мы можем получить доступ к атрибуту circle, но не о том, что данный атрибут есть
в пространстве имён New_point, что проверяется New_point.__dict__. К примеру, если прописать del New_point.circle, 
то мы получим ошибку, ибо данного атрибута нет в пространстве имён."""


# ----------------------------------------------------------------------------------------------------------------------

class Point:
    color = 'red'
    circle = 2


New_point1 = Point()
New_point2 = Point()
"""Требуется создать координаты, которые будут уникальны для каждого New_point."""

New_point1.x = 1
New_point1.y = 2

New_point2.x = 10
New_point2.y = 20
"""Результат работы этого кода - каждый объект обладает независимой точкой на плоскости, а цвет и размер являются 
общими данными. Таким образом, мы динамически создали локальные индивидуальные свойства."""


# ----------------------------------------------------------------------------------------------------------------------

class Point:
    """Класс для представления координат точек на плоскости."""
    color = 'red'
    circle = 2


print(Point.__doc__)

"""В любом классе языка Pyhon мы можем определяеть его описание в начальной строке:
        class Point:
            '''Класс для представления координат точек на плоскости''' (документация по стандарту PEP8 прописывается с
            троекратными двойными ковычками) 
            ..."""
