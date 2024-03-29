from random import randint

# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

lst = [1, 2, 3, 4, 5]
k = 3
for i in range(k):
    num = lst.pop()
    lst.insert(0, num)

print(lst)

# Напишите программу для печати всех уникальных значений в словаре.
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит


all_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
            {"VIII": "S007"}]
my_set = set()
for dict_list in all_dict:
    for item in dict_list.values():
        print(item)
        my_set.add(item)

print(my_set)

# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

first_list = [0, -1, 5, 2, 3]
count = 0

if len(first_list) % 2 != 0:
    for i in range(len(first_list)):
        if i % 2 != 0:
            if first_list[i] < first_list[i + 1]:
                count += 1
else:
    for i in range(len(first_list)):
        if i % 2 == 0:
            if first_list[i] < first_list[i + 1]:
                count += 1

print(count)

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

new_list = [1, 2, 3, 4, 5, 5, 1, 2, 4, 1, 3, 2, 1, 1, 6, 8]
user_number = int(input('Input number: '))
count = 0

if user_number in new_list:
    for item in new_list:
        if user_number == item:
            count += 1
    print(count)
else:
    print('Your number is not in the list')

# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
#
# -> 5

user_size = int(input('Input list size: '))
user_number = int(input('Input number: '))
user_list = []

for i in range(user_size):
    number = randint(-10000, 10000)
    user_list.append(number)

closest_number = user_list[0]
min_distance = abs(user_list[0] - user_number)

for number in user_list:
    distance = abs(number - user_number)
    if distance < min_distance:
        min_distance = distance
        closest_number = number

print(f"Your list - {sorted(user_list)}\n" # Для удобства вывода
      f"Nearest elem to {user_number} is - {closest_number}")

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать,
# что на вход подается только одно слово, которое содержит либо только английские, либо только
# русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

one_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
two_point = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
three_point = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
four_point = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
five_point = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
eight_point = ['J', 'X', 'Ш', 'Э', 'Ю']
ten_point = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

point_dict = {}
for key in one_point:
    point_dict[key] = 1
for key in two_point:
    point_dict[key] = 2
for key in three_point:
    point_dict[key] = 3
for key in four_point:
    point_dict[key] = 4
for key in five_point:
    point_dict[key] = 5
for key in eight_point:
    point_dict[key] = 8
for key in ten_point:
    point_dict[key] = 10

count = 0
user_word = input('Input one word without symbols: ').upper()

try:
    for letter in user_word:
        count += point_dict[letter]

    print(count)
except KeyError:
    print('Please input only one word without symbols')
