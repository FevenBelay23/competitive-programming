class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarrays = 0
        for i in range(n):
            temp = nums[i]
            for j in range(i, n):
                temp = math.gcd(temp, nums[j])
                if temp == k:
                    subarrays += 1
                elif temp < k:
                    break
        return subarrays