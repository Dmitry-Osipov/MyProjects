from jinja2 import Template
from markupsafe import escape

data = """Модуль Jinja вместо 
определения {{ name }} 
подставляет соответствующее значение\n\n"""

"""
Рассмотрим способы экранирования данных в строках. 
Представим, что мы бы хотели фрагмент шаблона никак не преобразовывать. Если реализовать шаблон на основе класса 
Template и выполнить метод render(), то вместо name будет подставлено Фёдор:
"""

tm = Template(data)
msg = tm.render(name='Фёдор')
print(msg)

"""
Но это не совсем то, что нам нужно. Мы хотим, чтобы эти строчки data никак не преобразовывались. Как это сделать? 
Для этого в Jinja есть специальный блок: {% raw %} ... {% endraw %} - всё, что находится внутри блока, никак не будет 
преобразовано, а будет представлено ровно так, как записано. Преобразуем программу:
"""

data = """{% raw %}Модуль Jinja вместо 
определения {{ name }} 
подставляет соответствующее значение{% endraw %}\n\n"""

tm = Template(data)
msg = tm.render(name='Фёдор')
print(msg)

"""
При работе с текстовыми html-шаблонами часто возникает необходимость экранирования некоторых символов, которые браузером
воспринимаются как опережения тегов. Например: 
"""

link = """В HTML-документе ссылки определяются так: 
<a href='#'>Ссылка</a>\n\n"""

tm = Template(link)
msg = tm.render()
print(msg)

"""
В консоли всё как нужно, но если перенести этот код в html-файл и открыть в браузере, то мы увидим подчёркнутую надпись
Ссылка, а она, естественно, ведёт на ошибку 404. Т.е. на сайте мы не увидим текста "<a href...". Мы видим обработанную 
html-страницу. Так вот экранирование заключается в том, чтобы текст в браузерах выводить не как тэг <a>, а в виде 
текста. Для этого Jinja позволяет внутри скобок прописывать специальные флаги. Например, флаг e (escape - экранирование)
в данном случае будет означать экранирование символов-тэгов.

Чтобы это реализовать, мы должны преобразовать шаблон, где будет помещена некая переменная link и далее после 
вертикальной черты указать тот или иной флаг:
"""

tm = Template('{{ link | e }}')
msg = tm.render(link=link)
print(msg)

"""
На выходе мы получили, что у нас теперь угловые скобки представляются в виде спец символов (например, &lt;).
И теперь при отображении в браузере такой строки вместо ссылки мы увидим нужный нам текст.

Но мы используем довольно громоздкую конструкцию для того, чтобы просто экранировать такой простой текст.
Т.к. это довольно частая операция, то в модуле markupsafe предусмотрен специальный класс escape, который и делает такое 
преобразование:
"""

msg = escape(link)
print(msg)

"""
Следующий вид блока, который мы рассмотрим, - это блок for, который позволяет формировать список на основе любого 
итерируемого объекта. Например, упорядоченного списка:
{% for <выражение> %}
    <повторяемый_элемент>
{% endfor %}
"""

cities = [
    {'id': 1, 'city': 'Москва', },
    {'id': 5, 'city': 'Тверь', },
    {'id': 7, 'city': 'Минск', },
    {'id': 8, 'city': 'Смоленск', },
    {'id': 11, 'city': 'Калуга', }
]

link = """<select name="cities>
{% for item in cities %}
    <option value="{{ item['id'] }}">{{ item['city'] }}</option>
{% endfor %}
</select> 
"""

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)

"""
Но у каждого элемента мы видим перенос строки из-за нашей записи. Чтобы переноса строки не было, нам нужно прописать всё
в одну строчку с переносом endfor на другую. Если же требуется всё записать в одну строку, то всё и пишем в одну строку.
"""

link = """<select name="cities>
{% for item in cities %}<option value="{{ item['id'] }}">{{ item['city'] }}</option>
{% endfor %}</select> 
"""

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)

"""
Либо есть ещё один вариант записи. Добавляем минус к последнему проценту в блоке for и endfor:
"""

link = """<select name="cities>
{% for item in cities -%}
    <option value="{{ item['id'] }}">{{ item['city'] }}</option>
{% endfor -%}
</select> 
"""

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)

"""
Видим такой же вывод, что и чуть выше.

Последний блок, что мы рассмотрим - это блок условий. Запись в самом простом варианте:
{% if <условие> %}
    <фрагмент при истинности условия>
{% endif %}
"""

link = """<select name="cities>
{% for item in cities -%}
{% if item.id > 6 -%}
    <option value="{{ item['id'] }}">{{ item['city'] }}</option>
{% endif -%}
{% endfor -%}
</select> 
"""

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
print()

"""
Итак, мы получили вывод строк по городам, у которых id > 6. Также в блоке if можно использовать else:
"""

link = """<select name="cities>
{% for item in cities -%}
{% if item.id > 6 -%}
    <option value="{{ item['id'] }}">{{ item['city'] }}</option>
{% else -%}
    {{ item['city'] }}
{% endif -%}
{% endfor -%}
</select> 
"""

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
print()

"""
Также в блоке if может быть и конструкция elif:
"""

link = """<select name="cities>
{% for item in cities -%}
{% if item.id > 6 -%}
    <option value="{{ item['id'] }}">{{ item['city'] }}</option>
{% elif item.city == 'Москва' -%}
    <option>{{ item['city']}}</option>
{% else -%}
    {{ item['city'] }}
{% endif -%}
{% endfor -%}
</select> 
"""

tm = Template(link)
msg = tm.render(cities=cities)
print(msg)
