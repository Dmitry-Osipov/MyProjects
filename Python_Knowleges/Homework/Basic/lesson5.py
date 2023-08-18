# сортировка слиянием
def merge_sort(numbers_list):
    if len(numbers_list) > 1:
        mid = len(numbers_list) // 2
        left_list = numbers_list[:mid]
        right_list = numbers_list[mid:]
        merge_sort(left_list)
        merge_sort(right_list)
        item = item_left = item_right = 0

        while item_left < len(left_list) and item_right < len(right_list):
            if left_list[item_left] < right_list[item_right]:
                numbers_list[item] = left_list[item_left]
                item_left += 1
            else:
                numbers_list[item] = right_list[item_right]
                item_right += 1
            item += 1

        while item_left < len(left_list):
            numbers_list[item] = left_list[item_left]
            item_left += 1
            item += 1

        while item_right < len(right_list):
            numbers_list[item] = right_list[item_right]
            item_right += 1
            item += 1


my_list = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(my_list)
print(my_list)


# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5
# Output: yes

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


input_number = int(input('Input number: '))
if is_prime(input_number):
    print("yes")
else:
    print("no")


# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность
# в обратном порядке.Примечание. В программе запрещается объявлять массивы и
# использовать циклы (даже для ввода и вывода).
# Input:    2 -> 3 4
# Output: 4 3

def reverse_number(variable):
    if len(variable) == 1:
        return variable
    else:
        return variable[-1] + reverse_number(variable[:-1])


print(reverse_number('1 3 5 7 9'))


# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью
# рекурсии. Функция не должна ничего выводить, только возвращать значение.

def f(a, b):
    if b == 0:
        return 1
    return a * f(a, b - 1)


print(f(2, 8))
