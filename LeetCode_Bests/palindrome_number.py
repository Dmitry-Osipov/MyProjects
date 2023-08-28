"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    x_str = str(x)
    length = len(x_str)
    for i in range(length // 2):
        if x_str[i] != x_str[length - i - 1]:
            return False

    return True


print(isPalindrome(1001))

"""
Преобразовали цифру в строку для упрощения проверки палиндрома. Определяем длину в отдельную переменную, ибо будет 
использовать длину строки несколько раз. На 28 строчке проверяем: если элемент строки не равен элементу строки с другой
стороны(строка[длина - текущая итерация цикла - 1] - вычисляем длину - 1, чтобы выйти на конец списка, далее вычитаем из 
этого значения значение текущей итерации цикла). 
"""
