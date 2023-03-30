class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i <<= 1
        shf = i - 1
        return shf ^ num
        