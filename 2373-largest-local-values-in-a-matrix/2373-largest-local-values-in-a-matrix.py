class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                large = grid[i+1][j+1]
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        large = max(large,grid[k][l])
                result[i][j] = large 
        return result
        
