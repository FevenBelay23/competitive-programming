class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        queue = deque([(0, 0, 1)])
        visited = set((0, 0))
        while queue:
            x, y, path = queue.popleft()
            if x == n-1 and y == n-1:
                return path
            neighbor = [
                        (x+i, y+j) 
                        for i in (-1, 0, 1) 
                        for j in (-1, 0, 1) 
                        if i != 0 or j != 0
                    ]
            for k, l in neighbor:
                if 0 <= k < n and 0 <= l < n and grid[k][l] == 0 and (k, l) not in visited:
                    queue.append((k, l, path + 1))
                    visited.add((k, l))
        return -1
        
        
        