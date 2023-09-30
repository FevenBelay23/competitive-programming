class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        longest = 0
        for i in arr:
            if i - difference in dp:
                dp[i] = dp[i - difference] + 1
            else:
                dp[i] = 1
            longest = max(longest, dp[i])
        return longest