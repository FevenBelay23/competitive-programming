class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maximum = 0
        count = 0
        def backtrack(index, current):
            nonlocal maximum, count
            if index == len(nums):
                if current > maximum:
                    maximum = current
                    count = 1
                elif current == maximum:
                    count += 1
                return
            backtrack(index + 1, current | nums[index])
            backtrack(index + 1, current)
        backtrack(0, 0)
        return count
