class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        previous = None
        while n:
            curr = n & 1
            if previous is not None and curr == previous:
                return False
            previous = curr
            n >>= 1
        return True
    
        