class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        longest = {}
        length = 0
        for i in arr:
            if i - difference in longest:
                longest[i] = longest[i - difference] + 1
            else:
                longest[i] = 1
            length = max(length, longest[i])
        return length