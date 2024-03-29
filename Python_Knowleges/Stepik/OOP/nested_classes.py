"""
Хорошим примером использования вложенных классов является описание модели во фреймворке Django.
Ниже класс Women представляет данные некоей таблицы в базе данных. А внутри этого класса прописывается атрибуты.
Атрибуты - это соответствующие поля этой таблицы. Когда создаётся экземпляр этого класса, то автоматически в экземплярах
класса сразу появляются необходимые данные из этой таблицы.
Внутри такой модели в Django можно прописывать вложенные классы (например, Meta), где можно прописывать дополнительные
параметры (например, параметр ordering говорит о том, что перед тем, как достать данные из таблицы, их надо
отсортировать по параметру id).
Но почему во фреймворке Django реализовали через вложенный класс, а не просто перенесли ordering к атрибутам класса?
Представим, что в нашей таблице уже есть некий ordering. Таким образом, получается конфликт, ибо ordering - это поле из
таблицы базы данных и одновременно с этим ordering - это параметр, который управляет сортировкой этих записей в таблице.
Чтобы разрешить этот конфликт, нужен вложенный класс. Вложенный класс реализует пространство имён, независимое от класса
Women, и в Meta мы можем спокойно прописывать различные атрибуты
"""


class Women:
    title = 'Объект класса для поля title'
    photo = 'Объект класса для поля Photo'
    ordering = 'Объект класса для поля ordering'

    class Meta:
        ordering = ['id']


w = Women()
print(Women.ordering)  # Объект класса для поля ordering
print(Women.Meta.ordering)  # ['id']

print(w.ordering)
print(w.Meta.ordering)  # Увидим тот же вывод.
print(w.__dict__)  # Видим, что локальных атрибутов в этом экземпляре класса у нас нет, ибо внутри класса Women нет
# инициализатора, соответственно, мы и не создавали никаких локальных свойств. Пропишем __init__ в Women:


class Women:
    title = 'Объект класса для поля title'
    photo = 'Объект класса для поля Photo'
    ordering = 'Объект класса для поля ordering'

    def __init__(self, user, password):
        self.user = user
        self._password = password

    class Meta:
        ordering = ['id']


w = Women('root', '12345')
print(w.__dict__)  # Теперь у нас создаётся экземпляр класса Women, внутри которого есть 2 локальных свойства, а
# остальные атрибуты (photo, title, ordering) находятся в классе Women и вложенном классе Meta. Важно обратить внимание,
# что мы не создаём класс Meta. Мы создаём объект класса Women, но не Meta. Если при создании экземпляра Women требуется
# также создавать и Meta, то это нужно явно указать в инициализаторе Women (self.meta = self.Meta()):


class Women:
    title = 'Объект класса для поля title'
    photo = 'Объект класса для поля Photo'
    ordering = 'Объект класса для поля ordering'

    def __init__(self, user, password):
        self.user = user
        self._password = password
        self.meta = self.Meta()

    class Meta:
        ordering = ['id']


w = Women('root', '12345')
print(w.__dict__)  # Добавилось локальное свойство 'meta': <__main__.Women.Meta object at 0x00000275EFFAB310>
print(w.meta.__dict__)  # Выдаст пустой словарь для экземпляра вложенного класса. Соответственно, если нам требуется
# заполнить локальные свойства, то во вложенном классе требуется реализовать инициализатор:


class Women:
    title = 'Объект класса для поля title'
    photo = 'Объект класса для поля Photo'
    ordering = 'Объект класса для поля ordering'

    def __init__(self, user, password):
        self.user = user
        self._password = password
        self.meta = self.Meta(user + '@' + password)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access


w = Women('root', '12345')
print(w.__dict__)
print(w.meta.__dict__)  # {'_access': 'root@12345'}.
"""
Т.е. мы из класса Women спокойно обращаться к вложенному классу
Meta и создавать его объекта. Но делать наоборот: из вложенного класса обращаться к атрибутам основного класса -
нельзя. Например, если после атрибута в классе Meta прописать: t = Women.title - мы получим NameError, что класс Women
не определён. Почему это так? Когда мы выполняем эту строчку, то класс Women ещё не создан - такого пространства имён
не существует, и мы обращаемся в той строчке к несуществующему пространству имён. Поэтому напрямую во вложенных
классах обращаться к каким-либо атрибутам внешнего класса нельзя, хотя в инициализаторе вложенного класса мы это уже
можем сделать, ибо когда инициализатор Meta срабатывает, то все классы созданы, и тогда мы уже можем через
пространство имён обращаться к Women и брать оттуда какие-либо атрибуты. Например:
"""


class Women:
    title = 'Объект класса для поля title'
    photo = 'Объект класса для поля Photo'
    ordering = 'Объект класса для поля ordering'

    def __init__(self, user, password):
        self.user = user
        self._password = password
        self.meta = self.Meta(user + '@' + password)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access
            self._t = Women.title


w = Women('root', '12345')
print(w.__dict__)
print(w.meta.__dict__)  # Добавилось - '_t': 'Объект класса для поля title'
"""
Но на практике так делать не следует - не следует обращаться к атрибутам внешнего класса из вложенных классов. Логику 
программы следует продумывать так, чтобы вложенный класс никак не был связан с внешним классам. Т.е. внутренний класс 
используется исключительно внешним классом, но не наоборот - вложенный класс не должен использовать атрибуты внешнего 
класса. 
Подобные вложения служат исключительно для удобства программирования, какого-то особого смысла во вложенных классах нет. 
Всё, что можно делать через вложения, так же можно реализовать и без них, используя обычные независимые объявления.
"""
