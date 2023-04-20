class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        row = set()
        column = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    column.add(j)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for j in column:
            for i in range(m):
                matrix[i][j] = 0