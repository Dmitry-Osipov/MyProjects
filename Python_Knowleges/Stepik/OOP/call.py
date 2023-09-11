from math import sin, pi


class Counter1:
    def __init__(self):
        self.__counter = 0


c1 = Counter1()  # Автоматически вызывается метод __call__, внутри которого отрабатывают сначала магический метод
# __new__, а затем магический метод __init__.
c1()  # Экземпляры класса мы не можем вызывать подобно функциям. Они не вызываемы, т.к. не определён магический
# метод __call__.


class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter


c = Counter()
c()  # Видим, как отработал метод __call__. Благодаря ему мы теперь можем вызывать экземпляры класса подобно функциям.
c()
c()
res = c()
print(res)  # Выводит 4, т.к. вызвали функцию 4 раза, счётчик увеличился на соразмерное число, вывели его в консоль.
c2 = Counter()
res2 = c2()  # Вывело 1, т.к. счётчики работают независимо друг от друга.
print(res2)

# Добавили шаг счётчика с установленным значением 1. Таким образом, можно вызывать экземпляр класса как с аргументом,
# так и без него.
c3 = Counter()
c3()
c3(2)
res3 = c3(-5)
print(res3)


# Примеры использования __call__:
# 1) замена замыкания функций:


class StripChars:
    """Удаляет из начала и конца строки определённые символы"""
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')

        return args[0].strip(self.__chars)


s1 = StripChars('?:!.; ')
res = s1(' Hello World! ')
print(res)
s2 = StripChars(' ')
res2 = s2(' Hello world! ')
print(res2)


# 2) реализация декораторов с помощью классов:


class Derivate:
    """Класс-декоратор, который позволяет вычислять производные определённой функции в некой точке x"""
    def __init__(self, func):
        self.__func = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__func(x + dx) - self.__func(x)) / dx


# @Derivate  # Т.к. наш класс является декоратором, то можно использовать символ @ непосредственно над функцией
def df_sin(value):
    return sin(value)


print(df_sin(pi/3))
df_sin = Derivate(df_sin)  # Вариант в лоб. Фактически, мы превратили функцию в экземпляр класса. Т.е. df_sin теперь
# будет ссылаться не на функцию, а на экземпляр класса. И когда мы её будем вызывать (т.е. будем вызывать экземпляр
# класса), то сработает метод __call__.
print(df_sin(pi/3))
