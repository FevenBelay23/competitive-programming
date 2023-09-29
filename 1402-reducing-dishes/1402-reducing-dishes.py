class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        total = 0
        maximum_sum = 0  
        for i in range(n - 1, -1, -1):
            total += satisfaction[i]
            if total > 0:
                maximum_sum += total
        return maximum_sum