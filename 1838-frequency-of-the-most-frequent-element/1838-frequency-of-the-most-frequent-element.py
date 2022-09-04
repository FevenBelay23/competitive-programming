class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        answer = 1
        j = 0
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            length = (i - j) * diff
            k -= length
            while k < 0:
                k += nums[i] - nums[j]
                j += 1
            answer = max(answer,i-j+1)
        return answer