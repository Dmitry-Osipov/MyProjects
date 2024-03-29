class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):  # Параметр cls - это ссылка на текущий класс.
        return cls.MIN_COORD <= arg <= cls.MAX_COORD
    # В данном случае метод класса работает исключительно с атрибутами этого класса, но не может обращаться
    # к локальным атрибутам экземпляров классов (потому что в методе validate нет ссылки на экземпляр класса)

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and self.validate(y):  # Данные ниже не были перезаписаны, ибо нарушилось условие,
            # Установленное атрибутами класса. Также технически без разницы, как писать (по имени класса или self).
            # Однако лучшей практикой является пропись self вместо имени класса
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @staticmethod  # С помощью него можем определить методы, которые не имеют доступа ни к атрибутам класса,
    # ни к атрибутам его экземпляров
    def norm2(x, y):
        return x * x + y * y  # В статическом методе не рекомендуется обращаться к атрибутам класса.
        # Если предполагается использовать метод класса, то следует использовать соответсвующий декоратор (classmethod)


v = Vector(1, 200)
res = Vector.get_coord(v)  # При такой записи должна быть ссылка на объект, ибо должен быть параметр self
print(res)  # это равно записи: print(v.get_coord())
print(Vector.validate(5))  # Если мы объявляем метод как метод первоначального класса, мы вызываем его без доп. ссылок
print(Vector.norm2(-5, -3))

"""
Итог:

Когда мы прописываем обычные методы (def __init__(self, x, y):... или def get_coord(self):...), мы предполагаем,
что они вызываются из экземпляров класса и работают с атрибутами этого экземпляра через параметр self, а также работают 
с атрибутами самого класса. Т.е. такие методы имеют доступ и к локальным свойствам экземпляра, из которого были 
вызваны - (v1 = Vector(1, 2)) - в данном случае 1 и 2 - и к атрибутам самого класса - MIN_COORD = 0, MAX_COORD = 100.

Если предполагается определить метод, который будет работать только с атрибутами класса, то его следует определять как 
classmethod. Соответственно, появляется первый параметр cls, т.е. ссылка на текущий класс, и через эту ссылку мы будем 
обращаться к атрибутам класса (MIN_COORD и MAX_COORD). А работать с локальными свойствами экземпляров класса напрямую 
не получится, ибо нет ссылки на соответствующий экземпляр.

Если нам необходимо определить совершенно независимую сервисную функцию, которая бы работала с параметрами, что мы 
определяем непосредственно в ней, то её следует определить как статическую с помощью декоратора staticmethod. 
Соответственно, полагается, что она будет работать совершенно независимо, не будет обращаться ни к атрибутам класса, 
ни локальным атрибутам экземпляра класса. Т.е. она работает сама по себе.
"""
