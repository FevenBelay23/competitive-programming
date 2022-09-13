class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        temp = []
        left= 0
        right = len(matrix[0])
        top =0
        bottom =len(matrix)
        while left< right and top< bottom:
            for i in range(left,right):
                temp.append(matrix[top][i])
            top +=1
            for i in range(top,bottom):
                temp.append(matrix[i][right-1])
            right -= 1
            for i in range(right-1,left-1,-1):
                temp.append(matrix[bottom-1][i])
            bottom -=1
            for i in range(bottom-1,top -1,-1):
                temp.append(matrix[i][left])
            left +=1
        return temp[:len(matrix)*len(matrix[0])]