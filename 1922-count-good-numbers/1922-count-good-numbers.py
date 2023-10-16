class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def Pow(x, y):
            if y == 0:
                return 1
            if y % 2 == 0:
                temp = Pow(x, y // 2)
                return (temp * temp) % mod
            else:
                temp = Pow(x, (y - 1) // 2)
                return (x * temp * temp) % mod

        even = (n + 1) // 2
        odd = n // 2
        count1 = Pow(5, even)
        count2 = Pow(4, odd)
        total = (count1 * count2) % mod
        return total