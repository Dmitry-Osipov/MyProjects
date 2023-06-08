import random

minimum = 1
maximum = 100
number = None

print('Загадайте число от 0 до 100')
print('Если выданное компьютером число меньше вашего, напишите ">"')
print('Если выданное компьютером число больше вашего, напишите "<"')
print('Если компьютер угадал, напишите "="')

while True:
    number = random.randint(minimum, maximum)
    print(f'Компьютер выдал число: {number}')
    user_number = input('Введите значение: ')
    if user_number == '=':
        print('Компьютер победил!')
        break
    elif user_number == '>':
        minimum = number + 1
    else:
        maximum = number - 1