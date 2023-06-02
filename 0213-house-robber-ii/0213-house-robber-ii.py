class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.total(nums[1:]),self.total(nums[:-1]))
    def total(self,nums):
        first,second = 0,0
        for i in nums:
            amt = max(first+i,second)
            first = second
            second = amt
        return second
        
        