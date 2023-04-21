class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c ** 0.5)
        while i <= j:
            res = i*i + j*j
            if res == c:
                return True
            elif res < c:
                i += 1
            else:
                j -= 1
        return False