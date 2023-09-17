class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row-2,-1,-1):
            for j in range(column):
                if j == 0:
                    matrix[i][j] = min(matrix[i+1][j], matrix[i+1][j+1]) + matrix[i][j]
                elif j == column -1:
                    matrix[i][j] = min(matrix[i+1][j], matrix[i+1][j-1]) + matrix[i][j]
                else:
                    matrix[i][j] = min(matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j-1]) + matrix[i][j]
        return min(matrix[0])