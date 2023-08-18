from math import factorial
from random import randint


# Императивное программирование:
# Задача 1: Подсчет суммы четных чисел от 1 до N. Напишите программу, используя цикл, которая находит сумму всех четных
# чисел в диапазоне от 1 до заданного числа N.


def summ_even(number):
    summ = 0
    for item in range(1, number + 1):
        if item % 2 == 0:
            summ += item

    return summ


user_number = int(input('Input number: '))
print(summ_even(user_number))


# Задача 2: Поиск наименьшего числа в списке. Напишите программу, которая находит наименьшее число в заданном списке
# с помощью цикла.


def find_min_value(some_list):
    min_value = max(some_list)  # Использование данной функции является декларативной парадигмой, но без данной функции
    # могут быть некорректными значения для минимального значения (в силу того, что нет границы у int в Python).

    for item in some_list:
        if min_value > item:
            min_value = item

    return min_value


user_list = [1, 5, 6, 8, -7, 0, 6, 1, 9, -6, 8]
print(find_min_value(user_list))


# Задача 5: Поиск простых чисел. Напишите программу, которая находит все простые числа в заданном диапазоне от 1 до N.


def is_prime(number, divisor=2):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % divisor == 0:
        return False
    if divisor * divisor > number:
        return True

    return is_prime(number, divisor + 1)


user_end = int(input('Input the number that ends our list: '))
if user_end <= 1:
    raise ValueError('Your number cannot be less than 2')

new_user_list = []
for i in range(1, user_end + 1):
    new_user_list.append(i)

temp_list = []
for item in new_user_list:
    if is_prime(item):
        temp_list.append(item)

print(new_user_list)
print(temp_list)


# Задача 6: Упорядочивание списка. Напишите программу, которая сортирует список чисел в порядке возрастания с
# использованием пузырьковой сортировки или другого метода сортировки.


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = [x for x in array[1:] if x <= pivot]
    right = [x for x in array[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


user_count = int(input('Input the length of list: '))
if user_count <= 0:
    raise ValueError('The length of the list cannot be less than or equal to 0: ')

random_list = []
for i in range(user_count):
    num = randint(0, 9)  # Использование данной функции является декларативной парадигмой, но я использовал
    # данную функцию для получения полностью случайных чисел, ибо пользователю было бы долго вводить каждый элемент.

    random_list.append(num)

print(quick_sort(random_list))


# Декларативное программирование:
# Задача 3: Вычисление факториала числа. Напишите программу, которая находит факториал заданного числа N с
# использованием рекурсии или встроенных функций.


def find_factorial(number):
    return factorial(number)


print(find_factorial(5))


# Задача 4: Поиск уникальных элементов в списке. Напишите программу, которая создает новый список, содержащий только
# уникальные элементы из исходного списка.


def find_uniq_elem(numbers_list):
    return list(set(numbers_list))


print(find_uniq_elem([1, 1, 2, 4, 2, 6, 4, 1, 2, 6, 8, 9, 0, 0, 4]))


# Задача 7: Поиск подстроки. Напишите программу, которая находит все вхождения заданной подстроки в строке с
# использованием встроенных функций.


def find_repeat(parent_string, user_string):
    start_index = 0
    found_indexes = []
    while True:
        index = parent_string.find(user_string, start_index)
        if index == -1:
            break

        found_indexes.append(index)
        start_index = index + 1

    return found_indexes


print(find_repeat('Hello, world! Goodbye, world!', 'world'))


# Задача 8: Вычисление суммы цифр числа. Напишите программу, которая вычисляет сумму всех цифр заданного числа,
# используя математические операции и деление нацело.


def sum_digits(number):
    """
    Согласно условию задачи, написание данного метода сводилось к императивной парадигме. Однако сама задача
    находится в блоке декларативного программирования. Соответственно, данная функция решает задачу
    декларативной парадигмой
    """
    if number >= 0:
        return sum(int(digit) for digit in str(number))

    return sum(int(digit) for digit in str(abs(number)))


number = int(input('Input your number: '))
print(sum_digits(number))
