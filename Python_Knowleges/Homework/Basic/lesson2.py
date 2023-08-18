import random

# Задача 10: На столе лежат user_number монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
# число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

coins = int(input('Input the number of coins: '))
count_heads = 0
count_tails = 0
for i in range(coins):
    coin = random.randint(0, 1)
    print(coin, end=' ')
    if coin == 0:
        count_heads += 1
    else:
        count_tails += 1
print()
if count_heads >= count_tails:
    print(count_tails)
else:
    print(count_heads)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

sum_numbers = int(input('Input sum: '))
prod_numbers = int(input('Input prod: '))
for first_number in range(0, 1000):
    for second_number in range(0, 1000):
        if first_number + second_number == sum_numbers and first_number * second_number == prod_numbers:
            print(f'first number is {first_number}, second number is {second_number}')

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

stop_number = int(input('Input value to stop: '))
count = 0
for i in range(stop_number + 1):
    count += 1
    if 2 ** i <= stop_number:
        print(f'{count}) 2 ** {i} = {2 ** i}')
