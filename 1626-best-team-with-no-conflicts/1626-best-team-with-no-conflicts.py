class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        total =[ (ages[i],scores[i]) for i in range(n)]
        total.sort()
        dp = [0]*n
        dp[0] = total[0][1]
        for i in range(1,n):
            dp[i]  = total[i][1]
            for j in range(i):
                if total[i][1] >= total[j][1] and dp[i] < dp[j] + total[i][1]:
                    dp[i] = dp[j] + total[i][1]
        return max(dp)
            
        
        