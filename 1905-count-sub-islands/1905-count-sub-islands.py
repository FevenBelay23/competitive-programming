class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        row, column = len(grid2), len(grid2[0])
        sub_islands = 0
        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= column or grid2[i][j] != 1:
                return True
            grid2[i][j] = 0
            island = grid1[i][j] == 1
            for rx, ry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                fir, sec = i + rx, j + ry
                island &= dfs(fir, sec)
            return island
        for i in range(row):
            for j in range(column):
                if grid2[i][j] == 1:
                    sub_islands += dfs(i, j)
        return sub_islands