class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        n = len(nums)
        minimum_difference = float('inf')
        for i in range(4):
            minimum_difference = min(minimum_difference, nums[n - 4 + i] - nums[i])
        return minimum_difference
        