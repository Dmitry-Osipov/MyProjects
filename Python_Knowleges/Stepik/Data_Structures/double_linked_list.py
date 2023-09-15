"""
Двусвязный список - это тот же односвязный список, но у каждого элемента есть 2 ссылки next и prev (на следующий и
прошлый элементы соответственно).

                head                                                    tail
                 |                                                       |
                 V                                                       V
            |---------|       |---------|        |---------|        |---------|
None <==    |  data   |<== ==>|  data   |<==  ==>|  data   |<==  ==>|  data   |     ==> None
       ||   |---------|  ||   |---------|   ||   |---------|   ||   |---------|   ||
         ===|prev-next|=== ===|prev-next|===  ===|prev-next|===  ===|prev-next|===
            |---------|       |---------|        |---------|        |---------|

Также имеем 2 элемента списка: head и tail, которые ссылаются на первый и последний элементы соответственно.
В результате можно быстро обрабатывать элементы. Например, делать добавление элементов в начало или конец списка, а
также удалять их. Важно обратить внимание, что у граничных объектов next и prev принимают значение None:
для head.prev = None (ибо это первый элемент списка, раньше него ничего стоять не может) и для tail.next = None (ибо это
последний элемент списка, после него ничего стоять не может).

Добавление в конец списка.
Меняем ссылку tail.next на наш новый элемент (пусть node), и вместе с тем меняем ссылку node.prev на наш хвост, после
чего двигаем указатель tail на наш новы последний элемент списка. На псевдокоде: tail.next = node -> node.prev = tail ->
tail = node. Сложность данной операции О(1). Реализуется командой push_back().

Добавление в начало списка.
По аналогии реализуется добавление в начало списка. Меняем ссылку head.prev на новый элемент (пусть node), и вместе с
тем меняем ссылку node.next на нашу голову, после чего двигаем указатель head на наш новый первый элемент.
На псевдокоде: head.prev = node -> node.next = head -> head = node. Скорость работы этой операции так же O(1).
Реализуется командой push_front().

Доступ к произвольному элементу.
Допустим, есть список, в котором мы знаем только head и tail. Создадим временную переменную node, которая указывает на
head. Благодаря временной переменной мы можем читать данные в списке (на псевдокоде - value = node.data) и переходить к
следующему элементу (на псевдокоде - node = node.next). Таким образом в цикле мы можем проходить по элементам. Чтобы
изменить значение в нужном элементе нужно перезаписать его (на псевдокоде - node.data = value). Сложность операции
доступа к элементу в середине списка - O(n).

Важной отличительной особенностью двусвязного списка является то, что мы можем двигаться по нему как вперёд, так и
назад: node = node.next - для движения вперёд - и node = node.prev - для движения назад. Во всём остальном они работаю
в принципе одинаково.

Вставка элемента в произвольную позицию двусвязного списка.
Создаём новый элемент с временной переменной node. Находим нужный элемент слева и справа, указываем ссылки на них
(left и right соответственно). Далее связываем с нашим node элемент слева (left.next = node -> node.prev = left) и
элемент справа (right.prev = node -> node.next = right). Сложность данной операции O(n) - вставка О(1) + нахождение left
и right O(n). Реализуется командой insert().

Удаление промежуточных элементов.
Находим нужный элемент. Указываем его как node. Далее присваиваем переменные слева и справа от него (left = node.prev и
right = node.next). После чего освобождаем память, занимаемое объектом node, настраивая связи между left и right
(left.next = right -> right.prev = left). Удаление занимает O(n), ибо получение элемента O(n) + само удаление O(1). Сама
функция реализуется через erase().

Удаление первого элемента.
Устанавливаем ссылку на следующий элемент от head (пусть node), т.е. node = head.next. Убираем ссылку на head у нашего
node (node.prev = None), после чего переносим ссылку head на новое начало (head = node). Сложность операции O(1).
Реализуется методом pop_front().

Удаление последнего элемента.
Удаление последнего элемента происходит примерно так же. Устанавливаем ссылку на элемент, который предшествует
последнему (node = tail.prev). Далее убираем ссылку на tail у нашего node (node.next = None). И в конце переносим
указатель tail на наш node (tail = node). Сложность операции O(1). Реализуется командой pop_back().

Итоги теории:
|=========================================================|
| Название                         | Команда      | Big O |
|=========================================================|
| Добавление в конец               | push_back()  | O(1)  |
|---------------------------------------------------------|
| Добавление в начало              | push_front() | O(1)  |
|---------------------------------------------------------|
| Удаление с конца                 | pop_back()   | O(1)  |
|---------------------------------------------------------|
| Удаление с начала                | pop_front()  | O(1)  |
|---------------------------------------------------------|
| Вставка элемента                 | insert()     | O(n)  |
|---------------------------------------------------------|
| Удаление промежуточных элементов | erase()      | O(n)  |
|---------------------------------------------------------|
| Доступ к элементу                | at()         | O(n)  |
|=========================================================|
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def push_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_back(self):
        if not self.tail:
            raise Exception("List is empty")
        data = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def pop_front(self):
        if not self.head:
            raise Exception("List is empty")
        data = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def insert(self, prev_node_data, data):
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

    def erase(self, data):
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

    def at(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Создаем объект двусвязного списка
dll = DoublyLinkedList()

# Добавление элементов в конец
dll.push_back(10)
dll.push_back(20)
dll.push_back(30)

# Добавление элементов в начало
dll.push_front(5)
dll.push_front(2)

# Удаление элемента с конца
print("Pop back:", dll.pop_back())  # Output: Pop back: 30

# Удаление элемента с начала
print("Pop front:", dll.pop_front())  # Output: Pop front: 2

# Вставка элемента после указанного
dll.insert(10, 15)

# Удаление элемента по значению
dll.erase(20)

# Проверка наличия элемента
print("Contains 20:", dll.at(20))  # Output: Contains 20: False

# Вывод списка
dll.print_list()  # Output: 5 10 15
