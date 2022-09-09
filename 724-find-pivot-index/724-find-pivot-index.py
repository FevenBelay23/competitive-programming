class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = sum(nums)
        left = 0
        i=0
        while i<len(nums):
            right-=nums[i]
            if left==right : 
                return i
            left+=nums[i]
            i+=1
        return -1