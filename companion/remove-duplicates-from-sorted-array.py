class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        check = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[check] = nums[i]
                check += 1
        return check