"""
Структурами данных называют некоторый контейнер с данными, обладающий специфическим внутренним устройством (макетом) и
логикой хранения. Различные макеты могут быть эффективны для некоторых операций и неэффективны для других.
Массив (для Python список) - это контейнер, хранящий данные, идентифицируемые по индексу. К любому элементу массива
всегда можно обратиться по его индексу или заменить его. Особенностью массива является то, что доступ к элементам по
индексу осуществляется за константное время, т.е. имеет сложность О(1).
Всего есть несколько стандартных операций с массивами: поиск по массиву, сортировка массива. Рассмотрим простые
алгоритмы сортировки, алгоритмы поиска, продвинутые алгоритмы сортировки.
"""

"""
Простые алгоритмы сортировки: пузырьковая сортировка, сортировка выбором, сортировка вставками.
Все простые алгоритмы поиска имеют одинаковую сложность O(n^2).
"""


def bubble_sort(numbers):  # Алгоритм сортировки пузырьком - сложность O(n^2).
    length = len(numbers)
    for i in range(length - 1):
        for j in range(0, length - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


array1 = [4, 2, 5, 8, 1, 9, 2, 3, 6, 8]
bubble_sort(array1)
print(array1)


def direct_sort(numbers):  # Сортировка выбором - сложность O(n^2), но на один проход меньше, чем у пузырька.
    length = len(numbers)
    for i in range(length - 1):
        min_pos = i
        for j in range(i + 1, length):
            if numbers[j] < numbers[min_pos]:
                min_pos = j

        if i != min_pos:
            numbers[i], numbers[min_pos] = numbers[min_pos], numbers[i]


array2 = [4, 2, 5, 8, 1, 9, 2, 3, 6, 8]
direct_sort(array2)
print(array2)


def insert_sort(numbers):  # Сортировка вставками - сложность O(n^2).
    length = len(numbers)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


array3 = [4, 2, 5, 8, 1, 9, 2, 3, 6, 8]
direct_sort(array3)
print(array3)

"""
Алгоритмы поиска: простой перебор, бинарный поиск.
Для простого перебора не требуется сортировать массив.
В свою очередь, бинарный поиск требует отсортированного массива.
"""


def simple_find(numbers, value):  # Простой перебор - сложность O(n).
    for i in range(len(numbers)):
        if numbers[i] == value:
            return i

    return -1


array4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(simple_find(array4, 5))

# Бинарный поиск - сложность O(log(n)). minimum и maximum - это диапазон, в котором будет осуществляться бинарный поиск,
# что позволит нам эту функцию рекурсивно вызывать постоянно, изменяя min и max, тем самым изменяя диапазон, в
# котором хотим найти элементы, для которых хотим определить позицию.


def binary_search(numbers, value, minimum, maximum):
    if maximum < minimum:
        return -1

    mid_point = (maximum - minimum) // 2 + minimum

    if numbers[mid_point] < value:
        return binary_search(numbers, value, mid_point + 1, maximum)

    if numbers[mid_point] > value:
        return binary_search(numbers, value, minimum, mid_point - 1)

    return mid_point


print(binary_search(array4, 5, 0, len(array4) - 1))


"""
Продвинутые алгоритмы сортировки: быстрая сортировка, пирамидальная сортировка.

Быстрая сортировка.
Разделяй и властвуй - парадигма разработки алгоритмов, заключающаяся в рекурсивном разбиении решаемой задачи на две или
более подзадачи того же типа, но меньшего размера, и комбинировании их решений для получения ответа к исходной задаче;
разбиения выполняются до тех пор, пока все подзадачи не окажутся элементарными.
Pivot - элемент, служащий точкой сравнения элементов и их "поворота", в случае необходимости.

Пирамидальная сортировка.
Бинарная куча. Если принять элемент с индексом i за родителя, то индексы его дочерних элементов будут 2 * i + 1 и
2 * i + 2. 
"""


def quick_sort(numbers):  # Быстрая сортировка - сложность O(n * log(n)).
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    left = [x for x in numbers[1:] if x <= pivot]
    right = [x for x in numbers[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


array5 = [4, 2, 5, 8, 1, 9, 2, 3, 6, 8]
print(quick_sort(array5))


def heapify(array, heap_size, root_index):  # Пирамидальная сортировка - сложность O(n * log(n)).
    largest = root_index  # Инициализируем наибольший элемент как корень.
    left_child = 2 * root_index + 1  # Левый 2 * rootIndex + 1.
    right_child = 2 * root_index + 2  # Правый 2 * rootIndex + 2.

    # Если левый дочерний элемент больше корня.
    if left_child < heap_size and array[left_child] > array[largest]:
        largest = left_child

    # Если правый дочерний элемент больше, чем самый большой элемент на данный момент.
    if right_child < heap_size and array[right_child] > array[largest]:
        largest = right_child

    # Если самый большой элемент не корень.
    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]

        # Рекурсивно преобразуем в двоичную кучу затронутое поддерево.
        heapify(array, heap_size, largest)


def heap_sort(array):
    n = len(array)

    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]

        # Вызываем процедуру heapify на уменьшенной куче.
        heapify(array, i, 0)


array6 = [4, 2, 5, 8, 1, 9, 2, 3, 6, 8]
heap_sort(array6)
print(array6)
