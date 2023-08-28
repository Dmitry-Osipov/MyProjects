"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def isValid(s: str) -> bool:
    stack = []  # Мы используем стек для отслеживания открывающих скобок.
    brackets = {')': '(', '}': '{', ']': '['}  # Создаем словарь brackets, где ключи - это закрывающие скобки,
                                               # а значения - соответствующие открывающие скобки.

    for char in s:
        # Если символ - это открывающая скобка, мы добавляем ее в стек:
        if char in brackets.values():
            stack.append(char)

        # Если символ - это закрывающая скобка, то мы проверяем, соответствует ли верхний элемент стека открывающей
        # скобке того же типа. Если нет, то строка не валидна:
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack  # Возвращаем True, если стек пуст, иначе False.


print(isValid('()[]{}'))
print(isValid('){'))
print(isValid('{[]}'))
print(isValid('(){}}{'))
