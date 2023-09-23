import sqlite3 as sq

"""
INSERT - добавление записи в таблицу;
SELECT - выборка данных из таблиц (в т.ч. и при создании свободной выборки из нескольких таблиц).

Рассмотрим синтаксис INSERT:
INSERT INTO <table_name> (<column_name1>, <column_name2>, ...) VALUES (<value1>, <value2>, ...)

либо можно записывать иначе, если подразумеваем, что будем записывать данные во все поля по порядку:
INSERT INTO <table_name> VALUES (<value1>, <value2>, ...)
"""

with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")

"""
Исполняем запрос, а далее в программе про работе с БД добавим туда данные при помощи SQL-запроса: 
INSERT INTO users VALUES('Михаил', 1, 19, 1000), а далее нажимаем Ctrl + Enter. Запрос выполняется с сообщением:
Execution finished without errors.
Result: запрос успешно выполнен. Заняло 5мс, 1 строк изменено
At line 1:
INSERT INTO users VALUES('Михаил', 1, 19, 1000)

Далее напишем ещё один запрос, где перечислим все поля, кроме sex (по умолчанию 1):
INSERT INTO users (name, old, score) VALUES('Федор', 32, 200). При исполнении команды видим сообщение:
Execution finished without errors.
Result: запрос успешно выполнен. Заняло 0мс, 1 строк изменено
At line 1:
INSERT INTO users (name, old, score) VALUES('Федор', 32, 200)

По итогу ошибок или непредсказуемого поведения нет, ибо мы заранее задали в поле sex значение по умолчанию 1.

Далее рассмотрим наиболее часто используемую команду при составлении SQL-запросов - SELECT:
SELECT <col_name1>, <col_name2>, ... FROM <table_name> - самый простой вариант команды. 

Реализуем же его:
Переходим в программу с БД, где прописываем запрос, а также видим соответсвующую нашему запросу таблицу:
SELECT name, old, score FROM users. И видим сообщение:
Execution finished without errors.
Result: 2 строк возвращено за 15мс
At line 1:
SELECT name, old, score FROM users

Также мы можем получить всю таблицу при запросе:
SELECT * FROM users

Но обычно команду SELECT использует с условием WHERE. Т.е. мы выбираем не все записи из таблицы, а только определённые:
SELECT <col_name1>, <col_name2>, ... FROM <table_name> WHERE <условие>

Например, напишем запрос по выводу всех пользователей, у которых количество очков меньше 1000:
SELECT * FROM users WHERE score < 1000

Для проверки в условии можно писать следующие операторы:
= или == или !=;
> или <;
>= или <=;
BETWEEN (с английского между, включает в себя крайние значения тоже).

Рассмотрим пример с BETWEEN:
SELECT * FROM users WHERE score BETWEEN 500 AND 1000
Соответственно, получили двух пользователей, у которых 500 и 1000 очков (были бы другие со значениями между, они бы тоже
сюда попались).

Но на практике часто нужны условия сразу в нескольких столбцах. Например, мы хотим выбрать игроков старше 20 лет и с 
числом очков менее 1000. Здесь уже нужно использовать составное условие:
AND - условное И: exp1 AND exp2 - истинно, если одновременно истинны exp1 и exp2;
OR - условное ИЛИ: exp1 OR exp2 - истинно, если истинно exp1, или exp2, или оба сразу;
NOT - условное НЕ: NOT exp - преобразует ложное условие в истинное и, наоборот, истинное - в ложное;
IN - вхождение во множество значений: col IN (val1, val2, ...);
NOT IN - НЕ вхождение во множество значений: col NOT IN (val1, val2, ...).

Рассмотрим пример составного условия:
SELECT * FROM users WHERE old > 20 AND score < 1000
SELECT * FROM users WHERE old IN (19, 32) AND score <= 1000 - возраст 19 или 32
SELECT * FROM users WHERE old IN (19, 32) AND score <= 1000 or sex == 1 - по факту последнее условие выбирает всех 
игроков мужского пола. Причём необходимо заметить, что приоритет операции AND выше, чем у OR. Т.е. сначала выполнились 
2 подусловия по возрасту и очкам, а потом уже оператор OR. Если следует изменить приоритет операций, то следует ставить 
скобки:
SELECT * FROM users WHERE old IN (19, 32) AND (score <= 1000 or sex == 1) - теперь мы проверяем, чтобы у нас выводились 
пользователи мужского пола или с количеством очков меньше либо равным 1000 и + к этому условию чтобы у пользователя был 
возраст 19 или 32 года.

На приоритет операций всегда нужно обращать внимание, чтобы получать корректный вывод под нужную задачу. 

Также у оператора SELECT в конце можно указать оператор ORDER BY <column_name> - он выполняет сортировку по указанному 
столбцу.
SELECT * FROM users WHERE old IN (19, 32) AND score <= 1000 or sex == 1 ORDER BY old

Если нам нужно, чтобы была сортировка по возрастанию, то указываем дополнительно в конце ASC или DESC:
SELECT * FROM users WHERE old IN (19, 32) AND score <= 1000 or sex == 1 ORDER BY old ASC

Ну и в конце рассмотрим оператор LIMIT, который говорит, сколько записей мы будем отбирать из нашей выборки:
SELECT * FROM users WHERE old IN (19, 32) AND score <= 1000 or sex == 1 ORDER BY old ASC LIMIT 2

Синтаксис LIMIT такой:
LIMIT <max>[OFFSET offset] - указываем число, которое хотим получить от нашей выборки или же дополнительно прописываем
оператор OFFSET, где указываем число, которое будет означать сколько первых записей мы пропускаем, а затем выбираем 
следующие <max>. Либо можно записать LIMIT <offset, max>

SELECT * FROM users WHERE score >= 100 ORDER BY score DESC LIMIT 5 - выведем пользователей, у которых количество очков 
больше либо равно 100, отсортируем по убыванию по столбцу score, и выведем первые 5 записей.

Если прописать OFFSET 1, то мы увидим второго далее, кто прошёл выборку.

Конечно, все приведённые SQL-запросы можно выполнять и из питона.
"""

with sq.connect('saper.db') as con:
    cur = con.cursor()

    cur.execute('SELECT * FROM users WHERE score >= 1000 ORDER BY score DESC')
    result = cur.fetchall()  # Вызываем этот метод для получения результатов отбора SQL-запроса.
    print(result)  # [('Сергей', 1, 33, 2000), ('Михаил', 1, 19, 1000)] - Получили список кортежей.

"""
Если число выбираемых записей большое, то следует перебирать список циклом с выводом кортежей, либо использовать функцию
pprint, что существенно экономит память.

Наконец, есть ещё 2 метода:
fetchmany(size) - возвращает число записей не более size;
fetchone() - возвращает первую запись.
"""

with sq.connect('saper.db') as con:
    cur = con.cursor()

    cur.execute('SELECT * FROM users WHERE score < 1000 ORDER BY score DESC')
    result = cur.fetchmany(2)
    print(result)

with sq.connect('saper.db') as con:
    cur = con.cursor()

    cur.execute('SELECT * FROM users WHERE score > 100 ORDER BY score ASC LIMIT 2, 5')
    result = cur.fetchone()
    print(result)
