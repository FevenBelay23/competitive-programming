class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
        