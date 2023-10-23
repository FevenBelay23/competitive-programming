class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + costs[0] 
            for j in range(i, 0, -1):
                if days[i - 1] - days[j - 1] < 7:
                    dp[i] = min(dp[i], dp[j - 1] + costs[1])
                if days[i - 1] - days[j - 1] < 30:
                    dp[i] = min(dp[i], dp[j - 1] + costs[2])
                else:
                    break
        return dp[n]