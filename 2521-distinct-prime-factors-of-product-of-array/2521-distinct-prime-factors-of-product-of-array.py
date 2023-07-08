class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def distinctFactors(n):
            factors = set()
            i = 2
            while i * i <= n:
                if n % i == 0:
                    factors.add(i)
                    while n % i == 0:
                        n //= i
                i += 1
            if n > 1:
                factors.add(n)
            return factors
        distinct_factors = set()
        for i in nums:
            factors = distinctFactors(i)
            distinct_factors.update(factors)
        return len(distinct_factors)