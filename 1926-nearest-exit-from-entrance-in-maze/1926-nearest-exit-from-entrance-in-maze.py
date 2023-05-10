class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = collections.deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])
        possible = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            x, y, step = queue.popleft()
            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and (x != entrance[0] or y != entrance[1]):
                return step
            for i, j in possible:
                k, l = x + i, y + j
                if 0 <= k < m and 0 <= l < n and maze[k][l] == '.' and (k, l) not in visited:
                    visited.add((k, l))
                    queue.append((k, l, step+1))
        return -1