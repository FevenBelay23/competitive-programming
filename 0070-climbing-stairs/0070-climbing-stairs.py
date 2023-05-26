class Solution:
    def climbStairs(self, n: int) -> int:
        climb = {}
        def stairs(n):
            if n <= 2:
                return n
            if n not in climb:
                climb[n] = stairs(n - 1) + stairs(n - 2)
            return climb[n]
        return stairs(n)