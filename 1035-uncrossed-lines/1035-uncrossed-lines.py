class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        first_line, second_line = len(nums1), len(nums2)
        dp = [[0] * (second_line + 1) for _ in range(first_line + 1)]
        for i in range(1, first_line + 1):
            for j in range(1, second_line + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[first_line][second_line]