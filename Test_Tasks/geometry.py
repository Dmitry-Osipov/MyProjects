from abc import ABC, abstractmethod
from math import pi, sqrt

# Напишите на C# или Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и
# треугольника по трем сторонам.
# Дополнительно к работоспособности оценим:
# Юнит-тесты
# Легкость добавления других фигур
# Вычисление площади фигуры без знания типа фигуры в compile-time
# Проверку на то, является ли треугольник прямоугольным


class Figure(ABC):
    """
    Абстрактный базовый класс для геометрически фигур. Определяет интерфейсы для различных геометрических фигур.
    Атрибуты реализуются через дочерние классы.
    """

    @abstractmethod
    def find_area(self):
        """
        Метод вычисляет площадь фигуры. Должен быть реализован дочерними классами.

        :return: float - площадь фигуры.
        """
        pass

    @abstractmethod
    def _check_figure(self):
        """
        Служебный метод проверяет, возможно ли создать фигуру с заданными параметрами.
        Должен быть реализован через дочерние классы. Рекомендуется использовать исключение ValueError.

        :raises ValueError: Если невозможно построить фигуру с заданными параметрами.
        """
        pass


class Circle(Figure):
    """
    Класс геометрической фигуры круг, наследующий абстрактный класс. Реализует методы родительского класса.

    Локальные свойства:
    radius - радиус круга.
    """

    def __init__(self, radius: int | float):
        """
        Инициализатор круга с заданным радиусом.

        :param radius: int или float - радиус круга.
        :raises ValueError: Если невозможно построить круг с заданным радиусом.
        """
        self.__radius = radius
        self._check_figure()

    def _check_figure(self):
        """
        Служебный метод проверяет, является ли круг возможным с заданным радиусом.

        :raises ValueError: Если невозможно построить круг с заданным радиусом.
        """
        if not isinstance(self.__radius, int | float) or self.__radius <= 0:
            raise ValueError('Невозможное значение радиуса')

    @property
    def radius(self):
        """
        Получить текущее значение радиуса круга.

        :return: int или float - текущий радиус круга.
        """
        return self.__radius

    @radius.setter
    def radius(self, radius):
        """
        Установить новое значение радиуса круга.

        :param radius: int или float - новый радиус круга.
        :raises ValueError: Если невозможно построить круг с заданным радиусом.
        """
        self.__radius = radius
        self._check_figure()

    def find_area(self):
        """
        Реализация абстрактного метода по поиску площади фигуры.

        :return: float - площадь круга.
        """
        return pi * self.__radius ** 2


class Triangle(Figure):
    """
    Класс геометрической фигуры треугольник, наследующий абстрактный класс. Реализует методы родительского класса.

    Локальные свойства:
    a - первая сторона треугольника;
    b - вторая сторона треугольника;
    c - третья сторона треугольника.
    """

    def __init__(self, a, b, c):
        """
        Инициализатор треугольника с тремя сторонами.

        :param a: int или float - первая сторона треугольника.
        :param b: int или float - вторая сторона треугольника.
        :param c: int или float - третья сторона треугольника.
        :raises ValueError: Если невозможно построить треугольник с заданными сторонами.
        """
        self.__a = a
        self.__b = b
        self.__c = c
        self._check_figure()

    def _is_square(self):
        """
        Служебный метод проверяет, является ли треугольник прямоугольным с использованием теоремы Пифагора.

        :return: bool - True, если треугольник прямоугольный, в противном случае False.
        """
        return (self.__a ** 2 + self.__b ** 2 == self.__c ** 2
                or self.__b ** 2 + self.__c ** 2 == self.__a ** 2
                or self.__a ** 2 + self.__c ** 2 == self.__b ** 2)

    def _check_figure(self):
        """
        Служебный метод проверяет, является ли треугольник возможным с заданными сторонами.

        Проверяет, что сумма длин двух сторон треугольника всегда больше длины третьей стороны,
        что является необходимым условием для существования треугольника.

        :raises ValueError: Если невозможно построить треугольник с заданными сторонами.
        """
        if (not isinstance(self.__a, int | float) or not isinstance(self.__b, int | float)
                or not isinstance(self.__c, int | float) or self.__a + self.__b < self.__c
                or self.__a + self.__c < self.__b or self.__b + self.__c < self.__a):
            raise ValueError('Невозможный треугольник.')

    @property
    def a(self):
        """
        Получение значения стороны a треугольника.

        :return: float или int - значение стороны a.
        """
        return self.__a

    @a.setter
    def a(self, a):
        """
        Установка значения стороны a треугольника.

        :param a: float или int - новое значение стороны a.
        :raises ValueError: Если невозможно построить треугольник с заданными сторонами.
        """
        self.__a = a
        self._check_figure()

    @property
    def b(self):
        """
        Получение значения стороны b треугольника.

        :return: float или int - значение стороны b.
        """
        return self.__b

    @b.setter
    def b(self, b):
        """
        Установка значения стороны b треугольника.

        :param b: float или int - новое значение стороны b.
        :raises ValueError: Если невозможно построить треугольник с заданными сторонами.
        """
        self.__b = b
        self._check_figure()

    @property
    def c(self):
        """
        Получение значения стороны c треугольника.

        :return: float или int - значение стороны c.
        """
        return self.__c

    @c.setter
    def c(self, c):
        """
        Установка значения стороны c треугольника.

        :param c: float или int - новое значение стороны c.
        :raises ValueError: Если невозможно построить треугольник с заданными сторонами.
        """
        self.__c = c
        self._check_figure()

    def find_perimeter(self):
        """
        Метод для расчета периметра треугольника.

        Рассчитывает периметр треугольника по формуле:
        периметр = a + b + c

        :return: int или float - периметр треугольника.
        :raises ValueError: Если невозможно построить треугольник с заданными сторонами.
        """
        return self.__a + self.__b + self.__c

    def find_area(self):
        """
        Метод для расчета площади треугольника.

        :return: float - площадь треугольника.
        :raises ValueError: Если невозможно построить треугольник с заданными сторонами.
        """
        sides = [self.__a, self.__b, self.__c]

        if self._is_square():
            hypotenuse = max(sides)
            sides.remove(hypotenuse)
            return (sides[0] * sides[1]) / 2

        semi_per = self.find_perimeter() / 2
        return sqrt(semi_per * (semi_per - sides[0]) * (semi_per - sides[1]) * (semi_per - sides[2]))
