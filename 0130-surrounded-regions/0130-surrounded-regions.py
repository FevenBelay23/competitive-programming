class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if (i in [0, m-1] or j in [0, n-1]) and board[i][j] == 'O':
                    queue.append((i, j))
        while queue:
            i, j = queue.pop(0)
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'N'
                queue += [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for i in range(m):
            for j in range(n):
                board[i][j] = 'XO'[board[i][j] == 'N']
        