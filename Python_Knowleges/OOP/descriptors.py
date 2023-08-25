class Point3D1:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
        # Не ставим подчёркивания перед координатами, ибо когда мы выполняем присваивание выше, то будет срабатывать
        # соответствующий сеттер, и будет формироваться нужное локальное свойство причём сразу с проверкой
        # на целочисленный тип данных

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord


p1 = Point3D1(1, 2, 3)
print(p1.__dict__)
"""
Всё работает, но мы имеем очень много повторений функционала с заменой лишь 1 переменной. В случае, когда мы имеем много
переменных, то следует использовать дескрипторы.
Если класс содержит специальный магический метод __get__(self, instance, owner). Тогда мы получим дескриптор не данных 
(non-data descriptor). Или если этот класс содержит так же ещё хотя бы один из магических методов
__set_name__(self, instance, value) и/или __del__(self), то это будет дескриптор данных (data descriptor).
"""


class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:
    """
    Т.к. координатами будут целые числа, то интерфейс взаимодействия с ними мы определим через дескриптор.
    В классе Point3D создаём экземпляры класса Integer (x = Integer()...). После того, как мы тх создали, то
    автоматически срабатывает метод __set_name__, в котором первый параметр (self) является ссылкой на создаваемый
    экземпляр класса (name = '_x'). Второй параметр (owner) - это ссылка на класс Point3D. Третий параметр (name) -
    это имя атрибута (например, x), которому присваивается экземпляр класса, и через этот параметр создаём локальное
    свойство self.name = "_" + name. В итоге в создаваемом экземпляре класса появляется локальное свойство с именем
    name, а содержать будет строку с атрибутом (в нашем случае '_x'). Таким образом работает магический метод
    __set_name__, который вызывается, когда создаётся экземпляр класса.

    Далее мы создаём экземпляр класса Point3D. При создании этого класса вызывается инициализатор (__init__),
    в инициализаторе идёт обращение к дескрипторам (x, y, z), и присваивается соответствующее значение (x, y или z),
    которое мы передаём в качестве аргументов при создании объекта класса. В итоге в момент присваивания
    срабатывает сеттер __set__. В этом сеттере первый аргумент (self) - это ссылка на соответствующий экземпляр
    (например, когда мы присваиваем что-то x, т.е. используем дескриптор х, то self будет ссылаться на х -
    экземпляр класса Integer. Второй параметр (instance) ссылается на экземпляр класса Point3D, из которого этот
    дескриптор был вызван. Третий параметр (value) - это числовое значение (в данном случае 4), которое мы присваиваем.
    Зная все эти данные мы можем в экземпляре класса Point3D создать соответствующие локальные свойства. Делаем это
    через instance, т.е. через ссылку на этот экземпляр. В частности мы обращаемся к словарю __dict__, который и
    отвечает за формирование всех локальных свойств экземпляра класса. И в этом словаре явно указываем ключ self.name.
    Мы помним, что self.name - это атрибут (name), которое сейчас содержит строку (например, '_x'). В результате
    мы создаём в экземпляре класса Point3D свойство (например, _x) и помещаем туда числовое значение
    value (в нашем случае 4). В итоге мы и формируем так локальное свойство экземпляра класса Point3D - сначала _х,
    потом _y, потом так же _z.

    Если потом мы обратимся к дескриптору через экземпляр класса Point3D для считывания данных, то выполнится геттер
    __get__. В этом геттере self - это ссылка на экземпляр класса Integer. instance - это ссылка на экземпляр класса
    Point3D (в нашем случае p), через который мы обратились к данному дескриптору. А owner - это уже ссылка на сам
    класс Point3D. В частности, геттер берёт из коллекции __dict__ нужное локальное свойство self.name и возвращает его.
    А затем это значение автоматически возвращается дескриптором (например, х) и присваивается нужной переменной.

    В итоге сколько бы интерфейсов нам бы ни понадобилось, мы можем их легко прописать, и всё будет выглядеть понятно
    и компактно.
    """
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координата должна быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
        # return instance.__dict__[self.name] - поменяли на функцию getattr, ибо правильнее будет не напрямую обращаться
        # к коллекции __dict__. Первым аргументом передаём область видимости того объекта, из которого хотим взять
        # значение атрибута, а вторым аргументом передаём название этого атрибута, которое хранится в локальном
        # свойстве name.

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f'__set__: {self.name} = {value}')
        setattr(instance, self.name, value)
        # instance.__dict__[self.name] = value - вместо использования коллекции __dict__, воспользовались функцией
        # setattr. Аргументы используем, как и в getattr, но третьим аргументом уже указываем значение,
        # которое присваивается.


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(4, 5, 6)
p.z = 8
p.xr = 5
print(p.z, p.xr, p.__dict__)

"""
В итоге созданный нами класс Integer является data descriptor, на основе которого мы создали 3 объекта - x, y, z 
в классе Point3D. 

Отличия data и non-data дескрипторов:
1) non-data descriptor могут только считывать значение какого-либо свойства (т.к. не имеет сеттера или делитера).
2) data descriptor имеет тот же приоритет доступа, что и обычные атрибуты класса (т.е. его приоритет выше, чем у 
локальных атрибутов).
"""
