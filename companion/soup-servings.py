class Solution:
    def soupServings(self, n: int) -> float:
        dp = {}
        if n >= 5000:
            return 1.0
        def serving(one, two):
            if (one, two) in dp:
                return dp[(one, two)]
            if one <= 0 and two <= 0:
                return 0.5 
            if one <= 0:
                return 1.0  
            if two <= 0:
                return 0.0  
            dp[(one, two)] = 0.25 * (
                serving(one - 100, two) +
                serving(one - 75, two - 25) +
                serving(one - 50, two - 50) +
                serving(one - 25, two - 75)
            )
            return dp[(one, two)]
        return serving(n,n)