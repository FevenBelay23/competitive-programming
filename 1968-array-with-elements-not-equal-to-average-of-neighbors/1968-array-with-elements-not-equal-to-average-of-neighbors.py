class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(15):
            for j in range(len(nums)-2):
                if (nums[j]+nums[j+2])/2==nums[j+1]:
                    nums[j+1],nums[j+2]=nums[j+2],nums[j+1]
        return nums
        