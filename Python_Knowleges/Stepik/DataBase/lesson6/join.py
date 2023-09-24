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
        uesr_id INTEGER,
        score INTEGER,
        time INTEGER
        )""")

"""
Рассмотрим связывание таблиц games и users. Синтаксис:
JOIN таблица ON условие_связывания

Связывать будем по user_id для games (внешний ключ) и rowid для users (первичный ключ). Благодаря этим двум ключам можно 
связать данные этих таблиц, что и делается оператором JOIN.

Предположим, мы хотим сформировать сводный отчёт, который бы содержал следующие поля: name(users), sex(users), 
score(games).

Для этой задачи можно написать следующий запрос:
SELECT name, sex, games.score FROM games JOIN users ON games.user_id = users.rowid

Обязательно в SELECT нужно указывать таблицу, откуда берём значение (иначе возьмёт score из таблицы users). Также и в ON
требуется указать, что из какой таблицы мы будем брать. 

Выполняем запрос выше и видим ожидаемый вывод. Получили name, sex и score(из games). Т.к. у нас главной таблицей стоит 
games (что мы указали оператором FROM). Соответственно, вместо user_id == 1 был подставлен Михаил + 1(sex), ибо у 
Михаила row_id == 1. Аналогично со второй, третьей и т.д. Теперь хорошо видно, кто сколько очков набрал по играм, видно
именно по имени, а не просто по некоему user_id.

Также отметим, что объединять данные из таблиц можно и без оператора JOIN:
SELECT name, sex, games.score FROM users, games - но тут мы получаем просто набор данных из двух таблиц, что является 
совершенно разными вещами - т.е. по факту в таблицу games мы поочерёдно подставили каждое имя (строк в games 7, 
пользователя 3 - получили 21 строку), что не является корректным отображением данных. Для сводного отчёта всё же следует 
использовать JOIN.

Итак, эта команда - SELECT name, sex, games.score FROM games JOIN users ON games.user_id = users.rowid - является INNER
JOIN, т.е. соединением записи двух таблиц, если соответствие в обеих из них были найдены. Например, удалив Фёдора, у 
которого rowid == 3, то удалились бы из сводного отчёта все данные по user_id == 3. Т.е. когда мы пишем JOIN, то имеем 
ввиду именно INNER JOIN - объединение таблиц, если данные есть в обоих таблицах.

Но что если нам нужны все записи по таблице games? Пропишем LEFT JOIN, удалив предварительно Фёдора:
SELECT name, sex, games.score FROM games LEFT JOIN users ON games.user_id = users.rowid

Теперь видим, что у нас возвращается назад пятая строка, но поля name и sex обозначены как NULL, а поле score осталось 
равным 600.

Но теперь вернём Фёдора и сформируем топ игроков:
раньше мы писали - SELECT user_id, sum(score) as sum FROM games GROUP BY user_id ORDER BY sum DESC - но это неудобно, 
ибо используется user_id, а не имя.

Так что вот новое решение:
SELECT name, sex, sum(games.score) as score FROM games JOIN users ON games.user_id = users.rowid 
GROUP BY score ORDER BY sum DESC

Причём в конце заметим, что в операторе JOIN может быть несколько таблиц:
SELECT поля FROM таблица1 JOIN таблица2 JOIN таблица3 ... JOIN таблицаN ON условие_связывания
"""
