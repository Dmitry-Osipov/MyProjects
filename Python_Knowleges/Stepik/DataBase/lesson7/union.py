import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER, 
        score INTEGER
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS games (
        user_id INTEGER,
        score INTEGER,
        time INTEGER
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tab1 (
        score INTEGER,
        form TEXT
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tab2 (
        val INTEGER,
        type TEXT
        )""")


"""
Имеются 2 таблицы. К слову, Python выбросил ошибку при создании поля from, но если бы оно было создано, то обращаться к
нему следует через обратные кавычки `from`.

tab1                tab2
--------------      -----------------
score |  form |     |  val |  type  |
------|-------|     -------|--------| 
100   |  tab1 |     |  200 |  tab2  |
200   |  tab1 |     |  300 |  tab2  |
300   |  tab1 |     |  400 |  tab2  |
--------------      -----------------

А далее выполняем следующий SQL-запрос:
SELECT score, form FROM tab1 UNION SELECT val, type FROM tab2

В итоге получили следующую таблицу:
--------------
score | form |
------|------|
 100  | tab1 |
 200  | tab1 |
 200  | tab2 |
 300  | tab1 |
 300  | tab2 |
 400  | tab2 |
--------------

Но что, если мы укажем в этом запросе только первое поле:
SELECT score FROM tab1 UNION SELECT val FROM tab2

--------
 score |
-------|
  100  |
  200  |
  300  |
  400  |
--------

Дело в том, что оператор UNION при объединении данных оставляет только уникальные записи. Т.е. у нас значения 200 и 300 
находились как в первой, так и во второй таблице, поэтому они были оставлены как уникальные значения, а 100 было взято 
из первой таблицы, а 400 из второй. 

Соответственно, если бы в поле form были значения tab2, то UNION бы также откинул все повторы.

Но объединять данные можно ещё и другим образом. Из первой таблицы возьмём только первое поле score, а второе значение, 
которое будет отображаться во втором столбце, мы явно укажем 'table 1' и чтобы СУБД знала, как называется второе поле, 
мы укажем as tbl. Аналогично поступим и со второй таблицей:
SELECT score, 'table 1' as tbl FROM tab1 UNION SELECT val, 'table 2' FROM tab2

Получаем следующую таблицу:

-----------------
score |   tbl   |
------|---------|
 100  | table 1 |
 200  | table 1 |
 200  | table 2 |
 300  | table 1 |
 300  | table 2 |
 400  | table 2 |
-----------------

А ещё можно сделать доп фильтры:
SELECT score, 'table 1' as tbl FROM tab1 WHERE score IN (300, 400) UNION SELECT val, 'table 2' FROM tab2 
ORDER BY score DESC LIMIT 3
"""
