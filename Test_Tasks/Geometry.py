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


class Circle(Figure):
    """
    Класс геометрической фигуры круг, наследующий абстрактный класс. Реализует методы родительского класса.

    Атрибуты:
    radius - радиус круга.
    """

    def __init__(self, radius: int | float):
        """
        Инициализатор круга с заданным радиусом.

        :param radius: int или float - радиус круга.
        :raises ValueError: Если на вход кругу было дано не число или если значение радиуса меньше 0.
        """
        if not isinstance(radius, int | float) or radius <= 0:
            raise ValueError('Невозможное значение радиуса')

        self.__radius = radius

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
        :raises ValueError: Если была попытка заменить значение радиуса на число <= 0 либо была попытка заменить
        тип данных, на отличный от int или float.
        """
        if not isinstance(radius, int | float) or radius <= 0:
            raise ValueError('Невозможно изменить радиус на новое значение.')

        self.__radius = radius

    def find_area(self):
        """
        Реализация абстрактного метода по поиску площади фигуры.

        :return: float - площадь круга.
        """
        return pi * self.__radius ** 2


class Triangle(Figure):
    """
    Класс геометрической фигуры треугольник, наследующий абстрактный класс. Реализует методы родительского класса.

    Атрибуты:
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
        :raises ValueError: Если на вход треугольнику были даны не числа.
        """
        if not isinstance(a, int | float) or not isinstance(b, int | float) or not isinstance(c, int | float):
            raise ValueError('Невозможно создать такой треугольник.')

        self.__a = a
        self.__b = b
        self.__c = c

    def _is_square(self):
        """
        Приватный метод проверяет, является ли треугольник прямоугольным с использованием теоремы Пифагора.

        :return: bool - True, если треугольник прямоугольный, в противном случае False.
        """
        return (self.__a ** 2 + self.__b ** 2 == self.__c ** 2
                or self.__b ** 2 + self.__c ** 2 == self.__a ** 2
                or self.__a ** 2 + self.__c ** 2 == self.__b ** 2)

    def _check_triangle(self):
        """
        Приватный метод проверяет, является ли треугольник возможным с заданными сторонами.

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

        :return: float или int, значение стороны a.
        """
        return self.__a

    @a.setter
    def a(self, a):
        """
        Установка значения стороны a треугольника.

        :param a: float или int, новое значение стороны a.
        :raises TypeError: Если невозможно построить треугольник с заданными сторонами.
        """
        self._check_triangle()
        self.__a = a

    @property
    def b(self):
        """
        Получение значения стороны b треугольника.

        :return: float или int, значение стороны b.
        """
        return self.__b

    @b.setter
    def b(self, b):
        """
        Установка значения стороны b треугольника.

        :param b: float или int, новое значение стороны b.
        :raises TypeError: Если невозможно построить треугольник с заданными сторонами.
        """
        self._check_triangle()
        self.__b = b

    @property
    def c(self):
        """
        Получение значения стороны c треугольника.

        :return: float или int, значение стороны c.
        """
        return self.__c

    @c.setter
    def c(self, c):
        """
        Установка значения стороны c треугольника.

        :param c: float или int, новое значение стороны c.
        :raises TypeError: Если невозможно построить треугольник с заданными сторонами.
        """
        self._check_triangle()
        self.__c = c

    def find_perimeter(self):
        """
        Метод для расчета периметра треугольника.

        Рассчитывает периметр треугольника по формуле:
        периметр = a + b + c

        :return: Периметр треугольника.
        :raises TypeError: Если невозможно построить треугольник с заданными сторонами.
        """
        self._check_triangle()
        return self.__a + self.__b + self.__c

    def find_area(self):
        """
        Метод для расчета площади треугольника.

        Рассчитывает площадь треугольника, используя формулу Герона:
        площадь = sqrt(s * (s - a) * (s - b) * (s - c)),
        где s - полупериметр треугольника.

        Если треугольник является прямоугольным, площадь вычисляется как
        половина произведения катетов.

        :return: float, площадь треугольника.
        :raises TypeError: Если невозможно построить треугольник с заданными сторонами.
        """
        self._check_triangle()
        sides = [self.__a, self.__b, self.__c]

        if self._is_square():
            hypotenuse = max(sides)
            sides.remove(hypotenuse)
            return 0.5 * sides[0] * sides[1]

        semi_per = self.find_perimeter() / 2
        return sqrt(semi_per * (semi_per - sides[0]) * (semi_per - sides[1]) * (semi_per - sides[2]))
