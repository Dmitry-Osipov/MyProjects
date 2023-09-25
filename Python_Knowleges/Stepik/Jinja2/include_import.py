from jinja2 import Environment, FileSystemLoader

"""
Часто при создании сайтов страницу делят как минимум на 3 части: header, content и footer. Т.е. мы можем сайт разделить
на 3 разные страницы и конкретно каждую страницу поместить в свой файл, а потом их соединить. Соединить как раз при
помощи конструкции include.

Например, разобьём страницу main.html на 3 составляющие: с начала и до открывающего тэга body будет header, закрывающий
тэг body и до конца - это footer, а остальным будет content.

В контенте(page.html) пишем:
{% include 'header.html' %}
<p>Содержимое страницы</p>
{% include 'footer.html' %}

Вот мы как раз используем конструкцию include, в котором подключаем вначале header.html, а в конце footer.html, по
центру же выводим некое содержимое страницы. И далее в программе мы и будем загружать шаблон из page.html
"""

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render()
print(msg)
print()

"""
В результате, мы получили собранную страницу. В дальнейшем так же можно работать и с другими страницами.
Но что, если какой-то файл не будет найден?
Мы получим исключение TemplateNotFound. Конечно, можно поймать, обработать это исключение. Но если нас интересует просто 
пропустить это исключение без обработки, а и нам не требуется подключать файл, если его нет, то мы можем преобразовать 
блок include:
{% include 'header.html' ignore missing %}
<p>Содержимое страницы</p>
{% include 'footer.html' %}

Теперь при запуске программы, если неверно указать header, то мы подключим оставшееся.

А если нам требуется, что для каждой страницы был свой заголовок, но при этом нам нужно не создавать новые header?
Преобразуем файл header.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <base href="{{ domain }}">
    <title>{{ title }}</title>
</head>
<body>

Далее, чтобы подставлять нужные домены и заголовки, делаем следующее:
"""

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain='https://proproprogs.ru/', title='Про Jinja')
print(msg)
print()

"""
Если в блоке include требуется подцепить сразу несколько страниц, то мы это указываем в квадратных скобках:
{% include ['page1.html', 'page2.html'] ignore missing %}

В заключении рассмотрим конструкцию import. Jinja позволяет не только включать отдельные файлы в общий шаблон, но и 
импортировать их. Отличие import от include состоит в том, что при import файл не добавляется, но мы можем использовать
функционал этого файла, который импортируем. Часто это делается, когда в импортируемом файле находится какой-нибудь 
макрос. И этот макрос мы и используем в нашем исходном шаблоне. Посмотрим, как это делается:
есть файл dialogs.html, в котором хранится макрос, создающий диалоговые окна на нашей html-странице. Мы ему можем 
передать заголовок диалогового окна и сообщение, которое будет появляться в этом диалоговом окне. А сам диалог 
формируется внутри тэгов div:
{% macro dialog_1(title, msg='') -%}
<div class="dialog">
    <p class="title">{{ title }}</p>
    <p class="message">{{ msg }}</p>
    <p><input type="button" value="Закрыть"></p>
</div>
{%- endmacro %}

Теперь импортируем всё это в page.html:
{% import 'dialogs.html' as dlg %}
{% include 'header.html' ignore missing %}
<p>Содержимое страницы</p>
{{ dlg.dialog_1('Внимание', 'Это тестовый диалог') }}
{% include 'footer.html' %}

либо:
{% from 'dialogs.html' import dialog_1 as dlg %}
{% include 'header.html' ignore missing %}
<p>Содержимое страницы</p>
{{ dlg('Внимание', 'Это тестовый диалог') }}
{% include 'footer.html' %}

либо без as, если так удобнее.

Запустим заново программу (она у нас не изменилась).
"""
