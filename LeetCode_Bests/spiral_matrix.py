"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


def spiral_order(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    columns = len(matrix[0])
    total_elements = rows * columns
    result = []

    # Переменные ниже будут служить границами для прохода по матрице в различных направлениях
    top = 0
    bottom = rows - 1
    left = 0
    right = columns - 1

    while len(result) < total_elements:  # Входим в цикл, который будет выполняться, пока не добавлены все элементы
        # Перемещение по верхнему ряду:
        # в цикле проходим по верхней строке (верхняя граница фиксирована, а столбцы меняются от left до right)
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Перемещение по правой колонке:
        # в цикле проходим по правому столбцу (правая граница фиксирована, а строки меняются от top до bottom).
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Перемещение по нижнему ряду:
        # в цикле проходим по нижней строке (нижняя граница фиксирована, а столбцы меняются в обратном порядке
        # от right до left).
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Перемещение по левой колонке:
        #  в цикле проходим по левому столбцу (левая граница фиксирована, а строки меняются в обратном порядке
        #  от bottom до top).
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


input_matrix = [
    [1, 11],
    [2, 0],
    [3, 13],
    [0, 14],
    [5, 0],
    [6, 16],
    [0, 0],
    [8, 18],
    [9, 19],
    [10, 20]
]
output = spiral_order(input_matrix)
print(output)
