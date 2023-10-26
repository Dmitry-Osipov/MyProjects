import re

text = "<font color=#CC0000>"
match = re.search(r"(\w+)=(#[\da-fA-F]{6}\b)", text)  # Метод возвращает объект Match, когда находит совпадения,
# иначе возвращается None.
print(match)

"""
Свойства и методы объекта Match.
В нашем примере мы нашли совпадения: 
Под индексом 0 идёт полное вхождение (color=#CC0000), а далее вхождение во вхождение будет таким: под индексом 1 идёт 
color, а под индексом 2 - #CC0000 (т.е. ключ и значение). Эти результаты можно посмотреть с помощью метода group(): 
"""

print(match.group(0))  # color=#CC0000.
print(match.group(1))  # color.
print(match.group(2))  # #CC0000.
print(match.group(0, 1, 2))  # ('color=#CC0000', 'color', '#CC0000').
print(match.groups())  # Возвращаем кортеж из всех групп, начиная с индекса 1 - ('color', '#CC0000').
print(match.lastindex)  # Получаем индекс последней сохраняющей группы.
print(match.start(1))  # Получаем индекс начала определённой группы - 6.
print(match.start(2))  # Получаем индекс начала определённой группы - 12.
print(match.end(1))  # Получаем индекс конца определённой группы - 11.
print(match.end(2))  # Получаем индекс конца определённой группы - 19.
print(match.span())  # Получаем кортеж с начальными и конечными позициями для каждой группы - (6, 19).
print(match.span(1))  # (6, 11).
print(match.span(2))  # (12, 19).
print(match.endpos)  # 20 - последняя позиция, до которой прошёл метод search при поиске шаблона.
print(match.pos)  # 0 - первая позиция, с которой пошёл метод search при поиске шаблона.
print(match.re)  # Получаем скомпилированный шаблон - re.compile('(\\w+)=(#[\\da-fA-F]{6}\\b)').
print(match.string)  # Получаем анализируемую строку - <font color=#CC0000>.

match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print(match.groupdict())  # Получаем словарь, содержащий имя группы и её значение - {'key': 'color', 'value': '#CC0000'}
print(match.lastgroup)  # Получаем имя последней группы либо None - value.
print(match.expand(r"\g<key>:\g<value>"))  # Формируем строку с использованием сохранённых групп - color:#CC0000.

"""
В методе expand() можно использовать следующий синтаксис: 
    \g<name> - обращение к группе по имени;
    \1, \2... - обращение к группе по номеру.
"""

print(match.expand(r"\1:\2"))  # Получаем то же самое, но это менее удобно и безопасно.

"""
Методы re.search, re.finditer и re.findall.
Начнём с метода re.search. Записывается в виде re.search(pattern, string, flags), где:
    - pattern - регулярное выражение;
    - string - анализируемая строка;
    - flags - один или несколько флагов.
"""

text = "<font color=#CC0000 bg=#ffffff>"
match = re.search(r"(\w+)=(#[\da-fA-F]{6}\b)", text)  # Игнорируется второй атрибут.
print(match)  # <re.Match object; span=(6, 19), match='color=#CC0000'>

"""
Таким образом, если нам нужно выделить всё, то требуется воспользоваться методом re.finditer. Этот метод имеет те же 
самые параметры и возвращает итерируемый объект, с помощью которого можно перебрать все найденные вхождения.
"""

for match in re.finditer(r"(\w+)=(#[\da-fA-F]{6}\b)", text):
    print(match)  # <В итоге получаем: re.Match object; span=(6, 19), match='color=#CC0000'> и
    # <re.Match object; span=(21, 31), match='bg=#ffffff'>.

"""
Если же на выходе следует получить просто список найденных вхождений, то следует использовать re.findall. Этот метод 
имеет те же самые параметры.
"""

match = re.findall(r"(\w+)=(#[\da-fA-F]{6}\b)", text)
print(match)  # [('color', '#CC0000'), ('bg', '#ffffff')] - причём получаем только сохраняющие группы, полное вхождение
# здесь будет отсутствовать. Недостатком данного метода является получение данных в виде списка, в то время как
# остальные методы возвращают объект Match, обладающий богатым функционалом.
