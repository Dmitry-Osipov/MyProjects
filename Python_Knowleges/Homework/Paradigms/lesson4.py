from functools import reduce
from typing import Callable


# **На выбор 4 задачи(или все для продвинутых)
# __
# Рекурсивная сумма: Напишите рекурсивную функцию, которая вычисляет сумму всех чисел от 1 до n. Например, для n = 5
# результат должен быть 1 + 2 + 3 + 4 + 5 = 15.


def find_sum_recursion(number: int) -> int:
    """
    Рекурсивно считает сумму чисел от 1 до заданного числа.
    :param number: Целое число, до которого нужно посчитать сумму.
    :return: Целое число, которое является суммой чисел от 1 до заданного числа.
    """
    if not isinstance(number, int):
        number = int(number)

    if number == 0:
        return 0
    elif number > 0:
        return number + find_sum_recursion(number - 1)
    else:
        return number + find_sum_recursion(number + 1)


print(f'Сумма чисел от 1 до 5: {find_sum_recursion(5)}')

# Факториал: Напишите рекурсивную функцию для вычисления факториала числа n. Факториал числа n обозначается как n! и
# равен произведению всех положительных целых чисел от 1 до n.


def find_factorial_recursion(number: int) -> int:
    """
    Рекурсивно считает факториал заданного числа.
    :param number: Целое число, от которого будет производиться поиск факториала.
    :return: Целое число, которое является факториалом заданного числа.
    """
    if not isinstance(number, int):
        number = int(number)

    if number == 0:
        return 0

    if number == 1:
        return 1

    if number < 0:
        number = abs(number)

    return number * find_factorial_recursion(number - 1)


print(f'Факториал числа 5: {find_factorial_recursion(5)}')

# __
# Фибоначчи через рекурсию: Напишите рекурсивную функцию для вычисления числа Фибоначчи с индексом n. Напоминаю, что
# последовательность Фибоначчи определяется как: F(0) = 0, F(1) = 1 и F(n) = F(n-1) + F(n-2) для n > 1.


def find_fib_by_index(index: int) -> int:
    """
    Рекурсивно ищет число Фибоначчи по заданному индексу.
    :param index: Целое число, которое является индексом последовательности Фибоначчи.
    :return: Целое число, которое находится по заданному индексу в последовательности Фибоначчи.
    """
    if not isinstance(index, int):
        index = int(index)

    if index <= 0:
        return 0

    if index in [1, 2]:
        return 1

    return find_fib_by_index(index - 1) + find_fib_by_index(index - 2)


print(f'Число Фибоначчи по индексу 7: {find_fib_by_index(7)}')

# __
# Функция-редуктор: Напишите функцию-редуктор (или функцию свертки), которая принимает начальное значение и список
# чисел, а затем возвращает произведение всех чисел в списке. Используйте эту функцию для вычисления произведения
# чисел в списке.


def reducer_product(acc, current_value):
    """
    Функция-редуктор для вычисления произведения чисел.
    :param acc: Целое число, которое является начальным значением для вычисления.
    :param current_value: Целое число, которое является текущим значением из списка чисел.
    :return: Целое число, которое является результатом умножения аккумулятора на текущее значение.
    """
    return acc * current_value


numbers = [2, 3, 4, 5]
product_result = reduce(reducer_product, numbers, 1)
"""
Работа функции reduce:
1)Принимает три аргумента:
    - Функцию, которая будет применяться к элементам. Эта функция должна принимать два аргумента: аккумулятор и 
      текущий элемент.
    - Последовательность (например, список), которую нужно обработать.
    - Начальное значение аккумулятора.
2) Функция reduce начинает с начального значения аккумулятора и первого элемента из последовательности.
3) Затем она вызывает переданную функцию с текущим значением аккумулятора и следующим элементом последовательности. 
Результат этого вызова становится новым значением аккумулятора.
4) reduce повторяет этот процесс для всех оставшихся элементов в последовательности, каждый раз обновляя значение 
аккумулятора.
5) В конечном итоге, когда все элементы обработаны, функция reduce возвращает окончательное значение аккумулятора.

Важно помнить, что функция, которую вы передаете в reduce, должна быть такой, чтобы она могла быть последовательно 
применена к аккумулятору и каждому элементу в последовательности.
"""

print("Произведение чисел:", product_result)

# __
# Замыкание: Создайте функцию, которая принимает некоторое число n и возвращает функцию, которая прибавляет n к своему
# аргументу. Продемонстрируйте использование этой функции-замыкания.


def create_adder(number):
    """
     Функция-замыкание для создания функции, которая прибавляет number к своему аргументу.
    :param number: Число, которое будет прибавляться к аргументу.
    :return: Функцию, прибавляющую number к своему аргументу.
    """
    def add_number(summand):
        return number + summand

    return add_number


add_5 = create_adder(5)  # Создаём функцию-замыкание, которое будет прибавлять 5.
result_func = add_5(10)  # Пример использование функции замыкания (будет прибавлять к аргументу свой аргумент).
print(f'Пример работы замыкания для 5 и 10: {result_func}')

# __
# Функции-редукторы для списков: Напишите функцию-редуктор, которая принимает список строк и возвращает строку,
# состоящую из объединенных элементов списка через запятую. Например, для списка ["apple", "banana", "cherry"] результат
# должен быть "apple, banana, cherry".


def join_with_comma(acc, current_value):
    """
    Функция-редуктор для объединения элементов списка строк через запятую.
    :param acc: Аккумулятор, cтрока с предыдущими объединенными элементами.
    :param current_value: Текущая строка из списка.
    :return: Строка с добавленной текущей строкой и запятой.
    """
    if acc:
        return f'{acc}, {current_value}'

    return current_value


string_list = ['apple', 'banana', 'cherry']
result_string = reduce(join_with_comma, string_list, '')  # Логика работы аналогично примеру выше.

# __
# Монады: Реализуйте класс IO (ввод-вывод), который будет представлять действие ввода-вывода. Создайте функцию-редуктор,
# которая будет принимать список IO и последовательно выполнять каждое действие, сохраняя результаты в список.


class IO:
    def __init__(self, action):
        self.action = action

    def perform(self):
        return self.action()


def io_reducer(acc, current_value):
    """
    Функция-редуктор для выполнения последовательных действий IO.
    :param acc: Аккумулятор, список результатов выполнения действий.
    :param current_value: Текущее действие IO.
    :return: Список результатов выполнения действий.
    """
    result = current_value.perform()
    return acc + [result]


io_actions = [IO(lambda: 'Hello'), IO(lambda: 'World'), IO(lambda: 'Python')]  # Создаём список действий IO.
result_list = reduce(io_reducer, io_actions, [])  # Используем функцию для выполнения действий и сохранения результата.
print(f'Результаты: {result_list}')

# __
# Ленивые вычисления: Напишите функцию, которая будет генерировать бесконечную последовательность простых чисел.
# Используйте ленивые вычисления, чтобы генерировать только те числа, которые действительно нужны.


def is_prime(number):
    """
    Функция по определению, является ли число простым.
    :param number: Целое число, для которого требуется определение.
    :return: Булева-значение: True - если число является простым, и False - если число не является простым.
    """
    if not isinstance(number, int):
        number = int(number)

    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    # Здесь i начинается с 5, потому что в проверке на простоту числа мы пропускаем проверку деления на числа,
    # кратные 2 и 3. Начиная с 5, мы проверяем только числа вида 6k ± 1, где k - целое число. Это связано с тем, что все
    # остальные простые числа могут быть представлены в виде 6k ± 1 (за исключением 2 и 3). Именно поэтому мы начинаем
    # с 5 и затем прибавляем 6 к i, чтобы проверить следующие возможные простые числа.

    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_generator():
    """
    Генератор для бесконечной последовательности чисел.
    """
    yield 2
    yield 3
    # yield 2 и yield 3 используются для генерации первых двух простых чисел.

    current_number = 5  # current_number установлен в 5, так как мы начинаем проверку с этого числа, согласно стратегии
    # проверки только чисел вида 6k ± 1.

    while True:
        if is_prime(current_number):   # Затем, мы последовательно проверяем каждое простое число (используя функцию
            # is_prime), и если текущее число простое, мы добавляем его в последовательность с помощью yield.
            yield current_number
        # После этого мы увеличиваем current_number на 2 и повторяем проверку и добавление для следующего числа.
        current_number += 2

        if is_prime(current_number):
            yield current_number
        # Затем мы увеличиваем current_number на 4 и повторяем проверку и добавление. Это связано с тем, что в
        # последовательности простых чисел, разница между двумя соседними числами "6k - 1" и "6k + 1" составляет 2 и 4.
        current_number += 4


primes = prime_generator()
for _ in range(1, 11):  # Вывод первых 10 чисел.
    if _ == 3:
        print(f'Ваше {_}-ье простое число: {next(primes)}')
    else:
        print(f'Ваше {_}-ое простое число: {next(primes)}')

# __
# Функции высшего порядка: Создайте функцию высшего порядка, которая принимает другую функцию и список чисел. Функция
# высшего порядка должна возвращать список, содержащий результаты применения переданной функции к каждому
# элементу списка.


def higher_order_function(function: Callable, numbers_list: list):
    """
    Функция высшего порядка для применения функции к списку чисел.
    :param function: Функция, которая будет применяться к каждому элементу списка.
    :param numbers_list: Список, множество, словарь или кортеж.
    :return: Список результатов применения функции к каждому элементу.
    """
    if isinstance(numbers_list, str):
        raise TypeError('Ожидается некорректный вывод строки, преобразуйте список в list, set, dict или tuple')

    results = []
    for number in numbers_list:
        results.append(function(number))

    return results


def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
squared_list = higher_order_function(square, numbers)
print(f'Результаты возведения в квадрат списка {numbers}: {squared_list}')

# __
# Чистые функции и неизменяемость данных: Напишите функцию, которая принимает список чисел и возвращает новый список,
# в котором каждый элемент умножен на 2. Убедитесь, что вы используете только чистые функции и не изменяете
# исходный список.


def doubled_list(numbers_list: list) -> list:
    """
    Чистая функция (не изменяет внешнюю среду) для удвоения чисел внутри списка, множества или словаря.
    :param numbers_list: Список, множество, словарь или кортеж, элементы (ключи для словаря) которого нужно удвоить.
    :return: Список удвоенных значений каждого элемента первоначального списка.
    """
    if isinstance(numbers_list, str):
        raise TypeError('Ожидается некорректный вывод строки, преобразуйте список в list, set, dict или tuple')

    return [x * 2 for x in numbers_list]


original_list = [1, 2, 3, 4, 5]
print(f'Удвоенный список от {original_list}: {doubled_list(original_list)}')
