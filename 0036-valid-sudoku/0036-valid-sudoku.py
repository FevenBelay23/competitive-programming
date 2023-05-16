class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            diff_row = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in diff_row:
                        return False
                    diff_row.add(board[i][j])
        for j in range(9):
            diff_col = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in diff_col:
                        return False
                    diff_col.add(board[i][j])
        for box in range(9):
            diff_grid = set()
            new_row = 3 * (box // 3)
            new_col = 3 * (box % 3)
            for i in range(new_row, new_row + 3):
                for j in range(new_col, new_col + 3):
                    if board[i][j] != ".":
                        if board[i][j] in diff_grid:
                            return False
                        diff_grid.add(board[i][j])
        return True

        