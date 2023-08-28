"""
Если имеется некий базовый класс Geom, и мы создаём дочерний класс Line, в котором дополнительно прописан метод draw, то
это называется расширением (extended) базового класса. Как правило дочерние классы создаются с целью расширения
базового класса:

class Geom:
    name = 'Geom'


class Line(Geom):
    def draw(self):
        print('Рисование линии')

Однако, если в базовом классе Geom уже есть метод draw(), то реализация метода draw() в классе Line является
переопределением (overriding). Т.е. поведение базового класса в дочернем в общем не меняется, только несколько меняется
функциональность:

class Geom:
    name = 'Geom'

    def draw(self):
        print('Рисование примитива')


class Line(Geom):
    def draw(self):
        print('Рисование линии')
"""


class Geom:
    name = 'Geom'

    def __init__(self):
        print('Инициализатор класса Geom')


class Line(Geom):
    def draw(self):
        print('Рисование линии')


l = Line()
"""
После отработки программы мы видим, что в консоли вышло сообщение об отработке инициализатора в базовом
классе Geom. В действительности происходит следующая цепочка вызовов:

l = Line()
    |
__call__(self, *args, **kwargs):
    obj = self.__new__(self, *args, **kwargs)
    self.__init__(obj, *args, **kwargs)
    return obj

Когда мы прописываем круглые скобки после вызова класса, то вызывается магический метод __call__, который в свою очередь
последовательно вызывает метод __new__ для создания экземпляра класса, а затем метод __init__ для его инициализации. Все 
эти методы изначально ищутся в начальном классе Line, если не находятся, то поиск продолжается в к соответствующим 
базовым классам (Geom -> object), в частности инициализатор (в примере 52 строка) был найден в классе Geom, а метод
__new__ прописан в классе object. Метод __call__ берётся из метакласса. Параметр self будет ссылаться на объект 
класса Line (l). Соответственно, если определить инициализатор в классе Line, то этот инициализатор и будет вызван.
"""


class Geom:
    name = 'Geom'

    def __init__(self):
        print('Инициализатор класса Geom')


class Line(Geom):
    def __init__(self):
        print('Инициализатор класса Line')

    def draw(self):
        print('Рисование линии')


l = Line()  # При запуске программы видим, что был вызван инициализатор класса Line. Но его лучше переписать
# следующим образом:


class Geom:
    name = 'Geom'

    def __init__(self):
        print('Инициализатор класса Geom')


class Line(Geom):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print('Рисование линии')


l = Line(0, 0, 10, 20)
print(l.__dict__)  # В целом всё работает, но добавим класс графического примитива прямоугольники. У него будут те же
# параметры, но добавим дополнительно fill (заливка):


class Geom:
    name = 'Geom'

    def __init__(self):
        print('Инициализатор класса Geom')


class Line(Geom):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = fill

    def draw(self):
        print('Рисование прямоугольника')


# По итогу в классе Line и Rect у нас получилось дублирование кода. Поправить это можно, если вынести общий код в
# базовый класс:


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор класса Geom для {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        print('Инициализатор Rect')
        self.fill = fill

    def draw(self):
        print('Рисование прямоугольника')


l = Line(0, 0, 10, 20)  # Инициализатор класса Geom для <class '__main__.Line'>.
r = Rect(1, 2, 3, 4)  # Инициализатор Rect. Для корректной работы программы в будущем нам потребуется
# сделать так, чтобы инициализатор брался из Geom (ибо там мы инициализируем начальные и конечные координаты).
# Как это сделать? В дочернем классе Rect мы должны явно вызвать инициализатор базового класса. Самый простой вариант:


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор класса Geom для {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        Geom.__init__(self, x1, y1, x2, y2)
        print('Инициализатор Rect')
        self.fill = fill

    def draw(self):
        print('Рисование прямоугольника')


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
"""
Видим 2 вывода инициализатора базового класса для Line и для Rect, как мы того и хотели: общий код находится в
инициализаторе базового класса, и он вызывается для обоих дочерних классов. Однако вот так явно указывать базовый
класс в инициализаторе дочернего класса - это не совсем лучшая практика, потому что имена базовых классов и иерархия
наследования могут меняться. Поэтому в Python для обращения к базовому классу используется специальная функция
super(). Она возвращает ссылку на объект-посредник, через который происходит вызов базового класса (а потому self при
использовании функции super() прописывать уже не нужно, потому что self возвращает объект, а мы через объект вызываем
метод __init__, поэтому от нас необходимы только параметры). 
Следует обратить внимание, что инициализатор базового класса нужно вызывать в первую очередь. С чем это связано? Если мы
в инициализаторе базового класса неявно будем менять параметр fill, а затем инициализатор базового класса в дочернем 
классе будем вызывать в последнюю очередь, то параметр fill у нас изменится на то значение, которое мы присвоили ему в 
инициализаторе базового класса. 
Кроме того, такой вызов методов базового класса через функцию super() называется делегированием. Т.е. мы в дочернем 
классе как бы делегируем некие действия, вызывая инициализатор базового класса (в данном случае мы просто создаём 
локальные свойства наших геометрических примитивов).
"""


class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор класса Geom для {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print('Инициализатор Rect')
        self.fill = fill

    def draw(self):
        print('Рисование прямоугольника')


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
print(r.__dict__)
