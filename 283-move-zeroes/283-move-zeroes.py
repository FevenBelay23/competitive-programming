class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                j+=1
                i-=1
            i+=1
        for k in range(j):
            nums.append(0)