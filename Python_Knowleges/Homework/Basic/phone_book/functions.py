def create_data(recs):
    """
    Функция создаёт запись в файле.
    :param recs: Строковый тип данных. Пользователь вводит параметры, далее параметры сохраняются в файл в том порядке,
    в котором пользователь ввёл данные.
    :return: Данные, полученные от пользователя. Уведомление о создании записи.
    """
    with open('file.txt', 'a', encoding='utf-8') as data:
        for i, item in enumerate(recs):
            data.write(item + '\n')
            print('Запись создана')


def find_data(key_str):
    """
    Функция выводит в консоль весь строку по указанному параметру.
    :param key_str: Строка - параметр, который вводит пользователь.
    :return: Все строки, в которой встречен параметр пользователя.
    """
    flag = False
    with open('file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if key_str in line:
                print(line)
                flag = True

        if not flag:
            print("Данные по Вашим параметрам не найдены")


def print_data():
    """
    Функция выводит все данные построчно из файла.
    """
    with open('file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)


def update_data(key_str, new_data):
    """
    Функция обновляет данные в файле по указанному параметру.
    :param key_str: Строка - параметр, который вводит пользователь для поиска.
    :param new_data: Строка с новыми данными для замены.
    """
    updated = False
    lines = []  # Список будет использоваться для хранения строк файла после обновления.
    with open('file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if key_str in line:
                lines.append(new_data + '\n')
                updated = True
            else:
                lines.append(line)

    if updated:
        with open('file.txt', 'w', encoding='utf-8') as data:
            data.writelines(lines)
        print('Данные обновлены')
        # Подытожим: мы переписываем весь файл (поочерёдно добавляем каждую строку; если надо, перезаписываем
        # определённую строку).
    else:
        print('Данные по Вашим параметрам не найдены')


def delete_data(key_str):
    """
    Функция удаляет данные из файла по указанному параметру.
    :param key_str: Строка - параметр, который вводит пользователь.
    """
    lines = []
    deleted = False
    with open('file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if key_str not in line:
                lines.append(line)
            else:
                deleted = True

    if deleted:
        with open('file.txt', 'w', encoding='utf-8') as data:
            data.writelines(lines)
        print("Данные удалены")
        # Действуем по аналогичной логике: проверяем каждую строку. Если в строке нет нужного параметра, то добавляем
        # строку в список актуальных строк (lines); если параметр есть, то меняем флаг на True без добавления строки
        # в список.
    else:
        print("Данные по Вашим параметрам не найдены")
