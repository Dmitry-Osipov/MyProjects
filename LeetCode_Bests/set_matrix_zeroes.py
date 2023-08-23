"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


def setZeroes(matrix: list[list[int]]) -> None:
    rows = len(matrix)
    columns = len(matrix[0])

    # Создаем множества для отметки индексов строк и столбцов, в которых нужно установить нули.
    zero_rows = set()
    zero_columns = set()

    # Проходим по матрице, находя элементы, которые равны нулю.
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 0:
                zero_rows.add(row)
                zero_columns.add(column)

    # Устанавливаем нули в соответствующих строках.
    for row in zero_rows:
        for column in range(columns):
            matrix[row][column] = 0

    # Устанавливаем нули в соответствующих столбцах.
    for column in zero_columns:
        for row in range(rows):
            matrix[row][column] = 0

    print(matrix)


first_matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
second_matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(first_matrix)
setZeroes(second_matrix)
