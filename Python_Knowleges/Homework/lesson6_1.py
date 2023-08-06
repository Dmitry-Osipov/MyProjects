import random


# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def get_progression_list(start_number, step, quantity):
    temp_list = [start_number]
    while quantity > 1:
        temp_list.append(start_number + step)
        start_number += step
        quantity -= 1
    return temp_list


user_number, step_progression, user_quantity = map(int, input('Input numbers of start, step and stop separated '
                                                              'by a space: ').split())

print(get_progression_list(user_number, step_progression, user_quantity))

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


def find_list_index(numbers_list, min_number, max_number):
    temp_list = []
    for i, item in enumerate(numbers_list, 0):
        if min_number <= item <= max_number:
            temp_list.append(i)
    return temp_list


min_user_number, max_user_number = map(int, input('Input min and max numbers separated by a space: ').split())
size_list = 10
random_list = []
for j in range(size_list):
    number = random.randint(1, 100)
    random_list.append(number)
print(random_list)  # Для проверки

print(find_list_index(random_list, min_user_number, max_user_number))
