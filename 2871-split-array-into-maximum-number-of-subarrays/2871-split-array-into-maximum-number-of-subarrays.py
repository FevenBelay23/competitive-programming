class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        i = -1
        split = 0
        for j in nums:
            i &= j
            if i == 0:
                split += 1
                i = -1         
        return split or 1