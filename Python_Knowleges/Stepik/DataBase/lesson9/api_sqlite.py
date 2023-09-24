import sqlite3 as sq

with sq.connect('cars.db') as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
        )""")

"""
При работе с API SQLite в менеджере контекста автоматически выполняются 2 метода:
con.commit() - сохраняет все изменения в БД, т.е. физически сохраняет все изменения, которые мы вносили внутри менеджера
контекста;
con.close() - закрывает соединение с БД.

Итак, каким образом происходит работа с БД?
Команда execute() позволяет выполнять определённые SQL-запросы. В частности выше мы создаём таблицу. 
Теперь добавим несколько записей. Самый простой случай:
"""

with sq.connect('cars.db') as con:
    cur = con.cursor()

    cur.execute('INSERT INTO cars VALUES(1, "Audi", 52642)')
    cur.execute('INSERT INTO cars VALUES(2, "Mercedes", 57127)')
    cur.execute('INSERT INTO cars VALUES(3, "Skoda", 9000)')
    cur.execute('INSERT INTO cars VALUES(4, "Volvo", 29000)')
    cur.execute('INSERT INTO cars VALUES(5, "Bentley", 350000)')

"""
Проблема этого запроса в том, что такие данные с машинами и ценой, как правило, хранятся в каких-либо коллекциях.
Создадим же список машин и преобразуем SQL-запрос.
"""

cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]

with sq.connect('cars.db') as con:
    cur = con.cursor()

    for car in cars:
        cur.execute('INSERT INTO cars VALUES(NULL, ?, ?)', car)  # Вместо первого вопросительного знака будет
        # подставлено название машины, а вместо второго - цена.

"""
Или можно поступить ещё проще и использовать встроенный метод:
"""

with sq.connect('cars.db') as con:
    cur = con.cursor()
    cur.executemany('INSERT INTO cars VALUES(NULL, ?, ?)', cars)

"""
Также отметим, что вместо знаков вопроса можно использовать именованные параметры с помощью двоеточия, а затем через 
запятую указываем словарь, в котором ключ является именем параметра, а значение ключа как раз будет подставлено вместо 
него:
"""

# Устанавливаем цену 0 для всех автомобилей, что начинаются с А:
with sq.connect('cars.db') as con:
    cur = con.cursor()
    cur.execute('UPDATE cars SET price = :Price WHERE model LIKE "A%"', {'Price': 0})

"""
Выполняем сразу несколько SQL-команд:
"""

# Удаляем все машины, что начинаются с А, и увеличиваем цены на оставшиеся автомобили на 1000:
with sq.connect('cars.db') as con:
    cur = con.cursor()
    cur.executescript('''DELETE FROM cars WHERE model LIKE "A%";
        UPDATE cars SET price = price + 1000
        ''')

"""
Однако у данного метода есть одно важное ограничение: здесь нельзя использовать шаблон на запросы, как мы это делали в 
предыдущих методах. В executescript() буквально записываются SQL-запросы так, как они есть, со всеми данными.

Также важным замечанием будет, что менеджер контекста сохранит все данные. Если же нужно, чтобы при ошибке не было 
ничего сохранено, то следует использовать try-except-finally с использованием rollback() внутри except и использованием
фага BEGIN в начале и метода commit() в конце в блоке try. А в finally мы закрываем работу с БД с помощью метода close().

Представим, что у нас есть следующая задача. Имеется таблица cust (name, tr_in, buy), которая содержит покупателей машин.
Причём, если покупка происходит по trade in, то прежняя машина владельца добавляется в конец списка таблицы cars. А в 
поле tr_in появляется id машина из таблицы cars, которая была сдана по trade in. А поле buy будет подрежать id машины, 
которую приобрёл покупатель. Чтобы реализовать SQL-запрос для добавления записи в таблицу cust, нам нужно знать id 
автомобиля, который был сдан по trade in. Предположим, что клиент ещё не совершил покупку, а значит таблица cars не 
содержит запись с его сданным автомобилем. Поэтому для начала добавим её: 
"""

with sq.connect('cars.db') as con:
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust (name TEXT, tr_in INTEGER, buy INTEGER);""")

    cur.execute('INSERT INTO cars VALUES(NULL, "Запорожец", 1000)')
    last_row_id = cur.lastrowid  # автомобиль, который Фёдор сдаёт по trade in.
    # Переменная выше содержит id последней записи. Воспользуемся этой информацией для формирования второго запроса:
    buy_car_id = 2  # автомобиль, который купит Фёдор.
    cur.execute('INSERT INTO cust VALUES("Фёдор", ?, ?)', (last_row_id, buy_car_id))

"""
fetchall() - возвращает число записей в виде упорядоченного списка;
fetchmany(size) - возвращает число записей не более size;
fetchone() - возвращает первую запись.
"""

with sq.connect('cars.db') as con:
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust (name TEXT, tr_in INTEGER, buy INTEGER);""")

    cur.execute('SELECT model, price FROM cars')
    rows = cur.fetchall()  # Запрос выше выполняется этой командой.
    print(rows)

    cur.execute('SELECT model, price FROM cars')
    first_car = cur.fetchone()  # Получаем первый элемент из таблицы.
    print(first_car)

    cur.execute('SELECT model, price FROM cars')
    first_four_cars = cur.fetchmany(4)  # Получаем первые 4 записи.
    print(first_four_cars)

    # Также мы говорили ранее, что по объекту cursor() можно итерироваться:
    cur.execute('SELECT model, price FROM cars')
    for result in cur:
        print(result)  # Преимущество такого подхода в экономии памяти, ибо на каждой итерации цикла берём лишь 1 запись.

"""
Но мы получаем словарь, что может быть не особо удобно. Удобным вариантом также может быть словарь, т.е. набор 
данных в виде ключ + значение, так что подключим row_factory:
"""

with sq.connect('cars.db') as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust (name TEXT, tr_in INTEGER, buy INTEGER);""")

    cur.execute('SELECT model, price FROM cars')
    for result in cur:
        print(result)

"""
Теперь на выходе мы получаем объекты sqlite3.Row. Так вот объект Row как раз и содержит данные в виде ключа и значения.
Т.е. теперь вместо print(result) мы должны прописать следующее:
"""

with sq.connect('cars.db') as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust (name TEXT, tr_in INTEGER, buy INTEGER);""")

    cur.execute('SELECT model, price FROM cars')
    for result in cur:
        print(result['model'], result['price'])

"""
Теперь, когда мы разобрались как брать записи из БД, рассмотрим способ хранения изображений в БД. Часто это требуется 
при работе с автарами у пользователя. Для этого в таблице запишем поле ava с типом данных BLOB - этот как раз тот тип, 
который представляет данные в бинарном виде, т.е. они никак не преобразуются, записываются буквально так, как есть, что 
как раз хорошо подходит для изображений.
"""


def read_ava(n):
    try:
        with open(f'avas/{n}.jpeg', 'rb') as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


with sq.connect('cars.db') as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            ava BLOB,
            score INTEGER
        )""")

    img = read_ava(2)
    if img:
        binary = sq.Binary(img)  # преобразуем бинарные данные в специальный бинарный объект. Если этого не сделать, то
        # данные могут быть записаны некорректно.
        cur.execute("INSERT INTO users VALUES ('Николай', ?, 1000)", (binary,))

"""
А теперь попробуем прочитать эту аватарку из таблицы users:
"""


def write_ava(name, data):
    try:
        with open(name, 'wb') as f:
            f.write(data)
    except IOError as e:
        print(e)
        return False

    return True


with sq.connect('cars.db') as con:
    con.row_factory = sq.Row
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            ava BLOB,
            score INTEGER
        )""")

    cur.execute("SELECT ava FROM users LIMIT 1")
    img = cur.fetchone()['ava']  # Из первой записи прочитаем бинарные данные.
    write_ava('uot.jpeg', img)

"""
Далее разберём полезный метод iterdump() класса Cursor, который возвращает итератор для SQL-запросов, на основе которых
можно воссоздать текущую БД (создание бэкапа БД).
"""

with sq.connect('cars.db') as con:
    cur = con.cursor()

    for sql in con.iterdump():
        print(sql)

"""
В итоге получили список команд, которые необходимы для создания БД. Т.е. выполнив все эти команды, мы в точности 
воссоздадим нашу БД. Сохраним теперь все эти данные в отдельном файле:
"""

with sq.connect('cars.db') as con:
    cur = con.cursor()

    with open('sql_dump.sql', 'w') as f:
        for sql in con.iterdump():
            f.write(sql)

"""
Попробуем восстановить нашу БД. Допустим, она у нас потерялась
"""

with sq.connect('cars.db') as con:
    cur = con.cursor()

    with open('sql_dump.sql', 'r') as f:
        sql = f.read()
        cur.executescript(sql)

"""
Ещё одной интересной особенностью модуля SQLite является возможность создания БД непосредственно в памяти. Такая 
организация позволяет хранить временные данные программы в формате таблиц, и работать с ними через SQL-запросы. 
Для создания БД в памяти устройства подключение производится таким образом:
"""

data = [('car', 'машина'), ('house', 'дом'), ('tree', 'дерево'), ('color', 'цвет')]
con = sq.connect(':memory:')  # благодаря такому ключевому слову таблица создаётся не на диске, а в памяти.
with con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS dict(
            eng TEXT, rus TEXT
        )""")

    cur.executemany("INSERT INTO dict VALUES(?,?)", data)

    cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(cur.fetchall())
