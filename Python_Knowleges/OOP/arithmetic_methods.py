"""
Магические методы арифметический операций:
__add__() - для операции сложения.
__sub__() - для операции вычитания.
__mul__() - для операции умножения.
__truediv__() - для операции деления.
__floordiv__() - для операции целочисленного деления.
__mod__() - для операции нахождения остатка от деления.
Для реализации этих магических методов создадим класс для отчёта секунд.
"""


class Clock:
    __DAY = 86400


    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны целым быть числом')

        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, value):
        return str(value).rjust(2, '0')  # Добавляем 0 справа (01, 02 и т.д.).

    def __add__(self, other):  # other - это то значение, которое стоит справа от оператора сложения.
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds  # Если аргумент other является экземпляром класса Clock, то невозможно просто прибавить
            # other, для корректной работы программы требуется прописать other.seconds.

        return Clock(self.seconds + sc)

    def __radd__(self, other):
        return self + other  # Когда будет выполняться операция сложения, то вызовется магический метод __add__,
        # который сформирует новый экземпляр класса Clock и этот новый экземпляр класса Clock вернёт метод __radd__.

    def __iadd__(self, other):
        print('__iadd__')  # Проверяем отработку данного магического метода.
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds += sc
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds - sc)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        print('__isub__')  # Проверяем отработку данного магического метода.
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds -= sc
        return self

    def __mul__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        return Clock(self.seconds * sc)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        print('__imul__')  # Проверяем отработку данного магического метода.
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        self.seconds *= sc
        return self

    def __truediv__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        if sc == 0:
            raise ZeroDivisionError('Деление на ноль недопустимо')

        return Clock(int(self.seconds / sc))  # Преобразуем в целочисленное значение.

    def __rtruediv__(self, other):
        return self / other  # Когда будет выполняться операция деления, то вызовется магический метод __truediv__,
        # который сформирует новый экземпляр класса Clock и этот новый экземпляр класса Clock вернёт метод __rtruediv__,
        # это также говорит о том, что не требуется преобразовывать возвращаемое значение в int.

    def __itruediv__(self, other):
        print('__itruediv__')  # Проверяем отработку данного магического метода.
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        if sc == 0:
            raise ZeroDivisionError('Деление на ноль недопустимо')

        self.seconds //= sc  # Единственный вариант - это использовать целочисленное деление. В противном случае будет
        # неправильный вывод или исключительная ситуация.
        return self

    def __floordiv__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        if sc == 0:
            raise ZeroDivisionError('Деление на ноль недопустимо')

        return Clock(self.seconds // sc)

    def __rfloordiv__(self, other):
        return self // other

    def __ifloordiv__(self, other):
        print('__ifloordiv__')  # Проверяем отработку данного магического метода.
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        if sc == 0:
            raise ZeroDivisionError('Деление на ноль недопустимо')

        self.seconds //= sc
        return self

    def __mod__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        if sc == 0:
            raise ZeroDivisionError('Деление на ноль недопустимо')

        return Clock(self.seconds % sc)  # Преобразуем в целочисленное значение.

    def __rmod__(self, other):
        return self % other

    def __imod__(self, other):
        print('__imod__')  # Проверяем отработку данного магического метода.
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть целым числом или экземпляром класса Clock')

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds

        if sc == 0:
            raise ZeroDivisionError('Деление на ноль недопустимо')

        self.seconds %= sc
        return self


c1 = Clock(1000)
c1.seconds = c1.seconds + 100  # Пока мы не прописали магический метод __add__ требуется именно так прибавлять секунды.
print(c1.get_time())
c1 += 100
print(c1.get_time())
"""
После прописи магического метода __add__ мы выполняем операцию сложения привычным способом.
Эквивалентом записи c1 = c1 + 100 является запись c1.__add__(100). После исполнения данного метода образуется новый
экземпляр класса Clock(c1.seconds + 100) -> seconds = 1100, после чего ссылка c1 перемещается на новый экземпляр
класса, ибо мы присваиваем c1 тому классу, который возвращаем в методе __add__ (т.е. Clock(self.seconds + other)).
Также из этих записей требуется заметить, что порядок постановки операндов крайне важен, ибо если написать
c1 = 100 + c1, то программа выдаст ошибку, т.к. по сути мы попытаемся вызвать метод __add__ для класса int.
Чтобы избежать данной ошибки, нам требуется определить методы __radd__() (для записи c1 = 100 + c1) и
__iadd__() (для записи c1 += 100) (прим. код отработает и без инициализации __iadd__, выдаст верное значение, но 
во время этой операции создаётся новый экземпляр класса Clock, а по идее этого делать не стоит, потому что новый 
экземпляр класса для таких операций создавать в принципе не надо, требуется лишь изменить значение его локальной 
переменной seconds).
"""

c2 = Clock(2000)
c3 = Clock(3000)
c4 = 100 + c1 + c2 + c3
print(c4.get_time())

# Проверка самостоятельной работы по определению других магических методов.
# Вычитание:
c5 = c4 - 100
print(c5.get_time())  # 01:43:20
c5 = 20 - c5
print(c5.get_time())  # 01:43:00
c5 -= 100
print(c5.get_time())  # __isub__ 01:41:20

# Умножение:
c5 = c4 * 2
print(c5.get_time())  # 03:30:00
c5 = 2 * c5
print(c5.get_time())  # 07:00:00
c5 *= 2
print(c5.get_time())  # __imul__ 14:00:00

# Деление:
c5 = c4 / 2
print(c5.get_time())  # 00:52:30
c5 = 2 / c5
print(c5.get_time())  # 00:26:15
c5 /= 3
print(c5.get_time())  # __itruediv__ 00:08:45

# Целочисленное деление:
c5 = c4 // 3
print(c5.get_time())  # 00:35:00
c5 = 3 // c5
print(c5.get_time())  # 00:11:40
c5 //= 3
print(c5.get_time())  # __ifloordiv__ 00:03:53

# Остаток от деления:
c5 = c4 % 1000
print(c5.get_time())  # 00:05:00
c5 = 200 % c4
print(c5.get_time())  # 00:01:40
c5 %= 100
print(c5.get_time())  # __mod__ 00:00:00
