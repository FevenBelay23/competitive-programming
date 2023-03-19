class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n

        for i in range(2 * n):
            j = i % n
            while stack and nums[stack[-1]] < nums[j]:
                result[stack.pop()] = nums[j]
            stack.append(j)

        return result
