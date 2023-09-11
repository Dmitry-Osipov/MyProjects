from accessify import private, protected


class Point:
    """
    Attribute (без одного или двух подчёркиваний в начале) - публичное свойство (public).
    _Attribute (с одним подчёркиванием) - режим доступа protected (служит для обращения внутри класса и во
    всех его дочерних классах).
    __Attribute (с двумя подчёркиваниями) - режим доступа private (служит для обращения только внутри класса).

    В результате можно сказать, что public можно и менять, и просматривать напрямую.
    Protected можно напрямую только просматривать. А private нельзя напрямую ни посмотреть, ни изменить.
    Ключевое слово - напрямую. Для просмотра и изменения есть сеттеры и геттеры (интерфейсные методы).
    Также эти методы существуют не только для просмотра и корректировки информации, но и для типизирования.

    Таким образом, мы изучили первый принцип ООП - инкапсуляция. Суть инкапсуляции в том, что разработчик может изменять
    и просматривать только то, что к чему он получил доступ. По аналогии с автомобилем - можно смотреть в зеркала,
    крутить руль, переключать передачи. Но внутрь узла (например, коробки передач) простой водитель залезть не может.
    """

    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, value):
        return type(value) in (int, float)

    def set_coord(self, x, y):  # данный метод в ООП называется сеттер
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):  # данный метод в ООП называется геттер
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
print(pt.get_coord())
print(pt.__dir__())  # '_Point__x', '_Point__y' - в окружении имён pt данные строки являются кодовыми именами
# приватных свойств класса Point.
print(pt._Point__x)  # Так лучше никогда не писать, ибо могут произойти ненужные нам последствия. Всегда нужно
# взаимодействовать с кодом только разрешённым и заранее предусмотренным образом.


# Если требуется лучшим образом защитить данные, то требуется использовать модуль accessify.
# Использовать данную библиотеку нужно только в том случае, если по каким-то причинам нужно очень обезопасить атрибуты
# или методы. Чаще всего используют просто два подчёркивания. Ибо если разработчик, зная про приватность атрибута или
# метода, всё же полезет прямым способом менять что-то, то в случае падения программы он сам будет виноват.


class NewPoint:
    def __init__(self, x, y):
        self.__x = self.__y = 0
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y

    @private
    @classmethod
    def check_value(cls, value):
        return type(value) in (int, float)

    def set_coord(self, x, y):  # данный метод в ООП называется сеттер
        if self.check_value(x) and self.check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_coord(self):  # данный метод в ООП называется геттер
        return self.__x, self.__y


npt = NewPoint(1, 2)
npt.set_coord(10, 20)
npt.check_value(5)  # Получаем ошибку:
# raise InaccessibleDueToItsProtectionLevelException(accessify.errors.InaccessibleDueToItsProtectionLevelException:
# NewPoint.check_value() is inaccessible due to its protection level
