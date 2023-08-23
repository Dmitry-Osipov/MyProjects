from abc import ABC, abstractmethod


# На Выбор Часть 1 или Часть 2

# Часть 1: Парадигмы программирования и ООП
# __
# Императивная vs Декларативная парадигма:
# Опишите задачу на Python, решение которой может быть представлено как императивное решение и как декларативное
# решение. Объясните, в чем различие между двумя подходами и какой из них предпочтительнее в данном случае.

"""
Рассмотрим задачу по поиску среднего арифметического в массиве. Данная задача может быть решена как императивно, так и
декларативно. Для начала рассмотрим императивный способ.

В императивном подходе: мы будем использовать цикл для итерации по всем объектам. Создадим 2 переменные, в одну будем
суммировать значение элементов, а во вторую количество итераций (что равно длине коллекции). В конце возвращаем сумму,
делённую на количество. Таким образом, мы получили среднее арифметическое, делая упор на процессе получения
этого значения, а не на желаемом результате.

В декларативном подходе: мы воспользуемся двумя встроенным функциями без импорта библиотек. Создаём переменную,
которая будет ссылаться на результат отработки встроенной функции (summ = sum(array)). Далее создаём вторую переменную,
которая определяет длину коллекции (length = len(array)). В конце возвращаем сумму элементов, делённую на длину
коллекции. Таким образом, мы получили среднее арифметическое, делая упор на желаемом результате, а не процессе получения
этого значения.
"""

# __
# ООП Концепции:
# Создайте класс Person, который имеет атрибуты name, age и метод introduce(), выводящий информацию о человеке. Создайте
# несколько объектов этого класса и вызовите метод introduce() для каждого из них.


class Person:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str) and isinstance(age, int) and 0 >= age >= 120:
            raise ValueError('Incorrect values for name and/or age')

        self.name = name
        self.age = age

    def introduce(self):
        return f'My name is {self.name}. I am {self.age} y.o.'


me = Person('Dmitry', 22)
friend = Person('Nadezhda', 21)
mom = Person('Irina', 41)
print(me.introduce(), friend.introduce(), mom.introduce(), sep='\n')

# __
# Шаблон Singleton:
# Реализуйте паттерн Singleton на языке Python для класса Logger, который будет использоваться для логирования
# информации в приложении. Гарантируйте, что только один экземпляр класса Logger будет создан.


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_file = open("log.txt", "w")
        return cls._instance

    def log(self, message):
        self.log_file.write(message + "\n")

    def close(self):
        self.log_file.close()


logger1 = Logger()
logger1.log("Message 1 from logger1")

logger2 = Logger()
logger2.log("Message 2 from logger2")

logger1.close()

print(logger1 is logger2)

# __
# Шаблон Наблюдатель:
# Реализуйте паттерн Наблюдатель на языке Python для системы уведомлений. Создайте класс NotificationSystem
# (наблюдаемый объект), который будет иметь методы для добавления наблюдателей и уведомления о событиях.
# Создайте несколько наблюдателей, реагирующих на уведомления.


class NotificationSystem:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class User:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise ValueError('The name should be a string')

        self._name = name

    def update(self, message):
        print(f'{self._name} received a notification: {message}')


notification_system = NotificationSystem()  # Создаём наблюдательный объект (система уведомлений)
first_user = User('Tom')  # Создаём наблюдателей (пользователи)
second_user = User('Ann')
third_user = User('Alex')

notification_system.attach(first_user)  # Подписываем пользователей на уведомления (наблюдатель начинает слежку)
notification_system.attach(second_user)
notification_system.attach(third_user)

notification_system.notify('New message: Hello, everyone!')  # Уведомляем наблюдателей о действии

notification_system.detach(first_user)  # Отписываем одного пользователя (наблюдатель прекращает слежку)

notification_system.notify('New message: Meeting at 2 PM!')  # Проверяем отписку

# __
# Часть 2: Паттерны проектирования
# __
# Фабричный метод:
# Реализуйте паттерн Фабричный метод на языке Python для создания геометрических фигур. Создайте класс ShapeFactory,
# имеющий метод create_shape(), который возвращает объекты различных геометрических фигур.


class Shape(ABC):  # Абстрактный класс для геометрической фигуры
    @abstractmethod
    def draw(self):
        pass


# Конкретные классы геометрических фигур:
class Circle(Shape):
    def draw(self):
        return "Drawing a circle"


class Square(Shape):
    def draw(self):
        return "Drawing a square"


class Triangle(Shape):
    def draw(self):
        return "Drawing a triangle"


class ShapeFactory:  # Фабричный метод для создания геометрических фигур
    @staticmethod
    def create_shape(shape_type: str):
        if not isinstance(shape_type, str):
            raise ValueError('The shape type should be a string')

        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "square":
            return Square()
        elif shape_type.lower() == "triangle":
            return Triangle()
        else:
            raise ValueError("Invalid shape type")


factory = ShapeFactory()

circle = factory.create_shape("Circle")
print(circle.draw())

square = factory.create_shape("SquaRe")
print(square.draw())

triangle = factory.create_shape("trianglE")
print(triangle.draw())

# __
# Адаптер:
# Создайте класс ElectricSocket, который имеет метод supply_electricity(voltage). Реализуйте класс USPlugAdapter,
# который адаптирует розетку стандарта США к европейскому стандарту. Создайте объекты и продемонстрируйте
# передачу электроэнергии через адаптер.


class ElectricSocket:  # Класс, представляющий розетку
    def supply_electricity(self, voltage):
        print(f"Supplying electricity at {voltage} volts")


class USPlugAdapter:  # Класс адаптера для стандарта США к европейскому стандарту
    def __init__(self, socket):
        self.socket = socket

    def supply_electricity(self, voltage):
        converted_voltage = voltage * 2.54
        self.socket.supply_electricity(converted_voltage)


euro_socket = ElectricSocket()
us_adapter = USPlugAdapter(euro_socket)

voltages = 110
us_adapter.supply_electricity(voltages)  # Адаптер адаптирует напряжение под евростандарт

# __
# Стратегия:
# Реализуйте паттерн Стратегия на языке Python для сортировки списка чисел. Создайте класс SortStrategy, имеющий метод
# sort(numbers), и несколько конкретных стратегий для различных методов сортировки.


class SortStrategy:  # Базовый класс стратегии
    def sort(self, numbers):
        if not isinstance(numbers, list):
            raise TypeError('The array must be a list')

        raise NotImplementedError('The sort method must be overridden in subclass')


# Конкретные стратегии:
class QuickSortStrategy(SortStrategy):
    def sort(self, numbers):
        print('Using quick sort')
        return self.quick_sort(numbers)

    def quick_sort(self, numbers):
        if len(numbers) <= 1:
            return numbers

        pivot = numbers[0]
        left = [x for x in numbers[1:] if x < pivot]
        right = [x for x in numbers[1:] if x >= pivot]
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)


class MergeSortStrategy(SortStrategy):
    def sort(self, numbers):
        print('Using merge sort')
        return self.merge_sort(numbers)

    def merge_sort(self, numbers):
        if len(numbers) <= 1:
            return numbers

        middle = len(numbers) // 2
        left_half = numbers[:middle]
        right_half = numbers[middle:]

        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result


class BubbleSortStrategy(SortStrategy):
    def sort(self, numbers):
        print('Using bubble sort')
        return self.bubble_sort(numbers)

    def bubble_sort(self, numbers):
        for i in range(len(numbers) - 1):
            for j in range(len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


class SortContext:  # Контекст
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort(self, numbers):
        return self.strategy.sort(numbers)


user_numbers = [9, 1, 5, 2, 7, 4, 8, 3]

context = SortContext(QuickSortStrategy())
sorted_numbers = context.sort(user_numbers)
print(f'Sorted list: {sorted_numbers}')

context.set_strategy(MergeSortStrategy())
sorted_numbers = context.sort(user_numbers)
print(f'Sorted list: {sorted_numbers}')

context.set_strategy(BubbleSortStrategy())
sorted_numbers = context.sort(user_numbers)
print(f'Sorted list: {user_numbers}')

# __
# Декоратор:
# Создайте класс Coffee с методом cost(), возвращающим стоимость кофе. Реализуйте декораторы Sugar и Milk, которые
# добавляют сахар и молоко к кофе, соответственно. Создайте объект кофе и последовательно примените к нему декораторы,
# затем выведите общую стоимость.


class Coffee:
    def cost(self):
        return 5


class Sugar:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1


class Milk:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2


simple_coffee = Coffee()  # Создаём обычное кофе

# Применяем декораторы:
coffee_with_sugar = Sugar(simple_coffee)
coffee_with_milk = Milk(simple_coffee)
top_coffee = Milk(coffee_with_sugar)

print(f'Cost of simple coffee: {simple_coffee.cost()}\n'
      f'Cost of coffee with sugar: {coffee_with_sugar.cost()}\n'
      f'Cost of coffee with milk: {coffee_with_milk.cost()}\n'
      f'Cost of coffee with sugar and milk: {top_coffee.cost()}')
