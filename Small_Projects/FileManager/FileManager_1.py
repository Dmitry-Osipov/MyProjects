import os, shutil, datetime, random


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('../log.txt', 'side_a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_folder(name):
    os.chdir(name)
    print(os.getcwd())

def game():
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