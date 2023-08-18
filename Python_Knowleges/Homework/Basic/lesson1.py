import math

# Найдите сумму цифр трехзначного числа user_number
# Результат сохраните в перменную res
# user_number = 123 -> res = 6 (1 + 2 + 3)
# user_number = 100 -> res = 1 (1 + 0 + 0)

number = 123
result = number // 100 + number // 10 % 10 + number % 10
print(result)


# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали user_number журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.
# user_number = 6 -> (1, 4, 1)
# user_number = 24 -> (4, 16, 4)
# user_number = 60 -> (10, 40, 10)

count_of_paperwork = 50
count_of_Kate = math.ceil(2/3 * count_of_paperwork)
count_of_Serge = count_of_Kate // 4
count_of_Petr = count_of_Kate // 4
tuple_of_people = (count_of_Petr, count_of_Kate, count_of_Serge)
print(tuple_of_people)


# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером user_number и
# выводит на экран yes или no.
# user_number = 385916 -> yes
# user_number = 123456 -> no


ticket = int(input('Input number of ticket: '))

digit1 = ticket // 100000
digit2 = ticket // 10000 % 10
digit3 = ticket // 1000 % 10
digit4 = ticket // 100 % 10
digit5 = ticket // 10 % 10
digit6 = ticket % 10

if digit1 + digit2 + digit3 == digit4 + digit5 + digit6:
    print('yes')
else:
    print('no')
