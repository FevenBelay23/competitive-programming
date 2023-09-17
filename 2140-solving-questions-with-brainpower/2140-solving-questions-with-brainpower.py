class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)
        for i in range(n-1, -1, -1):
            temp, last = questions[i]
            dp[i] = max(dp[i+1], temp+dp[min(n, i+last+1)])
        return dp[0]
        