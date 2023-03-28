class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        result = []
        for i in range(len(grid)-2):
            for j in range(1,len(grid[0])-1):
                temp = 0
                temp+=grid[i][j-1]+grid[i][j]+grid[i][j+1]
                temp+=grid[i+1][j]
                temp+=grid[i+2][j-1]+grid[i+2][j]+grid[i+2][j+1]
                result.append(temp)
        return max(result)