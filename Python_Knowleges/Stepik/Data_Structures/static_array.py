"""
Рассмотрим одну из наиболее простых и распространённых структур данных: статический массив.
Представим, что нам в программе требуется сохранить значение функции косинус в диапазоне от 0 до 2Pi с шагом 0.1.
Как это сделать? Как раз для этого хорошо подходит статический массив так, чтобы каждый элемент этого статического
массива хранил соответствующее значение функции. Или другой пример: нам нужно хранить состояние игрового поля размером
3 * 3. Удобно воспользоваться статическим массивом, длиной 9 элементов. Тогда каждые 3 элемента соответствуют строке
игрового поля. Или следующая задача: в программе надо сохранять фамилию студентов.
Это всё примеры рационального использования статического массива.

Рассмотрим же его подробнее.
Первый важный момент: все элементы статического массива должны быть одного типа данных. Не предполагается в одном
массиве иметь разные типы данных.
Второй важный момент: длина статического массива (т.е. кол-во его элементов) задаётся фиксированным значением и не
меняется. Т.е. если задать массив на 50 элементов, то на протяжении работы всей программы, этот статический массив будет
иметь именно такую размерность. Поэтому данные массивы и называются статическими - они не изменяют количества элементов,
но значения элементов мы менять можем.
Третий важный момент: все элементы статического массива располагаются в памяти компьютера последовательно друг за другом
без каких-либо пропусков, начиная с некоторого стартового адреса (т.е. с некоторой стартовой ячейки). Предположим, что
массив заполнен целыми числами, каждое число занимает 4 байта. Тогда размер массива будет 4 байта * кол-во элементов.
А в общем случае можно сказать так: если один элемент n в массиве занимает k-байт, то весь массив будет занимать:
size = n элементов * k байт.

Посмотрим, как можно обращаться к отдельным элементам этого массива.
Мы всегда знаем, с какого адреса хранятся данные в этом массиве. Эту информацию даёт нам имя массива. Имя массива по
сути дела хранит адрес, начиная с которого хранятся все значения в этом массиве. Т.е. ссылка на массив (переменная ar,
например) хранит адрес начала массива (например, 1000 - тогда адрес первой ячейки равен 1000). Далее зная начальный
адрес и размер, который занимает один элемент в этом массиве, мы легко можем обратиться к первому элементу, т.е. взять
все 4 байта, начиная с адреса равному 1000. Математически это можно записать так:
1-ый элемент = ar (имя массива, 1000) + 0 * k (размер, который занимает 1 элемент в памяти компьютера). Т.е. данное
математическое выражение нам говорит: начиная с какого адреса мы должны взять первый элемент этого массива. Очевидно,
что ar + 0 * k - это просто ar, и в данном случае ar составляет 1000, и мы будем ссылаться на эти первые 4 байта, т.е.
мы знаем, что первые 4 байта - это первый элемент массива, ибо k в нашем примере равен 4.
Далее, чтобы получить доступ ко второму элементу, нам нужно сместиться (сместить указатель ячейки) на 4 байта и взять
следующие 4 байта, которые соответствуют второму элементу. Математически это выглядит так:
2-ой элемент = ar (имя массива, 1000) + 1 * k (размер, который занимает 1 элемент в памяти). Подставляем:
2-ой элемент = 1000 + 1 * 4 = 1004 - получили адрес ячейки, начиная с которой хранится второй элемент массива. И т.д.
Для любого i-того элемента получаем: ar + (i-1) * k - важно заметить, что в формуле мы используем i-1, ибо нумерация
начинается с нуля. И вот эти i-тые элементы получили название индексы элемента массива. Последний элемент будет иметь
значение n-1. Для j-того элемента имеем следующую запись: p_j = ar + j-1 * k.
В языках программирования это записывается следующим образом:
- при считывании значения: value = ar[j];
- при записи значения: ar[j] = value.
Очевидно, что для таких записей мы пользуемся операцией с константным временем. В терминах О большого - это О(1). И это
главное преимущество такой структуры. Она обеспечивает мгновенный доступ к любому элементу.
Но не всё так радужно. Помимо чтения и записи данных коллекция должна обеспечивать операции вставки и удаления.
Начнём с операции вставки. Допустим, мы определили массив длиной 10 элементов, мы записали в нём первые 6 значений.
Далее мы хотим записать в седьмую ячейку элемент со значением 7. Как это сделать: ar[6] = 7. Но если нам нужно вставить
элемент не в конец, а в начало, то операция такой вставки будет работать несколько по-другому: вначале мы должны
сдвинуть все элементы вправо на один элемент, и только после сдвига в первую ячейку мы должны записать нужное нам
значение. Какова вычислительная сложность такого алгоритма с точки зрения О большого? Если в общем случае принять длину
массива n элементов, то сложность составит O(n), т.е. в общем случае для того, чтобы вставить тот или иной элемент в
статический массив требуется О(n) операций.
Аналогично выполняется удаление. Вводится счётчик k, который работает вне зависимости от самого массива. Тогда при
удалении мы его уменьшаем на 1 (и он показывает значение size = 6), а при дополнении увеличиваем на 1
(и он показывает size = 7). А если нам требуется удалить первый элемент массива, то мы получим сдвиг всего массива, что
аналогично добавлению, характеризует сложность данной операции как O(n).
Вычислительная сложность:
запись - О(1);
чтение - О(1);
вставка - O(n);
удаление - O(n).

В итоге, если массив будет большим по размеру, а операции вставки и удаления происходят достаточно часто, то от
статического массива стоит отказаться.
Преимущества статического массива:
- скорость доступа к произвольному элементу O(1) для записи или чтения значения;
- просто реализуется и удобен для небольших наборов данных.
Недостатки статического массива:
- хранение данных выполняется в непрерывной области памяти. Не всегда эффективно для очень больших объёмов данных;
- статический массив не может менять число своих элементов в процессе работы программы. Если зарезервированного места
окажется недостаточно, то данные могут потеряться;
- вставка и удаление элементов вызывается за время O(n). Может быть критично при больших значениях n.
"""