# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел.
# Все числа списка находятся на разных строках.
# Ввод:			Вывод:
# 1 2 3 2 3			2


# 1 вариант:
def find_couple(numbers):
    count = 0
    temp_dict = {}
    for i, item in enumerate(numbers, 1):
        if item not in temp_dict:
            temp_dict[item] = count
        else:
            temp_dict[item] = count + 1
    for keys, values in temp_dict.items():
        if values > 0:
            count += 1
    return count


print(find_couple([1, 2, 3, 2, 3, 4, 5, 3, 4]))

# 2 вариант:
list1 = [1, 2, 3, 2, 3, 2]


def count_double(my_list):
    count = 0
    for i, item1 in enumerate(my_list, start=0):
        for item2 in my_list[i + 1:]:
            if item1 == item2:
                count += 1
                my_list.remove(item2)
                my_list.pop(i)
    return count


print(count_double(list1))


# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1,
# но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу n выведите
# все пары дружественных чисел, каждое из которых не превосходит n. Программа получает на вход одно натуральное число n,
# не превосходящее 10^5. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит n.
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).
# Ввод:			Вывод:
# 300			220 284


def get_divisors_sum(number):
    divisors_sum = 1
    for i in range(2, int(number ** 0.5) + 1):  # Для оптимизации вычислений, мы ищем делители только до квадратного корня числа number
        if number % i == 0:
            divisors_sum += i
            if i != number // i:  # Дополнительная проверка, чтобы избежать двойного учета делителей, если число number является полным квадратом.
                divisors_sum += number // i  # Если число number не является полным квадратом, добавляем number // i (то есть другой делитель) к сумме делителей
    return divisors_sum


def find_friendly_numbers(user_number):
    for first_item in range(1, user_number + 1):
        second_item = get_divisors_sum(first_item)
        if second_item > first_item and get_divisors_sum(second_item) == first_item and second_item <= user_number:  # Это условие проверяет, являются ли числа first_item и second_item дружественными. Для этого сравниваются их суммы делителей, и если числа являются дружественными и не превосходят user_number, то выполняется код внутри условия
            print(first_item, second_item)


your_number = int(input("Input number: "))
find_friendly_numbers(your_number)
