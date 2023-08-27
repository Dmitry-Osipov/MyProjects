from functions import create_data, find_data, print_data, update_data, delete_data


print("Добро пожаловать в телефонный справочник!")
while True:
    print("Чтобы добавить запись, нажмите 1;")
    print("Чтобы найти запись, нажмите 2;")
    print("Чтобы вывести все данные на экран, нажмите 3;")
    print('Чтобы изменить введённые данные, нажмите 4;')
    print('Чтобы удалить ранее введённые данные, нажмите 5;')
    string = int(input("Чтобы окончить работу с программой, нажмите 0: "))
    print()
    if string == 1:
        string1 = 0
        rec = []
        while True:
            line = input("Введите Фамилию Имя Отчество и Номер телефона через пробел: ")
            rec.append(line)
            print(rec)
            string1 = int(input("Если желаете добавить еще запись нажмите 1, иначе 0: "))
            if string1 == 0:
                break
        create_data(rec)
        print()

    elif string == 2:
        string1 = (input("Введите данные для поиска: "))
        print("Ищем...")
        find_data(string1)
        print()

    elif string == 3:
        print("Выводим все данные...")
        print()
        print_data()

    elif string == 4:
        key_str = input('Введите Фамилию Имя Отчество и Номер телефона через пробел для поиска: ')
        new_data = input('Введите Фамилию Имя Отчество и Номер телефона через пробел: ')
        print('Обновляем...')
        update_data(key_str, new_data)
        print()

    elif string == 5:
        key_str = input('Введите Фамилию Имя Отчество и Номер телефона через пробел для поиска: ')
        print('Удаляем...')
        delete_data(key_str)
        print()

    elif string == 0:
        print('Будем рады видеть Вас снова!')
        print()
        break

    else:
        print("Такой команды не существует :(")
        print()
