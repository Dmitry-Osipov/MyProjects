"""
Ознакомимся с относительно новой идеей: быстрое описание классов.
Data Classes - классы данных.
В наших уже изученных методах приходится выполнять слишком много типовой работы:
"""


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price


t = Thing('Учебник', 100, 1024)
print(t)  # Мы видим информацию, которая нам особо ничего не даёт - просто расположение в памяти, класс и файл. Поэтому
# для вот таких информационных классов, которые содержат некоторые данные, добавляют магический метод __repr__.


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'Класс Thing: {self.__dict__}'


t = Thing('Учебник', 100, 1024)  # Теперь вывод информативнее, но он требует дополнительной работы.
print(t)

"""
С версии Python 3.7+ появилась возможность "из коробки" объявлять классы, подобные нашему Thing. Данные классы получили 
название классов данных. 
Самым популярным способом является декоратор dataclass:
"""

from dataclasses import dataclass
from pprint import pprint


@dataclass
class ThingData:
    name: str  # Обязательно требуется аннотировать атрибуты, иначе декоратор не сделает атрибут параметром инициализатора.
    weight: int  # Обычно инициализация парамеров идёт в том же порядке, в котором будем прописывать локальные свойства.
    price: float


td = ThingData('Учебник', 100, 1024)
print(td)  # Получили практически аналогичный прошлому вывод, но более лёгким способом.
pprint(ThingData.__dict__)  # Видим, что этот декоратор автоматически добавляет инициализатор; магический метод
# __repr__; __eq__, о котором ниже:

td_2 = ThingData('ООП', 89, 512)
td_3 = ThingData('ООП', 89, 512)

print(td == td_2, td_2 == td_3)  # Видим ожидаемое False и True. Получим True, если все элементы попарно у нас совпали.
# Т.к. декоратор dataclass переопределил метод __eq__, то мы сравниваем не id, а именно значения. Если нам нужно
# сравнивать не все значения, а, например, только вес, то мы можем внутри класса переопределить метод __eq__:


@dataclass
class ThingData:
    name: str
    weight: int
    price: float

    def __eq__(self, other):
        return self.weight == other.weight


td = ThingData('Учебник', 100, 1024)
td_2 = ThingData('ООП', 89, 512)
td_3 = ThingData('ООП 2', 89, 900)
print(td == td_2, td_2 == td_3)

"""
Итак, при замене методов __init__, __repr__ и __eq__ произойдёт замена на наш вариант (пример выше). Но с другими так 
может не сработать.
Следующий базовый момент при определении dataclass состоит в порядке объявления атрибутов с начальными значениями. 
Предположим, что начальное значение цены 0:
"""


@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0


td = ThingData('Учебник', 100)
print(td)  # Подставилось значение по умолчанию. Т.е. наша запись выше эквивалентна тому, как если бы мы написали в
# инициализаторе при определении класса сразу указали начальное значение - def __init__(self,..., price=0):...

"""
Однако если заменить порядок:

class ThingData:
    name: str
    price: float = 0
    weight: int
    
то IDE сразу выведет предупреждение, а при исполнении кода мы получим ошибку TypeError. Но в чём дело? 
Когда мы так прописываем атрибуты класса:

@dataclass
class ThingData:
    name: str
    price: float = 0
    weight: int
    
то инициализатор при обычной записи должен быть таким:

class Thing:
    def __init__(self, name: str, price: float = 0, weight: int):
        ...
        
Здесь параметр price (со значением) идёт вторым, а weight (без значения) идёт третьим. Но мы знаем, что параметры со 
значением по умолчанию должны идти последними, ибо обычный позиционный параметр при стандартной передаче двух аргументов 
просто не получит своё значение - его значение (значение weight) отойдёт на price.

Следующий тонкий момент связан с тем, что значение по умолчанию может представлять собой изменяемый объект. 
Пример возможной проблемы:
"""


class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f'Класс Thing: {self.__dict__}'


t = Thing('Учебник', 100, 1024)
t.dims.append(10)
print(t.dims)  # Ожидаемо получили список, который состоит только из 1 числа. Однако если создать ещё один объект класса:

t2 = Thing('ООП', 120, 124)
print(t2.dims)  # Тоже получили список, состоящий из одного числа, хотя мы ничего не вносили в список для этого
# экземпляра класса. Т.е. мы получили, что в инициализаторе класса при создании локального свойства dims каждый
# экземпляр класса получает один и тот же список. Данный кейс приводит к непредсказуемому поведению программы, ибо
# изначально подразумевается пустой список для каждого экземпляра, а по факту он является общим.


@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    # dims: list = []  # Аналогично прошлому варианту нельзя присваивать изменяемые типы данных. При попытке выполнения
    # программы получаем ошибку ValueError, ибо нельзя напрямую присваивать изменяемые типы данных. Но тогда как
    # создавать объект, для которого по умолчанию требуется создание пустого списка? Используем специальную функцию:


from dataclasses import field


@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list)  # Параметр default_factory позволяет создавать некие объекты при инициализации
    # экземпляров класса ThingData


td = ThingData('Учебник', 100, 1024)
print(td)  # Видим новое локальное свойство: dims=[]
td.dims.append(10)
print(td)  # Естественно, наше число добавилось в список.
td_2 = ThingData('ООП', 89, 512)
print(td_2)  # Видим пустой список, хотя ранее мы добавляли число.

"""
Как и почему это работает? Функция field отрабатывает следующий образом: в классе ThingData создаётся инициализатор, и 
внутри этого инициализатора (внимание: ВНУТРИ ИНИЦИАЛИЗАТОРА) создаётся локальное свойство dims, которое присваивается 
вызову функции list() (ссылку на функцию мы передали в аргументе default_factory). Ну а функция list возвращает пустой 
список. Таким образом, dims ссылается на пустой список. И т.к. эта функция list вызывается внутри инициализатора класса
ThingData, то для каждого объекта создаётся свой пустой список.
"""

"""
Представим, что нам нужно в классе Vector3D при инициализации формировать вычисляемое свойство. Как это можно сделать 
через модуль dataclasses?
"""


class Vector3D:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5


@dataclass
class V3D:
    x: int
    y: int
    z: int

    # При завершении работы классы, использующие @dataclass, выполняют метод __post_init__, в котором как раз и можно
    # воспользоваться всеми локальными атрибутами. Т.к. данный метод вызывается самым последним, то все локальные
    # атрибуты у нас уже сформированы, так что к ним следует обращаться через self:

    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v)  # Локальные атрибуты присутствуют, но мы не видим вычисляемого свойства length, которое мы сформировали.
print(v.__dict__)  # Но на самом деле локальный атрибут length там есть, что видно в этом магическом методе.

"""
Но почему при операции вывода экземпляра класса мы не видим этого локального свойства? При использовании декоратора 
@dataclass меняется магический метод __repr__. В нём содержатся только локальные атрибуты, которые мы явно прописали. 
Четвёртый атрибут же мы формируем налету внутри инициализатора __post_init__, поэтому в магический метод __repr__ 
атрибут length не попадает. Как выйти из ситуации? Можно прописать атрибут явно, но нам нужно сделать так, чтобы он не 
был параметром инициализатора. Для этого воспользуемся функцией field(init=False):
"""


@dataclass
class V3D:
    x: int
    y: int
    z: int
    length: float = field(init=False)

    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v)  # Теперь мы видим сразу все 4 локальных свойства, как того и хотели.

"""
Теперь мы знаем 2 параметра функции field(), которые часто используются. Но есть и другие:
- repr - булева-значение True или False указывает, использовать ли атрибут в магическом методе __repr__ (по умолчанию True); 
- compare - булева-значение True или False указывает, использовать ли атрибут при сравнении объектов (по умолчанию True);
- default - значение по умолчанию (начальное значение) - используется, как правило, с неизменяемыми типами данных.
"""


@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    length: float = field(init=False, compare=False)

    def __post_init__(self):
        self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
v2 = V3D(1, 2, 5)
print(v)  # Теперь x не отображается, ибо мы прописали это в field(repr=False).
print(v == v2)  # Получили True, ибо единственный отличный аргумент (z) мы сказали не сравнивать: field(compare=False)

"""
Предположим, что мы хотим вычислять длину вектора (length) в зависимости от значения конкретного параметра, иначе 
вернётся 0. Т.е. при обычном определении класса мы можем указать параметр в инициализаторе. Но как это сделать с 
декоратором dataclass?
"""

from dataclasses import InitVar


class Vector3D:
    def __init__(self, x: int, y: int, z: int, calc_len: bool = True):
        self.x = x
        self.y = y
        self.z = z
        self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0


@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True  # Используем аннотацию через специальный класс.
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


"""
Что это за класс такой InitVar? Как только какой-либо атрибут аннотируется классом InitVar (в квадратных скобках 
указываем аннотацию), то этот атрибут передаётся автоматически в метод __post_init__. Соответственно, в этом магическом 
методе мы должны прописать этот параметр. А по умолчанию при инициализации метода, для которого мы всё делаем (в нашем 
случае дял метода length), следует установить начальное значение length = field(..., default=0).
Т.е. эта запись calc_len: 
    
InitVar[bool] = True  # Используем аннотацию через специальный класс.
length: float = field(init=False, compare=False, default=0)

эквивалентна такой записи:

self.length = (x * x + y * y + z * z) ** 0.5 if calc_len else 0

Убедимся, что всё работает:
"""

v = V3D(1, 2, 3)
v2 = V3D(1, 2, 5, False)
print(v)  # Видим, что length вычислилось, ибо значение calc_len по умолчанию True.
print(v2)  # Соответственно, length не вычислилось, ибо передали False.

"""
До сих пор мы использовали декоратор dataclass с параметрами по умолчанию. Разберёмся же с наиболее часто встречающимися 
параметрами этого декоратора:

Параметр:                     Описание:

init = [True|False]           Принимает булева-значение, по умолчанию True. Если True, то в классе объявляется 
                              инициализатор, иначе не объявляется.
                              
repr = [True|False]           Принимает булева-значение, по умолчанию True. Если True, то в классе объявляется 
                              магический метод __repr__, иначе не объявляется.

eq = [True|False]             Принимает булева-значение, по умолчанию True. Если True, то в классе объявляется 
                              магический метод __eq__, иначе не объявляется.

order = [True|False]          Принимает булева-значение, по умолчанию False. Если значение True, то в классе объявляются
                              магические методы для операций сравнения <;<=;>;>=, иначе не объявляются. 

unsafe_hash = [True|False]    Влияет на формирование магического метода __hash__.

frozen = [True|False]         Принимает булева-значение, по умолчанию False. Если True, то атрибуты объектов класса 
                              становятся неизменяемыми (можно лишь раз проинициализировать в инициализаторе).

slots = [True|False]          Принимает булева-значение, по умолчанию False. Если True, то атрибуты объявляются в 
                              коллекции __slots__.
"""


@dataclass(init=False)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True  # Используем аннотацию через специальный класс.
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


# v = V3D(1, 2, 3)  # Ожидаемо получаем ошибку TypeError: V3D() takes no arguments, ибо мы отказались от создания
# инициализатора для данного класса. Такое поведение бывает полезным, если мы хотим создать класс, который будет базовым
# для каких-то дочерних, и для этого базового класса не предполагается создание инициализатора.


@dataclass(repr=False)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True  # Используем аннотацию через специальный класс.
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
print(v)  # Снова видим невразумительную строчку <__main__.V3D object at 0x000001E05261ABD0>, ибо теперь у нас нет
# магического метода __repr__.


@dataclass(eq=False)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True  # Используем аннотацию через специальный класс.
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
v2 = V3D(1, 2, 3)
print(v == v2)  # Т.к. мы отказались от реализации магического метода __eq__, мы снова получаем сравнение id двух
# экземпляров вместо сравнения значений для этих экземпляров.


@dataclass(order=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True  # Используем аннотацию через специальный класс.
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5


v = V3D(1, 2, 3)
v2 = V3D(1, 5, 3)
print(v <= v2)  # Получаем ожидаемое True. Важное примечание: не может быть одновременно установлен order=True и eq=False.
# Также важное примечание: нельзя переопределять логику работы магических методов __lt__, __gt__ и пр., ибо вылезет
# ошибка TypeError.


@dataclass(frozen=True)
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = True  # Используем аннотацию через специальный класс.
    length: float = field(init=False, compare=False, default=0)

    # def __post_init__(self, calc_len: bool):
    #     if calc_len:
    #         self.length = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5  # IDE сразу показывает ошибку,
            # ибо мы уже присвоили свойству length значение 0.


v = V3D(1, 2, 3, True)  # dataclasses.FrozenInstanceError: cannot assign to field 'length'. Аналогично, попытавшись
# изменить локальные свойства экземпляра класса, получим ту же ошибку.

"""
Далее посмотрим, как декоратор dataclass работает при наследовании. В качестве примера сформируем базовый класс Goods
для представления различных товаров. На основе нашего класса сформируем другой через декоратор dataclass:
"""

from typing import Any


@dataclass
class Goods:
    uid: Any
    price: Any = None
    weight: Any = None


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0


"""
Но какие инициализаторы будут для каждого класса?
Очевидно, для Goods будет стандартный инициализатор:

class Goods:
    def __init__(self, uid: Any, price: Any = None, weight: Any = None):
        ...
        
Для класса Book будет аналогичный инициализатор. Т.е. те атрибуты, что мы пропишем явно, будут такими же и в 
инициализаторе (включая аннотацию типов), а вот те, которые прописаны не были, достанутся от базового класса. 
Очерёдность же будет, как у базового класса, несмотря на смену очерёдности в дочернем классе:

class Book(Goods):
    def __init__(self, id: Any, price: float = 0, weight: int | float = 0, title: str = '', author: str = ''):
        ...
"""

b = Book(1)
print(b)  # При вводе одного аргумента всё работает. Попробуем же прописать все аргументы:

b1 = Book(1, 1000, 100, 'Учебник ООП', 'Балакирев С.М.')
print(b1)  # Всё отработало корректно. Усложним программу так, чтобы уникальный id менялся автоматически при создании
# каждого нового объекта:


@dataclass
class Goods:
    current_uid = 0  # Атрибут не аннотирован никаким типом. Соответственно, этот декоратор его просто пропускает,
    # как следствие и никуда не добавит этот атрибут класса.

    uid: int = field(init=False)  # Исключаем данный параметр из инициализатора.
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: __post_init__')  # Проверяем, вызовется ли данный метод.
        Goods.current_uid += 1
        self.uid = Goods.current_uid  # Итак, мы реализовали нужный счётчик, ибо uid формируется автоматически для
        # каждого нового объекта.


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0


b = Book(1000, 100, 'Учебник ООП', 'Балакирев С.М.')  # Видим, что __post_init__ был вызван.
print(b)  # Видим, что uid увеличился. А теперь попробуем добавить метод __post_init__ в дочерний класс:


@dataclass
class Goods:
    current_uid = 0  # Атрибут не аннотирован никаким типом. Соответственно, этот декоратор его просто пропускает,
    # как следствие и никуда не добавит этот атрибут класса.

    uid: int = field(init=False)  # Исключаем данный параметр из инициализатора.
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: __post_init__')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0

    def __post_init__(self):
        print('Book: __post_init__')


b = Book(1000, 100, 'Учебник ООП', 'Балакирев С.М.')  # Видим, что метод __post_init__ отработал внутри дочернего класса
# print(b)  # А тут получаем ошибку AttributeError: 'Book' object has no attribute 'uid'. Но почему?

"""
У нас был вызван метод __post_init__ дочернего класса, но нигде не вызывался метод __post_init__ базового класса. И в 
результате свойство uid не было сформировано, отсюда и ошибка. Но почему метод __post_init__ базового класса не был 
вызван после переопределения его в дочернем классе? 
Когда мы формируем 2 класса: базовый и дочерний. Соответственно, метод __init__ дочернего класса вызывает метод 
__post_init__, то если этого метода нет в дочернем классе, то он ищется в базовом классе, и т.к. он там (в базовом 
классе) был прописан, то вызывался. После того же, как мы добавили метод __post_init__ в дочерний класс, то именно этот 
метод из именно дочернего класса и был вызван. Соответственно, метод __post_init__ базового класса не запускался, и 
атрибут класса uid не создавался, откуда и шла ошибка. Как можно это исправить? Самый простой вариант - это исползовать
метод super() в дочернем классе:
"""


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: __post_init__')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0

    def __post_init__(self):
        super().__post_init__()
        print('Book: __post_init__')


b = Book(1000, 100, 'Учебник ООП', 'Балакирев С.М.')  # Был вызван метод __post_init__ и базового, и дочернего классов.
print(b)  # Теперь все атрибуты сформированы корректно.

"""
Также важно обратить внимание: такой явный вызов метода базового класса через super() нужно делать именно для методов
__post_init__, для обычных инициализаторов (__init__) этого делать не нужно. Инициализаторы базовых классов здесь 
автоматически вызываются, что закладывается при наследовании, когда классы формируются через декоратор dataclass.
Если формировать цепочку наследования классическим способом (без декоратора dataclass), то вызов инициализаторов 
(__init__) базовых классов из дочерних нужно было бы явно указывать. 

Ещё усложним нашу программу новым атрибутом дочернего класса, которое будет содержать габарит предмета:  
"""


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: __post_init__')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)  # Передаём ссылку на функцию.
    # В результате мы должны получить список из трёх нулей.

    def __post_init__(self):
        super().__post_init__()
        print('Book: __post_init__')


b = Book(1000, 100, 'Учебник ООП', 'Балакирев С.М.')
print(b)

"""
Выше мы увидели пример того, как можно использовать параметр default_factory со своей функцией. Т.е. то, что вернёт эта 
функция get_init_measure внутри этого класса GoodsMethodsFactory.
Но почему бы не объявить метод get_init_measure внутри дочернего класса Book. Может, так было бы удобнее?
"""


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print('Goods: __post_init__')
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ''
    author: str = ''
    price: float = 0
    weight: int | float = 0
    # measure: list = field(default_factory=Book.get_init_measure)  # AttributeError: type object 'Book' has no
    # attribute 'get_init_measure'. Соответственно, требуется вспомогательный класс.

    @staticmethod
    def get_init_measure():
        return [0, 0, 0]

    def __post_init__(self):
        super().__post_init__()
        print('Book: __post_init__')


b = Book(1000, 100, 'Учебник ООП', 'Балакирев С.М.')
print(b)

"""
Есть ещё одна возможность для объявления класса данных - с помощью функции make_dataclasses, которая имеет следующие 
наиболее часто встречаемые параметры (но по факту параметров у функции больше):

- cls_name - название нового класса (в виде строки);
- fields - поля (локальные атрибуты) объектов класса;
- * - произвольный набор позиционных аргументов;
- bases - список базовых классов;
- namespace - словарь для определения атрибутов самого класса (например, так можно объявлять методы класса).

Попробуем реализовать это:
"""

from dataclasses import make_dataclass


class Car:  # Допустим, мы хотим с помощью функции make_dataclasses создать класс подобный этому.
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


CarData = make_dataclass('CarData', [('model', str),  # Можно аннотировать элементы в кортеже,
                                     'max_speed',  # а можно и не аннотировать.
                                     ('price', float, field(default=0))],  # Указали начальное значение.
                         namespace={'get_max_speed': lambda self: self.max_speed})  # Создали метод внутри класса.


c = CarData('BMW', 256, 4096)
print(c)
print(c.get_max_speed())  # Видим, что всё отработало, как мы того и хотели.

"""
Аналогично работают и все методы, что и через декоратор dataclass: методы repr, eq, frozen и т.д.
Обычно функцию make_dataclass используют, если требуется сформировать класс данных в процессе работы программы. Если же 
нам требуется обычное объявление (а это наиболее частая ситуация), то гораздо удобнее использовать декоратор dataclass.
"""
