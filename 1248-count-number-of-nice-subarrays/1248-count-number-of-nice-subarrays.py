class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        odd_indices = [-1] + [i for i in range(n) if nums[i] % 2 == 1] + [n]
        
        for i in range(1, len(odd_indices)-k):
            left_count = odd_indices[i] - odd_indices[i-1]
            right_count = odd_indices[i+k] - odd_indices[i+k-1]
            count += left_count * right_count
        
        return count
