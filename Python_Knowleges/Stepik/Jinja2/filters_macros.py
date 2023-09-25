from jinja2 import Template

"""
Подробнее рассмотрим фильтры, которые удобно применять для получения более точных представлений.
sum - вычисление суммы поля коллекции;
max - вычисление максимального элемента коллекции;
min - вычисление минимального элемента коллекции;
random - случайным образом выбирает запись из коллекции;
replace - замена символов в коллекции;
"""

cars = [
    {'model': 'Audi', 'price': 23000, },
    {'model': 'Skoda', 'price': 17300, },
    {'model': 'Volvo', 'price': 44300, },
    {'model': 'Volkswagen', 'price': 21300, }
]

tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = "Максимальная цена у автомобиля {{ (cs | max(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = "Минимальная цена у автомобиля {{ (cs | min(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = "Случайный элемент - {{ cs | random }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = "Новая коллекция - {{ cs | replace('o', 'O') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

"""
Фильтры так же можно применять непосредственно внутри шаблонов:
{% filter название_фильтра %}
фрагмент для применения фильтра
{% endfilter %}
"""

persons = [
    {'name': 'Алексей', 'old': 18, 'weight': 78.5, },
    {'name': 'Николай', 'old': 28, 'weight': 82.3, },
    {'name': 'Иван', 'old': 33, 'weight': 94.0, }
]

tpl = """
{%- for user in users -%}
{% filter upper %}{{user.name}}{% endfilter %}
{% endfor -%}
"""

tm = Template(tpl)
msg = tm.render(users=persons)
print(msg)

"""
Также модуль Jinja поддерживает макроопределения для шаблонов, которые весьма полезны, чтобы избежать повторяемых 
определений в соответствии с принципом DRY (Don't Repeat Yourself). Рассмотрим подробнее.
Допустим, мы формируем HTML-документ и хотим создать несколько полей input. Для этого пропишем макроопределение:
"""

html = """
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password')}} 
"""

tm = Template(html)
msg = tm.render()
print(msg)

"""
Вложенные макросы.
Jinja имеет специальные определения - call - которые позволяют создавать своего рода вложенные макросы. 
{% call[(параметры)] вызов_макроса %}
вложенный_шаблон
{% endcall %}


Проще всего понять работу этого блока можно на примере. Предположим, что мы хотим сформировать вот такой список:

Алексей:
    age: 18
    weight: 78.5
Николай:
    age: 28
    weight: 82.3
Иван:
    age: 33
    weight: 94.0

На уровне html это будет список с вложенным списком. Соответственно, будет очень много тэгов списков.
"""

html = """
{% macro list_users(list_of_user) -%}
<ul>
{% for item in list_of_user -%}
    <li>{{ item.name }}  {{ caller(item) }}
{%- endfor %}
</ul>
{% endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{ user.old }}
    <li>weight: {{ user.weight }}
    </ul>
{% endcall -%}
"""

tm = Template(html)
msg = tm.render(users=persons)
print(msg)
