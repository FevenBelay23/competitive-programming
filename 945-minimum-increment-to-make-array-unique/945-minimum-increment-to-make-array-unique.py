class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=1
        j=0
        
        while i<len(nums):
            if nums[i]<=nums[i-1]:
                k=nums[i-1]+1
                j+=(k-nums[i])
                nums[i]=k
            i+=1
        return j