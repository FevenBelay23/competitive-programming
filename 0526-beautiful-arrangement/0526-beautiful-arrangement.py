class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(place,visited):
            if place > n:
                return 1
            count = 0
            for i in range(1, n + 1):
                if not visited & (1 << (i - 1)) and (i % place == 0 or place % i == 0):
                    count += backtrack(place + 1, visited | (1 << (i - 1)))
            return count
        return backtrack(1, 0)