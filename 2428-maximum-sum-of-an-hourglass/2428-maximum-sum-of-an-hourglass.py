class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        for row in range(len(grid) - 2):
            for column in range(len(grid[0]) - 2):
                Sum = grid[row][column] + grid[row][column + 1] + grid[row][column+2] + \
                    grid[row+1][column+1] + grid[row+2][column] + grid[row+2][column+1] + \
                         grid[row+2][column+2]
                max_sum = max(max_sum,Sum)
        return max_sum