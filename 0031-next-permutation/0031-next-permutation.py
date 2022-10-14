class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        check=False
        for i in range(len(nums)-1, 0, -1):
            if nums[i] >nums[i-1]:
                nums[i:]=nums[i:][::-1]
                for j in range(i, len(nums)):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                check=True
                break
        if not check:
            nums.reverse()