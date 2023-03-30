class Solution:
    def missingNumber(self, nums: List[int]) -> int: 
        missed_num = len(nums)
        total = 0
        for i in range(len(nums)):
            missed_num ^= nums[i]
            total ^= i
        return total ^ missed_num

        