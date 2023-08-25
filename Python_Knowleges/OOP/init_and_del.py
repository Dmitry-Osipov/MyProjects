# В Python существуют специальные магические методы __имя метода__
# __init__(self) - инициализатор объекта класса
# __del__(self) - финализатор класса

class Point:
    color = 'red'
    circle = 2

    def __init__(self, a: int = 0, b: int = 0):
        # Для примера указали a, b, но грамотно будет указать те же параметры, что и ниже
        print("Вызов __init__")  # Проверяем, был ли вызван инициализатор
        self.x = a
        self.y = b

    def __del__(self):
        print("Удаление экземпляра: " + str(self))

    def get_coords(self):
        return self.x, self.y


pt = Point(1, 2)
print(pt.__dict__)  # В пространстве имён будут указаны переменные, которые мы указали с использованием self.
