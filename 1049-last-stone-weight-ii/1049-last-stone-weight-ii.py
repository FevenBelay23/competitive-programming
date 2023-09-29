class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        temp = sum(stones)//2        
        dp = [0 for i in range(temp+1)]
        for i in stones:
            for j in range(temp, i-1, -1): 
                dp[j] = max(dp[j], dp[j-i] + i)
        return sum(stones) - 2*dp[temp]