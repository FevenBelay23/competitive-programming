class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for _ in range (len(matrix[0])):
            temp = []
            for _ in range(len(matrix)):
                temp.append(0)
            transpose.append(temp)
        for i in range (len(matrix)):
            for j in range(len(matrix[0])):
                transpose[j][i] = matrix[i][j]
        return transpose
        
        
