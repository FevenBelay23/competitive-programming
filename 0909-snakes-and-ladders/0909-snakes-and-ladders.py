class Solution:
    def get_position(self, num, n):
        row = (num - 1) // n
        column = (num - 1) % n
        if row % 2 == 1:
            column = n - 1 - column
        row = n - 1 - row
        return row, column
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        double = n * n
        visited = set()
        queue = deque([(1, 0)])
        while queue:
            current, move = queue.popleft()
            if current == double:
                return move
            for i in range(1, 7):
                Next = current + i
                if Next > double:
                    break
                row, column = self.get_position(Next, n)
                if board[row][column] != -1:
                    Next = board[row][column]
                if Next not in visited:
                    visited.add(Next)
                    queue.append((Next, move + 1))       
        return -1