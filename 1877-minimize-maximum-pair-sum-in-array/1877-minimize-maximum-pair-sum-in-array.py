class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        temp = 0
        for i in range(len(nums)//2):
            temp = max(temp , nums[i]+nums[-i-1])
        return temp