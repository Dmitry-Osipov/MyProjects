from __future__ import annotations
from typing import Any, Type, TypeVar

tr: dict = {'car': 'машина'}

x: object = None  # Класс object является базовым для всех, так что такая аннотация будет работать для любого типа данных.
x = '123'
x = 123


class Geom:
    pass


class Line(Geom):
    pass


g: Geom
g = Line()  # Geom является базовым классом для Line, так что мы не нарушаем аннотацию типов. Однако если убрать
# наследование, то IDE высветит подсказку.

"""
Однако далее следует вопрос: есть ли разница между этими аннотациями - x: object... и x: Any..?
На самом деле есть. И отличие это можно указать следующей фразой:
Тип Any совместим с любым другим типом, а тип object - ни с каким другим:
"""

a: Any = None
s: str

s = a  # Переменной s, которая аннотирована как строка, присваиваем другой объект, который аннотирован, как Any. Т.е. a
# может являться любым типом данных. Соответственно, IDE ничего не подсвечивает

a: object = None
s: str

s = a  # Однако если вместо Any прописать object, то IDE нам сразу подсвечивает переменную a, ибо мы пытаемся переменной
# s, которая аннотирована как строка, присвоить объект, который аннотирован как object, а str является дочерним по
# отношению к object. В итоге нельзя тип object привести к типу str. Однако можно было бы наоборот (если a: str,
# s: object).

"""
Вспомним, что с помощью mypy можно проверять корректность аннотаций:

В консоли прописываем путь к нужной директории, далее используем команду mypy class_annotations.py, и видим вывод:
class_annotations.py:34: error: Name "a" already defined on line 28  [no-redef]
class_annotations.py:35: error: Name "s" already defined on line 29  [no-redef]
Found 2 errors in 1 file (checked 1 source file)

Данный модуль более строго проверяет аннотации типов, нежели обычная IDE.
Более подробная информация по модулю: https://mypy.readthedocs.io/en/stable/#

Вернёмся к аннотациям типов.
"""


class Geom:
    pass


class Point2D(Geom):
    pass


def factory_object(cls_object: Geom) -> Geom:  # Пропишем функцию по созданию объектов классов. cls_object - это ссылка
                                               # на класс (не на объект класса).
    return cls_object()  # Нам высвечивается ошибка, потому что подразумевается, что аннотация Geom будет ссылаться не
                         # на сам класс Geom, а на объекты класса Geom.


"""
Когда мы прописываем аннотации типов, то всегда подразумевается объекты тех типов, которые указываются. Переделаем нашу
функцию. Для начала импортируем из модуля typing тип Type, далее же укажем его в функции:
"""


def factory_object(cls_object: Type[Geom]) -> Geom:  # Теперь мы указали, что cls_object будет ссылаться на класс Geom.
    return cls_object()  # Соответственно, ошибки нет, ибо мы по итогу создаём объект класса Geom.


geom = factory_object(Geom)
point = factory_object(Point2D)  # Никаких проблем мы не видим, но если аннотировать переменные, то увидим подсветку:

geom: Geom = factory_object(Geom)  # Подсветки нет.
point: Point2D = factory_object(Point2D)  # Получаем подсветку, ибо ожидаем Point2D, а из функции возвращается Geom
# (вернее возвращается Point2D, но ожидаем мы Geom по функции).

"""
Программа выполнится без ошибок, но на уровне аннотаций типов мы имеем конфликт. Для исправления таких ситуаций из 
модуля typing необходимо импортировать специальный класс, который аннотирует общие типы - TypeVar. Как именно это сделать:
"""

T = TypeVar('T', bound=Geom)  # Определяем некий общий тип, создаём объект класса TypeVar, где указываем имя переменной
# (обычно пишут по названию переменной, просто "T"), далее воспользуемся именованным аргументом bound, в котором укажем,
# что допустимы все типы, которые связаны с базовым классом Geom.


def factory_object(cls_object: Type[T]) -> T:
    return cls_object()


geom: Geom = factory_object(Geom)
point: Point2D = factory_object(Point2D)  # Теперь конфликта типов нигде нет, ибо когда подставляем аргументом Geom, то
# Т становится классом Geom, а когда аргументом будет Point2D, то T становится классом Point2D.

"""
Вторым примером использования TypeVar является общее определение. Т.е. без использования именованных аргументов:
T = TypeVar('T')

Также можно аннотировать нужные нам классы внутри TypeVar по-другому. Например, мы хотим, чтобы наша общая аннотация 
была аннотацией для классов int, float:
T = TypeVar('T', int, float)

Далее рассмотрим аннотацию типов внутри класса Point2D более подробно:
"""


class Point2D1(Geom):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


p = Point2D1(10, 20)  # Ошибок не подсвечивает.
p = Point2D1(10.5, 10.3)  # Подсвечивает ошибку аргументов.

"""
Но далее возникает вопрос: для локальный атрибутов внутри класса Point2D (self.x и self.y), которые создаются внутри 
каждого объекта класса Point2D, - действует ли для них аннотация? Проверим:
"""

p.x = '10'  # IDE ничего не подсвечивает, однако модуль mypy выдаёт ошибку на этой строке.

"""
Если в инициализаторе прописать self.x = 10, то он примет значение для x и будет подразумевать, что далее для x должны 
поступать только целые числа.

Примечание по mypy: был пойман баг - если не определить новый класс, а использовать Point2D (который мы инициализировали 
выше, то мы поймаем ошибку не аннотации типов, а ошибку того, что локальное свойство x не определено для данного класса.
Т.е. класс Point2D был просканирован модулем mypy всего лишь раз - когда он был создан вверху программы.

Если мы хотим явно указать аннотация типов для атрибутов классов и для его объектов, то это нужно прописать внутри класса:
"""


class Point2D2(Geom):
    x: int  # Теперь эта аннотация будет распространяться и на локальные атрибуты, и на атрибуты самого класса.
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __copy__(self) -> Point2D2:  # Функция будет создавать копию объекта Point2D
        return Point2D2(self.x, self.y)


"""
Получаем проблему, что мы не можем указывать такую аннотацию. IDE подсвечивает красным. Есть 2 способа решения:
1) Заключить Point2D2 в строку: def __copy__(self) -> 'Point2D2': ... - устаревший способ.
2) Указываем типом этот класс (как и было выше), но чтобы всё работало, надо импортировать из модуля __future__ объект
annotations. Как только мы это импортировали, то ошибка сразу пропадает. Прим. работает с версии Python 3.7.

Но почему в более поздних версиях не сделали такую функцию? Почему надо импортировать отдельный модуль для этого?
Это сделано для обратной совместимости с более ранними версиями, из чего разработчики языка решили, что это важно.

Для чего нужна аннотация типов?
Если мы пишем короткую программу, которую можно легко охватить взглядом, то такая аннотация особо ничего не добавляет.
Мы и так всё сможем увидеть и понять, так что излишняя аннотация может только ухудшить восприятие кода. Для небольших 
программ будет достаточным аннотации ключевых функций либо вообще ничего не делать.
Если же пишется крупный проект, состоящий из нескольких модулей, то грамотное аннотирование заметно упрощает понимание 
кода сторонними программистами, да и самому будет проще восстанавливать в памяти все нюансы работы. Впрочем и тут можно 
всё замусорить. 
Важно помнить, что цель аннотирования - это упрощение восприятия текста программы, и как только аннотация начинает 
мешать - это верный признак убрать аннотации.
"""
