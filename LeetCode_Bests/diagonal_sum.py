"""
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25

mat = [[1,1,1,1],
       [1,1,1,1],
       [1,1,1,1],
       [1,1,1,1]]
Output: 8

mat = [[5]]
Output: 5
"""


def diagonalSum(mat: list[list[int]]) -> int:
    size = len(mat)

    if size == 1:
        for subarray in mat:
            for item in subarray:
                return item

    summ_main = sum(mat[i][i] for i in range(size))
    summ_secondary = sum(mat[i][size - i - 1] for i in range(size))

    if size % 2 != 0:
        rows = size
        columns = len(mat[0])
        middle_row = rows // 2
        middle_column = columns // 2
        middle_element = mat[middle_row][middle_column]

        return summ_main + summ_secondary - middle_element

    return summ_main + summ_secondary


print(diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(diagonalSum([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
print(diagonalSum([[5]]))

"""
Сумма главной и побочной диагоналей высчитывается итератором. Далее, если длина массива (а значит и подмассива) нечётна,
то находим середину массива, чтобы вычесть пересечение. Если длина чётна, то мы просто возвращаем сумму.
"""
