class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        r= 0
        temp = 0
        counter = collections.Counter()
        while r < len(nums):
            counter[nums[r]]+=1
            while counter[0]>k:
                counter[nums[l]]-=1
                l+=1   
            temp = max(temp, r-l+1)
            r+=1
        return temp