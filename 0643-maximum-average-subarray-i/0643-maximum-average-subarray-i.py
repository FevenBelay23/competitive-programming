class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = max_Avg = sum(nums[:k])

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            max_Avg = max(max_Avg, current_sum)

        return max_Avg / k

        