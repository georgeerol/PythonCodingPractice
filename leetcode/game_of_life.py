"""
The board is made up of an m x n grid of cells, where
each cell has an initial state: live (represented by a
1) or dead (represented by a 0). Each cell interacts
with its eight neighbours (horizontal, vertical,
diagonal) using the following four rules:

1. If a cell is ON and has fewer than two neighbours
that are ON, it turns OFF.

2. If a cell is ON and has either two or three
neighbours that are ON, it remains ON.

3. If a cell is ON and has more than three neighbours
that are ON, it turns OFF.

4. If a cell is OFF and has exactly three neighbours
that are ON, it turns ON.
The next state is created by applying the above rules
simultaneously to every cell in the current state,
where births and deaths occur simultaneously. Given
the current state of the m x n grid board, return the
next state.
"""

import copy
from typing import List

input_board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0],
]

output_board = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
]


class GameOfLife:
    def __init__(self, board: List[List[int]]):
        self.board = copy.deepcopy(board)
        self.rows = len(self.board)
        self.columns = len(self.board[0])

    def update_board(self):
        """
        Key Rules:
            1- live if 2 or 3 neighbors else die
            0 - live if 3 neighbors else die

            Example:
                  Input        Temp     Output
                [0, 1, 0]    [0,0,0]   [0,0,0]
                [0, 0, 1] -> [2,0,3]-> [1,0,1]
                [1, 1, 1]    [1,3,3]   [0,1,1]
                [0, 0, 0]    [0,2,0]   [0,1,0]

        :return:
        """

        # Temp Matrix
        for row in range(self.rows):
            for col in range(self.columns):
                c_nei = self.count_neighbors(row, col)
                if self.board[row][col] >= 1 and c_nei in [2, 3]:
                    self.board[row][col] = 3
                elif c_nei == 3:
                    self.board[row][col] = 2

        # Output Matrix
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] == 1:
                    self.board[row][col] = 0
                elif self.board[row][col] in [2, 3]:
                    self.board[row][col] = 1

    def count_neighbors(self, row, col):
        c_nei = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i == row and j == col) or i < 0 or j < 0 or i == self.rows or j == self.columns:
                    continue
                if self.board[i][j] in [1, 3]:
                    c_nei += 1
        return c_nei


game = GameOfLife(input_board)
game.update_board()

print(f"output board:    {output_board}")
print(f"generated board: {game.board}")

try:
    assert len(output_board) == len(game.board)
    for row in range(len(output_board)):
        assert output_board[row] == game.board[row]
except AssertionError:
    print("ERROR: The boards DO NOT MATCH!")
