class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def Mine(x, y):
            count = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    k, l = x + i, y + j
                    if 0 <= k < len(board) and 0 <= l < len(board[0]) and board[k][l] == 'M':
                        count += 1
            return count
        def Reveal(x, y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != 'E':
                return
            mines = Mine(x, y)
            if mines == 0:
                board[x][y] = 'B'
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        Reveal(x + i, y + j)
            else:
                board[x][y] = str(mines)
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            Reveal(x, y)

        return board
