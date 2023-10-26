import re

"""
Метод re.match(pattern, sting, flags) определяет совпадение шаблона (pattern) в начале строки (string) с учётом флагов 
flags. С помощью этого метода проверим, содержит ли строка номер телефона в следующем формате: +7(xxx)xxx-xx-xx:
"""

text = "+7(123)456-78-90"
match = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print(match)  # Всё отработало, но если в начале строки поставить любой символ, то получим None.

"""
Следующий метод re.split(pattern, string, flags) выполняет разбивку строки по заданному шаблону:
"""

text = """<point lon="40.8482" lat="52.6274" />
<point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
<point lon="40.8672" lat="52.6626" />, <point lon="40.8643" lat="52.6649" />
"""

match = re.split(r"[\n;,]", text)
print(match)  # ['<point lon="40.8482" lat="52.6274" />', '<point lon="40.8559" lat="52.6361" />',
# ' <point lon="40.8614" lat="52.651" />', '<point lon="40.8672" lat="52.6626" />',
# ' <point lon="40.8643" lat="52.6649" />', '']

"""
Следующий метод re.sub(pattern, repl, string, count, flags) выполняет замену строки найденных совпадений (string) 
строкой repl или результатом работы функции и возвращает преобразованную строку. 

pattern - регулярное выражение;
repl - строка или функция для замены найденного выражения;
string - анализируемая строка;
count - максимальное число замен (если не указано, то не ограничено);
flags - набор флагов (по умолчанию не используются).
"""

text = """Москва
Казань
Тверь
Самара
Уфа"""

# Предположим, что мы хоти превратить текст в следующее множество строк:
# <option>Москва</option>
# <option>Казань</option>
# <option>Тверь</option>
# <option>Самара</option>
# <option>Уфа</option>

string = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", text)
print(string)  # <option>Москва</option>
# <option>Казань</option>
# <option>Тверь</option>
# <option>Самара</option>
# <option>Уфа</option>

# Теперь предположим, что у каждого тега option должен быть свой value:
count = 0


def repl_find(match):  # Функция аргументом принимает объект re.Match.
    global count
    count += 1
    return f"<option value='{count}'>{match.group(1)}</option>\n"


string = re.sub(r"\s*(\w+)\s*", repl_find, text)
print(string)  # <option value='1'>Москва</option>
# <option value='2'>Казань</option>
# <option value='3'>Тверь</option>
# <option value='4'>Самара</option>
# <option value='5'>Уфа</option>

"""
Аналогично работает и subn, но он ещё возвращает и число произведённых замен.
"""

string, total = re.subn(r"\s*(\w+)\s*", r"<option>\1</option>\n", text)
print(string, total)  # <option>Москва</option>
# <option>Казань</option>
# <option>Тверь</option>
# <option>Самара</option>
# <option>Уфа</option>
#  5

"""
Метод re.compile(pattern, flags)  выполняет компиляцию регулярного выражения и возвращает его в виде экземпляра класса
Pattern. Это целесообразно использовать, когда, например, мы используем какой-то шаблон (pattern) и предполагаем, что 
много-много раз его будем в последующем использовать.
"""

text = """Москва
Казань
Тверь
Самара
Уфа"""

rx = re.compile(r"\s*(\w+)\s*")

string1 = rx.sub(r"<option>\1</option>\n", text)
string2, total = rx.subn(r"<option>\1</option>\n", text)
print(string1, string2, total, sep='\n')  # В итоге у нас всё отработало, и не пришлось дублировать код.

"""
В общем случае класс Pattern содержит следующие свойства:
    - flags - возвращает список флагов, которые были установлены при компиляции;
    - pattern - строка исходного шаблона;
    - groupindex - словарь, ключами которого являются имена сохраняющих групп, а значениями - номера групп (пустой, если 
    имена не используются).
"""
