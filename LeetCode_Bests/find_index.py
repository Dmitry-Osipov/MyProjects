"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


def strStr(haystack: str, needle: str) -> int:
    # возвращаем -1, если haystack меньше needle
    if len(haystack) < len(needle):
        return -1

    # возвращаем 0, если длины haystack и needle равны 1, а также если первые элементы равны
    if len(haystack) == len(needle) == 1 and haystack[0] == needle[0]:
        return 0

    for i in range(len(haystack)):
        start = i
        j = 0

        while haystack[i] == needle[j]:

            # возвращаем start индекс, если конец needle совпал, так как конец тоже совпал
            if j == len(needle) - 1:
                return start

            i += 1
            j += 1

            # возвращаем -1, если достигнули конца haystack и подстрока не совпала
            if i == len(haystack):
                return -1

    return -1


parent = "sadbutsad"
child = "sad"

print(strStr(parent, child))

"""
Итерация по каждому элементу haystack (i-индекс), сохранение совпадающих элементов (j-индекс) needle, если все элементы 
needle совпадают, то возвращается начальный индекс. Если конец haystack до совпадения, то возвращается -1.
"""