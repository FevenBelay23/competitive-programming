class Solution:
    def get_position(self, num, n):
        row = (num - 1) // n
        col = (num - 1) % n
        if row % 2 == 1:
            col = n - 1 - col
        row = n - 1 - row
        return row, col
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        sq = n * n
        visited = set()
        queue = deque([(1, 0)])
        while queue:
            current, move = queue.popleft()
            if current == sq:
                return move
            for i in range(1, 7):
                Next = current + i
                if Next > sq:
                    break
                row, col = self.get_position(Next, n)
                if board[row][col] != -1:
                    Next = board[row][col]
                if Next not in visited:
                    visited.add(Next)
                    queue.append((Next, move + 1))
                    
        return -1
    