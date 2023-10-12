import math
class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        total = 2 * n
        factorial = math.factorial(total)
        constr = pow(2 , n)
        unique_order = factorial // constr
        
        return unique_order % mod
        