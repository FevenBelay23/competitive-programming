class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        large, small = max(nums), min(nums)  # Change A to nums
        diff, temp = large - small, 2 * k  # Change K to k
        if diff <= temp:
            return 0
        else:
            return diff - temp