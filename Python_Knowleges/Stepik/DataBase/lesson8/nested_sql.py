import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS marks (
        id INTEGER,
        subject TEXT,
        mark INTEGER
        )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS female (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER
        )""")

"""
Имеем 2 таблицы со студентами и оценками. Стоит задача: выбрать всех студентов, у которых оценка по языку Си выше, чем 
оценка по этому же языку у Маши.

По идее мы должны реализовать 2 запроса: выяснить оценку Маши по языку Си и сравнить с остальными:
1) SELECT mark FROM marks WHERE id == 2 AND subject LIKE 'Си'
2) SELECT name, subject, mark FROM marks JOIN students ON students.rowid = marks.id WHERE mark > 3 AND subject LIKE 'Си'

Но в SQL можно реализовать это в одном запросе, используя идею вложенных запросов:
SELECT name, subject, mark FROM marks JOIN students ON students.rowid = marks.id 
WHERE mark > (SELECT mark FROM marks WHERE id == 2 AND subject LIKE 'Си') AND subject LIKE 'Си'

А что если вложенный запрос вернёт несколько записей? Например, возьмём все оценки, которые получила Маша по разным 
предметам:
SELECT name, subject, mark FROM marks JOIN students ON students.rowid = marks.id 
WHERE mark > (SELECT mark FROM marks WHERE id == 2) AND subject LIKE 'Си'

В итоге уже 3 раза получили один и тот же правильный ответ. Третий вариант сработал, потому что будет браться только 
первый полученный результат (у Маши это как раз был Си), а другие попросту игнорируются. Если же вложенный запрос 
возвращает NULL, то внешний запрос тоже не вернёт ни одной записи. Также можно использовать арифметические функции. 
К примеру, возьмём у Маши среднее арифметическое её оценок:
SELECT name, subject, mark FROM marks JOIN students ON students.rowid = marks.id 
WHERE mark > (SELECT avg(mark) as avg FROM marks WHERE id == 2) AND subject LIKE 'Си'

Вложенные запросы так же можно использовать и в команде INSERT. Предположим, что у нас имеется таблица female, которая 
идентична таблице students. Наша задача - добавить в таблицу female всех студентов женского пола. Для начала отберём 
всех студентов женского пола из таблицы students:
SELECT * FROM students WHERE sex == 2

А теперь, чтобы вставить эти строчки в таблицу female (она уже должна быть создана, иначе будет ошибка), 
реализуем следующее:
INSERT INTO female SELECT * FROM students WHERE sex == 2

Но в такой записи выше есть недостаток - выполнив его ещё раз, мы получаем ошибку, которая говорит, что мы вставляем 
записи, у которых поле female.id не является уникальным, так что перепишем запрос в таком виде:
INSERT INTO female SELECT NULL, name, sex, old FROM students WHERE sex == 2

Соответственно, теперь PRIMARY KEY (т.е. id определяется автоматически, ошибок больше нет).

Похожим образом можно создавать запросы и для команды update. Допустим, мы хотим обнулить все оценки в таблице marks, 
которые меньше или равны минимальной оценке студента с id == 1:
UPDATE marks SET mark = 0 WHERE mark <= (SELECT min(mark) FROM marks WHERE id == 1)

Аналогичные действия можно выполнять и в команде DELETE. Допустим, требуется удалить из таблицы students всех студентов, 
возраст которых меньше, чем у Маши:
DELETE FROM students WHERE old < (SELECT old FROM students WHERE id == 2)
"""
