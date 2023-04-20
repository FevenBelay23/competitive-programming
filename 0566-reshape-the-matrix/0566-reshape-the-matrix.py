class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        column = len(mat[0])
        if row * column != r * c:
            return mat
        converted = [num for row in mat for num in row]
        matrix = []
        for i in range(0, r):
            row = []
            for j in range(0, c):
                row.append(converted[i*c+j])
            matrix.append(row)
        return matrix