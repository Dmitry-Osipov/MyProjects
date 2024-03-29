import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS games (
    uesr_id INTEGER,
    score INTEGER,
    time INTEGER
    )""")

"""
Рассмотрим агрегирующие функции, используемые в SQL. А также разберём возможность группировки записей по определённому 
полю. Все эти операции доступны в SELECT.
Чтобы лучше понять, что такое агрегирующие функции, рассмотрим пример подсчёта числа записей в таблице games, которые 
были сыграны первым игроком. 

Привычный вид, который мы уже использовали ранее:
SELECT user_id FROM games WHERE user_id == 1 - мы вывели 3 записи, а нам нужно количество этих записей. Как раз для 
этого и существуют агрегирующие функции.

SELECT count(user_id) FROM games WHERE user_id == 1 - вот теперь мы получили нужное нам значение.

Но теперь вопрос: а почему именно поле user_id? В действительности можно взять любое другое поле. Например, score:
SELECT count(score) FROM games WHERE user_id == 1 - как видим, разницы нет вообще, ибо функция count() считает 
количество записей. 

SELECT count() FROM games WHERE user_id == 1 - можно даже вообще поля не указывать, и получить корректное значение.

На выходе функция count() даёт нам таблицу с полем count() (либо внутри скобок может быть название столбца, зависит от
запроса) - в программах использовать такое имя поля не очень удобно, поэтому можно подставить синоним:

SELECT count() as count FROM games WHERE user_id == 1 - теперь получаем более удобную таблицу.

Команда SELECT сначала выбирает все записи, которые удовлетворяют условию WHERE, и только после этого вычисляется их 
количество count(). Так работают все агрегирующие функции - они выполняются в последнюю очередь.

Наиболее часто используемые агрегирующие функции:
count() - подсчёт числа записей;
sum() - подсчёт суммы указанного поля по всем записям выборки;
agv() - вычисление среднего арифметического;
min() - нахождение минимального значения для указанного поля;
max() - нахождение максимального значения для указанного поля.

Отсчитаем количество уникальный игроков в games при помощи count():
SELECT count(DISTINCT user_id) as count FROM games - увидим количество уникальных игроков
SELECT DISTINCT user_id as count FROM games - увидим каждого уникального игрока по user_id

Посчитаем общую суму очков первого игрока:
SELECT sum(DISTINCT score) as scores FROM games WHERE user_id == 1

Максимальное и минимальное для первого игрока:
SELECT max(DISTINCT score) as max_score FROM games WHERE user_id == 1
SELECT min(DISTINCT score) as min_score FROM games WHERE user_id == 1

Рассмотрим группировку записей. 
Представим задачу: мы хотим для каждого игрока, который есть в таблице games, посчитать сумму очков. Т.е. для каждого 
игрока по отдельности посчитать его сумму очков.
Агрегаторы работают только в рамках определённой группы, а сама группа определяется с помощью оператора: 
GROUP BY имя_поля

Реализуем задачу выше:
SELECT user_id, sum(score) as sum FROM games GROUP BY user_id - производим группировку по полю user_id, а далее для 
каждой группы выводим user_id и сумму очков.

Дополним задачу - требуется отсортировать по убыванию получившийся список:
SELECT user_id, sum(score) as sum FROM games GROUP BY user_id ORDER BY sum DESC

Дополним фильтр - очков должно быть больше 300:
SELECT user_id, sum(score) as sum FROM games WHERE score > 300 GROUP BY user_id ORDER BY sum DESC

А если нужно сделать ограничение по числу отбираемых записей, то используется LIMIT:
SELECT user_id, sum(score) as sum FROM games WHERE score > 300 GROUP BY user_id ORDER BY sum DESC LIMIT 1
"""
