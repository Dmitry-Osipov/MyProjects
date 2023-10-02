# Ограничение времени	1 секунда
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt

# Сейчас активно развивается новая история, основателем которой является Профессор А.С. Багиров. Он выяснил, что на
# протяжении многих лет на земле вместе с людьми существовали ящеры. Строительство пирамид, захват Байкала и еще много
# разных событий произошли благодаря ящерам.
# Учёные ещё не выяснили, сколько времени ящеры существовали на земле. Они находят разные данные в виде даты начала и
# даты окончания, и чтобы проверить их на корректность, необходимо посчитать, сколько дней ящеры существовали для двух
# конкретных дат. Календарь ящеров очень похож на григорианский, лишь с тем исключением, что там нет високосных годов.
# Вам даны дата начала и дата окончания существования ящеров, нужно найти количество полных дней и секунд в неполном
# дне, чтобы учёные смогли оценить, насколько даты корректны.

# Формат ввода
# В первой строке содержатся 6 целых чисел:
# year1, month1, day1, hour1, min1, sec1
# (1 ≤ year1 ≤ 9999, 1 ≤ month1 ≤ 12, 1 ≤ day1 ≤ 31, 0 ≤ hour1 ≤ 23, 0 ≤ min1 ≤ 59, 0 ≤ sec1 ≤ 59) - дата начала
# существования ящеров.
# Во второй строке содержатся 6 целых чисел:
# year2, month2, day2, hour2, min2, sec2
# (1 ≤ year2 ≤ 9999, 1 ≤ month2 ≤ 12, 1 ≤ day2 ≤ 31, 0 ≤ hour2 ≤ 23, 0 ≤ min2 ≤ 59, 0 ≤ sec2≤ 59)
# - дата окончания существования ящеров. Гарантируется, что дата начала меньше,чем дата конца.

# Формат вывода
# В первой и единственной строке выведите 2 числа: количество дней, сколько существовали ящеры, а также количество
# секунд в неполном дне.

# Пример 1
# Ввод
# 980 2 12 10 30 1
# 980 3 1 10 31 37
# Вывод
# 17 96

# Пример 2
# Ввод:
# 1001 5 20 14 15 16
# 9009 9 11 12 21 11
# Вывод:
# 2923033 79555

# Примечания
# В одном году 365 дней. Год делится на 12 месяцев, количество дней в каждом месяце:
# [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]. В одном дне 24 часа (от 0 до 23), в одном часу 60 минут
# (от 0 до 59), в одной минуте 60 секунд (от 0 до 59).
# В первом тестовом примере года совпадают, а между 12 февраля и 1 марта прошло 17 полных дней, начало было в 10:30:01,
# а конец в 10:31:37,таким образом прошла 1 минута и 36 секунд, что в сумме получается 96 секунд.