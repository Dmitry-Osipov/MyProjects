"""
Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on
grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw".
If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and
A will play first.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.


Constraints:
1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
"""


def tictactoe(moves: list[list[int]]) -> str:
    grid = [[''] * 3 for _ in range(3)]  # Создаем пустое игровое поле (сетку) grid размером 3x3 с помощью двумерного
    # списка, где каждая ячейка инициализирована пустой строкой.

    for i, move in enumerate(moves):  # Проходим по каждому ходу в списке moves с помощью цикла for, используя enumerate
        # для получения индекса i и самого хода move.
        r, c = move  # Распаковываем координаты хода в переменные r (строка) и c (столбец).
        player = 'A' if i % 2 == 0 else 'B'  # Определяем, чей ход: если индекс i четный, то ходит игрок 'A',
        # иначе ходит игрок 'B'.
        grid[r][c] = player  # Обновляем значение ячейки в сетке grid с координатами (r, c) на символ
        # текущего игрока ('A' или 'B').

    for row in grid:
        # Затем проходим по каждой строке в сетке и проверяем, есть ли выигрышная комбинация для игрока
        # 'A' (три 'A' в строке) или 'B' (три 'B' в строке).
        if row.count('A') == 3:
            return 'A'
        if row.count('B') == 3:
            return 'B'

    for col in range(3):
        # Затем проходим по каждому столбцу в сетке и проверяем, есть ли выигрышная комбинация для игрока 'A' или 'B'
        # (три символа подряд в столбце).
        if grid[0][col] == grid[1][col] == grid[2][col] == 'A':
            return 'A'
        if grid[0][col] == grid[1][col] == grid[2][col] == 'B':
            return 'B'

    # Проверяем, есть ли выигрышная комбинация для игрока 'A' (по главной и побочной диагонали) или 'B':
    if grid[0][0] == grid[1][1] == grid[2][2] == 'A' or grid[0][2] == grid[1][1] == grid[2][0] == 'A':
        return 'A'

    if grid[0][0] == grid[1][1] == grid[2][2] == 'B' or grid[0][2] == grid[1][1] == grid[2][0] == 'B':
        return 'B'

    return 'Pending' if len(moves) < 9 else 'Draw'


print(tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
