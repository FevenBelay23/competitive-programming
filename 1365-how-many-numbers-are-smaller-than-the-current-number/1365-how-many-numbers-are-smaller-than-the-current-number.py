class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        less_than_num=[0]*len(nums)
        for i in range(len(nums)) :
            for j in nums:
                if nums[i]>j:
                    less_than_num[i]+=1
        return less_than_num
        