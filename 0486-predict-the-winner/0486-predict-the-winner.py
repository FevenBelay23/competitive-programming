class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(start, end):
            if start == end:
                return nums[start]
            first = nums[start] - winner(start + 1, end)
            last = nums[end] - winner(start, end - 1)
            return max(first, last)

        return winner(0, len(nums) - 1) >= 0