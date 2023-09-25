from jinja2 import Environment, FileSystemLoader

"""
Механизм расширения (или наследования) шаблонов позволяет избежать дублирование кода в шаблонах. Рассмотрим пример его
работы на наших html-страницах сайта. Возьмём шаблон ex_main.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
{% endblock %}

</body>
</html>

Здесь используется новый тип блоков - именованные блоки (block title и block content).
Общий синтаксис:
{% block имя_блока %}
{% endblock %}

Такие блоки как раз используются для создания расширения базового шаблона нашей страницы. Для этого создадим шаблон
about.html (который будет расширять ex_main.html):
{% extends 'ex_main.html' %}

{% block title %}О сайте{% endblock %}

{% block content %}
<h1>О сайте</h1>
<p>Классный сайт, если его доделать</p>
{% endblock %}

Первой строчкой идёт конструкция extends, а далее имя того шаблона, который мы собираемся расширять. Т.е. по сути имя
базового шаблона, на основе которого строится страница about.html. Далее мы говорим, что в именованном блоке title
должна помещаться определённая информация, а в блоке content должна размещаться другая информация: заголовок и параграф.

Таким образом, мы сделали расширение базового шаблона. Причём вместо именованного блока в базовом шаблоне будет
подставлено соответствующее содержимое, и аналогично с другим именованным блоком.
Рассмотрим, как взять шаблон about.html и получить конкретное его представление:
"""

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('about.html')
output = template.render()
print(output)
print('\n'*3)

"""
Но часто на практике бывает так, что базовые шаблоны находятся в каком-то другом подкаталоге. Например:
{% extends 'layout/default.html' %}

{% block title %}О сайте{% endblock %}

{% block content %}
<h1>О сайте</h1>
<p>Классный сайт, если его доделать</p>
{% endblock %}

Т.е. относительно всех наших шаблонов есть подкаталог layout, в котором лежит шаблон default.html. Попробуем проверить 
это в новом файле about2.html:
"""

subs = ['Математика', 'Физика', 'Информатика', 'Русский']

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('about2.html')
output = template.render(list_table=subs)
print(output)

"""
Далее предположим, что у нас блок title и тэг h1 содержат одну и ту же информацию. Так вот, чтобы не дублировать эту 
информацию, мы можем воспользоваться конструкцией:
{% extends 'layout/default.html' %}

{% block title %}О сайте{% endblock %}

{% block content %}
<h1>{{ self.title() }}</h1>
<p>Классный сайт, если его доделать</p>
{% endblock %}

Т.е. в тэге h1 мы обратились к title через self. И чтобы блок title выдал своё содержимое, мы вызовем его, как функцию.
Но а раз есть self, то должен быть и параметр super для обращения к блоку базового шаблона и взятия оттуда информации.
Для этого пропишем следующее:
{% extends 'layout/default.html' %}

{% block title %}О сайте{% endblock %}

{% block content %}
{{ super() }}
<h1>{{ self.title() }}</h1>
<p>Классный сайт, если его доделать</p>
{% endblock %}

Вызвали super. Т.е. будем предполагать, что в это место блока контента будет подставлено содержимое этого же блока 
контента, но уже из базового шаблона. А в базовом шаблоне пропише следующее:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
<p>Блок контента</p>
{% endblock %}

</body>
</html>

Действительно, всё отработало. Это пример показывает, что блок контента, который мы прописываем в дочернем шаблоне, 
полностью переписывает содержимое такого же блока, но в базовом шаблоне. Т.е. чего бы там в базовом шаблоне ни было, всё
это будет удалено и добавлено только то, что мы прописали в дочернем. А если мы всё-таки хотим что-то сохранить (из 
базового шаблона взять), то для этого используем super().

В шаблонах можно делать вложенные блоки:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
    {% block table_contents %}
    <ul>
        {% for li in list_table -%}
        <li>{{ li }}</li>
        {% endfor %}
    </ul>
    {% endblock table_contents %}
{% endblock content %}

</body>
</html>

Слова в окончаниях шаблонов приведены для лучшего понимания программы. Они необязательны, но когда они присутствуют, мы 
чётко понимаем, где какой блок кончается. Далее в дочернем шаблоне вызываем super() (ибо только благодаря нему всё 
заработает). И чтобы его наполнить конкретным содержимым в программе выше добавим список из предметов. И также выше 
дополним метод render, прописав в нём list_table=subs. Дополнительно преобразуем дочерний шаблон:
{% extends 'layout/default.html' %}

{% block title %}О сайте{% endblock %}

{% block content %}
{% block table_contents %}{{ super() }}{% endblock %}
<h1>{{ self.title() }}</h1>
<p>Классный сайт, если его доделать</p>
{% endblock %}

Т.е. мы указали конкретно блок table_contents и в нём прописали super(). Тогда этот super() будет относиться к 
информации только этого блока. Т.е. мы будем брать не из блока content что-то, а из блока table_contents.
Соответственно, такой вариант будет более гибким, ибо если у нас есть ещё другие именованные блоки, то мы можем их 
добавлять по мере необходимости. К примеру, если бы нам на какой-то странице не нужно было содержание, то мы бы просто 
убрали эту строчку с super(), и коллекция subs бы не отработала.

Ещё усовершенствуем базовый шаблон и добавим блок дя формирования списка:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
    {% block table_contents %}
    <ul>
        {% for li in list_table -%}
        <li>{% block item %}{{ li }}{% endblock item %}</li>
        {% endfor %}
    </ul>
    {% endblock table_contents %}
{% endblock content %}

</body>
</html>

Запустив программу, мы увидим, что у элементов списков нет имён, хотя ранее они были. Так произошло потому, что внутри 
блока item, который мы добавили, переменной li уже не существует. Ибо всё, что находится внутри блока, не имеет доступа 
к внешнему контексту. Т.е. мы не можем брать переменные за пределами блока. Чтобы исправить это, нужно добавить ключевое
слово scoped в блок item:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>

{% block content %}
    {% block table_contents %}
    <ul>
        {% for li in list_table -%}
        <li>{% block item scoped %}{{ li }}{% endblock item %}</li>
        {% endfor %}
    </ul>
    {% endblock table_contents %}
{% endblock content %}

</body>
</html>

Теперь всё работает. Но теперь оправдаем добавление блока item. В дочернем шаблоне добавим:
{% extends 'layout/default.html' %}

{% block title %}О сайте{% endblock %}

{% block content %}
{% block table_contents %}{{ super() }}{% endblock %}
<h1>{{ self.title() }}</h1>
<p>Классный сайт, если его доделать</p>
{% endblock %}

{% block item %}<p class="item">{{ super }}</p>{% endblock %}

Вызываем super(), чтобы подставить содержимое блока, т.е. название предмета внутрь тэга p.

В конце отметим очевидный момент: шаблоны поддерживают последовательное наследование. Например, возможна такая иерархия:
child2.html -> child1.html -> base.html.
"""
