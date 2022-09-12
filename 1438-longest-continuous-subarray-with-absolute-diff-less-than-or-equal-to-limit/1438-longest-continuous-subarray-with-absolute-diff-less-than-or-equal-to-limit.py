class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        i = 0
        j = 1
        maxi = nums[0]
        mini = nums[0]
        longest = 1
        while i <= j and j < len(nums):
            maxi = max(maxi, nums[j])
            mini = min(mini, nums[j])

            if maxi - mini <= limit:
                longest = max(longest, j - i + 1)
            else:
                if nums[i] == maxi:
                    maxi = max(nums[i + 1:j + 1]) 
                if nums[i] == mini:
                    mini = min(nums[i + 1:j + 1])
                i += 1
            j += 1
        return longest