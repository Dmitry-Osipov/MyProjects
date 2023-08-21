"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""


def checkStraightLine(coordinates: list[list[int]]) -> bool:
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
            return False

    return True


coord1 = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
coord2 = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
print(checkStraightLine(coord1))
print(checkStraightLine(coord2))

"""
Извлекаем из входных данных координаты первых двух точек (x0, y0) и (x1, y1).
Итерируем остальные точки, начиная с третьей.
Для каждой точки (x, y) в итерации:
Вычислить наклон между точками (x0, y0) и (x1, y1) как (x1 - x0) / (y1 - y0).
Вычислить наклон между (x0, y0) и текущей точкой (x, y) как (x - x0) / (y - y0).
Если два наклона не равны, то возвращается значение False, указывающее на то, что точки не образуют прямую линию.
Если все наклоны равны, то возвращается True, что свидетельствует о том, что точки образуют прямую линию.
Проверяя равенство наклонов, можно определить, лежат ли все точки на прямой или нет.
"""
