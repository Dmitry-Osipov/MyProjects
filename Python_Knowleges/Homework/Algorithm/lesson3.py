"""
Связанный список - это базовая структура данных, состоящая из узлов, где каждый узел содержит одну или две ссылки,
который ссылаются на следующий или на следующий и предыдущий узел соответственно. Связанный список очень похож на
массив, но работает не по принципу индексации каждого элемента, а по принципу связи элементов друг с другом. Связанные
списки бывают однонаправленными и двунаправленными (однонаправленные ссылаются на следующий, а двунаправленные на
предыдущий и следующий элемент списка).

 Head                          Tail
Узел 1 -> Узел 2 -> Узел 3 -> Узел 4 - однонаправленный
  1         3         2         4

 Head                             Tail
Узел 1 <-> Узел 2 <-> Узел 3 <-> Узел 4 - двунаправленный
  1          3          2          4

Сложность поиска элемента - O(n), т.к. поиск любой ноды требует перебора элементов. Использование бинарного поиска не
даёт выгоды, т.к. обращение по индексам с константой скоростью недоступно. Также важно особенностью является вставка
элементов. Вставка элемента в массив занимает O(n), в то время как вставка в связанный список O(1). При этом поиск места
вставки может занимать O(n).

Аналогично со сложностью удаления элемента. Удаление элемента из массива O(n), удаление элемента из связанного списка -
O(1), при этом поиск удаляемой ноды может занимать O(n).

Преимущества связанного списка:
- Массовые вставки и удаления в конец/начало списка;
- Массовые вставки и удаления в середину списка, если операция поиска выполняется единожды;
- Динамическая расширяемость.

Разворот:

 Head                          Tail
Узел 1 -> Узел 2 -> Узел 3 -> Узел 4
  1         3         2         4
                |
                V
 Head                          Tail
Узел 1 <- Узел 2 <- Узел 3 <- Узел 4
  1         3         2         4

Разворот связанного списка говорит нам о том, что раньше было head должно стать tail, и наоборот. При этом все ссылки
соседних элементов должны произвести обмен, т.е. next станет previous и наоборот. Проще всего писать разворот связанного
списка на двусвязном списке, ибо у нас есть ссылки на следующий и прошлый элемент.

Частные случаи связанного списка:
- Стэк - работает по принципу LIFO - Last In - First out;
- Очередь - работает по принципу FIFO - First In - First out.

Когда мы говорим про стэк, то идеально подходит односвязный список. Реализуем ниже 2 метода, которые характерны только
для стэка - push (положить данные) и pop (извлечь данные).

Код ниже представляет собой реализацию классов Node и LinkedList для двунаправленного связанного списка, а также
методов для работы с очередью и стеком, используя этот связанный список. Разберём его:
"""


class Node:
    """
    Начинаем с определения класса Node, который представляет узел в связанном списке. Каждый узел содержит
    данные (self.data), ссылку на предыдущий узел (self.prev) и ссылку на следующий узел (self.next).
    """
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    """
     Затем определяем класс LinkedList, представляющий сам связанный список. Этот класс содержит методы для работы с
     самим списком и дополнительно методы для работы с очередью и стеком.
    """
    def __init__(self):
        """
         Конструктор класса LinkedList инициализирует пустой связанный список, устанавливая self.head и self.tail в
         None. self.head указывает на начало списка, а self.tail на его конец.
        """
        self.head = None
        self.tail = None

    def is_empty(self):
        """
         Метод is_empty проверяет, пуст ли связанный список. Если self.head равен None, то список считается пустым, и
         метод возвращает True, иначе - False.
        """
        return self.head is None

    def append(self, data):
        """
        Метод append добавляет новый узел с данными data в конец связанного списка. Если список пуст, создается новый
        узел и он становится как self.head, так и self.tail. В противном случае, метод находит текущий конец списка
        (текущий self.tail) и добавляет новый узел после него. Становясь по итогу его концом (self.tail).
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, prev_node_data, data):
        """
        Метод insert_after вставляет новый узел с данными data после узла с данными prev_node_data. Метод перебирает
        список, находит узел с prev_node_data и вставляет новый узел после него.
        """
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                return
            current = current.next
        raise ValueError(f"Node with data {prev_node_data} not found")

    def delete(self, data):
        """
        Метод delete удаляет узел с данными data из связанного списка. Если узел находится в начале списка, self.head
        обновляется. В противном случае, метод перебирает список, находит узел с data и удаляет его, обновляя связи
        между узлами.
        """
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
        raise ValueError(f"Node with data {data} not found")

    def search(self, data):
        """
         Метод search выполняет поиск узла с данными data в связанном списке. Он перебирает список и возвращает True,
         если узел найден, и False, если нет.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def reverse(self):
        """
        Метод reverse разворачивает связанный список, меняя порядок узлов на обратный. Он использует три указателя:
        prev, current, и next_node, чтобы изменить связи между узлами и обратить список.
        """
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def enqueue(self, data):
        """
        Метод enqueue добавляет элемент в конец очереди, используя ссылки self.prev и self.next для обновления связей
        между узлами.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Метод dequeue удаляет элемент из начала очереди, обновляя ссылки self.head и self.tail.
        """
        if self.is_empty():
            raise Exception("Очередь пуста")
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def push(self, data):
        """
        Метод push добавляет элемент в вершину стека, изменяя self.head и self.tail в зависимости от состояния стека.
        """
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def pop(self):
        """
        Метод pop удаляет элемент из вершины стека, обновляя self.head и self.tail.
        """
        if self.is_empty():
            raise Exception("Стек пуст")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data

    def print_list(self):
        """
        Метод print_list выводит элементы связанного списка, начиная с self.head, в формате
        "значение -> значение -> ... -> None", чтобы можно было увидеть содержимое списка.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Создание двунаправленного связанного списка
my_list = LinkedList()

# Добавление элементов в конец списка
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_list()  # 1 -> 2 -> 3 -> None

# Вставка элемента после определенного узла
my_list.insert_after(2, 4)
my_list.print_list()  # 1 -> 2 -> 4 -> 3 -> None

# Удаление элемента из середины списка
my_list.delete(4)
my_list.print_list()  # 1 -> 2 -> 3 -> None

# Поиск элемента
print(my_list.search(2))  # True
print(my_list.search(5))  # False

# Разворот списка
my_list.reverse()
my_list.print_list()  # 3 -> 2 -> 1 -> None

# ----------------------------------------------------------------------------------------------------------------------

# Работа с очередью:
# Создание пустой очереди
my_queue = LinkedList()

# Добавление элементов в очередь
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.print_list()  # 10 -> 20 -> 30 -> None
"""Напоминание: очередь работает по принципу FIFO - First In - First out."""
# Удаление элемента из начала очереди
item = my_queue.dequeue()  # item = 10
my_queue.print_list()  # 20 -> 30 -> None

# ----------------------------------------------------------------------------------------------------------------------

# Работа со стэком:
# Создание пустого стека
my_stack = LinkedList()

# Добавление элементов в стек
my_stack.push(500)
my_stack.push(1000)
my_stack.push(1500)
my_stack.print_list()  # 1500 -> 1000 -> 500 -> None
"""Напоминание: стэк работает по принципу LIFO - Last In - First out."""
# Удаление элемента из вершины стека
item = my_stack.pop()  # item = 1500
my_stack.print_list()  # 1000 -> 500 -> None
