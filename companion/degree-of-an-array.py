class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = Counter(nums)
        degree = max(count.values())
        first = {}
        last = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
        ans = float('inf')
        for num, count in count.items():
            if count == degree:
                ans = min(ans, last[num] - first[num] + 1)
        return ans
        