from jinja2 import Environment, FileSystemLoader, FunctionLoader

"""
На прошлых занятиях мы прописывали шаблоны в виде многострочного текста. Но в действительности они хранятся в отдельных 
текстовых файлах и загружаются по мере необходимости. Для реализации такого функционала в Jinja есть класс Environment, 
который и представляет собой некий центральный объект, через который и происходит работа с API данного пакета.

Предположим, что все наши шаблоны находятся в подкаталоге templates относительно рабочего подкаталога программы. И 
внутри этого подкаталога шаблонов рассмотрим один из них - main.html:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <base href="https://proproprogs.ru/">
    <title>Про программирование</title>
</head>
<body>

<ul>
    {% for user in users -%}
        <li>{{ user.name }}</li>
    {% endfor -%}
</ul>

</body>
</html>

Мы должны получить текстовую строку с соответствующим содержимым. Для этого мы пропишем программу:
"""

persons = [
    {'name': 'Алексей', 'old': 18, 'weight': 78.5, },
    {'name': 'Николай', 'old': 28, 'weight': 82.3, },
    {'name': 'Иван', 'old': 33, 'weight': 94.0, }
]

file_loader = FileSystemLoader('templates')  # При работе с главным подкаталогом аргументом требуется указать пустую строку.
env = Environment(loader=file_loader)  # Класс окружения, через который происходит работа с API данного пакета. Т.е. этот
# загрузчик будет брать все шаблоны из нашего подкаталога templates.

tm = env.get_template('main.html')  # Далее берём шаблон, из которого будем работать. Метод get_template формирует экземпляр
# класса Template на основе содержимого передаваемого файла
msg = tm.render(users=persons)
print(msg)
print()

"""
Все варианты загрузчиков (templates):
FileSystemLoader - для загрузки шаблонов из файловой системы;
PackageLoader - для загрузки шаблонов из пакета;
DictLoader - для загрузки шаблонов из словаря;
FunctionLoader - для загрузки на основе функции;
PrefixLoader - загрузчик, использующий словарь для построения подкаталогов;
ChoiceLoader - загрузчик, содержащий список других загрузчиков (если один не сработает, выбирается следующий);
ModuleLoader - загрузчик для скомпилированных шаблонов.

В качестве примера рассмотрим FunctionLoader:
"""


def load_tpl(path):
    if path == 'index':
        return """Имя {{ user.name }}, возраст {{ user.old }}"""
    else:
        return """Данные: {{ user }}"""


file_loader = FunctionLoader(load_tpl)
env = Environment(loader=file_loader)

tm = env.get_template('index')
msg = tm.render(user=persons[0])
print(msg)

tm = env.get_template('notindex')
msg = tm.render(user=persons[0])
print(msg)

"""
Остальные загрузчики работают подобным прошлым классам образом, а более подробную информацию можно увидеть на сайте 
официальной документации.
"""
