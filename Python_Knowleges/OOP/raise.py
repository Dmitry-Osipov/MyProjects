"""
В Python есть специальная конструкция, которая позволяет генерировать исключения - raise Класс-исключение.
"""

print('Я к вам пишу - чего же боле?')
print('Что я могу ещё сказать?')
print('Теперь, я знаю, в вашей воле')
raise ZeroDivisionError('Деление на 0')  # Благодаря комментарию в исключении можно подсказать программисту, в чём
# именно возникает ошибка.
print('Меня презреньем наказать.')
print('Но вы, к моей несчастной доле')
print('Хоть каплю жалости храня,')
print('Вы не остановите меня.')

e = ZeroDivisionError('Деление на 0')
raise e  # Аналогично с прошлой записью возникает ошибка. Это говорит о том, что при желании мы можем создать
# переменную, которая будет ссылаться на класс-исключение.
raise 'Деление на 0'  # TypeError: exceptions must derive from BaseException - без обозначения типа ошибки невозможно
# вывести предупреждающую надпись.

"""
Но зачем самим генерировать исключения? Как известно, невозможно выявить все исключительные ситуации заранее. Так что 
программист в какой-то функции может генерировать свои исключения со своими комментариями, если это необходимо. 
К примеру, если на принтер не отправляются данные, то может быть вызвано своё исключение.
"""


class PrintData:
    def print(self, data):  # Метод для печати данных.
        self.send_data(data)
        print(f'Печать: {str(data)}')

    def send_data(self, data):  # Метод дял отправки данных.
        if not self.send_to_print(data):
            raise Exception('Принтер не отвечает')

    def send_to_print(self, data):  # Метод для проверки, возможна ли отправка.
        return False


p = PrintData()
try:
    p.print('123')  # Exception: Принтер не отвечает
except Exception:
    print('Принтер не отвечает')


# Если же заменить на True, то всё отработает корректно.


class PrintData:
    def print(self, data):  # Метод для печати данных
        self.send_data(data)
        print(f'Печать: {str(data)}')

    def send_data(self, data):  # Метод дял отправки данных
        if not self.send_to_print(data):
            raise Exception('Принтер не отвечает')

    def send_to_print(self, data):  # Метод для проверки, возможна ли отправка
        return True


p = PrintData()
p.print('123')

"""
Но почему мы генерируем исключение именно Exception?
По иерархии исключений класс Exception наследует от себя множество других различных исключений (другие дочерние для 
BaseException классы - SystemExit, GeneratorExit, KeyboardInterrupt - используются крайне редко и специализировано). 
Поэтому когда мы хотим обработать или выбросить исключение, то основываемся на классе Exception. Создадим свой класс с 
базовым классом Exception. Т.к. мы наследуемся от базового класса-исключения, то метод обработки исключений у нас уже 
есть, так что внутри нашего класса-исключения можно ничего не прописывать. 
Ценность наших собственных классов-исключений в том, что мы можем предпринять какие-то более конкретные действия для 
устранения ошибок во время работы программы.
"""


class ExceptionPrintSendData(Exception):  # На практике, если класс пустой, то пишут комментарий, содержащий информацию:
                                          # для чего нужен этот класс. Хотя, конечно, можно прописать свой функционал.
    """Класс исключения при отправке данных принтеру"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка: {self.message}'  # Если прописали аргументы при генерации исключения, то они покажутся: Ошибка:
        # Принтер не отвечает. Однако, если при генерации исключения мы не оставили комментария (аргумента), то Ошибка:
        # None - что мы и прописали в инициализаторе.


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'Печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('Принтер не отвечает')

    def send_to_print(self, data):
        return False


p = PrintData()
p.print('123')

"""
Также мы можем прописать общий класс исключений ExceptionPrint, соответственно, можем указать свою иерархию 
наследования у исключений. Таким образом, мы можем её использовать в блоке try-except.
"""


class ExceptionPrint(Exception):
    """Общий класс исключения принтера"""


class ExceptionPrintSendData(ExceptionPrint):
    """Класс исключения при отправке данных принтеру"""


def __init__(self, *args):
    self.message = args[0] if args else None


def __str__(self):
    return f'Ошибка: {self.message}'


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'Печать: {str(data)}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrint('Принтер не отвечает')

    def send_to_print(self, data):
        return False


p = PrintData()
try:
    p.print('123')
except ExceptionPrintSendData:
    print('Принтер не отвечает')
except ExceptionPrint:
    print('Общая ошибка печати')
