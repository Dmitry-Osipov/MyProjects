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
        new_node = Node(data)  # Создаём новый узел с данными data.
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail  # Устанавливается ссылка prev нового узла на текущий конец списка (tail).
            self.tail.next = new_node  # Устанавливается ссылка next текущего конца списка на новый узел, чтобы связать
                                       # его с новым узлом.
            self.tail = new_node  # Теперь новый узел становится новым концом списка.

    def insert_after(self, prev_node_data, data):
        """
        Метод insert_after вставляет новый узел с данными data после узла с данными prev_node_data. Метод перебирает
        список, находит узел с prev_node_data и вставляет новый узел после него.
        """
        new_node = Node(data)
        current = self.head  # Создаётся переменная current, указывающая на начало списка (head), чтобы начать поиск.
        while current:  # Запускается цикл, который перебирает узлы в списке до его конца.
            if current.data == prev_node_data:  # Если данные текущего узла совпадают с данными prev_node_data (указали
                # в аргументах при вызове функции), то выполняется вставка нового узла после текущего узла.
                new_node.next = current.next  # Устанавливается ссылка next нового узла на узел, который идёт после
                # текущего узла.
                new_node.prev = current  # Устанавливается ссылка prev нового узла на текущий узел.
                if current.next:  # Проверяется, есть ли у текущего узла следующий узел.
                    current.next.prev = new_node  # Если есть следующий узел, то его ссылка prev устанавливается на
                    # новый узел, чтобы обеспечить двунаправленную связь.
                current.next = new_node  # Ссылка next текущего узла устанавливается на новый узел, чтобы завершить
                                         # вставку.
                if current == self.tail:  # Проверяется, является ли текущий узел концом списка.
                    self.tail = new_node  # Если текущий узел является концом списка, то обновляется tail, чтобы указать
                    # на новый узел, который станет концом списка.
                return  # Метод завершает выполнение после успешной вставки.
            current = current.next  # Если данные текущего узла не совпадают с prev_node_data, то метод переходит к
                                    # следующему узлу.
        raise ValueError(f"Node with data {prev_node_data} not found")  # Если цикл завершается, и не найден узел с
        # данными prev_node_data, то метод вызывает исключение с сообщением.

    def delete(self, data):
        """
        Метод delete удаляет узел с данными data из связанного списка. Если узел находится в начале списка, self.head
        обновляется. В противном случае, метод перебирает список, находит узел с data и удаляет его, обновляя связи
        между узлами.
        """
        current = self.head  # Создаётся переменная current, указывающая на начало списка (head), чтобы начать поиск
                             # удаляемого узла.
        while current:  # Запускается цикл, который перебирает узлы в списке до его конца.
            if current.data == data:  # Если данные текущего узла совпадают с данными data, то выполняется его удаление.
                if current.prev:  # Проверяется, есть ли предыдущий узел у текущего узла. Если есть, это означает, что
                                  # текущий узел не является началом списка.
                    current.prev.next = current.next  # Ссылка next предыдущего узла устанавливается на следующий узел
                                  # текущего узла, пропуская текущий узел и тем самым удаляя его из списка.
                else:  # Если текущий узел является началом списка (т.е. у него нет предыдущего узла),
                    self.head = current.next  # то обновляется head, чтобы указать на следующий узел.
                if current.next:  # Проверяется, есть ли следующий узел у текущего узла. Если есть, это означает, что
                    # текущий узел не является концом списка.
                    current.next.prev = current.prev  # Ссылка prev следующего узла устанавливается на предыдущий узел
                    # текущего узла, чтобы обеспечить двунаправленную связью
                else:  # Если текущий узел является концом списка (т.е. нет следующего узла), то обновляется tail,
                    self.tail = current.prev  # чтобы указать на предыдущий узел и сделать его концом списка.
                return  # Метод завершает выполнение после успешного выполнения.
            current = current.next  # Если данные текущего узла не совпадают с data, метод переходит к следующему узлу.
        raise ValueError(f"Node with data {data} not found")  # Если цикл завершается, и не найден узел с данными data,
        # то метод вызывает исключение, сообщая, что узел с такими данными не был найден в списке.

    def search(self, data):
        """
         Метод search выполняет поиск узла с данными data в связанном списке. Он перебирает список и возвращает True,
         если узел найден, и False, если нет.
        """
        current = self.head  # Создаём переменную current и устанавливаем её на начало списка head.
        while current:  # Запускаем цикл, который будет выполняться пока не достигнем конца списка.
            if current.data == data:  # Проверяем, совпадают ли данные текущего узла (current.data) с искомыми данными.
                return True  # Если совпадение найдено, то возвращаем True.
            current = current.next  # Если совпадение не найдено, то переходим к следующему узлу, обновляя current.
        return False  # Если совпадение так и не было найдено, возвращаем False.

    def reverse(self):
        """
        Метод reverse разворачивает связанный список, меняя порядок узлов на обратный. Он использует три указателя:
        prev, current, и next_node, чтобы изменить связи между узлами и обратить список.
        """
        current = self.head  # Создаём переменную current и устанавливаем её на начало списка (head).
        while current:  # Запускаем цикл, который будет выполняться, пока не достигнем конца списка.
            current.prev, current.next = current.next, current.prev  # Меняем местами ссылки prev и next у текущего узла
            current = current.prev  # Переходим к следующему узлу, чтобы продолжить разворот.
        self.head, self.tail = self.tail, self.head  # После завершения цикла обновляем указатели head и tail,
        # чтобы head на новое начало списка (старый конец), а tail - на новый конец (старое начало).

    def enqueue(self, data):
        """
        Метод enqueue добавляет элемент в конец очереди, используя ссылки self.prev и self.next для обновления связей
        между узлами.
        """
        new_node = Node(data)  # Создаём новый узел с данными data.
        if self.is_empty():  # Проверяем, пуст ли список.
            self.head = self.tail = new_node  # Если очередь пуста, то новый узел становится началом и концом списка.
        else:  # Если список не пустой:
            new_node.prev = self.tail  # Устанавливаем ссылку prev нового узла на текущий конец очереди (tail).
            self.tail.next = new_node  # Устанавливаем ссылку next текущего конца очереди на новый узел, чтобы связать
                                       # его с новым узлом.
            self.tail = new_node  # Теперь новый узел становится новым концом очереди.

    def dequeue(self):
        """
        Метод dequeue удаляет элемент из начала очереди, обновляя ссылки self.head и self.tail.
        """
        if self.is_empty():  # Проверяем, пуста ли очередь.
            raise Exception("Очередь пуста")  # Если очередь пуста, то вызываем исключение.
        data = self.head.data  # Получаем данные из узла, который находится в начале очереди.
        if self.head == self.tail:  # Проверяем, является ли текущий узел началом и концом очереди.
            self.head = self.tail = None  # Если да, то очередь становится пустой, обновляем ссылки.
        else:
            self.head = self.head.next  # Если очередь не пуста, перемещаем указатель начала на следующий узел.
            self.head.prev = None  # Устанавливаем ссылку prev нового начала на None, чтобы разорвать связь с
                                   # прошлым узлом.
        return data  # Возвращаем данные удалённого элемента.

    def push(self, data):
        """
        Метод push добавляет элемент в вершину стека, изменяя self.head и self.tail в зависимости от состояния стека.
        """
        new_node = Node(data)  # Создаём новый узел с данными data.
        new_node.next = self.head  # Устанавливаем ссылку next нового узла на текущий верхний элемент стека (head).
        if self.head:  # Проверяем, не является ли стэк пустым.
            self.head.prev = new_node  # Если стек не пуст, устанавливаем ссылку prev текущего верхнего элемента стэка
            # на новый узел, чтобы обеспечить двунаправленную связь.
        self.head = new_node  # Новый узел становится новым верхним элементом стэка.
        if self.tail is None:  # Если tail не указывает ни на какой элемент (стэк был пуст),
            self.tail = new_node  # то обновляем tail на новый узел.

    def pop(self):
        """
        Метод pop удаляет элемент из вершины стека, обновляя self.head и self.tail.
        """
        if self.is_empty():  # Проверяем, пуст ли стэк.
            raise Exception("Стек пуст")  # Если стэк пуст, вызываем исключение.
        data = self.head.data  # Получаем данные из верхнего элемента стэка.
        self.head = self.head.next  # Устанавливаем ссылку head на следующий элемент стека, удаляя этим верхний элемент.
        if self.head:  # Проверяем, не стал ли стэк пустым после удаления.
            self.head.prev = None  # Если стек не пуст, устанавливаем ссылку prev нового верхнего элемента на None,
            # чтобы разорвать связь с предыдущим верхним элементом.
        return data  # Возвращаем данные удалённого элемента.

    def print_list(self):
        """
        Метод print_list выводит элементы связанного списка, начиная с self.head,
        чтобы можно было увидеть содержимое списка.
        """
        current = self.head  # Создаём переменную current и устанавливаем её на начало списка (head).
        while current:  # Запускаем цикл, пока не достигнем конца списка.
            print(current.data, end=" ")  # Выводим значение текущего узла, добавляя пробел для разделения элементов.
            current = current.next  # Переходим к следующему узлу, обновляя переменную current.
        print()  # По завершении цикла выводим пустую строку, чтобы следующие выводи в консоли не слипались.


# Создание двунаправленного связанного списка
my_list = LinkedList()

# Добавление элементов в конец списка
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_list()  # 1 2 3
# Вставка элемента после определенного узла
my_list.insert_after(2, 4)
my_list.print_list()  # 1 2 4 3

# Удаление элемента из середины списка
my_list.delete(4)
my_list.print_list()  # 1 2 3

# Поиск элемента
print(my_list.search(2))  # True
print(my_list.search(5))  # False

# Разворот списка
my_list.reverse()
my_list.print_list()  # 3 2 1

# ----------------------------------------------------------------------------------------------------------------------

# Работа с очередью:
# Создание пустой очереди
my_queue = LinkedList()

# Добавление элементов в очередь
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.print_list()  # 10 20 30
"""Напоминание: очередь работает по принципу FIFO - First In - First out."""
# Удаление элемента из начала очереди
first_in_queue = my_queue.dequeue()  # first_in_queue = 10
my_queue.print_list()  # 20 30

# ----------------------------------------------------------------------------------------------------------------------

# Работа со стэком:
# Создание пустого стека
my_stack = LinkedList()

# Добавление элементов в стек
my_stack.push(500)
my_stack.push(1000)
my_stack.push(1500)
my_stack.print_list()  # 1500 1000 500
"""Напоминание: стэк работает по принципу LIFO - Last In - First out."""
# Удаление элемента из вершины стека
last_in_stack = my_stack.pop()  # last_in_stack = 1500
my_stack.print_list()  # 1000 500

# ----------------------------------------------------------------------------------------------------------------------
# Задача с семинара 1: реализовать односвязный список с методами: удаления из начала и конца, добавление в начало и
# конец, нахождением элемента (если элемент есть, возвращаем True, иначе False).


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is not None

    def append_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        if self.is_empty():
            self.head = self.head.next

    def find_value(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False

    def append_last(self, value):
        current_node = self.head
        new_node = Node(value)
        while current_node:
            if current_node.next is None:
                current_node.next = new_node
                break
            current_node = current_node.next

    def delete_last(self):
        current_node = self.head
        if self.is_empty():
            while current_node.next:
                if current_node.next.next is None:
                    current_node.next = None
                    return
                current_node = current_node.next
            self.head = None

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value, end=' ')
            temp_node = temp_node.next
        print()


linked_list = LinkedList()
print()
print('Методы односвязного списка:')
linked_list.append_first(1)
linked_list.append_first(2)
linked_list.append_first(3)
linked_list.append_first(4)
linked_list.append_first(5)
linked_list.append_first(6)
linked_list.append_first(7)
linked_list.print_list()
linked_list.delete_first()
linked_list.delete_first()
linked_list.print_list()
print(linked_list.find_value(3))
print(linked_list.find_value(10))
linked_list.append_last(11)
linked_list.print_list()
linked_list.delete_last()
linked_list.print_list()

# Задача с семинара 2: преобразовать односвязный список в двусвязный, реализовать метод сортировки пузырьком в списке.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is not None

    def append_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.is_empty():
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def delete_first(self):
        if self.is_empty() and self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None

    def find_value(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False

    def append_last(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.is_empty():
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def delete_last(self):
        if self.is_empty() and self.head.next is not None:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None

    def bubble_sort(self):
        need_sort = True
        while need_sort:
            need_sort = False
            current_node = self.head
            while current_node.next is not None and current_node is not None:
                if current_node.value > current_node.next.value:
                    current_node.value, current_node.next.value = current_node.next.value, current_node.value
                    need_sort = True
                current_node = current_node.next

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value, end=' ')
            temp_node = temp_node.next
        print()


linked_list = LinkedList()
print()
print('Методы двусвязного списка:')
linked_list.append_first(1)
linked_list.append_first(2)
linked_list.append_first(3)
linked_list.append_first(4)
linked_list.append_first(5)
linked_list.append_last(90)
linked_list.append_last(53)
linked_list.print_list()
linked_list.bubble_sort()
linked_list.print_list()
linked_list.delete_first()
linked_list.delete_last()
linked_list.print_list()

# Домашнее задание: добавить в двусвязный список функцию по его развороту.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is not None

    def append_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.is_empty():
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def delete_first(self):
        if self.is_empty() and self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None

    def find_value(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next

        return False

    def append_last(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.is_empty():
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def delete_last(self):
        if self.is_empty() and self.head.next is not None:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None

    def bubble_sort(self):
        need_sort = True
        while need_sort:
            need_sort = False
            current_node = self.head
            while current_node.next is not None and current_node is not None:
                if current_node.value > current_node.next.value:
                    current_node.value, current_node.next.value = current_node.next.value, current_node.value
                    need_sort = True
                current_node = current_node.next

    def reverse_list(self):
        current_node = self.head
        while current_node:
            current_node.prev, current_node.next = current_node.next, current_node.prev
            current_node = current_node.prev
        self.head, self.tail = self.tail, self.head

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value, end=' ')
            temp_node = temp_node.next
        print()


linked_list = LinkedList()
print()
print('Разворот списка:')
linked_list.append_first(8)
linked_list.append_first(2)
linked_list.append_first(3)
linked_list.append_first(4)
linked_list.append_first(0)
linked_list.append_first(1)
linked_list.print_list()
linked_list.reverse_list()
linked_list.print_list()
