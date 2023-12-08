class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans += matrix.pop(0)
            if matrix and matrix[0]:
                for i in matrix:
                    ans.append(i.pop())
            if matrix:
                ans += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for i in matrix[::-1]:
                    ans.append(i.pop(0))
        return ans