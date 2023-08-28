"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

 Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:  # Если список пуст, то общего префикса нет
        return ""

    # Находим самую короткую строку в массиве
    shortest_str = min(strs, key=len)

    for i, char in enumerate(shortest_str):
        for string in strs:
            if string[i] != char:
                return shortest_str[:i]

    return shortest_str  # Если не найдено несовпадений, сама короткая строка является общим префиксом


print(longestCommonPrefix(["ab", "a"]))

"""
Эта функция longestCommonPrefix сначала проверяет, пуст ли входной список strs. Если он пуст, то общего префикса нет и 
возвращается пустая строка.

Затем она находит самую короткую строку в массиве, используя функцию min и параметр key с функцией len.

После этого она перебирает символы самой короткой строки с помощью enumerate. Для каждого символа она сравнивает его с 
соответствующим символом в каждой строке массива. Если обнаружено несовпадение, она возвращает общий префикс до 
этой позиции. 

Если не найдено ни одного несовпадения, то сама короткая строка является общим префиксом и возвращается в результате.
Например, если использовать этот код с входным списком strs = ["flower","flow","flight"], результат будет "fl". 
Если использовать его с strs = ["dog","racecar","car"], результат будет "", что означает отсутствие общего префикса.
"""
