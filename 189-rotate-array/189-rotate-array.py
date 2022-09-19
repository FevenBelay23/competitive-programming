class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) 
        i=0 
        j=len(nums)-1
        while i<j :
            nums[i],nums[j] = nums[j],nums[i]
            i,j = 1+i,j-1
        print(nums)      
        i= 0 
        j=k-1
        while i<j :
            nums[i],nums[j] = nums[j],nums[i]
            i,j = 1+i,j-1   
        i= k 
        j=len(nums)-1
        while i<j :
            nums[i],nums[j] = nums[j],nums[i]
            i,j = 1+i,j-1