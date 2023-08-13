import sys
from Small_Projects.FileManager.FileManager_1 import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_folder, game

save_info('Старт')
command = sys.argv[1]

if command == 'list':
    get_list()
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Не задано название файла')
    else:
        create_file(name)
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Не задано название папки')
    else:
        create_folder(name)
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Не задано название файла')
    else:
        delete_file(name)
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Не задано название файла')
    else:
        copy_file(name, new_name)
elif command == 'change':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Не задано имя папки')
    else:
        change_folder(name)
elif command == 'game':
    game()
elif command == 'help':
    print('list - список папок и файлов')
    print('create_file - создание файла')
    print('create_folder - создание папки')
    print('delete - удалить папку или файл')
    print('copy - копирование папки или файла')
    print('change - изменение текущей директории')
    print('game - сыграть в игру FindNumber')

save_info('Конец')
