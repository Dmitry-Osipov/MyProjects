import math

"""
Task
The sequence of Chando is an infinite sequence of all Chando's numbers in ascending order.

A number is called Chando's if it is an integer that can be represented as a sum of different positive integer powers of 5.

The first Chando's numbers is 5 (5^1). And the following nth Chando's numbers are:

25  (5^2)
30  (5^1 + 5^2)
125 (5^3)
130 (5^1 + 5^3)
150 (5^2 + 5^3)
...
...
Your task is to find the Chando's nth number for a given n.

Input/Output
[input] integer n
1 <= n <= 7000

[output] an integer
nth Chando's number
"""


def nth_chandos_number(n):
    if n == 0:
        return 0

    if n <= 2:
        return 5 ** n

    m = int(math.log2(n))
    return 5 ** (m + 1) + nth_chandos_number(n - 2 ** m)


print(nth_chandos_number(5))
"""
В начале функции nth_chandos_number(n) проводится проверка случая, когда n равно 0. В этом случае функция возвращает 0, 
так как первое число Чандо равно 5^1 = 5.

Затем идет проверка для n, которые меньше или равны 2. Если n равно 1, функция возвращает 5 (5^1), если n равно 2, 
функция возвращает 25 (5^2).

Далее мы определяем переменную m, которая равна наибольшей степени двойки, которая меньше или равна n. Это делается с 
использованием функции math.log2(n) для вычисления двоичного логарифма n. Например, если n равно 9, то m будет равно 3, 
так как 2^3 = 8 <= 9, но 2^4 = 16 > 9.

Теперь мы используем рекурсию для нахождения n-го числа Чандо. Мы берем следующую степень 5, то есть 5^(m + 1), и 
прибавляем к ней результат вызова функции nth_chandos_number(n - 2^m). Таким образом, мы находим n-е число Чандо, 
используя результаты для меньших значений n.

Например, если мы хотим найти 5-е число Чандо (n = 5), то m будет равно 3, и функция 
вернет 5^(3+1) + nth_chandos_number(5 - 2^3), что равно 5^4 + nth_chandos_number(1). Затем, для nth_chandos_number(1), 
функция вернет 5 (5^1). Таким образом, 5-е число Чандо равно 625 + 5 = 630.
"""
