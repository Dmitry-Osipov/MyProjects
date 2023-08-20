from random import randint
from collections import deque


# ТЕОРИЯ:
# Структурное программирование:
# Трассировка пути в лабиринте:
# __
# Описание: Имеется двумерный массив, представляющий лабиринт, где '0' - это проход, а '1' - это стена. Начальная и
# конечная точки заданы. Необходимо определить путь от начальной до конечной точки.
# Почему это структурное программирование: Задача может быть решена с помощью последовательных шагов, ветвлений
# (проверка на наличие стены или уже посещенной клетки) и циклов (для обработки всех возможных направлений движения).
# Процедурное программирование:
# __
# Разбиение массива на подмассивы:
# Описание: Имеется массив чисел. Необходимо разбить его на подмассивы так, чтобы сумма чисел в каждом подмассиве была
# меньше или равна заданному значению X.
# Почему это процедурное программирование: Можно создать процедуру, которая будет принимать массив и значение X,
# а затем последовательно формировать подмассивы, следуя определенной логике. Это позволяет выделить процесс создания
# каждого подмассива в отдельную подпрограмму, делая основной код более чистым и понятным.
# __
# Рекурсивное вычисление чисел Фибоначчи:
# Описание: Написать функцию, которая возвращает n-тое число Фибоначчи.
# Почему это процедурное программирование: Здесь мы можем использовать рекурсивную процедуру, где каждый вызов функции
# делает два дополнительных вызова (для n-1 и n-2). Хотя это не самый эффективный способ решения, он хорошо
# демонстрирует концепцию процедурного программирования.
# Эти задачи служат хорошими примерами того, как структурное и процедурное программирование может быть применено
# в реальных сценариях

# ______________________________________________________________________________________________________________________

# Структурное программирование:
# Трассировка пути в лабиринте:
# Задание: Создайте функцию, которая принимает двумерный массив (лабиринт) и начальную и конечную точки.
# Функция должна возвращать путь от начальной до конечной точки или сообщение, что путь невозможен.
# Входные данные:
# Двумерный массив размера MxN, где '0' - это проход, а '1' - это стена.
# Координаты начальной и конечной точки.
# Выходные данные:
# Массив координат пути или сообщение об ошибке.
# Решение:
def create_2d_array(rows, columns, min_value, max_value):
    created_array = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(randint(min_value, max_value))
        created_array.append(row)

    return created_array


def find_way(two_dimensional_array, start, end):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]  # Указываем соседние точки по горизонтали и по вертикали
    rows, cols = len(two_dimensional_array), len(two_dimensional_array[0])
    # Получаем количество строк и количество столбцов. Для определения количества столбцов можно взять любую строку, ибо
    # длина столбцов везде одинаковая (иначе это не является двумерным массивом).
    visited = set()  # Создали множество для отслеживания посещённых клеток

    q = deque([(start[0], start[1], [])])  # Создали очередь с кортежем (x, y, path), где (x, y) - текущие координаты,
    # а path - список, представляющий текущий путь. Начинаем с координат начальной точки и пустого пути.

    while q:  # Запускаем цикл, пока очередь не пуста.
        x, y, path = q.popleft()  # Извлекаем кортеж (x, y, path) из начала очереди, представляющий текущую позицию и
        # путь до этой позиции.
        if (x, y) == end:
            return path + [(x, y)]

        for i in range(4):  # Здесь индексы соответствуют направлениям движения по горизонтали и вертикали: → ← ↑ ↓
            # Перебираем все возможные направления (dx и dy), чтобы проверить соседние клетки.
            nx, ny = x + dx[i], y + dy[i]  # Вычисляем новые координаты соседней клетки (nx, ny) путём добавления dx[i]
            # и dy[i] к текущим координатам (x, y).
            if 0 <= nx < rows and 0 <= ny < cols and two_dimensional_array[nx][ny] == 0 and (nx, ny) not in visited:
            # Проверяем, что новые координаты (nx, ny) находятся внутри границ лабиринта и являются проходом
            # (значение 0) и не посещены ранее.
                q.append((nx, ny, path + [(x, y)]))  # Если условие выполнено, добавляем (nx, ny, path + [(x, y)]) в
                # очередь q, чтобы продолжить поиск.
                visited.add((nx, ny))  # Добавляем (nx, ny) в множество visited, чтобы не посещать эту клетку снова.

    return 'Path not found'


# test_array = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#           [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
#           [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
#           [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]]  # Двумерный массив заданный заранее создан для наглядности и проверки.
# start_point = (1, 0)
# end_point = (3, 10)

test_array = create_2d_array(4, 11, 0, 1)
print(test_array[0], test_array[1], test_array[2], test_array[3], sep='\n')  # Для проверки случайного массива
start_x, start_y = map(int, input('Enter the row number and column number of the start point, separated by a space: ')
                       .split())
end_x, end_y = map(int, input('Enter the row number and column number of the end point, separated by a space: ')
                   .split())
start_point = (start_x, start_y)
end_point = (end_x, end_y)

result = find_way(test_array, start_point, end_point)
if isinstance(result, str):
    print(result)
else:
    print(f'The path from {start_point} to {end_point}: ')
    for x, y in result:
        print(f'({x}, {y})', end=' -> ' if (x, y) != result[-1] else '\n')


# Процедурное программирование:
# Разбиение массива на подмассивы:
# Задание: Напишите функцию, которая принимает массив чисел и значение X. Функция должна возвращать массив подмассивов
# так, чтобы сумма чисел в каждом подмассиве была меньше или равна X.
# Входные данные:
# Массив чисел длиной N.
# Число X.
# Выходные данные:
# Массив подмассивов.
# Решение:


def find_valid_subarray(subarrays_array, valid_sum):
    new_array = []
    for subarray in subarrays_array:
        if sum(subarray) <= valid_sum:
            new_array.append(subarray)

    return new_array


user_rows = int(input('Enter the number of subarrays: '))
user_columns = int(input('Enter the number of subarray elements: '))
user_min_value = int(input('Enter the minimum value for the array: '))
user_max_value = int(input('Enter the maximum value for the array: '))
random_array = create_2d_array(user_rows, user_columns, user_min_value, user_max_value)
print(random_array)
user_sum = int(input('Enter the allowable sum of elements: '))
print(f'Arrays that contain a sum of elements less than or equal to {user_sum}: '
      f'{find_valid_subarray(random_array, user_sum)}')


# Рекурсивное вычисление чисел Фибоначчи:
# Задание: Напишите рекурсивную функцию для вычисления n-того числа Фибоначчи.
# Входные данные:
# Число n.
# Выходные данные:
# n-тое число Фибоначчи.
# Решение:


def find_fib_number(count):
    if count in [1, 2]:
        return 1

    return find_fib_number(count - 1) + find_fib_number(count - 2)


user_count = int(input('Input the sequence number of the Fibonacci number: '))
if user_count <= 0:
    print('Zero or less cannot be an ordinal number in a sequence')
elif user_count == 1:
    print(f'{user_count}st Fibonacci number: {find_fib_number(user_count)}')
elif user_count == 2:
    print(f'{user_count}nd Fibonacci number: {find_fib_number(user_count)}')
elif user_count == 3:
    print(f'{user_count}rd Fibonacci number: {find_fib_number(user_count)}')
else:
    print(f'{user_count}th Fibonacci number: {find_fib_number(user_count)}')
