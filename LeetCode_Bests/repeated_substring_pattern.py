"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the
substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
"""


def repeatedSubstringPattern(s: str) -> bool:
    ss = (s + s)[1:-1]
    return ss.find(s) != -1


my_string = "ababba"

print(repeatedSubstringPattern(my_string))
"""
Первый символ входной строки - первый символ повторяющейся подстроки.
Последний символ входной строки - последний символ повторяющейся подстроки.
Пусть S1 = S + S (где S - входная строка).
Удалим 1 и последний символы из S1. Пусть это будет S2.
Если S существует в S2, то возвращается true, иначе false.
Пусть i - индекс в S2, с которого начинается S, тогда длина повторяющейся подстроки i + 1 и 
повторяющаяся подстрока S[0: i+1]
"""