class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, current):
            if len(current) > 1:
                result.append(current[:])
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used or (current and nums[i] < current[-1]):
                    continue
                used.add(nums[i])
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        result = []
        backtrack(0, [])
        return result