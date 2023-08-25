# Лекция.

# Задача: определить допустимые делители для числа

def find_available_divider(number):
    result_list = []
    for divider in range(1, number + 1):
        if number % divider == 0:
            result_list.append(divider)

    return result_list


print(find_available_divider(12))


# Данный алгоритм является линейным. Линейная зависимость характеризуется симметричным ростом количества шагов
# относительно увеличения объёма входных данных. Для числа 12 будет 12 действий по перебору элементов, для 25 - 25.

# Усложним задачу: требуется написать алгоритм, который будет искать простые числа на определённом отрезке от 0 до n.


def find_simple_numbers(max_number_in_list):
    result_list = []
    counter = 0
    for i in range(1, max_number_in_list + 1):
        simple = True
        for j in range(2, i):
            counter += 1
            if i % j == 0:
                simple = False
        if simple:
            result_list.append(i)

    print(f'Counter: {counter}')
    return result_list


print(find_simple_numbers(6))

# С ростом числа количество входящих операций растёт гораздо быстрее. Данная зависимость называется квадратичной.
# Она характеризуется резким ростом сложности относительно роста размера входных данных.

"""
Для описания сложности алгоритма существует общепринятая нотация - O(f(n)) или просто O(n), где n - это размер входных 
данных. 
Например, алгоритм перебора массива циклом for имеет сложность O(n). С ростом n на x, количество шагов алгоритма
тоже вырастает на x.
А использование вложенного цикла for уже будет иметь сложность O(n^2), например, при n = 3 цикл сделает 9 итераций, 
а при n = 4 - уже 16 и т.д.
Нотация большого О не даёт точного количества действий. Как минимум, мы не учитываем преобразование из двоичной системы 
в десятичную, не учитываем выделение временной памяти для заполнения массива, не учитываем операцию сравнения чисел 
и т.п. Чётко это высказывание можно понять, добавив счётчик операций для вложенного цикла. Для числа отрезка от 1 до 4
потребовалось 3 действия для нахождения всех простых чисел. При этом, увеличивая длину отрезка на 1, мы получим на 
счётчике цифру 6. Для 6 счётчик увеличился до 10. Однако данный счётчик чётко показывает резкое увеличение количества 
операций с постепенным увеличением входных данных.
Оценка сложности алгоритма - это достаточно абстрактная вещь, которая не призвана, чтобы делать точный расчёт сложности.
Однако она может помочь при работе с высоко нагруженными системами.
"""


# Помимо двух перечисленных выше алгоритмов существует ещё более крутой график (а на самом деле один из наименее
# релевантных с точки зрения использования в программировании) - это график экспоненциальной зависимости. Пример:
# задача по поиску шанса выпадения определённой суммы на игральных костях (для трёх шестигранных кубиков).


def find_sum_dice(amount):
    count = 0
    success_result = 0
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i + j + k == amount:
                    success_result += 1
                count += 1

    return round(success_result / count, 3)


print(find_sum_dice(12))


# Когда мы не знаем глубину вложенных циклов для наших расчётов, то така зависимость называется экспоненциальной.
# Технически у неё низкая производительность засчёт того, что увеличение числа n приводит к колоссальному росту
# количества операций. Для примера экспоненциальной сложности можно рассмотреть рекурсивный расчёт числа Фибоначчи.
# Сложность поиска m числа Фибоначчи можно представить как O(n^(2^(m-1))).


def fib_numbers(count):
    if count in [1, 2]:
        return 1

    return fib_numbers(count - 1) + fib_numbers(count - 2)


print(fib_numbers(5))

"""
Правила объединения сложности. 
Вызов нескольких методов на каждом шаге: O(2n) == O(n).
Обход половины размерности массива: O(n/2) == O(n).
Вызов нескольких методов вне цикла: O(2+n) == O(n).
Цифровые множители и цифровые слагаемые сокращаются. Это связано с тем, что математическая погрешность допускается в 
пределах 5%. Также это связано с тем, что базовая характеристика кривизны от цифровых показателей не изменится - мы всё
равно будем получать линейный, квадратичный и т.п. рост. 

Всё сложнее обстоит, когда алгоритмы вложены друг в друга.
method1 имеет сложность O(n^3). method2 имеет сложность O(n^2). Если method1 будет вызываться из method2, то их 
сложности перемножаются: O(n^3) * O(n^2) = O(n^5). А если методы будут вызываться последовательно, то их сложности 
складываются, т.е. берётся максимальная из них: O(n^3) + O(n^2) = O(n^3).
"""


def method1(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1

    return count


def method2(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1

    return count


"""
Наиболее частые сложности алгоритмов:
O(1) - константная. Не зависит от объёма данных. Например, поиск по хэш-таблице.
O(log n) - логарифмическая. Увеличение размера почти не сказывается на количестве итераций. Например, бинарный поиск, 
поиск по сбалансированному дереву.
O(n) - линейная. Увеличение сложности эквивалентно увеличению размера. Например, поиск по неотсортированному массиву.
O(n * log n) - увеличение размера заметно сказывается на сложности. Например, быстрая сортировка.
O(n^2) - квадратичная. Увеличение размера очень сильно сказывается на сложности. Например, пузырьковая сортировка.
O(2^n) - экспоненциальная. С увеличением размера на 1 сложность возрастает вдвое.
"""


# ----------------------------------------------------------------------------------------------------------------------
# Семинар.
# Написать программу, считывающую сумму от 1 до n. Сложность данного алгоритма O(n).
def find_sum(number):
    count = 0
    for i in range(1, number + 1):
        count += i

    return count


print(find_sum(5))


# Написать алгоритм поиска простых чисел (делятся только на себя и на 1) в диапазоне от 1 до N. В алгоритме будет
# использоваться вложенный for, что явно говорит о сложности O(n^2).
def find_simple_numbers(number):
    for i in range(1, number + 1):
        flag = True
        for j in range(2, (i + 1) // 2 + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            print(i)


find_simple_numbers(13)


# Посчитать количество действий для разных способов вычисления вариантов выпадения 4 кубиков.
# Решение с 4 циклами for:
def cycles_counter(faces):
    count = 0
    for i in range(faces):
        for j in range(faces):
            for k in range(faces):
                for m in range(faces):
                    count += 1
    return count


print(cycles_counter(6))


# Решение с рекурсией:
def recursive_counter(depth, max_depth, faces):
    # max = 4, faces = 6 | count = 214 * 6 = 1296
    count = 0
    for i in range(1, faces + 1):
        if depth == max_depth:
            count += 1
        else:
            count += recursive_counter(depth + 1, max_depth, faces)
    return count


result = recursive_counter(1, 4, 6)
print(result)


# Пишем алгоритм поиска нужного числа последовательности Фибоначчи.
# Считаем, что 1 и 2 значения последовательности равны 1.
# Искать будем по формуле On=On-1+On-2 что предполагает использовать рекурсивного алгоритма.

def find_fib(number):  # Сложность O(2^n)
    if number in [1, 2]:
        return 1

    return find_fib(number - 1) + find_fib(number - 2)


print(find_fib(7))


def find_fib_while(number):  # Сложность O(n)
    count = 1
    temp = 1
    for item in range(2, number):
        t = count
        count = count + temp
        temp = t

    return count


print(find_fib_while(7))
