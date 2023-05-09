class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        result = [[m+n]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                else:
                    if i > 0:
                        result[i][j] = min(result[i][j], result[i-1][j]+1)
                    if j > 0:
                        result[i][j] = min(result[i][j], result[i][j-1]+1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if mat[i][j] == 1:
                    if i < m-1:
                        result[i][j] = min(result[i][j], result[i+1][j]+1)
                    if j < n-1:
                        result[i][j] = min(result[i][j], result[i][j+1]+1)
        return result