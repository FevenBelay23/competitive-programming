class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        Sum = 0
        min_length = float('inf')

        while right < len(nums):
            Sum += nums[right]
            while Sum >= target:
                min_length = min(min_length, right - left + 1)
                Sum -= nums[left]
                left += 1
            right += 1

        if min_length == float('inf'):
            return 0
        else:
            return min_length

        