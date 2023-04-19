class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if i > 0 and j > 0 and matrix[i][j] != matrix[i-1][j-1]:
                    return False

        return True