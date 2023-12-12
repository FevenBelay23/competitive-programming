class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, columns = len(matrix), len(matrix[0])
        row, column = 0, columns - 1 
        while row < rows and column >= 0:
            current_value = matrix[row][column]
            if current_value == target:
                return True
            elif current_value < target:
                row += 1 
            else:
                column -= 1 
        return False