"""
Полиморфизм - это возможность работы с совершенно разными объектами языка Python единым образом. Т.е. через единый
интерфейс.
"""


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_rect_pr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_sq_pr(self):
        return 4 * self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)

# # Представим, что мы хотим представить все эти объекты в виде одного списка.
# geom = [r1, r2, s1, s2]
# for g in geom:
#     print(g.get_rect_pr())  # При выборе функции видим 2 разных метода для прямоугольника и для квадрата.
#     # Ожидаемо получаем ошибку AttributeError: 'Square' object has no attribute 'get_rect_pr'

# Но как можно решить нашу проблему? Можно решить в лоб:
